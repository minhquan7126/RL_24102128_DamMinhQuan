
"""Bai 26. Greedy policy tu V"""

import numpy as np
import gymnasium as gym
from mdp_utils import policy_evaluation, greedy_policy_from_value


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states, n_actions = env.observation_space.n, env.action_space.n
    uniform_policy = np.ones((n_states, n_actions)) / n_actions

    V, _ = policy_evaluation(env, uniform_policy, gamma=0.99)
    greedy_policy = greedy_policy_from_value(env, V, gamma=0.99)
    print("Greedy policy:", greedy_policy)
    env.close()


if __name__ == "__main__":
    main()