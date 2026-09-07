
"""Bai 29. Policy Iteration hoan chinh"""

import gymnasium as gym
from mdp_utils import policy_iteration


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    policy, V, n_iter = policy_iteration(env, gamma=0.99, theta=1e-8)
    print(f"Policy Iteration converged after {n_iter} iterations.")
    print("V:", V)
    print("Policy:", policy)
    env.close()


if __name__ == "__main__":
    main()