
"""Bai 09. Return tu cuoi episode ve dau"""

def discounted_returns(rewards, gamma):
    G = 0.0
    returns = []
    for r in reversed(rewards):
        G = r + gamma * G
        returns.insert(0, G)
    return returns


def main():
    rewards = [0, 0, 0, 1]
    returns = discounted_returns(rewards, gamma=0.9)
    for t, G in enumerate(returns):
        print(f"G_{t} = {G:.4f}")


if __name__ == "__main__":
    main()