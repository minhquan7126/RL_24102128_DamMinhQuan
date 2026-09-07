# Muc dich: so sanh policy "luon trai" va "luon phai"
import gymnasium as gym
import numpy as np

def always_left_policy(observation):
    return 0

def always_right_policy(observation):
    return 1

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

mean_left = run_policy(always_left_policy)
mean_right = run_policy(always_right_policy)

print("Mean reward (luon trai):", mean_left)
print("Mean reward (luon phai):", mean_right)