# AI_GAME

# Reinforcement Learning Game Suite

This project is a modular reinforcement learning framework for training and testing agents across multiple OpenAI Gym environments and custom games. It includes support for:

- **Cliff Climbing (Q-Learning & SARSA)**
- **Taxi-v3 (Q-Learning)**
- **Blackjack-v1 (Q-Learning)**
- **MountainCar-v0 (Deep Q-Learning)**

The user can interactively choose to **train** or **test** any of the included environments.

---

## 📁 Project Structure

```
.
├── blackjack.py          # Blackjack Q-learning agent
├── cliff_climbing.py     # Cliff Climbing Q-learning and SARSA agents
├── main.py               # Entry point for training/testing via terminal
├── mountaincar.py        # MountainCar Deep Q-Learning agent
├── taxi.py               # Taxi Q-learning agent
├── __pycache__/          # Compiled Python cache files
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies

Make sure you have the required libraries installed:

```bash
pip install gymnasium torch matplotlib numpy
```

### 2. Run the Program

```bash
python main.py
```

You will be prompted to choose whether to **train** or **test**, followed by selecting a game.

---

## 🎮 Environments

---

### `cliff_climbing.py` - Cliff Climbing (Q-Learning and SARSA)

Implements both **Q-Learning** and **SARSA** for the **CliffWalking-v0** environment.

- **Q-Learning**: Off-policy TD control
- **SARSA**: On-policy TD control
- Tracks and prints total rewards over episodes
- Compares performance visually

#### Example Usage

```bash
# Train Q-Learning agent
python main.py → Train → Cliff Climbing

# Test trained Q-table
python main.py → Test → Cliff Climbing
```
![SARSA Final Test](https://github.com/user-attachments/assets/696706ca-eac7-4e6d-963a-93f7a969b44a)
![Q-Learning Final Test](https://github.com/user-attachments/assets/5b3d20dc-c6e8-4c8a-b951-4b7baf5c2d48)

---

### `taxi.py` - Taxi-v3 with Q-Learning

Implements a Q-Learning agent for OpenAI's **Taxi-v3** environment.

- Uses ε-greedy policy
- Saves and loads Q-tables via pickle
- Visualizes reward trends

#### Key Functions

- `train_taxi(episodes=5000)`: Trains the agent
- `test_taxi()`: Loads `taxi_q_table.pkl` and tests the agent


![taxi_episode_4](https://github.com/user-attachments/assets/9a06448d-76da-4057-98d6-72b03ec2992e)

---

### `blackjack.py` - Blackjack-v1 with Q-Learning

Implements a Q-Learning agent for **Blackjack-v1** using discrete state encoding.

- Visualizes state-action values via 3D surface plots
- Encodes state as a tuple: `(player_sum, dealer_card, usable_ace)`

#### Key Functions

- `train_blackjack(episodes=500000)`: Trains the agent and saves Q-table
- `test_blackjack()`: Tests the trained agent


![blackjack_ep4](https://github.com/user-attachments/assets/48c69c4b-dfe6-4e07-a664-be4551063309)

---

### `mountaincar.py` - MountainCar Deep Q-Learning (DQL)

This module solves the **MountainCar-v0** problem using **Deep Q-Learning** with PyTorch.

#### Features

- DQN with experience replay
- Target network synchronization
- Epsilon decay for exploration
- Saves model (`best_model.pt`) during training
- Outputs GIFs of testing runs

#### Key Functions

- `train_mountaincar()`: Trains the DQN for 20,000 episodes
- `test_mountaincar()`: Loads `best_model.pt` and generates episode GIFs

#### Output Example

Testing will generate:
```
./gifs/mountaincar_test_episode_0.gif
./gifs/mountaincar_test_episode_1.gif
...
```
![mountaincar_test_episode_9](https://github.com/user-attachments/assets/4a380d89-8c25-474b-9306-bc2fe452c9af)

---
🎮 Included Environments

🧱 Cliff Climbing (cliff_climbing.py)
Q-Learning and SARSA for CliffWalking-v0

Visual reward comparisons

🚕 Taxi-v3 (taxi.py)
Classic discrete environment with Q-Learning

Saves and loads Q-table with pickle

🃏 Blackjack-v1 (blackjack.py)
Q-Learning with 3D surface plots

Tracks usable ace and dealer showing card

⛰️ MountainCar-v0 (mountaincar.py)
Deep Q-Learning with PyTorch

Saves model + outputs testing GIFs to gifs/


## 🧠 How It Works

Each environment is encapsulated in its own file. The main entry point (`main.py`) provides a CLI menu that lets you choose:

- Mode: **Train** or **Test**
- Environment: **Cliff Climbing**, **Taxi**, **Blackjack**, or **MountainCar**

Training functions save Q-tables or models, and testing functions load them automatically.

---

## 📊 Visualizations

- `blackjack.py`: 3D surface plots of optimal policy
- `mountaincar.py`: GIF animations of agent behavior
- `cliff_climbing.py`: Line graphs comparing SARSA vs Q-learning

---

## 📦 Dependencies

Ensure these libraries are available in your environment:

- `gymnasium`
- `numpy`
- `matplotlib`
- `torch`
- `pickle`

Install using:

```bash
pip install gymnasium torch matplotlib numpy
```

---

## ✅ To Do

- [x] Add MountainCar DQL support
- [x] Integrate all games into `main.py`
- [x] Add test mode for all environments

---

## 👨‍💻 Author

Developed by 

TEAM LEADER NAME – PRIYANSHI AGRAWAL  

ROLL NO – 2301CS90 

MEMBER 2 NAME – MANVITHA REDDY 

ROLL NO – 2301CS29 

MEMBER 3 NAME – SHIKSHA RAGINEE 

ROLL NO – 2301AI13 

MEMBER 4 NAME – GOMPA VASAVI  

ROLL NO – 2301AI43 

MEMBER 5 NAME – PREETHI 

ROLL NO – 2301AI17 

MEMBER 6 NAME – GURU SAI BHASKARI  

ROLL NO – 2301AI19

as part of a Reinforcement Learning project to explore different RL algorithms in classic environments.

---
