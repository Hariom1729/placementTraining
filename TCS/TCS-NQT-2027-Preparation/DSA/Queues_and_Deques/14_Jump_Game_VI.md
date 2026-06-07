# Problem 14: Jump Game VI

## Problem Statement
You are given a 0-indexed integer array `nums` and an integer `k`.
You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` inclusive.
You want to reach the last index of the array (index `n - 1`). Your score is the sum of all `nums[j]` for each index `j` you visited in the array.
Return the maximum score you can get.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An integer representing the maximum score.

## Constraints
- `1 <= nums.length, k <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach: Dynamic Programming + Monotonic Deque

This problem is almost identical in logic to "Constrained Subsequence Sum".
Let `dp[i]` be the maximum score to reach index `i`.
`dp[i] = nums[i] + max(dp[i-k], dp[i-k+1], ..., dp[i-1])`.
Again, we use a monotonically decreasing deque to find the maximum in the sliding window of size `k` in `O(1)` time.

1. Initialize `dp` array. `dp[0] = nums[0]`.
2. Initialize `deque<int> dq` and push `0`.
3. For `i` from `1` to `n-1`:
   - Remove out of bounds indices: `if (dq.front() < i - k)` pop front.
   - `dp[i] = nums[i] + dp[dq.front()]`.
   - Maintain monotonic decreasing order based on `dp` values: while `dq` not empty and `dp[i] >= dp[dq.back()]`, pop back.
   - Push `i` to deque.
4. Return `dp[n-1]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, 0);
        deque<int> dq;
        
        dp[0] = nums[0];
        dq.push_back(0);
        
        for (int i = 1; i < n; i++) {
            // Remove out of bounds elements
            if (!dq.empty() && dq.front() < i - k) {
                dq.pop_front();
            }
            
            // The front of the deque is the max element in the valid window
            dp[i] = nums[i] + dp[dq.front()];
            
            // Maintain monotonic decreasing order
            while (!dq.empty() && dp[i] >= dp[dq.back()]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
        }
        
        return dp[n - 1];
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, -1, -2, 4, -7, 3};
    int k = 2;
    cout << "Max Score: " << sol.maxResult(nums, k) << endl; 
    // Expected: 7 (1 -> -1 -> 4 -> 3)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each index is pushed and popped from the deque at most once.
- **Space Complexity:** `O(N)` for the `dp` array and the deque.
