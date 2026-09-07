# Muc dich: so sanh is_slippery=False vs True tren 500 episode
import gymnasium as gym
import numpy as np

def run_experiment(is_slippery, n_episodes=500):
    env = gym.make("FrozenLake-v1", is_slippery=is_slippery)
    success = 0
    rewards = []
    lengths = []

    for ep in range(n_episodes):
        observation, info = env.reset()
        terminated = truncated = False
        total_reward = 0.0
        length = 0
        while not (terminated or truncated):
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
            length += 1
        if terminated and reward == 1.0:
            success += 1
        rewards.append(total_reward)
        lengths.append(length)

    env.close()
    return {
        "success_rate": success / n_episodes,
        "avg_reward": np.mean(rewards),
        "avg_length": np.mean(lengths),
    }

deterministic = run_experiment(is_slippery=False)
stochastic = run_experiment(is_slippery=True)

print("Deterministic (is_slippery=False):", deterministic)
print("Stochastic (is_slippery=True):    ", stochastic)

# Nhan xet: voi random policy, is_slippery=True lam agent di chuyen
# khong theo y muon (co the truot sang huong khac), nen success rate
# va reward trung binh thap hon dang ke so voi is_slippery=False.