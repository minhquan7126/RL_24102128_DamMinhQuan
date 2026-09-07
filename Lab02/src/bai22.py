
"""Bai 22. Toan bo Q cua mot state"""

import numpy as np
import gymnasium as gym
from mdp_utils import action_values


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    V = np.zeros(env.observation_space.n)
    print("Q(0, .):", action_values(env, V, state=0, gamma=0.99))
    env.close()


if __name__ == "__main__":
    main()