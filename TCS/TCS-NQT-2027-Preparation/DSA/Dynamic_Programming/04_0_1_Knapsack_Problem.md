# Problem 4: 0/1 Knapsack Problem

## Problem Statement
You are given weights and values of `N` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.
Note that we have only **one quantity of each item** (0/1). In other words, given two integer arrays `val[0..N-1]` and `wt[0..N-1]` which represent values and weights associated with `N` items respectively, and an integer `W` which represents knapsack capacity, find out the maximum value subset of `val[]` such that sum of the weights of this subset is smaller than or equal to `W`.

## Constraints
- `1 <= N <= 1000`
- `1 <= W <= 1000`
- `1 <= wt[i], val[i] <= 1000`

---

## Approach: 2D DP (Include/Exclude)

Let `dp[i][w]` be the maximum value that can be attained with the first `i` items and a knapsack capacity of `w`.

- **Base Case:** If `i == 0` or `w == 0`, `dp[i][w] = 0`.
- **Recursive Step:**
  - If the weight of the `i`th item (`wt[i-1]`) is greater than the current capacity `w`, we CANNOT include it:
    - `dp[i][w] = dp[i-1][w]`
  - Otherwise, we take the maximum of EXCLUDING the item or INCLUDING the item:
    - `dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])`

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to return max value that can be put in knapsack of capacity W.
    int knapSack(int W, int wt[], int val[], int n) { 
        vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= W; w++) {
                if (wt[i - 1] <= w) {
                    // Include or Exclude
                    dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]]);
                } else {
                    // Exclude
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }
        
        return dp[n][W];
    }
};

int main() {
    Solution sol;
    int n = 3;
    int W = 4;
    int val[] = {1, 2, 3};
    int wt[] = {4, 5, 1};
    
    cout << "Max Value in Knapsack: " << sol.knapSack(W, wt, val, n) << endl; 
    // Expected: 3 (Item 3 with weight 1 and value 3)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * W)`.
- **Space Complexity:** `O(N * W)`. *(Can be optimized to `O(W)` space using a 1D array since we only need the previous row `i-1`).*
