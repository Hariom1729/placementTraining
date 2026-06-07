# Problem 7: Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach: 1D DP / Kadane's Algorithm

Let `dp[i]` be the maximum subarray sum ending exactly at index `i`.
To calculate `dp[i]`, we have two choices:
1. Append `nums[i]` to the maximum subarray ending at `i-1`. (Sum: `nums[i] + dp[i-1]`).
2. Start a completely new subarray at `nums[i]`. (Sum: `nums[i]`).

Therefore, `dp[i] = max(nums[i], nums[i] + dp[i-1])`.
Since `dp[i]` only depends on `dp[i-1]`, we don't need an array. We can keep a running `current_sum` and update it: `current_sum = max(nums[i], current_sum + nums[i])`.
We also maintain a `max_sum` to store the maximum value encountered so far.

*(This is known as Kadane's Algorithm).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current_sum = nums[0];
        int max_sum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            // Either add to the existing subarray, or start a new subarray
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update the global maximum
            max_sum = max(max_sum, current_sum);
        }
        
        return max_sum;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    
    cout << "Maximum Subarray Sum: " << sol.maxSubArray(nums) << endl; 
    // Expected: 6 (The subarray is [4, -1, 2, 1])

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We do a single pass through the array.
- **Space Complexity:** `O(1)`. No extra space is used.
