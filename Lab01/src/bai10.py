# Muc dich: tinh tong reward va do dai episode
import gymnasium as gym

env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)

total_reward = 0.0
episode_length = 0

for t in range(20):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    episode_length += 1
    if terminated or truncated:
        break

print("Episode length:", episode_length)
print("Total reward:", total_reward)

env.close()