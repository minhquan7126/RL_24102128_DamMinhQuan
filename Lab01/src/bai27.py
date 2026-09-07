# Muc dich: chay 100 episode voi random policy, tinh success rate
import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)

success = 0
failure = 0
total_episodes = 100

for ep in range(total_episodes):
    observation, info = env.reset()
    terminated = truncated = False
    final_reward = 0.0
    while not (terminated or truncated):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        final_reward = reward
    if terminated and final_reward == 1.0:
        success += 1
    else:
        failure += 1

success_rate = success / total_episodes
print("So lan thanh cong:", success)
print("So lan that bai:", failure)
print("Success rate:", success_rate)

env.close()