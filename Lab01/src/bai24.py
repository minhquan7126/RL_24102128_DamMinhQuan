# Muc dich: render moi truong duoi dang text de quan sat ban do
import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")
observation, info = env.reset(seed=42)

print(env.render())
# Ky hieu: S=Start, F=Frozen (di duoc), H=Hole (rot xuong = thua),
# G=Goal (dich den = thang)

env.close()