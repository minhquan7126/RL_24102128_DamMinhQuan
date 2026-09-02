# Muc dich: sinh 20 action ngau nhien va tinh tan suat xuat hien
import gymnasium as gym
from collections import Counter

env = gym.make("CartPole-v1")
env.reset(seed=42)

actions = [env.action_space.sample() for _ in range(20)]
print("Danh sach action:", actions)

freq = Counter(actions)
print("Tan suat xuat hien:", dict(freq))

env.close()