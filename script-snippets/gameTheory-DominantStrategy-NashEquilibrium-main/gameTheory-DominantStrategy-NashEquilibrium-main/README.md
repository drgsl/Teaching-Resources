# Game Theory Dominant Strategy and Nash Equilibrium Calculator

This Python script calculates the dominant strategy and Nash equilibrium for a given player in game theory.

## Usage
The script reads a game file in the following format:

```
Player 1 Move 1	Player 1 Move 2	Player 1 Move 3	
Player 2 Move 1	 1/1	        2/3	        0/0	
Player 2 Move 2	-1/3	        0/2	        3/3	
Player 2 Move 3	 1/2	        1/1	        0/0	
```

### Running
To run the script, execute the following command:

```
python dominant_strategy.py
```

### Output
The script outputs the following:

- The best move for player 1
- The best move for player 2
- The Nash equilibria (if any)
