# Muc dich: seed rieng cho action_space va kiem tra tinh tai lap
import gymnasium as gym

env = gym.make("CartPole-v1")
env.action_space.seed(123)

actions = [env.action_space.sample() for _ in range(20)]
print("Chuoi action:", actions)

env.close()

# Chay file nay 2 lan: chuoi actions in ra phai giong het nhau
# vi action_space da duoc seed co dinh = 123.