# -*- coding: utf-8 -*-
"""Blackjack.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bcExNKmKM0bH8CF7np_Ij12U2E2TwOf9
"""

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
from collections import defaultdict
import numpy as np
from tqdm import tqdm
import gymnasium as gym
import pickle

env = gym.make("Blackjack-v1", sab=True)
def default_q_values():
    return np.zeros(env.action_space.n)
class BlackjackAgent:
    def __init__(self, learning_rate, initial_epsilon, epsilon_decay, final_epsilon, discount_factor=0.95):
        # self.q_values = defaultdict(lambda: np.zeros(env.action_space.n))
        self.q_values = defaultdict(default_q_values)
        self.lr = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.training_error = []

    def get_action(self, obs):
        if np.random.random() < self.epsilon:
            return env.action_space.sample()
        return int(np.argmax(self.q_values[obs]))

    def update(self, obs, action, reward, terminated, next_obs):
        future_q_value = (not terminated) * np.max(self.q_values[next_obs])
        td = reward + self.discount_factor * future_q_value - self.q_values[obs][action]
        self.q_values[obs][action] += self.lr * td
        self.training_error.append(td)

    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)


def train_blackjack(n_episodes=1000000):
    global agent
    agent = BlackjackAgent(
        learning_rate=0.1,
        initial_epsilon=1.0,
        epsilon_decay=1.0 / (n_episodes / 2),
        final_epsilon=0.1,
    )
    env = gym.make("Blackjack-v1", sab=True)
    env = gym.wrappers.RecordEpisodeStatistics(env, n_episodes)
    for episode in tqdm(range(n_episodes)):
        obs, info = env.reset()
        done = False
        while not done:
            action = agent.get_action(obs)
            next_obs, reward, terminated, truncated, info = env.step(action)
            agent.update(obs, action, reward, terminated, next_obs)
            done = terminated or truncated
            obs = next_obs
        agent.decay_epsilon()
    with open("blackjack_agent.pkl", "wb") as f:
        pickle.dump(agent, f)
    print("Training complete and agent saved.")


def test_blackjack_one_episode():
    try:
        with open("blackjack_agent.pkl", "rb") as f:
            agent = pickle.load(f)
    except FileNotFoundError:
        print("No trained agent found.")
        return

    agent.epsilon = 0.0
    env = gym.make("Blackjack-v1", sab=True, render_mode="rgb_array")
    obs, info = env.reset()
    done = False
    frames = []

    while not done:
        frames.append(env.render())
        action = agent.get_action(obs)
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

    print("Final Reward:", reward)
    plt.imshow(frames[-1])
    plt.axis("off")
    plt.title(f"Final Reward: {reward}")
    plt.show()

    fig = plt.figure(figsize=(6, 4))
    img = plt.imshow(frames[0])
    plt.axis("off")

    def animate(i):
        img.set_data(frames[i])
        return [img]

    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=500, blit=True)
    anim.save("blackjack_agent.gif", writer=PillowWriter(fps=2))
    print("Animation saved as blackjack_agent.gif")


def test_blackjack_multiple_episodes(num_test_episodes=5):
    try:
        with open("blackjack_agent.pkl", "rb") as f:
            agent = pickle.load(f)
    except FileNotFoundError:
        print("No trained agent found.")
        return

    agent.epsilon = 0.0
    for episode_num in range(1, num_test_episodes + 1):
        env = gym.make("Blackjack-v1", sab=True, render_mode="rgb_array")
        obs, info = env.reset()
        done = False
        frames = []
        print(f"\n--- Test Episode {episode_num} ---")
        print("Initial Observation:", obs)
        while not done:
            frames.append(env.render())
            action = agent.get_action(obs)
            print(f"Agent action: {'Hit' if action == 1 else 'Stick'}, Obs: {obs}")
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
        print("Final Reward:", reward)

        fig = plt.figure(figsize=(6, 4))
        img = plt.imshow(frames[0])
        plt.axis("off")

        def animate(i):
            img.set_data(frames[i])
            return [img]

        anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=500, blit=True)
        anim.save(f"blackjack_ep{episode_num}.gif", writer=PillowWriter(fps=2))
        print(f"Saved GIF as blackjack_ep{episode_num}.gif")


def test_blackjack_statistics(n=1000):
    try:
        with open("blackjack_agent.pkl", "rb") as f:
            agent = pickle.load(f)
    except FileNotFoundError:
        print("No trained agent found.")
        return

    agent.epsilon = 0.0
    env = gym.make("Blackjack-v1", sab=True)
    wins, draws, losses = 0, 0, 0

    for _ in range(n):
        obs, info = env.reset()
        done = False
        while not done:
            action = agent.get_action(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
        if reward == 1.0:
            wins += 1
        elif reward == 0.0:
            draws += 1
        else:
            losses += 1

    print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")

def test_blackjack():
    print("\nBlackjack Testing Options:")
    print("1. Run and visualize one episode")
    print("2. Run and visualize multiple episodes")
    print("3. Evaluate statistics over 1000 episodes")
    choice = input("Enter choice (1, 2, or 3): ").strip()

    if choice == "1":
        test_blackjack_one_episode()
    elif choice == "2":
        test_blackjack_multiple_episodes()
    elif choice == "3":
        test_blackjack_statistics()
    else:
        print("Invalid choice.")