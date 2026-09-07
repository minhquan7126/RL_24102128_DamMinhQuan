# Muc dich: tu xay dung chuoi action dua agent tu Start den Goal
import gymnasium as gym

ACTION_NAMES = {0: "LEFT", 1: "DOWN", 2: "RIGHT", 3: "UP"}

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")
observation, info = env.reset(seed=42)
print("Trang thai ban dau:")
print(env.render())

# Ban do mac dinh 4x4:
# S F F F
# F H F H
# F F F H
# H F F G
# Mot duong di an toan tu o 0 (goc tren trai) den o 15 (goc duoi phai):
actions = [1, 1, 2, 2, 1, 2]  # DOWN, DOWN, RIGHT, RIGHT, DOWN, RIGHT (vi du - ban tu kiem tra lai theo ban do that)

for a in actions:
    observation, reward, terminated, truncated, info = env.step(a)
    print(f"Action: {ACTION_NAMES[a]}")
    print(env.render())
    if terminated or truncated:
        print("Reward cuoi:", reward)
        break

env.close()