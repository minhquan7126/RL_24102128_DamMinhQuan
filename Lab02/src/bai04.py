"""
Bai 04. Tinh distribution sau nhieu buoc (t = 1, 2, 5, 10, 50)
"""

import numpy as np
from bai01 import P


def state_distribution(p0, P, n_steps):
    p = p0.copy()
    for _ in range(n_steps):
        p = p @ P
    return p


def main():
    p0 = np.array([1.0, 0.0, 0.0])

    for t in [1, 2, 5, 10, 50]:
        dist = state_distribution(p0, P, t)
        print(f"t={t:>2}: {dist}")


if __name__ == "__main__":
    main()