# Muc dich: thuc hien dung 1 buoc tuong tac va quan sat day du ket qua
import gymnasium as gym

env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)
print("State before action:", observation)

action = env.action_space.sample()
print("Action:", action)

next_observation, reward, terminated, truncated, info = env.step(action)

print("State after action:", next_observation)
print("Reward:", reward)
print("Terminated:", terminated)
print("Truncated:", truncated)
print("Info:", info)

env.close()