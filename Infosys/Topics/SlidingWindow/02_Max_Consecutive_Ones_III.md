# Max Consecutive Ones III

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Amazon, Google, Uber

## Topic
Sliding Window / Arrays

## Pattern
Variable Size Window

## Problem Statement
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is length 6.
```

**Example 2:**
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is length 10.
```

## Edge Cases
- `k = 0` (You cannot flip any zeros, you just want the longest contiguous block of 1s).
- `k >= nums.size()` (You can flip everything, return `nums.size()`).
- Array consists of all 0s and `k = 1`.

## Intuition
The problem translates to: **Find the longest contiguous subarray that contains at most `k` zeros.**
If we find a subarray with `k` zeros, we know we could theoretically flip all those zeros to `1`s, making the entire subarray all `1`s!

Since we are looking for the "longest contiguous subarray" based on a condition (at most `k` zeros), this is a textbook **Variable Size Sliding Window** problem!

We maintain a window defined by `[left, right]`.
- We expand the window by moving `right` forward.
- If we encounter a `0`, we increment our `zeroCount`.
- If `zeroCount` exceeds `k`, our window is invalid! We must shrink it from the left side until it becomes valid again. We do this by moving `left` forward. If the element leaving the window was a `0`, we decrement `zeroCount`.
- Throughout this process, we keep track of the maximum window size `right - left + 1`.

## Optimal Approach (Variable Sliding Window)
**Detailed explanation:**
1. Initialize `left = 0`, `zeroCount = 0`, `maxLength = 0`.
2. Loop `right` from `0` to `nums.size() - 1`:
   - If `nums[right] == 0`, `zeroCount++`.
   - While `zeroCount > k`:
     - The window is invalid. We must shrink it.
     - If `nums[left] == 0`, `zeroCount--`.
     - `left++`.
   - The window is now guaranteed to be valid (`zeroCount <= k`).
   - Update `maxLength = max(maxLength, right - left + 1)`.
3. Return `maxLength`.

**Time Complexity:** $O(N)$ since both `left` and `right` pointers only move forward and traverse the array at most once.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            // Expand the window by adding nums[right]
            if (nums[right] == 0) {
                zeroCount++;
            }
            
            // If the window is invalid, shrink it from the left
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            
            // Window is valid, update max length
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

## Dry Run
`nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- `right = 0 to 2` (all 1s): `zeroCount = 0`. `max = 3`. Window: `[1,1,1]`.
- `right = 3` (0): `zeroCount = 1`. `max = 4`. Window: `[1,1,1,0]`.
- `right = 4` (0): `zeroCount = 2`. `max = 5`. Window: `[1,1,1,0,0]`.
- `right = 5` (0): `zeroCount = 3`. Invalid!
  - `while (3 > 2)`:
    - `nums[left]` is `nums[0] = 1`. `left++ -> 1`.
    - `nums[left]` is `nums[1] = 1`. `left++ -> 2`.
    - `nums[left]` is `nums[2] = 1`. `left++ -> 3`.
    - `nums[left]` is `nums[3] = 0`. `zeroCount-- -> 2`. `left++ -> 4`.
  - Window is now valid: `left=4`, `right=5` (`[0,0]`). Length = 2. `max` stays 5.
- `right = 6 to 9` (all 1s): Valid, `zeroCount = 2`. Length grows to 6 (`[0, 0, 1, 1, 1, 1]`). `max = 6`.
- `right = 10` (0): `zeroCount = 3`. Invalid!
  - Shrink until we drop the `0` at index 4. `left` becomes 5.
  - Window: `[0, 1, 1, 1, 1, 0]`. Length = 6. `max = 6`.
- End of array. Return 6.

## Common Mistakes
- **Resetting `zeroCount` and `left` completely:** Some beginners try to reset the count to 0 and jump `left` to `right` whenever `k` is exceeded. This fails because a valid subarray might start somewhere in the middle of the current window! Sliding the `left` pointer gracefully one by one is required.

## Similar Problems
- Longest Substring Without Repeating Characters
- Max Consecutive Ones (Easier version with `k = 0`)
