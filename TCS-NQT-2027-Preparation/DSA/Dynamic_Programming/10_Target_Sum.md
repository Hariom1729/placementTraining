# Problem 10: Target Sum

## Problem Statement
You are given an integer array `nums` and an integer `target`.
You want to build an expression out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.
For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.
Return the number of different expressions that you can build, which evaluates to `target`.

## Constraints
- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

---

## Approach: DP (Subset Sum variation)

This problem can be mathematically reduced to the **Count Subsets with a Given Sum** problem.
Let the subset of numbers with `+` signs be $S_1$ and the subset with `-` signs be $S_2$.
We know:
1. $Sum(S_1) - Sum(S_2) = target$
2. $Sum(S_1) + Sum(S_2) = TotalSum$

Adding the two equations:
$2 * Sum(S_1) = target + TotalSum$
$Sum(S_1) = (target + TotalSum) / 2$

So the problem simply becomes: Find the number of subsets in `nums` whose sum is exactly equal to `(target + TotalSum) / 2`.
If `(target + TotalSum)` is odd, or if `abs(target) > TotalSum`, the answer is 0.

Let `dp[w]` be the number of ways to make sum `w`.
Initialize `dp[0] = 1` (1 way to make sum 0: empty set).
For each number in `nums`, update `dp` array backwards (to avoid using the same element multiple times).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        
        // Edge cases
        if (abs(target) > totalSum || (totalSum + target) % 2 != 0) {
            return 0;
        }
        
        int subsetSum = (totalSum + target) / 2;
        
        // dp[i] represents the number of ways to get sum i
        vector<int> dp(subsetSum + 1, 0);
        dp[0] = 1; // 1 way to get sum 0 (empty subset)
        
        for (int num : nums) {
            // Traverse backwards to simulate 0/1 knapsack (use each item once)
            for (int i = subsetSum; i >= num; i--) {
                dp[i] += dp[i - num];
            }
        }
        
        return dp[subsetSum];
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1, 1, 1, 1};
    int target = 3;
    
    cout << "Number of ways: " << sol.findTargetSumWays(nums, target) << endl; 
    // Expected: 5

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * SubsetSum)` where `N` is the size of `nums`.
- **Space Complexity:** `O(SubsetSum)` for the 1D DP array.
