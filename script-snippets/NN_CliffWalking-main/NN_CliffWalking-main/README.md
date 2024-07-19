# Reinforcement Learning - Cliff Walking

This repository contains a Python implementation of a reinforcement learning agent solving the Cliff Walking problem.

## Problem Description

The agent is situated on a grid with dimensions 4x12. The start state is the bottom left cell of the grid and the goal state is the bottom right cell. The agent must navigate to the goal state while avoiding a cliff of cells located on the bottom row, between the start and goal cells. If the agent falls off the cliff, it is reset to the start state.

The agent has four possible actions: up, down, left, and right. Each action incurs a reward of -1. The goal state has a reward of +100 and falling off the cliff incurs a penalty of -100.

## Solution
The agent uses a Q-learning algorithm to learn an optimal policy for navigating the grid. The Q-learning algorithm maintains a Q-table that maps states and actions to their expected future rewards. During training, the agent uses an epsilon-greedy policy to choose actions based on the Q-table. As the agent becomes more confident in the Q-values, the value of epsilon is gradually reduced to shift the agent towards more exploitation and less exploration.

## Requirements
- Python 3.6 or later
- NumPy
- Matplotlib
- Gym

## Usage
To run the script, simply execute the following command:

```
python NN_CliffWalking.py
```
This will train the agent using the default hyperparameters and output the average reward obtained during each epoch. The script also outputs a plot of the average reward over time.

## Hyperparameters
The following hyperparameters can be modified to adjust the behavior of the agent:

- `LEARNING_RATE`: The learning rate determines the extent to which newly acquired information overrides old information.
- `DISCOUNT`: The discount factor determines the extent to which future rewards are considered when calculating the Q-values.
- `EPOCHS`: The number of epochs to train the agent for.

## Results
After training the agent for 1000 epochs, the average reward per epoch increases from -1300 to +50. This demonstrates that the agent has learned to navigate to the goal state while avoiding the cliff.

On average, the agent was able to reach the goal state in 14 steps after 27 epochs of training.
