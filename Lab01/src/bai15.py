# Muc dich: tinh mean, min, max, std bang NumPy
import gymnasium as gym
import numpy as np

def random_agent(env, max_steps=500):
    observation, info = env.reset()
    total_reward = 0.0
    for _ in range(max_steps):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        if terminated or truncated:
            break
    return total_reward

env = gym.make("CartPole-v1")
episode_rewards = [random_agent(env) for _ in range(100)]
env.close()

arr = np.array(episode_rewards)
print(f"Mean reward : {arr.mean():.2f}")
print(f"Min reward  : {arr.min():.2f}")
print(f"Max reward  : {arr.max():.2f}")
print(f"Std reward  : {arr.std():.2f}")