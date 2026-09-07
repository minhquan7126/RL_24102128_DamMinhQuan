# Muc dich: pipeline RL hoan chinh cho CartPole-v1
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

SEED = 42

def create_environment():
    return gym.make("CartPole-v1")

def policy(observation):
    # Policy cai tien tu Bai 32
    score = observation[2] + 0.5 * observation[3]
    return 1 if score > 0 else 0

def run_episode(env, policy_fn, seed=None, max_steps=1000):
    observation, info = env.reset(seed=seed)
    total_reward = 0.0
    length = 0
    terminated = truncated = False
    for _ in range(max_steps):
        action = policy_fn(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        length += 1
        if terminated or truncated:
            break
    return {"reward": total_reward, "length": length}

def evaluate_policy(env, policy_fn, n_episodes=500, seed=SEED):
    rewards, lengths = [], []
    for i in range(n_episodes):
        result = run_episode(env, policy_fn, seed=seed + i)
        rewards.append(result["reward"])
        lengths.append(result["length"])
    return np.array(rewards), np.array(lengths)

def moving_average(values, window_size=10):
    n = len(values) - window_size + 1
    return np.array([values[i:i + window_size].mean() for i in range(n)])

def plot_results(rewards):
    ma = moving_average(rewards, 10)

    plt.figure()
    plt.plot(rewards, alpha=0.4, label="Reward")
    plt.plot(range(9, 9 + len(ma)), ma, linewidth=2, label="Moving average")
    plt.title("Mini-project: CartPole voi Improved Policy")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.legend()
    plt.grid(True)
    plt.savefig("Lab01/figures/miniproject_reward.png")

def main():
    env = create_environment()
    rewards, lengths = evaluate_policy(env, policy, n_episodes=500)
    env.close()

    print(f"Mean reward   : {rewards.mean():.2f}")
    print(f"Std reward    : {rewards.std():.2f}")
    best_idx = int(np.argmax(rewards))
    worst_idx = int(np.argmin(rewards))
    print(f"Episode tot nhat : index {best_idx}, reward {rewards[best_idx]}")
    print(f"Episode te nhat  : index {worst_idx}, reward {rewards[worst_idx]}")

    plot_results(rewards)

    # Ket luan (vi du - ban thay bang nhan xet thuc te cua minh):
    # Improved policy dat mean reward cao hon nhieu so voi random baseline
    # o cac bai truoc, cho thay viec su dung goc nghieng + van toc goc
    # giup agent giu thang bang tot hon dang ke.

if __name__ == "__main__":
    main()