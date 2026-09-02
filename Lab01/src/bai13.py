# Muc dich: chay 10 episode bang random agent va in bang ket qua
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

print(f"{'Episode':>8} | {'Reward':>7} | {'Length':>7}")
for ep in range(1, 11):
    reward, length = random_agent(env)
    print(f"{ep:>8} | {reward:>7.1f} | {length:>7}")

env.close()