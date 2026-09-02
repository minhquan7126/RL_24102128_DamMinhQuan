# Muc dich: kham pha cau truc cua observation_space
import gymnasium as gym
env = gym.make("CartPole-v1")
obs_space = env.observation_space
print("Observation space:", obs_space)
print("Shape:", obs_space.shape)
print("Dtype:", obs_space.type)
print("Low:", obs_space.low)
print("High:", obs_space.high)
env.close()
