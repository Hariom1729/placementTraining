# Problem 9: Subset Sum Problem

## Problem Statement
Given an array of non-negative integers, and a value `sum`, determine if there is a subset of the given set with sum equal to given `sum`.

## Constraints
- `1 <= N <= 100`
- `1 <= arr[i] <= 100`
- `1 <= sum <= 10^5`

---

## Approach: 2D DP (0/1 Knapsack Pattern)

This is a variation of the 0/1 Knapsack problem. We either include an element in the subset or exclude it.
Let `dp[i][j]` be a boolean indicating whether a subset with sum `j` can be formed using the first `i` elements.

- **Base Cases:**
  - `dp[i][0] = true`: Sum 0 can always be achieved by picking an empty subset.
  - `dp[0][j] = false` (for `j > 0`): With 0 elements, no positive sum can be achieved.

- **Recursive Step:**
  - If `arr[i-1] > j` (current element is greater than the required sum), we CANNOT include it:
    - `dp[i][j] = dp[i-1][j]`
  - Otherwise, we check if the sum can be achieved by either EXCLUDING or INCLUDING the current element:
    - `dp[i][j] = dp[i-1][j] || dp[i-1][j - arr[i-1]]`

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isSubsetSum(vector<int> arr, int sum) {
        int n = arr.size();
        // dp[i][j] will be true if subset of arr[0..i-1] has sum equal to j
        vector<vector<bool>> dp(n + 1, vector<bool>(sum + 1, false));
        
        // Sum 0 is possible for any number of elements (empty subset)
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] <= j) {
                    // Exclude OR Include
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
                } else {
                    // Exclude
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[n][sum];
    }
};

int main() {
    Solution sol;
    vector<int> arr = {3, 34, 4, 12, 5, 2};
    int sum = 9;
    
    cout << "Subset sum exists? " << (sol.isSubsetSum(arr, sum) ? "Yes" : "No") << endl; 
    // Expected: Yes (4 + 5 = 9)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * sum)` where `N` is the number of elements in the array.
- **Space Complexity:** `O(N * sum)` for the DP table. (Can be optimized to `O(sum)` using a 1D array).
