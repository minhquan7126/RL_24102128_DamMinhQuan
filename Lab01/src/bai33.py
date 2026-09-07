# Muc dich: viet ham run_episode dung chung cho moi environment/policy
import gymnasium as gym

def run_episode(env, policy, seed=None, max_steps=1000):
    observation, info = env.reset(seed=seed)
    total_reward = 0.0
    length = 0
    terminated = truncated = False

    for _ in range(max_steps):
        action = policy(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        length += 1
        if terminated or truncated:
            break

    return {
        "reward": total_reward,
        "length": length,
        "terminated": terminated,
        "truncated": truncated,
    }

if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    random_policy = lambda obs: env.action_space.sample()
    result = run_episode(env, random_policy, seed=42)
    print(result)
    env.close()