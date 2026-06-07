# Greedy Algorithms

## 1. Theory & Core Concepts

A **Greedy Algorithm** is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
In other words, it makes a locally optimal choice in the hope that this choice will lead to a globally optimal solution.

### Key Characteristics:
1. **Greedy Choice Property:** A global optimum can be arrived at by selecting a local optimum.
2. **Optimal Substructure:** An optimal solution to the problem contains an optimal solution to subproblems.

Unlike Dynamic Programming, greedy algorithms do NOT reconsider their choices. Once a choice is made, it is final. This makes greedy algorithms generally faster (`O(N \log N)` due to sorting, or `O(N)`), but they do not guarantee an optimal solution for all problems. You must mathematically prove that the greedy choice works for a specific problem.

### Common Greedy Patterns:
1. **Activity Selection / Intervals:** Sorting by end time to maximize the number of non-overlapping activities (e.g., N Meetings in One Room).
2. **Fractional Knapsack:** Sorting items by value-to-weight ratio (`val / wt`) and greedily picking the highest ratio.
3. **Scheduling / Jump Games:** Keeping track of the maximum reach or farthest point.
4. **Job Sequencing:** Sorting by profit and assigning the latest possible deadline slot.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Assign_Cookies.md`
*   `02_Fractional_Knapsack.md`
*   `03_Jump_Game.md`
*   `04_Jump_Game_II.md`
*   `05_N_Meetings_in_One_Room.md`
*   *(... and more)*
