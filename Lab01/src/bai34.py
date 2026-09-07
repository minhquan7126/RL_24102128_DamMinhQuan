# Muc dich: danh gia mot policy tren nhieu episode, tra ve thong ke tong hop
import gymnasium as gym
import numpy as np

def run_episode(env, policy, seed=None, max_steps=1000):
    observation, info = env.reset(seed=seed)
    total_reward = 0.0
    length = 0
    terminated = truncated = False
    for _ in range(max_steps):
        action = policy(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        length += 1
        if terminated or truncated:
            break
    return {"reward": total_reward, "length": length}

def evaluate_policy(env_name, policy, n_episodes=100, seed=42):
    env = gym.make(env_name)
    rewards, lengths = [], []
    for i in range(n_episodes):
        result = run_episode(env, policy, seed=seed + i)
        rewards.append(result["reward"])
        lengths.append(result["length"])
    env.close()

    arr = np.array(rewards)
    return {
        "mean_reward": arr.mean(),
        "std_reward": arr.std(),
        "min_reward": arr.min(),
        "max_reward": arr.max(),
        "mean_length": np.mean(lengths),
    }

if __name__ == "__main__":
    random_policy = lambda obs: np.random.randint(0, 2)
    stats = evaluate_policy("CartPole-v1", random_policy, n_episodes=100)
    print(stats)