# AA-Tournament

# Enhanced Adaptive Strategy for Iterated Prisoner's Dilemma

## Overview

This repository contains an advanced algorithm for the Iterated Prisoner's Dilemma game that employs pattern recognition, opponent modeling, and adaptive response mechanisms to maximize long-term payoff across a variety of opponent strategies.

## Algorithm Description

The Enhanced Adaptive Strategy is designed to:

1. Identify common opponent strategies (Tit-for-Tat, Random, Exploitative)
2. Detect and adapt to repeating patterns in opponent behavior
3. Maintain cooperation with cooperative players
4. Defend against exploitation attempts
5. Break out of mutual defection cycles

## Key Features

### Pattern Recognition

- **Tit-for-Tat Detection**: Identifies when opponents are mirroring our previous moves, with tolerance for occasional deviations
- **Random Strategy Detection**: Recognizes opponents using randomized strategies by analyzing move distribution
- **Exploitation Pattern Detection**: Determines if opponents systematically defect after our cooperation
- **Sequence Detection**: Identifies repeating patterns of any length in opponent's move history

### Adaptive Response System

- Employs different counter-strategies based on recognized opponent behavior
- Uses a sliding window approach to evaluate recent opponent cooperation rate
- Implements targeted responses to specific patterns rather than one-size-fits-all

### Cycle Breaking

- Uses probabilistic forgiveness (20% chance) to break out of mutual defection cycles
- Specifically attempts to recover from extended periods of mutual defection

### Strategic Defaults

- Always cooperates in the first round
- Always defects in the final round of known-length games
- Uses a modified Tit-for-Tat with forgiveness as the default strategy

## Implementation

```python
def enhanced_strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    # Implementation details...
```

The function takes three parameters:
- `my_history`: List of your previous moves (1 = cooperate, 0 = defect)
- `opponent_history`: List of opponent's previous moves
- `rounds`: Total number of rounds if known, otherwise None

Returns:
- `1` for cooperation
- `0` for defection

## Performance

This strategy performs exceptionally well against:
- Tit-for-Tat and its variants
- Always Defect/Always Cooperate strategies
- Random strategies
- Pattern-based strategies
- Exploitative strategies

The algorithm's strength lies in its ability to identify opponent patterns and adapt its strategy accordingly, while maintaining the possibility of mutual cooperation with cooperative players.

## Usage Example

```python
# Example tournament setup
my_moves = []
opponent_moves = []
total_rounds = 200

for round_num in range(total_rounds):
    my_move = enhanced_strategy(my_moves, opponent_moves, total_rounds)
    opponent_move = opponent_strategy(opponent_moves, my_moves, total_rounds)
    
    my_moves.append(my_move)
    opponent_moves.append(opponent_move)
```

## References

- Axelrod, R. (1984). The Evolution of Cooperation
- Press, W. & Dyson, F. (2012). Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent
- Wang, Z., & Kokubo, S. (2017). Memory-one strategies in repeated games