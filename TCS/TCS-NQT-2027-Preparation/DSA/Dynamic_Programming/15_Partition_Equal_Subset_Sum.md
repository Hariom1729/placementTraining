# Problem 15: Partition Equal Subset Sum

## Problem Statement
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

---

## Approach: Subset Sum DP

For the array to be partitioned into two subsets with equal sums, the total sum of the array MUST be an even number.
If the total sum is odd, it's impossible, so we return `false` immediately.
If the total sum is even, the problem reduces to finding if there exists a subset in the array whose sum is exactly equal to `TotalSum / 2`.
This is exactly the **Subset Sum Problem** (Problem 09).

1. Calculate `totalSum` of the array.
2. If `totalSum % 2 != 0`, return `false`.
3. Set `target = totalSum / 2`.
4. Use a 1D DP array where `dp[j]` represents whether a subset with sum `j` is possible.
5. Initialize `dp[0] = true` (empty subset has sum 0).
6. For each `num` in `nums`, iterate `j` backwards from `target` down to `num`:
   - `dp[j] = dp[j] || dp[j - num]`
7. Return `dp[target]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        
        // If total sum is odd, it cannot be partitioned into two equal subsets
        if (totalSum % 2 != 0) return false;
        
        int target = totalSum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        
        // 1D DP for Subset Sum
        for (int num : nums) {
            // Traverse backwards to use each element only once
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }
        
        return dp[target];
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 5, 11, 5};
    
    cout << "Can partition? " << (sol.canPartition(nums) ? "Yes" : "No") << endl; 
    // Expected: Yes (Array can be partitioned as [1, 5, 5] and [11])
    
    vector<int> nums2 = {1, 2, 3, 5};
    cout << "Can partition? " << (sol.canPartition(nums2) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * target)` where `target` is `TotalSum / 2`.
- **Space Complexity:** `O(target)` for the 1D DP array.
