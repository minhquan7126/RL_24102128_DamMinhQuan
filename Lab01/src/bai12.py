# Muc dich: viet lai random_agent, khong dung bien 'done', tu tao episode_finished
# va bao cao rieng nguyen nhan ket thuc (Termination / Truncation)
import gymnasium as gym

def random_agent_v2(env, max_steps=500):
    observation, info = env.reset()
    total_reward = 0.0
    episode_length = 0
    reason = None

    for _ in range(max_steps):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        episode_length += 1

        episode_finished = terminated or truncated
        if episode_finished:
            reason = "Termination" if terminated else "Truncation"
            break

    return total_reward, episode_length, reason

if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    total_reward, episode_length, reason = random_agent_v2(env)
    print("Total reward:", total_reward)
    print("Episode length:", episode_length)
    print("Ly do ket thuc:", reason)
    env.close()