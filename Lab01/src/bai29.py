# Muc dich: tach logic chon action ra thanh mot ham policy rieng
import gymnasium as gym

def policy(observation, env):
    return env.action_space.sample()

env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)

total_reward = 0.0
terminated = truncated = False
while not (terminated or truncated):
    action = policy(observation, env)   # thay vi goi truc tiep env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward

print("Total reward:", total_reward)
env.close()