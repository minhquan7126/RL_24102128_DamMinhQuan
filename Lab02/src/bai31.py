
"""Bai 31. Mot sweep cua Value Iteration"""

import numpy as np
import gymnasium as gym
from mdp_utils import action_values


def value_iteration_sweep(env, V, gamma):
    new_V = np.zeros_like(V)
    for s in range(env.observation_space.n):
        q = action_values(env, V, s, gamma)
        new_V[s] = np.max(q)
    return new_V


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    V = np.zeros(env.observation_space.n)
    new_V = value_iteration_sweep(env, V, gamma=0.99)
    print("V sau 1 sweep:", new_V)
    env.close()


if __name__ == "__main__":
    main()