"""
Bai 03. Tinh xac suat trang thai ke tiep sau 1 buoc
"""

import numpy as np
from bai01 import P, STATE_NAMES


def main():
    p0 = np.array([1.0, 0.0, 0.0])  # chac chan dang o Sunny

    p1 = p0 @ P

    print("Phan phoi ban dau p0:", p0)
    print("Phan phoi sau 1 buoc p1:", p1)
    for name, prob in zip(STATE_NAMES, p1):
        print(f"  {name}: {prob:.4f}")


if __name__ == "__main__":
    main()