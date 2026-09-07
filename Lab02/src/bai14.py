
"""Bai 14. Deterministic policy"""

import numpy as np

def print_policy(policy):
    for s, a in enumerate(policy):
        print(f"State {s}: Action {a}")


def main():
    policy = np.array([1, 1])
    print_policy(policy)


if __name__ == "__main__":
    main()