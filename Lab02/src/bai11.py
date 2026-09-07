
"""Bai 11. Reward som vs reward tre theo gamma"""

import numpy as np
from bai09 import discounted_returns


def main():
    sequence_A = [5, 0, 0, 0, 0]
    sequence_B = [0, 0, 0, 0, 10]

    gammas = np.linspace(0, 1, 1001)
    crossover = None
    for g in gammas:
        G_A = discounted_returns(sequence_A, g)[0]
        G_B = discounted_returns(sequence_B, g)[0]
        if G_B > G_A and crossover is None:
            crossover = g

    print(f"B > A khi gamma > {crossover:.4f}")


if __name__ == "__main__":
    main()