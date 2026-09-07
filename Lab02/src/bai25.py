
"""Bai 25. Theo doi hoi tu cua Policy Evaluation"""

import numpy as np
import matplotlib.pyplot as plt
import gymnasium as gym
from bai23 import policy_evaluation_sweep


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    n_states, n_actions = env.observation_space.n, env.action_space.n
    policy = np.ones((n_states, n_actions)) / n_actions

    V = np.zeros(n_states)
    deltas = []
    for i in range(10000):
        new_V = policy_evaluation_sweep(env, policy, V, gamma=0.99)
        delta = np.max(np.abs(new_V - V))
        deltas.append(delta)
        V = new_V
        if delta < 1e-8:
            break

    plt.figure()
    plt.plot(deltas)
    plt.xlabel("Iteration")
    plt.ylabel("Delta")
    plt.title("Hoi tu cua Policy Evaluation")
    plt.grid(True)
    plt.yscale("log")
    plt.savefig("../figures/policy_iteration_convergence.png")
    plt.close()
    print(f"Hoi tu sau {len(deltas)} iteration")
    env.close()


if __name__ == "__main__":
    main()