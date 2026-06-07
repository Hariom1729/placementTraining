# Dynamic Programming (DP)

## 1. Theory & Core Concepts

Dynamic Programming is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

### Two Key Characteristics:
1. **Overlapping Subproblems:** The problem can be broken down into subproblems which are reused several times.
2. **Optimal Substructure:** An optimal solution can be constructed efficiently from optimal solutions of its subproblems.

### Two Approaches:
1. **Top-Down with Memoization:** Write a recursive function and save the answers to subproblems in a Hash Map or Array.
   - *Pros:* Easier to write, only computes what is necessary.
   - *Cons:* Overhead of recursive calls.
2. **Bottom-Up with Tabulation:** Avoid recursion. Start from the base cases and build up the answer in an Array/Matrix.
   - *Pros:* No recursion overhead, often allows for space optimization.
   - *Cons:* Computes all subproblems, even those not strictly needed.

### Common DP Patterns:
1. **1D DP:** `dp[i]` represents the answer for prefix `i`. (e.g., Climbing Stairs, House Robber).
2. **2D DP (Grids/Matrices):** `dp[i][j]` represents the answer for reaching cell `(i, j)`. (e.g., Unique Paths, Minimum Path Sum).
3. **Subsequences (String/Array):** `dp[i][j]` represents the answer for index `i` of string A and index `j` of string B. (e.g., LCS, Edit Distance).
4. **0/1 Knapsack:** "Include or Exclude" pattern. `dp[i][w]` represents using items up to index `i` with capacity `w`.
5. **Unbounded Knapsack:** Items can be chosen multiple times. (e.g., Coin Change).

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Climbing_Stairs.md`
*   `02_Coin_Change.md`
*   `03_Longest_Common_Subsequence.md`
*   `04_0_1_Knapsack_Problem.md`
*   `05_Longest_Increasing_Subsequence.md`
*   *(... and more)*
