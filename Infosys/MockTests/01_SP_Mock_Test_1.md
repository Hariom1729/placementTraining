# Infosys Specialist Programmer (SP) Mock Test 1

## Overview
- **Role:** Specialist Programmer (SP)
- **Time Limit:** 90 Minutes
- **Total Questions:** 3 (1 Easy, 1 Medium, 1 Hard)
- **Target Score:** Pass 100% of test cases for 2 questions, and at least 40% partial test cases for the Hard question to guarantee a shortlisting.

---

## Question 1: String Palindrome Validation (Easy)

### Problem Statement
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.
A string is considered a palindrome if it reads the same forward and backward after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

### Constraints
- $1 \le s.length \le 2 \times 10^5$
- `s` consists only of printable ASCII characters.

### Examples
**Input:** `"A man, a plan, a canal: Panama"`
**Output:** `true`

---

## Question 2: Find Number of Islands (Medium)

### Problem Statement
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Constraints
- $1 \le m, n \le 300$
- `grid[i][j]` is `'0'` or `'1'`.

### Examples
**Input:** 
```
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
**Output:** `3`

---

## Question 3: Maximum Path Sum in Binary Tree (Hard)

### Problem Statement
A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.
The **path sum** of a path is the sum of the node's values in the path.
Given the `root` of a binary tree, return the maximum **path sum** of any non-empty path.

### Constraints
- The number of nodes in the tree is in the range $[1, 3 \times 10^4]$.
- $-1000 \le Node.val \le 1000$

### Examples
**Input:** `[-10, 9, 20, null, null, 15, 7]` (Level order traversal)
**Output:** `42`
**Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

---

## Solutions & Hints
*Do not look at the hints until you have spent at least 15 minutes on the problem.*

1. **Q1 Hint:** Use two pointers (left and right) and the `isalnum()` and `tolower()` functions in C++. Ignore non-alphanumeric characters.
2. **Q2 Hint:** Use DFS or BFS. When you see a `'1'`, increment a counter and DFS in all 4 directions, converting `'1'` to `'0'` so you don't count it twice. (Solution available in `/Topics/Graph/01_Number_of_Islands.md`).
3. **Q3 Hint:** Use Post-order traversal. For each node, calculate the max path going straight down its left child and right child. The max path through the current node as a curve is `node.val + left_max + right_max`. Return `node.val + max(left_max, right_max)` to the parent. Update a global `max_sum` variable along the way.
