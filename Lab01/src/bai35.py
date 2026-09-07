# Muc dich: so sanh random / angle-based / improved policy tren 500 episode
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

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

def evaluate_policy(env_name, policy, n_episodes=500, seed=42):
    env = gym.make(env_name)
    rewards, lengths = [], []
    for i in range(n_episodes):
        result = run_episode(env, policy, seed=seed + i)
        rewards.append(result["reward"])
        lengths.append(result["length"])
    env.close()
    arr = np.array(rewards)
    return {
        "mean_reward": arr.mean(), "std_reward": arr.std(),
        "min_reward": arr.min(), "max_reward": arr.max(),
        "mean_length": np.mean(lengths),
    }

def random_policy(obs):
    return np.random.randint(0, 2)

def angle_based_policy(obs):
    return 1 if obs[2] > 0 else 0

def improved_policy(obs):
    score = obs[2] + 0.5 * obs[3]
    return 1 if score > 0 else 0

agents = {
    "Random": random_policy,
    "Angle-based": angle_based_policy,
    "Improved": improved_policy,
}

results = {}
print(f"{'Agent':<12} | {'Mean':>7} | {'Std':>6} | {'Min':>6} | {'Max':>6} | {'MeanLen':>8}")
for name, pol in agents.items():
    stats = evaluate_policy("CartPole-v1", pol)
    results[name] = stats
    print(f"{name:<12} | {stats['mean_reward']:>7.2f} | {stats['std_reward']:>6.2f} | "
          f"{stats['min_reward']:>6.1f} | {stats['max_reward']:>6.1f} | {stats['mean_length']:>8.2f}")

plt.figure()
names = list(results.keys())
means = [results[n]["mean_reward"] for n in names]
plt.bar(names, means)
plt.title("So sanh Mean Reward giua 3 Agent")
plt.xlabel("Agent")
plt.ylabel("Mean Reward")
plt.grid(axis="y")
plt.savefig("Lab01/figures/comparison_agents.png")
plt.show()

# Nhan xet (vi du, ban tu viet lai bang loi minh sau khi xem so lieu that):
# - Random policy cho reward thap va bien thien lon (std cao) vi khong co
#   chien luoc, hanh dong hoan toan ngau nhien.
# - Angle-based policy cai thien dang ke vi biet phan ung theo huong pole nga.
# - Improved policy (dung them van toc goc) thuong on dinh va cao hon
#   angle-based vi "du doan" som huong pole se nga thay vi chi phan ung
#   khi da nghieng.