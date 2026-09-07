# Muc dich: ve bieu do reward theo tung episode
import gymnasium as gym
import matplotlib.pyplot as plt

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

plt.figure()
plt.plot(episode_rewards)
plt.title("Reward theo Episode - CartPole (Random Agent)")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.grid(True)
plt.savefig("Lab01/figures/reward_cartpole.png")
plt.show()