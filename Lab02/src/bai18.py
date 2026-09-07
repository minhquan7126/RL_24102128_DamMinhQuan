
"""Bai 18. Ham describe_state()"""

import gymnasium as gym

ACTION_NAMES = {0: "LEFT", 1: "DOWN", 2: "RIGHT", 3: "UP"}


def describe_state(env, state):
    print(f"--- State {state} ---")
    for action in range(env.action_space.n):
        print(f"  {ACTION_NAMES[action]}: {env.unwrapped.P[state][action]}")


def main():
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    for s in [0, 1, 14]:
        describe_state(env, s)
    env.close()


if __name__ == "__main__":
    main()