
"""Bai 33. Trich xuat optimal policy"""

import gymnasium as gym
from mdp_utils import value_iteration, greedy_policy_from_value, print_policy


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    V, n_iter, deltas = value_iteration(env, gamma=0.99, theta=1e-8)
    optimal_policy = greedy_policy_from_value(env, V, gamma=0.99)

    print("Optimal state values:")
    print(V.reshape(4, 4))
    print("Optimal policy:")
    print_policy(env, optimal_policy)
    env.close()


if __name__ == "__main__":
    main()