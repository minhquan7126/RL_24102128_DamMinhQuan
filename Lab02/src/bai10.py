
"""Bai 10. Anh huong cua gamma len G_0 - luu figures/gamma_comparison.png"""

import numpy as np
import matplotlib.pyplot as plt
from bai09 import discounted_returns


def main():
    rewards = [0, 0, 0, 0, 10]
    gammas = np.linspace(0, 1, 101)
    G0_values = [discounted_returns(rewards, g)[0] for g in gammas]

    plt.figure()
    plt.plot(gammas, G0_values)
    plt.xlabel("Gamma")
    plt.ylabel("G_0")
    plt.title("Anh huong cua Gamma len Return G_0")
    plt.grid(True)
    plt.savefig("../figures/gamma_comparison.png")
    plt.close()
    print("Da luu figures/gamma_comparison.png")


if __name__ == "__main__":
    main()