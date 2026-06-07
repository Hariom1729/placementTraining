# Problem 6: House Robber

## Problem Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

## Approach: 1D DP (Include/Exclude)

For each house `i`, you have two choices:
1. **Rob house `i`:** You cannot rob house `i-1`. The total money is `nums[i] + money robbed up to house i-2`.
2. **Do not rob house `i`:** The total money is `money robbed up to house i-1`.

Let `dp[i]` be the max money robbed up to house `i`.
`dp[i] = max(nums[i] + dp[i-2], dp[i-1])`

Since we only need `dp[i-1]` and `dp[i-2]`, we can optimize the space to `O(1)` by using two variables: `prev1` and `prev2`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        int prev2 = nums[0]; // Max money if we rob up to house 0
        int prev1 = max(nums[0], nums[1]); // Max money if we rob up to house 1
        
        for (int i = 2; i < n; i++) {
            // Include current house + prev2, OR exclude current house (take prev1)
            int curr = max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 9, 3, 1};
    
    cout << "Max money robbed: " << sol.rob(nums) << endl; 
    // Expected: 12 (Rob house 0 (2), house 2 (9), and house 4 (1))

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once.
- **Space Complexity:** `O(1)`. We only use a few variables.
