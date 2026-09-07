
"""Bai 12. MDP hai state"""

P = {
    0: {
        0: [(1.0, 0, 0, False)],
        1: [(0.8, 1, 5, False), (0.2, 0, 0, False)],
    },
    1: {
        0: [(1.0, 0, 1, False)],
        1: [(1.0, 1, 10, True)],
    },
}
N_STATES = 2
N_ACTIONS = 2


def main():
    for s in P:
        for a in P[s]:
            print(f"State {s}, Action {a}: {P[s][a]}")


if __name__ == "__main__":
    main()