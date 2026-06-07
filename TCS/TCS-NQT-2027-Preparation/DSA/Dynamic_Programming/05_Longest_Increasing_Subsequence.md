# Problem 5: Longest Increasing Subsequence (LIS)

## Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach: 1D DP

Let `dp[i]` be the length of the longest increasing subsequence that strictly **ends** at index `i`.
Initialize `dp` array of size `N` with `1` (because a single element is an increasing subsequence of length 1).

1. Loop `i` from `1` to `N - 1`.
2. For each `i`, loop `j` from `0` to `i - 1`.
3. If `nums[i] > nums[j]`, it means `nums[i]` can be appended to the LIS ending at `j`.
4. Therefore, `dp[i] = max(dp[i], dp[j] + 1)`.
5. The overall LIS is the maximum value in the entire `dp` array.

*(Note: There is an `O(N \log N)` approach using Binary Search, but the `O(N^2)` DP approach is fundamental).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        vector<int> dp(n, 1); // Base case: every element is an LIS of length 1
        int maxLIS = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLIS = max(maxLIS, dp[i]);
        }
        
        return maxLIS;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    
    cout << "Length of LIS: " << sol.lengthOfLIS(nums) << endl; 
    // Expected: 4 (The subsequence is [2, 3, 7, 101])
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` due to the nested loops.
- **Space Complexity:** `O(N)` for the `dp` array.
