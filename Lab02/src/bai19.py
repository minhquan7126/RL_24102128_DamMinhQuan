
"""Bai 19. Kiem tra tong xac suat transition"""

import numpy as np
import gymnasium as gym


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    all_valid = True

    for s in range(env.observation_space.n):
        for a in range(env.action_space.n):
            probs = [t[0] for t in env.unwrapped.P[s][a]]
            if not np.isclose(sum(probs), 1.0):
                print(f"Sai tai state={s}, action={a}")
                all_valid = False

    print("Tat ca transition hop le:", all_valid)
    env.close()


if __name__ == "__main__":
    main()