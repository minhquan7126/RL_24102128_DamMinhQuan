"""Bai 08. Discounted return voi nhieu gia tri gamma"""

from bai07 import compute_return

def main():
    rewards = [1, 1, 1, 1, 1]
    gammas = [0.0, 0.5, 0.9, 0.99, 1.0]

    print(f"{'Gamma':>6} | {'Return':>8}")
    for g in gammas:
        G = compute_return(rewards, g)
        print(f"{g:>6.2f} | {G:>8.4f}")


if __name__ == "__main__":
    main()