# Longest Subarray of 1's After Deleting One Element

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft

## Topic
Sliding Window / Arrays

## Pattern
Variable Size Window (Max Zeros = 1)

## Problem Statement
Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only `1`'s in the resulting array. Return `0` if there is no such subarray.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Input
- `nums` vector of integers.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

**Example 2:**
```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

**Example 3:**
```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

## Edge Cases
- All 1s array. We are FORCED to delete an element, so return `nums.size() - 1`.
- All 0s array. Returns `0`.

## Intuition
This problem is mathematically identical to **Max Consecutive Ones III**, but specifically with `k = 1`.
Instead of "flipping" a 0, we "delete" it, which achieves the exact same effect: the two blocks of 1s on either side of the 0 become connected!

So we use a **Variable Size Sliding Window**:
- Expand `right` and count the zeros.
- If `zeroCount > 1`, shrink `left` until `zeroCount <= 1`.
- Update `maxLength = max(maxLength, right - left)`.
  - Notice that the length of the window is `right - left + 1`. But because we MUST delete one element, the resulting subarray of 1s will be `(right - left + 1) - 1`, which is just `right - left`.

## Optimal Approach (Sliding Window)
**Detailed explanation:**
1. Initialize `left = 0`, `zeroCount = 0`, `maxLength = 0`.
2. Loop `right` from `0` to `nums.size() - 1`:
   - If `nums[right] == 0`, `zeroCount++`.
   - While `zeroCount > 1`:
     - If `nums[left] == 0`, `zeroCount--`.
     - `left++`.
   - `maxLength = max(maxLength, right - left)`.
3. Return `maxLength`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }
            
            // If more than one zero is in the window, shrink from the left
            while (zeroCount > 1) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            
            // The size of the window is (right - left + 1).
            // But we must delete exactly one element, so the size of 1s is (right - left).
            maxLength = max(maxLength, right - left);
        }
        
        return maxLength;
    }
};
```

## Dry Run
`nums = [1, 1, 0, 1]`
- `right = 0 (1)`: `zeroCount = 0`. `max = max(0, 0 - 0) = 0`.
- `right = 1 (1)`: `zeroCount = 0`. `max = max(0, 1 - 0) = 1`.
- `right = 2 (0)`: `zeroCount = 1`. `max = max(1, 2 - 0) = 2`.
- `right = 3 (1)`: `zeroCount = 1`. `max = max(2, 3 - 0) = 3`.
- Return 3.

`nums = [1, 1, 1]`
- `right = 0`: max = 0.
- `right = 1`: max = 1.
- `right = 2`: max = 2.
- Return 2. (Handled the forced deletion edge case perfectly!).

## Common Mistakes
- **Returning `right - left + 1`:** The problem strictly requires deleting an element, so the contiguous block of 1s will always be one less than the entire window size.

## Similar Problems
- Max Consecutive Ones III
