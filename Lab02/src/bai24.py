
"""Bai 24. Iterative Policy Evaluation"""

import numpy as np
import gymnasium as gym
from mdp_utils import policy_evaluation


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states, n_actions = env.observation_space.n, env.action_space.n
    policy = np.ones((n_states, n_actions)) / n_actions

    V, n_iter = policy_evaluation(env, policy, gamma=0.99, theta=1e-8)
    print(f"Hoi tu sau {n_iter} iteration")
    print("V:", V)
    env.close()


if __name__ == "__main__":
    main()