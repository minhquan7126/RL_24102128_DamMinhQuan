# Muc dich: tao moi truong CartPole-v1 va dong no dung cach
import gymnasium as gym

env = gym.make("CartPole-v1")
print(env)
env.close()