# Problem 11: Minimum Path Sum

## Problem Statement
Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

---

## Approach: 2D DP

Let `dp[i][j]` be the minimum path sum to reach cell `(i, j)`.
Because we can only move down or right, to reach cell `(i, j)`, we must have come from either `(i-1, j)` (above) or `(i, j-1)` (left).
So, the minimum cost to reach `(i, j)` is the cost of the cell itself plus the minimum of the costs to reach the cells above and left of it.

`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`

- **Base Cases:**
  - `dp[0][0] = grid[0][0]`
  - First row (`i=0`): can only come from the left. `dp[0][j] = grid[0][j] + dp[0][j-1]`
  - First column (`j=0`): can only come from above. `dp[i][0] = grid[i][0] + dp[i-1][0]`

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        dp[0][0] = grid[0][0];
        
        // Fill first row
        for (int j = 1; j < n; j++) {
            dp[0][j] = grid[0][j] + dp[0][j - 1];
        }
        
        // Fill first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = grid[i][0] + dp[i - 1][0];
        }
        
        // Fill rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        
        return dp[m - 1][n - 1];
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };
    
    cout << "Minimum Path Sum: " << sol.minPathSum(grid) << endl; 
    // Expected: 7 (Path: 1 -> 3 -> 1 -> 1 -> 1)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(M * N)` to iterate through the entire grid.
- **Space Complexity:** `O(M * N)` for the DP table. (Can be optimized to `O(N)` since we only need the previous row).
