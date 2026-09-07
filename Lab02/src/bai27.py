
"""Bai 27. Hien thi policy tren luoi 4x4"""

import numpy as np
import gymnasium as gym
from mdp_utils import policy_evaluation, greedy_policy_from_value, print_policy as print_frozenlake_policy


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states, n_actions = env.observation_space.n, env.action_space.n
    uniform_policy = np.ones((n_states, n_actions)) / n_actions

    V, _ = policy_evaluation(env, uniform_policy, gamma=0.99)
    policy = greedy_policy_from_value(env, V, gamma=0.99)
    print_frozenlake_policy(env, policy)
    env.close()


if __name__ == "__main__":
    main()