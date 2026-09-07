"""
Bai 01. Tao transition matrix cho Markov chain (Sunny/Cloudy/Rainy)
"""

import numpy as np

STATE_NAMES = ["Sunny", "Cloudy", "Rainy"]

P = np.array([
    [0.7, 0.2, 0.1],   # tu Sunny:  70% van nang, 20% chuyen may, 10% chuyen mua
    [0.3, 0.4, 0.3],   # tu Cloudy: 30% nang, 40% van may, 30% mua
    [0.2, 0.3, 0.5],   # tu Rainy:  20% nang, 30% may, 50% van mua
])


def main():
    print("Transition matrix P:")
    print(P)
    print("Tong moi hang:", P.sum(axis=1))


if __name__ == "__main__":
    main()