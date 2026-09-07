
"""Bai 32. Value Iteration hoan chinh"""

import matplotlib.pyplot as plt
import gymnasium as gym
from mdp_utils import value_iteration


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    V, n_iter, deltas = value_iteration(env, gamma=0.99, theta=1e-8)
    print(f"Hoi tu sau {n_iter} iteration")
    print("V:", V)

    plt.figure()
    plt.plot(deltas)
    plt.xlabel("Iteration")
    plt.ylabel("Delta")
    plt.title("Hoi tu cua Value Iteration")
    plt.yscale("log")
    plt.grid(True)
    plt.savefig("../figures/value_iteration_convergence.png")
    plt.close()
    env.close()


if __name__ == "__main__":
    main()