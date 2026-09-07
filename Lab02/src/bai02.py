"""
Bai 02. Kiem tra tinh hop le cua transition matrix
"""

import numpy as np
from bai01 import P


def validate_transition_matrix(P, tol=1e-10):
    P = np.asarray(P)

    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        print("Loi: P khong phai ma tran vuong.")
        return False

    if np.any(P < 0) or np.any(P > 1):
        print("Loi: co phan tu ngoai khoang [0, 1].")
        return False

    row_sums = P.sum(axis=1)
    if not np.allclose(row_sums, 1.0, atol=tol):
        print("Loi: co hang khong tong bang 1:", row_sums)
        return False

    return True


def main():
    print("P hop le:", validate_transition_matrix(P))

    bad_P = np.array([[0.5, 0.6], [0.3, 0.7]])
    print("bad_P hop le:", validate_transition_matrix(bad_P))


if __name__ == "__main__":
    main()