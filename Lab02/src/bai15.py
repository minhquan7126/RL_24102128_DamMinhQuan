
"""Bai 15. Stochastic uniform policy tren FrozenLake"""

import numpy as np
import gymnasium as gym


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states = env.observation_space.n
    n_actions = env.action_space.n

    policy = np.ones((n_states, n_actions)) / n_actions
    print("Tong xac suat moi state == 1:", np.allclose(policy.sum(axis=1), 1.0))
    env.close()


if __name__ == "__main__":
    main()