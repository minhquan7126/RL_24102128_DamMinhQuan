"""
Bai 05. Mo phong Markov chain bang sampling
"""

import numpy as np
from bai01 import P, STATE_NAMES


def sample_next_state(current_state, P, rng):
    n_states = P.shape[0]
    probs = P[current_state]
    return rng.choice(n_states, p=probs)


def main():
    rng = np.random.default_rng(seed=42)

    state = 0  # bat dau o Sunny
    trajectory = [state]

    for _ in range(30):
        state = sample_next_state(state, P, rng)
        trajectory.append(state)

    print("Chuoi state (so):", trajectory)
    print("Chuoi state (ten):", [STATE_NAMES[s] for s in trajectory])


if __name__ == "__main__":
    main()