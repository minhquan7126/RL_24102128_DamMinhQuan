# Muc dich: kiem tra cung mot seed co cho ra cung 1 observation ban dau khong
import gymnasium as gym
import numpy as np

observations = []
for i in range(10):
    env = gym.make("CartPole-v1")
    obs, info = env.reset(seed=42)
    observations.append(obs)
    env.close()

all_same = all(np.array_equal(observations[0], o) for o in observations)
print("Tat ca observation ban dau giong nhau:", all_same)

# Ket luan: khi dat cung mot seed=42 cho tung environment doc lap,
# initial observation tra ve giong het nhau, vi RNG noi bo duoc
# khoi tao lai cung mot trang thai xac dinh boi seed.