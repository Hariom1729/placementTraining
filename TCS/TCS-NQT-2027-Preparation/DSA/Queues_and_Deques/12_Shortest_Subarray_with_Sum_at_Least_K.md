# Problem 12: Shortest Subarray with Sum at Least K

## Problem Statement
Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An integer representing the length of the shortest subarray.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

---

## Approach: Monotonic Deque + Prefix Sum

If the array only had positive numbers, we could use the classic Sliding Window (Two Pointers). Because there are negative numbers, the prefix sum is NOT monotonically increasing, so sliding window fails.
We can solve this using a Monotonic Deque.

1. Compute the prefix sum array `prefix`, where `prefix[i]` is the sum of `nums[0...i-1]`. (`prefix` size is `n + 1`).
2. Maintain a `deque<int> dq` that stores indices of `prefix` array.
3. The deque will maintain the prefix sums in a **monotonically increasing** order.
4. Iterate `i` from `0` to `n`:
   - If `prefix[i] - prefix[dq.front()] >= k`, we found a valid subarray. Update `min_len = min(min_len, i - dq.front())`. Since any future `i` will be larger, a subarray starting at `dq.front()` will only be longer, so we can `dq.pop_front()`.
   - To maintain monotonic increasing order: while the deque is not empty and `prefix[i] <= prefix[dq.back()]`, `dq.pop_back()`. (If a future index pairs with `dq.back()`, it could also pair with `i` which would be shorter and have a lower/equal prefix sum).
   - Push `i` to the back of the deque.

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
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        deque<int> dq;
        int min_len = n + 1;
        
        for (int i = 0; i <= n; i++) {
            // Check if we found a valid subarray
            while (!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
                min_len = min(min_len, i - dq.front());
                dq.pop_front();
            }
            
            // Maintain monotonic increasing order
            while (!dq.empty() && prefix[i] <= prefix[dq.back()]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
        }
        
        return min_len == n + 1 ? -1 : min_len;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, -1, 2};
    int k = 3;
    cout << "Shortest Subarray length: " << sol.shortestSubarray(nums, k) << endl; 
    // Expected: 3 (Subarray: [2, -1, 2])
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each index is pushed and popped at most once.
- **Space Complexity:** `O(N)` for the prefix sum array and deque.
