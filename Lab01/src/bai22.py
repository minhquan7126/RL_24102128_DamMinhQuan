# Muc dich: dong goi 1 thi nghiem hoan chinh co seed, chay voi nhieu seed khac nhau
import gymnasium as gym
import numpy as np

def experiment(seed, n_episodes):
    env = gym.make("CartPole-v1")
    rewards = []
    for ep in range(n_episodes):
        obs, info = env.reset(seed=seed + ep)
        total_reward = 0.0
        terminated = truncated = False
        while not (terminated or truncated):
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    env.close()

    arr = np.array(rewards)
    return {
        "seed": seed,
        "mean_reward": arr.mean(),
        "std_reward": arr.std(),
        "max_reward": arr.max(),
        "min_reward": arr.min(),
    }

seeds = [0, 42, 100, 123, 2024]
for s in seeds:
    result = experiment(s, n_episodes=20)
    print(result)