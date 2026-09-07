# Muc dich: tim episode co reward lon nhat MA KHONG chay lai moi truong
import gymnasium as gym
import numpy as np

def random_agent(env, max_steps=500):
    observation, info = env.reset()
    total_reward = 0.0
    episode_length = 0
    for _ in range(max_steps):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        episode_length += 1
        if terminated or truncated:
            break
    return total_reward, episode_length

env = gym.make("CartPole-v1")

episode_rewards = []
episode_lengths = []
for _ in range(100):
    reward, length = random_agent(env)
    episode_rewards.append(reward)
    episode_lengths.append(length)

env.close()

rewards_arr = np.array(episode_rewards)
best_index = int(np.argmax(rewards_arr))   # chi so cua episode tot nhat

print("Episode tot nhat (chi so):", best_index)
print("Reward tuong ung:", episode_rewards[best_index])
print("Do dai episode tuong ung:", episode_lengths[best_index])