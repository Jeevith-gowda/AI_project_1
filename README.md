# 8-Puzzle Solver using A* Search 

This project is a Python implementation of the A* search algorithm to solve the classic 8-puzzle problem. It allows users to input any initial and goal state and finds the optimal solution path using two different heuristics for comparison.



---
## About The Project

The goal of this project is to demonstrate the A* search algorithm and analyze the performance of different heuristic functions. The A* algorithm finds the shortest path by combining the cost to reach the current state (`g-cost`) with an estimated cost to the goal (`h-cost`).

This implementation includes:
* A robust A* search algorithm.
* A solvability check to determine if a solution is possible.
* Two classic heuristics for performance comparison:
    1.  **Misplaced Tiles**: Counts the number of tiles not in their goal position.
    2.  **Manhattan Distance**: Sums the distances of each tile from its goal position.

---
## Features

* **Solves any valid 8-puzzle**: Provide your own start and goal configurations.
* **Solvability Check**: Instantly determines if a puzzle is solvable before starting the search.
* **Heuristic Comparison**: Automatically solves the puzzle using both heuristics and reports performance metrics for each.
* **Performance Metrics**: Reports the number of moves in the solution, total nodes generated, and total nodes expanded.

---
## Getting Started

All you need is Python 3 installed on your system.

1.  Clone this repository or download the source code.
2.  Open a terminal or command prompt in the project directory.

---
## Usage

Run the main script from your terminal:

```bash
python eight_puzzle.py
```

The program will then prompt you to enter the initial and goal states. Enter the numbers for each row, separated by spaces. Use `0` to represent the empty tile.

### Example

```
Enter the initial state (3x3 grid, use 0 for empty space):
7 2 4
5 0 6
8 3 1

Enter the goal state (3x3 grid, use 0 for empty space):
1 2 3
4 5 6
7 8 0

--- Solving with h1: Misplaced Tiles Heuristic ---
Path found in 20 moves.
Nodes Generated: 106093
Nodes Expanded: 39556

--- Solving with h2: Manhattan Distance Heuristic ---
Path found in 20 moves.
Nodes Generated: 2479
Nodes Expanded: 940
```

---
## Author

* **Jeevith Doddalingegowda Rama** - *https://github.com/Jeevith-gowda*
