# Muc dich: goi reset() va hieu cau truc du lieu tra ve
import gymnasium as gym
env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)
print("Observation:", observation)
print("Type:", type(observation))
print("Shape:", observation.shape)
print("Info:", info)
# observation[0] = vi tri xe (cart position), kieu float
# observation[1] = van toc xe (cart velocity), kieu float
# observation[2] = goc nghieng cua pole (pole angle, radian), kieu float
# observation[3] = van toc goc cua pole (pole angular velocity), kieu float
env.close()

