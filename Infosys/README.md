# 🎯 Infosys Specialist Programmer (SP) & Digital Specialist Engineer (DSE) Preparation Repository

Welcome to the ultimate preparation repository for cracking the Infosys SP and DSE roles. This repository is rigorously curated by analyzing years of previous Infosys Online Assessments (OA) and interview experiences.

---

## 🗺️ Preparation Roadmap

Depending on your timeline, follow the roadmap that best fits your schedule.

### 🚀 30-Day Crash Course (High-Frequency Focus)
For those short on time, focusing on high-ROI topics is critical.
- **Days 1-7:** Arrays, Strings, Hashing, Two Pointers.
- **Days 8-14:** Sliding Window, Stack, Queue, Basic Recursion, Linked List.
- **Days 15-21:** Trees (BST, Traversals), Graphs (BFS, DFS), Greedy Algorithms.
- **Days 22-25:** 1D DP, Knapsack, Math/Number Theory.
- **Days 26-30:** Mock Tests, Revision, and OA Simulations.

### 🏃 45-Day Intermediate Plan (DSE Standard)
- **Days 1-15:** Master basic data structures (Arrays to Linked Lists).
- **Days 16-25:** Deep dive into Trees and Graphs (Shortest Path, MST).
- **Days 26-35:** Dynamic Programming (1D, 2D, Strings, LIS).
- **Days 36-40:** Advanced topics (Trie, Bit Manipulation).
- **Days 41-45:** Full length SP & DSE Mock Tests.

### 🏋️ 60-Day Mastery Plan (SP Standard)
- **Days 1-20:** Exhaustive coverage of basic DSA (Focus on edge cases and optimal code).
- **Days 21-35:** Trees, Graphs, and Greedy (Focus on Hard/Complex difficulty).
- **Days 36-45:** Advanced DP (Heavy DP, Digit DP, Bitmask DP).
- **Days 46-52:** Advanced DS (Segment Tree, Fenwick Tree, Union Find, Trie).
- **Days 53-60:** Intensive OA Simulations and Last-Minute Revision Notes.

---

## 📈 Recommended Order of Topics

1. **Math & Number Theory:** GCD, LCM, Primes. (Very common in Infosys).
2. **Arrays & Hashing:** The foundation for most logic.
3. **Strings:** Heavy emphasis in Infosys OA on string manipulations and palindromes.
4. **Two Pointers & Sliding Window:** Crucial for optimization.
5. **Stack & Queue:** Next Greater Element variations.
6. **Linked List:** Traversal and reversal logic.
7. **Trees & BST:** Extremely popular in SP rounds.
8. **Graphs:** Shortest Path (Dijkstra) and Graph components.
9. **Greedy Algorithms:** Activity selection, interval merging.
10. **Dynamic Programming:** Knapsack, LCS, LIS.
11. **Advanced:** Segment Trees, Tries (L3 SP level).

---

## 🧠 OA Strategy & Time Management

- **Total Time:** Usually 90-120 minutes for 3 questions.
- **Question Distribution:**
  - **Q1 (Easy):** 10-15 minutes. Often Math, Strings, or basic Array manipulations.
  - **Q2 (Medium):** 30-40 minutes. Often Greedy, Trees, or Basic DP.
  - **Q3 (Hard):** 45-60 minutes. Often Advanced Graph, DP on Trees, or Segment Trees.
- **Actionable Tips:**
  - **Solve Q1 fast:** Do not over-optimize Q1. Get the points and move on.
  - **Read constraints:** If $N \le 10^4$, an $O(N^2)$ solution will TLE. If $N \le 10^5$, you need $O(N \log N)$ or $O(N)$. If $N \le 18$, it's likely Bitmask DP.
  - **Partial Test Cases:** If you can't pass all cases for the Hard question, write a brute-force approach to pass 30-50% of the cases. Partial points matter significantly for SP.

---

## ⚠️ Common Mistakes to Avoid
- **Ignoring Edge Cases:** Infosys test cases are notorious for $N=0$, negative numbers, or extremely large inputs. Always check your bounds.
- **Overflow Issues:** Use `long long` in C++ instead of `int` if constraints mention numbers up to $10^9$, as products or sums will overflow.
- **Spending too long on Q3:** If Q3 uses a concept you don't know (like a Persistent Segment Tree), write the brute force and spend the rest of your time ensuring Q1 and Q2 are flawless.

---

## 📂 Repository Navigation

- **`/Topics/`**: The core directory. Contains every question, explanation, and optimal C++ solution categorized by data structure.
- **`/Role_Wise/`**: Curated lists matching the L1, L2, and L3 expectations.
- **`/DSA/`**: Questions sorted purely by Difficulty (Easy to Complex).
- **`/MockTests/`**: Full 90-120 minute OA Simulations for practice.
- **`/Revision/`**: Cheat sheets, formula sheets, and Top 50/100 lists for the night before the exam.
