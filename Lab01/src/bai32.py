# Muc dich: cai tien policy bang cach ket hop 2 thanh phan cua observation
import gymnasium as gym
import numpy as np

def improved_policy(observation):
    pole_angle = observation[2]
    pole_ang_vel = observation[3]
    # Ket hop goc nghieng va toc do nghieng: neu tong co trong so > 0 thi day phai
    score = pole_angle + 0.5 * pole_ang_vel
    return 1 if score > 0 else 0

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

mean_improved = run_policy(improved_policy)
mean_random = run_policy(random_policy)

print("Mean reward (improved policy):", mean_improved)
print("Mean reward (random policy):  ", mean_random)
assert mean_improved > mean_random, "Policy cai tien chua tot hon random, hay dieu chinh he so!"