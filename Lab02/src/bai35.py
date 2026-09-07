
"""Bai 35. So sanh Value Iteration va Policy Iteration"""

from time import perf_counter
import matplotlib.pyplot as plt
import gymnasium as gym
from mdp_utils import value_iteration, policy_iteration, greedy_policy_from_value, evaluate_policy_by_simulation


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)

    t0 = perf_counter()
    V_vi, n_iter_vi, _ = value_iteration(env, gamma=0.99)
    time_vi = perf_counter() - t0
    policy_vi = greedy_policy_from_value(env, V_vi, gamma=0.99)
    result_vi = evaluate_policy_by_simulation(env, policy_vi, n_episodes=1000)

    t0 = perf_counter()
    policy_pi, V_pi, n_iter_pi = policy_iteration(env, gamma=0.99)
    time_pi = perf_counter() - t0
    result_pi = evaluate_policy_by_simulation(env, policy_pi, n_episodes=1000)

    print(f"{'Thuat toan':<20}{'So vong lap':>12}{'Thoi gian':>12}{'Success':>10}{'MeanR':>8}")
    print(f"{'Value Iteration':<20}{n_iter_vi:>12}{time_vi:>12.4f}{result_vi['success_rate']:>10.2f}{result_vi['mean_reward']:>8.2f}")
    print(f"{'Policy Iteration':<20}{n_iter_pi:>12}{time_pi:>12.4f}{result_pi['success_rate']:>10.2f}{result_pi['mean_reward']:>8.2f}")

    plt.figure()
    plt.bar(["Value Iteration", "Policy Iteration"], [time_vi, time_pi])
    plt.ylabel("Thoi gian (s)")
    plt.title("So sanh thoi gian chay: Value Iteration vs Policy Iteration")
    plt.savefig("../figures/algorithm_comparison.png")
    plt.close()

    env.close()


if __name__ == "__main__":
    main()