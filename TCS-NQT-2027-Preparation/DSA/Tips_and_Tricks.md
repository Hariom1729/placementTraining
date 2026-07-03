# 💡 DSA Tips & Pattern Recognition Tricks

During coding tests like TCS NQT or Zoho, recognizing the underlying pattern is 80% of the work. If you know *which* algorithm to use just by reading the problem statement, writing the code becomes significantly faster.

Here is a cheat sheet of keywords and patterns to help you instantly map a problem to the correct Data Structure or Algorithm.

---

## 1. Arrays & Subarrays
* **Keyword:** "Sorted Array", "Search an element", "Find a target in $O(\log N)$ time"
  * 👉 **Trick:** Use **Binary Search**.
* **Keyword:** "Find two numbers that sum to a target", "Pair with given sum"
  * 👉 **Trick:** If the array is sorted, use **Two Pointers**. If unsorted, use a **Hash Map** (`unordered_map`).
* **Keyword:** "Subarray", "Contiguous elements", "Longest/Shortest sequence"
  * 👉 **Trick:** Think **Sliding Window**. If window size is fixed, it's a static window. If finding max/min length, it's a dynamic window.
* **Keyword:** "Sum of elements between index L and R"
  * 👉 **Trick:** Precompute a **Prefix Sum Array**. It reduces range sum queries to $O(1)$ time.
* **Keyword:** "Majority Element", "Element appearing more than N/2 times"
  * 👉 **Trick:** Use **Moore's Voting Algorithm** for $O(N)$ time and $O(1)$ space.

## 2. Strings
* **Keyword:** "Anagram", "Permutations of a string", "Character frequencies"
  * 👉 **Trick:** Use a **Frequency Map / Array of size 26/256**. For anagrams, count frequencies of string A, subtract frequencies of string B.
* **Keyword:** "Palindrome"
  * 👉 **Trick:** Use **Two Pointers** starting at index `0` and `length - 1` and move inward.
* **Keyword:** "Longest Palindromic Substring"
  * 👉 **Trick:** Use **Expand Around Center**. For every character, expand outward left and right as long as characters match.

## 3. Stacks & Queues
* **Keyword:** "Next Greater Element", "Next Smaller Element", "Largest Rectangle in Histogram"
  * 👉 **Trick:** Use a **Monotonic Stack**. (A stack that remains constantly increasing or decreasing).
* **Keyword:** "Valid Parentheses", "Matching brackets"
  * 👉 **Trick:** Use a **Stack**. Push open brackets, pop and compare for closing brackets.
* **Keyword:** "Sliding Window Maximum/Minimum"
  * 👉 **Trick:** Use a **Deque** (Double Ended Queue).

## 4. Linked Lists
* **Keyword:** "Find the middle of the linked list"
  * 👉 **Trick:** Use **Slow and Fast Pointers**. Slow moves 1 step, fast moves 2 steps. When fast reaches the end, slow is at the middle.
* **Keyword:** "Detect a Cycle / Loop"
  * 👉 **Trick:** **Floyd’s Tortoise and Hare Algorithm** (Slow and Fast Pointers). If they meet, there is a cycle.
* **Keyword:** "Reverse a Linked List"
  * 👉 **Trick:** Use three pointers: `prev`, `curr`, and `next`. 

## 5. Trees & Graphs
* **Keyword:** "Level order traversal", "Shortest path in an unweighted graph"
  * 👉 **Trick:** Use **BFS (Breadth First Search)** with a Queue.
* **Keyword:** "Root to leaf path", "All combinations/permutations", "Maze solving"
  * 👉 **Trick:** Use **DFS (Depth First Search)** with Recursion / Backtracking.
* **Keyword:** "Shortest path in a weighted graph"
  * 👉 **Trick:** Use **Dijkstra's Algorithm**.

## 6. Dynamic Programming (DP)
* **Keyword:** The problem asks to find the **Maximum**, **Minimum**, **Longest**, **Shortest**, or **"Number of ways"**.
  * 👉 **Trick:** Can you break it into smaller overlapping subproblems? Yes? It's **DP**.
* **Keyword:** "Given weights and values, find maximum value for a given capacity"
  * 👉 **Trick:** **0/1 Knapsack Pattern** (Standard 2D DP).
* **Keyword:** "Longest Common Subsequence", "Edit Distance"
  * 👉 **Trick:** **LCS Pattern** (Compare two strings with a 2D DP table).

## 7. Math & Bit Manipulation
* **Keyword:** "Missing Number from 1 to N"
  * 👉 **Trick:** Use the math formula: `Sum = N * (N + 1) / 2`. Subtract array elements from `Sum`.
* **Keyword:** "Check if a number is a power of 2"
  * 👉 **Trick:** Use Bitwise AND: `(N & (N - 1)) == 0`.
* **Keyword:** "Find the only number that appears once (others appear twice)"
  * 👉 **Trick:** Use **Bitwise XOR (`^`)**. `A ^ A = 0`, so all pairs cancel out, leaving the single number.

---

### 🔥 General Interview Tricks
1. **Never jump straight to coding:** Talk out loud. Explain the brute force $O(N^2)$ approach first, then optimize it.
2. **Handle Edge Cases First:** Always write `if (arr.empty()) return 0;` or `if (n == 0) return "";` before your main logic. It prevents segfaults.
3. **Space-Time Tradeoff:** If a solution is too slow (e.g., $O(N^2)$), try using extra space (like a Hash Map) to bring it down to $O(N)$.
