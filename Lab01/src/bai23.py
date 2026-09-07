# Muc dich: tao FrozenLake va xac dinh so state, so action
import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

n_states = env.observation_space.n
n_actions = env.action_space.n
print("So state:", n_states)
print("So action:", n_actions)

env.close()