"""Bai 07. Undiscounted return"""

def compute_return(rewards, gamma):
    G = 0.0
    for k, r in enumerate(rewards):
        G += (gamma ** k) * r
    return G


def main():
    rewards = [1, 1, 1, 1, 1]
    print("Return (gamma=1.0):", compute_return(rewards, 1.0))


if __name__ == "__main__":
    main()