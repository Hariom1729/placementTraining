# Binary Search

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Google

## Topic
Searching / Arrays

## Pattern
Classic Binary Search

## Problem Statement
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Input
- `nums` vector of integers.
- `target` integer.

## Output
- Return an integer index.

## Sample Test Cases

**Example 1:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.
```

**Example 2:**
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1.
```

## Edge Cases
- Target is smaller than the first element.
- Target is larger than the last element.
- Array contains only 1 element.

## Intuition
The array is **sorted**, and we need $O(\log n)$ time. This is the definition of **Binary Search**.
Instead of scanning every element from left to right ($O(n)$), we look at the middle element.
If the middle element is what we're looking for, we're done!
If the middle element is *smaller* than our target, then every number to the left of the middle is ALSO smaller than our target. So we completely ignore the left half and only search the right half!
If the middle element is *larger* than our target, we completely ignore the right half and only search the left half.

We cut our search space in half every single step, leading to extremely fast $O(\log n)$ performance.

## Optimal Approach (Binary Search)
**Detailed explanation:**
1. Initialize two pointers: `left = 0` and `right = nums.size() - 1`.
2. Loop while `left <= right`:
   - Calculate the middle index: `mid = left + (right - left) / 2`. (This prevents integer overflow).
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, the target must be on the right. Set `left = mid + 1`.
   - If `nums[mid] > target`, the target must be on the left. Set `right = mid - 1`.
3. If the loop terminates without finding the target, return `-1`.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            // Prevent potential integer overflow that could happen with (left + right) / 2
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid; // Target found
            } else if (nums[mid] < target) {
                left = mid + 1; // Target is in the right half
            } else {
                right = mid - 1; // Target is in the left half
            }
        }
        
        return -1; // Target not found
    }
};
```

## Dry Run
`nums = [-1, 0, 3, 5, 9, 12], target = 9`
- `left = 0`, `right = 5`.
- `mid = 0 + (5 - 0) / 2 = 2`. `nums[2] = 3`.
- `3 < 9`. Target is on the right! `left = mid + 1 = 3`.
- `left = 3`, `right = 5`.
- `mid = 3 + (5 - 3) / 2 = 4`. `nums[4] = 9`.
- `9 == 9`. Target found! Return `mid (4)`.

## Common Mistakes
- **Using `left < right` instead of `left <= right`:** If you use strict inequality, you will miss the case where the array has 1 element, or when the pointers converge on the exact target element. Always use `<=` for standard binary search.
- **Using `(left + right) / 2`:** This causes integer overflow if `left` and `right` are massive numbers (close to `INT_MAX`). Always use `left + (right - left) / 2`.

## Similar Problems
- Search Insert Position
- First Bad Version
