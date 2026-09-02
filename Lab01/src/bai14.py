# Muc dich: chay 100 episode, chi luu reward, khong in tung timestep
import gymnasium as gym

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
for ep in range(100):
    reward, length = random_agent(env)
    episode_rewards.append(reward)

print("Da chay xong 100 episode.")
print("So luong reward da luu:", len(episode_rewards))

env.close()