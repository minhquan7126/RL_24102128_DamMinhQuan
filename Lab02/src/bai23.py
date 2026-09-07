
"""Bai 23. Mot sweep cua Policy Evaluation"""

import numpy as np
import gymnasium as gym
from mdp_utils import action_values


def policy_evaluation_sweep(env, policy, V, gamma):
    new_V = np.zeros_like(V)
    for s in range(env.observation_space.n):
        q = action_values(env, V, s, gamma)
        new_V[s] = np.sum(policy[s] * q)
    return new_V


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states, n_actions = env.observation_space.n, env.action_space.n
    policy = np.ones((n_states, n_actions)) / n_actions
    V = np.zeros(n_states)

    new_V = policy_evaluation_sweep(env, policy, V, gamma=0.99)
    print("V sau 1 sweep:", new_V)
    env.close()


if __name__ == "__main__":
    main()