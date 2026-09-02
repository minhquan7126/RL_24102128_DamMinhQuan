# Muc dich: dong goi 1 buoc tuong tac thanh ham de tai su dung
import gymnasium as gym

def run_one_step(env, action):
    observation, reward, terminated, truncated, info = env.step(action)
    return observation, reward, terminated, truncated, info

if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    env.reset(seed=42)

    for i in range(5):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = run_one_step(env, action)
        print(f"Test {i+1}: action={action}, reward={reward}, terminated={terminated}, truncated={truncated}")
        if terminated or truncated:
            env.reset(seed=42)

    env.close()