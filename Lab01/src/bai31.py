# Muc dich: xay dung heuristic policy dua tren goc nghieng cua pole
import gymnasium as gym
import numpy as np

def angle_based_policy(observation):
    pole_angle = observation[2]
    # Neu pole nghieng ve phai (angle > 0) thi day xe sang phai de "duoi kip" pole
    if pole_angle > 0:
        return 1  # phai
    else:
        return 0  # trai

def random_policy(observation):
    return np.random.randint(0, 2)

def run_policy(policy_fn, n_episodes=100):
    env = gym.make("CartPole-v1")
    rewards = []
    for ep in range(n_episodes):
        observation, info = env.reset()
        terminated = truncated = False
        total_reward = 0.0
        while not (terminated or truncated):
            action = policy_fn(observation)
            observation, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
        rewards.append(total_reward)
    env.close()
    return np.mean(rewards)

mean_angle = run_policy(angle_based_policy)
mean_random = run_policy(random_policy)

print("Mean reward (angle-based policy):", mean_angle)
print("Mean reward (random policy):     ", mean_random)