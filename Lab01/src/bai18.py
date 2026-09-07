# Muc dich: tu viet ham tinh moving average (khong dung pandas)
import gymnasium as gym
import numpy as np
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

def moving_average(values, window_size):
    values = np.array(values, dtype=float)
    n = len(values) - window_size + 1
    result = np.zeros(n)
    for i in range(n):
        result[i] = values[i:i + window_size].mean()
    return result

env = gym.make("CartPole-v1")
episode_rewards = [random_agent(env) for _ in range(100)]
env.close()

ma = moving_average(episode_rewards, window_size=10)

plt.figure()
plt.plot(episode_rewards, label="Reward goc", alpha=0.4)
plt.plot(range(9, 9 + len(ma)), ma, label="Moving average (window=10)", linewidth=2)
plt.title("Reward va Moving Average - CartPole")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.legend()
plt.grid(True)
plt.savefig("Lab01/figures/moving_average.png")
plt.show()