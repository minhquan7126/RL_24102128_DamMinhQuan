# Muc dich: so sanh reward trung binh giua seed=42 va seed=100
import gymnasium as gym
import numpy as np

def run_group(seed, n_episodes=20):
    env = gym.make("CartPole-v1")
    rewards = []
    for ep in range(n_episodes):
        obs, info = env.reset(seed=seed + ep)  # thay doi seed nhe moi episode de co du lieu da dang
        total_reward = 0.0
        terminated = truncated = False
        while not (terminated or truncated):
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    env.close()
    return np.mean(rewards)

mean_42 = run_group(42)
mean_100 = run_group(100)

print("Reward trung binh voi seed=42 :", mean_42)
print("Reward trung binh voi seed=100:", mean_100)