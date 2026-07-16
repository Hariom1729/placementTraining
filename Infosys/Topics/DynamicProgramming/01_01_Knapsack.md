# 0/1 Knapsack Problem

## Difficulty
Medium/Hard

## Asked In
Infosys SP (L2, L3)
Year: 2021, 2023
Frequency: Very High

---

## Problem Statement
Given weights and values of `N` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack. You cannot break an item, either pick the complete item or don't pick it (0-1 property).

---

## Optimal Approach (Dynamic Programming - Bottom Up)
**Detailed explanation:**
We use a 2D DP array where `dp[i][w]` represents the maximum value that can be attained with the first `i` items and a knapsack capacity of `w`.
For each item, we have two choices:
1. Include it (if weight $\le w$): `val[i-1] + dp[i-1][w - wt[i-1]]`
2. Exclude it: `dp[i-1][w]`
Take the maximum of the two.

**Complexity:**
- **Time Complexity:** $O(N \times W)$
- **Space Complexity:** $O(W)$ using 1D space optimization.

---

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

// 1D Space Optimized DP
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        // Traverse backwards to avoid using the same item multiple times
        for (int w = W; w >= wt[i]; w--) {
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }
    
    return dp[W];
}
```
