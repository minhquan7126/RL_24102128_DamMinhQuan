
"""Bai 17. In transition model cua state 0"""

import gymnasium as gym

ACTION_NAMES = {0: "LEFT", 1: "DOWN", 2: "RIGHT", 3: "UP"}


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    state = 0

    for action in range(env.action_space.n):
        print(f"Action: {ACTION_NAMES[action]}")
        for prob, next_state, reward, terminated in env.unwrapped.P[state][action]:
            print(f"  prob={prob}, next_state={next_state}, reward={reward}, terminated={terminated}")
    env.close()


if __name__ == "__main__":
    main()