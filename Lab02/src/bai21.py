
"""Bai 21. Mot Bellman backup"""

import numpy as np
import gymnasium as gym
from mdp_utils import q_from_v


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    V = np.zeros(env.observation_space.n)
    print("Q(0, RIGHT):", q_from_v(env, V, state=0, action=2, gamma=0.99))
    env.close()


if __name__ == "__main__":
    main()