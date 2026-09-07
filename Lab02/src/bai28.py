
"""Bai 28. Mot buoc Policy Improvement"""

import numpy as np
import gymnasium as gym
from mdp_utils import policy_evaluation, greedy_policy_from_value


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states = env.observation_space.n
    old_policy = np.zeros(n_states, dtype=int)  # tat ca chon action 0 (LEFT)

    V, _ = policy_evaluation(env, old_policy, gamma=0.99)
    new_policy = greedy_policy_from_value(env, V, gamma=0.99)

    n_changed = np.sum(old_policy != new_policy)
    print("Old policy:", old_policy)
    print("New policy:", new_policy)
    print(f"So state doi action: {n_changed}/{n_states}")
    env.close()


if __name__ == "__main__":
    main()