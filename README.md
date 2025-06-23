# Missionaries and Cannibals Solver 🧩

This Python program solves the classic **Missionaries and Cannibals** problem using **Breadth-First Search (BFS)**.

## Problem Description ✨

There are 3 missionaries and 3 cannibals on one side of a river, along with a boat that can carry at most two people.  
The goal is to move all missionaries and cannibals to the other side of the river without ever leaving more cannibals than missionaries on either bank (to prevent missionaries from being eaten).

## How the Code Works 🔑

- The state of the problem is represented by the number of missionaries and cannibals on the west bank, and the position of the boat.
- The program generates all possible legal successor states (valid moves of the boat carrying 1 or 2 people).
- It uses BFS to search through the state space to find the shortest sequence of moves that leads to the goal (all missionaries and cannibals safely moved to the east bank).
- Once a solution is found, the program prints the sequence of moves describing who moves across the river at each step.

## 🚀 Install & Run

```bash
git clone https://github.com/BrianBiggs4/Missionaries.git
cd missionaries
python missionaries.py
```

## 📚 Acknowledgments/References

This project was inspired and guided by concepts from the book  
**"Classic Computer Science Problems in Python"** by David Kopec.  
It helped shape my understanding of DFS, BFS, and A* search algorithms.

Kopec, D. (2019). *Classic Computer Science Problems in Python*. Manning Publications.
