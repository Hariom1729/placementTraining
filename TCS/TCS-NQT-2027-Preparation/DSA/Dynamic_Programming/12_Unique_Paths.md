# Problem 12: Unique Paths

## Problem Statement
There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

## Constraints
- `1 <= m, n <= 100`

---

## Approach: 2D DP

This is very similar to Minimum Path Sum.
Let `dp[i][j]` be the number of unique paths to reach cell `(i, j)`.
Since the robot can only come from `(i-1, j)` (above) or `(i, j-1)` (left), the total number of paths to `(i, j)` is the sum of paths to reach the cell above and the cell to the left.

`dp[i][j] = dp[i-1][j] + dp[i][j-1]`

- **Base Case:**
  - `dp[0][j] = 1` for all `j` (only 1 way to traverse the first row: keep going right).
  - `dp[i][0] = 1` for all `i` (only 1 way to traverse the first column: keep going down).

*(Note: This can also be solved using Combinatorics in `O(m+n)` time, by choosing `m-1` downs out of `(m-1) + (n-1)` total moves).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Base cases: First row and first column have exactly 1 path
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;
        
        // DP transitions
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        return dp[m - 1][n - 1];
    }
};

int main() {
    Solution sol;
    cout << "Unique Paths (3x7): " << sol.uniquePaths(3, 7) << endl; 
    // Expected: 28
    
    cout << "Unique Paths (3x2): " << sol.uniquePaths(3, 2) << endl; 
    // Expected: 3

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(M * N)`.
- **Space Complexity:** `O(M * N)` for the DP table. (Can be optimized to `O(N)` using a 1D array).
