# Muc dich: chay vong lap toi da 20 buoc, dung khi episode ket thuc
import gymnasium as gym

env = gym.make("CartPole-v1")
observation, info = env.reset(seed=42)

for t in range(20):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    print(f"t={t}, action={action}, reward={reward}")
    if terminated or truncated:
        print("Episode ket thuc som tai t =", t)
        break

env.close()