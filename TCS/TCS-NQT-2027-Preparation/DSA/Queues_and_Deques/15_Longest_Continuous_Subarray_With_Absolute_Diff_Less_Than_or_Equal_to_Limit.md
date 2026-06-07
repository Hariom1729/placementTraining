# Problem 15: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Problem Statement
Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

## Input Format
- An array of integers `nums`.
- An integer `limit`.

## Output Format
- An integer representing the length of the longest subarray.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

---

## Approach: Sliding Window + Two Monotonic Deques

For any subarray, the absolute difference between any two elements is `<= limit` if and only if `max(subarray) - min(subarray) <= limit`.
We can use a sliding window `[left, right]`. As we expand `right`, we need to keep track of the maximum and minimum elements in the current window.
We can do this using two Monotonic Deques:
1. `max_dq`: Monotonically decreasing to keep track of the maximum element in the window.
2. `min_dq`: Monotonically increasing to keep track of the minimum element in the window.

1. Iterate `right` from `0` to `n-1`.
2. Add `nums[right]` to `max_dq` (maintain decreasing order) and `min_dq` (maintain increasing order).
3. If `max_dq.front() - min_dq.front() > limit`:
   - The window is invalid. We must shrink the window by incrementing `left`.
   - If `nums[left] == max_dq.front()`, pop from `max_dq`.
   - If `nums[left] == min_dq.front()`, pop from `min_dq`.
   - `left++`.
4. Update maximum length: `ans = max(ans, right - left + 1)`.

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
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> max_dq; // Decreasing
        deque<int> min_dq; // Increasing
        int left = 0, ans = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            // Update max_dq
            while (!max_dq.empty() && nums[right] > max_dq.back()) {
                max_dq.pop_back();
            }
            max_dq.push_back(nums[right]);
            
            // Update min_dq
            while (!min_dq.empty() && nums[right] < min_dq.back()) {
                min_dq.pop_back();
            }
            min_dq.push_back(nums[right]);
            
            // Shrink window if condition is violated
            while (max_dq.front() - min_dq.front() > limit) {
                if (max_dq.front() == nums[left]) {
                    max_dq.pop_front();
                }
                if (min_dq.front() == nums[left]) {
                    min_dq.pop_front();
                }
                left++;
            }
            
            ans = max(ans, right - left + 1);
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {8, 2, 4, 7};
    int limit = 4;
    cout << "Longest Subarray Length: " << sol.longestSubarray(nums, limit) << endl; 
    // Expected: 2 (Subarray [2, 4])
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each element is pushed and popped from each deque at most once.
- **Space Complexity:** `O(N)` to store elements in the two deques.
