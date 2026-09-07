# Muc dich: xac dinh y nghia cua tung action bang thuc nghiem
import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")
observation, info = env.reset(seed=42)

# Theo tai lieu chinh thuc cua FrozenLake:
ACTION_NAMES = {0: "LEFT", 1: "DOWN", 2: "RIGHT", 3: "UP"}

action = env.action_space.sample()
print(f"Action {action} -> {ACTION_NAMES[action]}")

next_obs, reward, terminated, truncated, info = env.step(action)
print(env.render())

env.close()