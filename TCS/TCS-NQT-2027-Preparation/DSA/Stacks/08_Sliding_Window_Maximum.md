# Problem 8: Sliding Window Maximum

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An array of integers representing the maximum in each window.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## Approach: Deque (Double Ended Queue)

While this is technically a Deque problem, it falls under the Monotonic Data Structure umbrella (similar to stacks).
We maintain a strictly decreasing deque of **indices**. The front of the deque will always store the index of the maximum element for the current window.

1. Initialize `deque<int> dq`.
2. Iterate `i` from `0` to `n-1`.
3. **Remove out of bounds:** If the index at the front of the deque is `<= i - k` (outside the current window), pop it from the front.
4. **Maintain Decreasing Order:** While the deque is not empty and the current element `nums[i]` is **greater than** the element corresponding to the back of the deque `nums[dq.back()]`, pop from the back. (Smaller elements are useless if a larger element comes after them).
5. Push the current index `i` to the back.
6. If `i >= k - 1` (we have processed at least `k` elements to form a window), add `nums[dq.front()]` to the answer.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq; // Stores indices
        
        for (int i = 0; i < nums.size(); i++) {
            // Remove elements not within the window
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }
            
            // Remove elements smaller than the current element from the back
            // They can never be the maximum
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            // Add current element's index
            dq.push_back(i);
            
            // If window has k elements, add the maximum (front of deque) to result
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<int> result = sol.maxSlidingWindow(nums, k);
    
    cout << "Max in Windows: ";
    for(int x : result) cout << x << " ";
    cout << "\n";
    // Expected: 3 3 5 5 6 7
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Every element is added to and removed from the deque at most once.
- **Space Complexity:** `O(k)`. The deque stores at most `k` elements.
