
"""Bai 34. Danh gia policy bang simulation"""

import numpy as np
import gymnasium as gym
from mdp_utils import value_iteration, policy_iteration, greedy_policy_from_value, evaluate_policy_by_simulation


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states = env.observation_space.n

    random_policy = np.random.default_rng(0).integers(0, env.action_space.n, size=n_states)
    V_vi, _, _ = value_iteration(env, gamma=0.99)
    policy_vi = greedy_policy_from_value(env, V_vi, gamma=0.99)
    policy_pi, _, _ = policy_iteration(env, gamma=0.99)

    for name, policy in [("Random", random_policy), ("Value Iteration", policy_vi), ("Policy Iteration", policy_pi)]:
        result = evaluate_policy_by_simulation(env, policy, n_episodes=1000)
        print(f"--- {name} ---")
        print(result)

    env.close()


if __name__ == "__main__":
    main()