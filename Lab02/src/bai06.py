"""
Bai 06. So sanh phan phoi ly thuyet va phan phoi mo phong
"""

import numpy as np
from bai01 import P
from bai04 import state_distribution
from bai05 import sample_next_state


def simulate_many_transitions(p0, P, n_transitions, rng):
    n_states = P.shape[0]
    counts = np.zeros(n_states)

    state = rng.choice(n_states, p=p0)
    counts[state] += 1

    for _ in range(n_transitions):
        state = sample_next_state(state, P, rng)
        counts[state] += 1

    return counts / counts.sum()


def main():
    p0 = np.array([1.0, 0.0, 0.0])
    rng = np.random.default_rng(123)

    empirical_dist = simulate_many_transitions(p0, P, 100_000, rng)
    theoretical_dist = state_distribution(p0, P, 50)

    print("Thuc nghiem (100k transitions):", empirical_dist)
    print("Ly thuyet (sau 50 buoc):       ", theoretical_dist)
    print("Sai lech tuyet doi:", np.abs(empirical_dist - theoretical_dist))

    # Nhan xet (3-5 dong):
    # 1. Hai phan phoi rat gan nhau, sai lech chi o bac 10^-3.
    # 2. Chung minh Markov chain hoi tu ve stationary distribution.
    # 3. Sai lech con lai den tu ban chat ngau nhien cua sampling huu han.


if __name__ == "__main__":
    main()