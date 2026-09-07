"""
mdp_utils.py

Thu vien dung chung cho Lab02 - chua cac ham Dynamic Programming
duoc tai su dung boi bai21 -> bai36 (khong copy-paste code).

Sinh vien PHAI tu cai dat toan bo logic ben trong cac ham nay.
Khong duoc goi thu vien RL co san (vd: mdptoolbox, stable-baselines, ...).
"""

import numpy as np


def q_from_v(env, V, state, action, gamma=0.99):
    """
    Bai 21. Tinh Q(state, action) tu value function V hien tai,
    theo cong thuc Bellman backup:

        Q(s,a) = sum_{s',r} p(s',r|s,a) * [r + gamma * V(s')]
    """
    # TODO: lay danh sach transition tu env.unwrapped.P[state][action]
    # TODO: cong don theo probability
    pass


def action_values(env, V, state, gamma=0.99):
    """
    Bai 22. Tra ve vector Q(state, .) cho TAT CA action tai 1 state.
    """
    # TODO: goi q_from_v() cho tung action, gom lai thanh vector
    pass


def policy_evaluation(env, policy, gamma=0.99, theta=1e-8, max_iterations=10000):
    """
    Bai 23-25. Iterative Policy Evaluation cho MOT policy cho truoc.
    Dieu kien dung: delta = max|V_new - V_old| < theta.
    """
    n_states = env.observation_space.n
    V = np.zeros(n_states)

    for i in range(max_iterations):
        # TODO: 1 sweep qua tat ca state, tinh new_V[s] tu policy[s] + action_values()
        # TODO: tinh delta = max(|new_V - V|)
        # TODO: neu delta < theta thi dung
        break

    return V, 0


def greedy_policy_from_value(env, V, gamma=0.99):
    """
    Bai 26. Sinh 1 DETERMINISTIC policy: policy[s] = argmax_a Q(s,a)
    """
    n_states = env.observation_space.n
    policy = np.zeros(n_states, dtype=int)
    # TODO: voi moi state, tinh action_values() roi lay argmax
    return policy


def policy_iteration(env, gamma=0.99, theta=1e-8, max_iterations=1000):
    """
    Bai 29-30. Policy Iteration hoan chinh.
    Tra ve: policy, V, n_policy_iterations
    """
    n_states = env.observation_space.n
    policy = np.zeros(n_states, dtype=int)

    for i in range(max_iterations):
        # TODO: policy_evaluation
        # TODO: greedy_policy_from_value
        # TODO: kiem tra policy_stable, neu dung thi break
        break

    V = np.zeros(n_states)
    return policy, V, 0


def value_iteration(env, gamma=0.99, theta=1e-8, max_iterations=10000):
    """
    Bai 31-32. Value Iteration: V_new(s) = max_a Q(s,a)
    Tra ve: V, n_iterations, deltas
    """
    n_states = env.observation_space.n
    V = np.zeros(n_states)
    deltas = []

    for i in range(max_iterations):
        # TODO: 1 sweep, new_V[s] = max(action_values(env, V, s, gamma))
        # TODO: tinh delta, luu vao deltas
        # TODO: neu delta < theta thi dung
        break

    return V, 0, deltas


def evaluate_policy_by_simulation(env, policy, n_episodes=1000, seed=42):
    """
    Bai 34. Chay policy that su tren env bang reset()/step().
    """
    # TODO: for episode in range(n_episodes): reset, loop step() theo policy[obs]
    return {
        "success_rate": 0.0,
        "mean_reward": 0.0,
        "mean_length": 0.0,
        "min_length": 0,
        "max_length": 0,
    }


def print_policy(env, policy):
    """
    Bai 27. In policy dang luoi (4x4), dung mui ten, 'H' cho Hole, 'G' cho Goal.
    """
    ACTION_SYMBOLS = {0: "←", 1: "↓", 2: "→", 3: "↑"}
    # TODO: lay grid tu env.unwrapped.desc, ve theo policy
    pass