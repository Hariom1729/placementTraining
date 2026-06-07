# Problem 13: Constrained Subsequence Sum

## Problem Statement
Given an integer array `nums` and an integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An integer representing the maximum subsequence sum.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach: Dynamic Programming + Monotonic Deque

Let `dp[i]` be the maximum constrained subsequence sum ending at index `i`.
The relation is: `dp[i] = nums[i] + max(0, max(dp[i-k], dp[i-k+1], ..., dp[i-1]))`.
Finding the max in a sliding window of size `k` naively takes `O(k)`, leading to `O(N*k)` total time.

We can optimize this to `O(N)` using a Monotonic Decreasing Deque. The deque will store the indices of the `dp` array.
1. The deque maintains indices in decreasing order of their `dp` values. The front of the deque will always have the maximum `dp` value in the current window of size `k`.
2. Initialize `dp` array and `ans = nums[0]`.
3. For each `i` from `0` to `n-1`:
   - Remove indices from the front of the deque if they are out of the window `i - k`.
   - `dp[i] = nums[i] + (dq.empty() ? 0 : max(0, dp[dq.front()]))`.
   - Update the global maximum sum `ans = max(ans, dp[i])`.
   - Maintain the decreasing order in the deque: while `dq` is not empty and `dp[i] >= dp[dq.back()]`, pop from the back.
   - Push `i` to the back.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, 0);
        deque<int> dq; // Stores indices
        int maxSum = nums[0];
        
        for (int i = 0; i < n; i++) {
            // Remove out of bounds indices
            if (!dq.empty() && dq.front() < i - k) {
                dq.pop_front();
            }
            
            // Calculate dp[i]
            dp[i] = nums[i];
            if (!dq.empty() && dp[dq.front()] > 0) {
                dp[i] += dp[dq.front()];
            }
            
            maxSum = max(maxSum, dp[i]);
            
            // Maintain monotonically decreasing deque
            while (!dq.empty() && dp[i] >= dp[dq.back()]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        
        return maxSum;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {10, -2, -10, -5, 20};
    int k = 2;
    cout << "Max Sum: " << sol.constrainedSubsetSum(nums, k) << endl; 
    // Expected: 23 (10 + -2 + -5 + 20)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each index is pushed and popped from the deque at most once.
- **Space Complexity:** `O(N)` for the `dp` array and the deque.
