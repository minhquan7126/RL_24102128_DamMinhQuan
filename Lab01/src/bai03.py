# Muc dich: kham pha action_space va tu dong lay so luong action
import gymnasium as gym

env = gym.make("CartPole-v1")
print("Action space:", env.action_space)

# Discrete co thuoc tinh .n cho biet so luong gia tri co the
n_actions = env.action_space.n
print("Number of actions:", n_actions)

env.close()