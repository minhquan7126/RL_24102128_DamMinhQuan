
"""Bai 20. So sanh FrozenLake deterministic vs stochastic"""

import gymnasium as gym

RIGHT = 2


def main():
    for slippery in [False, True]:
        env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=slippery)
        transitions = env.unwrapped.P[0][RIGHT]
        print(f"is_slippery={slippery}: {len(transitions)} transition(s)")
        for prob, next_state, reward, terminated in transitions:
            print(f"  prob={prob}, next_state={next_state}")
        env.close()

    # Ket luan: khi is_slippery=True, moi action co the dan den 3 next_state
    # khac nhau (do truot ngang), moi cai xac suat ~0.333. Khi False, chi co
    # dung 1 next_state voi xac suat 1.0 - hanh vi hoan toan xac dinh.


if __name__ == "__main__":
    main()