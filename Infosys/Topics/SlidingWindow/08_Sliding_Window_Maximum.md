# Sliding Window Maximum

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft, Uber

## Topic
Sliding Window / Queue / Arrays

## Pattern
Monotonic Deque

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return a vector of integers.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Edge Cases
- `k == 1` (The output is just the original array).
- `k == nums.length` (The output is a single element: the maximum of the entire array).

## Intuition
The naive approach is to loop through the window of size `k` for every position and find the max. This takes $O(N \times K)$ time, which will TLE since $N, K \le 10^5$.

We need a way to find the max in a sliding window in $O(1)$ time.
We can use a **Monotonic Deque** (Double-Ended Queue).

The Deque will store the **indices** of elements. We want the Deque to be strictly decreasing in value. This means the front of the Deque will ALWAYS contain the index of the maximum element in the current window!

When a new element `nums[i]` enters the window:
1. We check the back of the Deque. Any elements in the Deque that are SMALLER than `nums[i]` are completely useless! Why? Because they are smaller, AND they are older than `nums[i]`, so they will never be the maximum of any future window. We pop them from the back.
2. We push the new index `i` to the back.
3. We check the front of the Deque. If the index at the front has fallen out of the window (`front <= i - k`), we pop it from the front!
4. The maximum of the current window is just `nums[deque.front()]`! We add it to our result array (once the window has actually reached size `k`).

## Optimal Approach (Monotonic Deque)
**Detailed explanation:**
1. Create a `deque<int> dq` to store indices.
2. Create a `vector<int> result`.
3. Loop `i` from `0` to `n - 1`:
   - **Remove out-of-bounds:** If the deque is not empty and `dq.front() == i - k`, pop the front.
   - **Maintain Monotonicity:** While the deque is not empty and `nums[dq.back()] <= nums[i]`, pop the back.
   - **Add new element:** Push `i` to the back.
   - **Record Answer:** If `i >= k - 1` (meaning the window has reached size `k`), push `nums[dq.front()]` to the result.
4. Return `result`.

**Time Complexity:** $O(N)$. Every element is pushed and popped at most once.
**Space Complexity:** $O(K)$ for the deque.

## C++ Solution

```cpp
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq; // Stores INDICES, not values
        
        for (int i = 0; i < nums.size(); i++) {
            // 1. Remove indices that are out of the current window
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }
            
            // 2. Remove elements from the back that are smaller than the current element
            // They are useless because they are smaller AND older
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }
            
            // 3. Add the current element's index
            dq.push_back(i);
            
            // 4. If our window has reached size k, the front of the deque is the max!
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};
```

## Dry Run
`nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- `i = 0` (1): `dq` is empty. `dq.push(0)`. `dq = [0]`. Window not full.
- `i = 1` (3): `nums[dq.back()] (1) <= 3`. Pop it. `dq.push(1)`. `dq = [1]`. Window not full.
- `i = 2` (-1): `nums[dq.back()] (3) > -1`. Keep it. `dq.push(2)`. `dq = [1, 2]`.
  - Window full (`i=2 >= 2`). Result = `[nums[1]]` = `[3]`.
- `i = 3` (-3): `nums[dq.back()] (-1) > -3`. Keep it. `dq.push(3)`. `dq = [1, 2, 3]`.
  - Result = `[3, nums[1]]` = `[3, 3]`.
- `i = 4` (5): `dq.front() == 1 == 4-3`. Pop front! `dq = [2, 3]`.
  - `nums[dq.back()] (-3) <= 5`. Pop. `dq = [2]`.
  - `nums[dq.back()] (-1) <= 5`. Pop. `dq = []`.
  - `dq.push(4)`. `dq = [4]`.
  - Result = `[3, 3, 5]`.
- ... Continues ... Output: `[3, 3, 5, 5, 6, 7]`.

## Common Mistakes
- **Storing values instead of indices in the Deque:** If you store values, you have NO WAY of knowing if the value at the front of the deque has fallen out of the window or not! You MUST store indices.

## Similar Problems
- Minimum Window Substring
- Constrained Subsequence Sum
