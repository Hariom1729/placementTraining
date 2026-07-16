# Search Insert Position

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Apple, Google

## Topic
Searching / Arrays

## Pattern
Binary Search (Lower Bound)

## Problem Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Input
- `nums` vector of integers.
- `target` integer.

## Output
- Return an integer index.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
Explanation: 2 is not in the array. It would be inserted between 1 and 3, which is index 1.
```

**Example 3:**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
Explanation: 7 is larger than all elements, so it would be inserted at the very end.
```

## Edge Cases
- Target is smaller than the first element (returns `0`).
- Target is larger than the last element (returns `nums.size()`).

## Intuition
This is a standard Binary Search problem, but with a slight twist: what happens when the target is **NOT** found?
In standard binary search, we return `-1`. Here, we need to return the index where the target *should* be inserted.

Let's think about how the pointers `left` and `right` behave when the target is NOT in the array.
The loop continues until `left > right`.
Right before the loop breaks, `left` and `right` will be pointing to the exact same element (or be adjacent).
If the target is slightly larger than this element, `left` will move to `mid + 1` (which is exactly where the target should be inserted!).
If the target is slightly smaller than this element, `right` will move to `mid - 1`, and `left` will remain exactly where the target should be inserted!

In ALL cases where the target is not found, when the `while (left <= right)` loop terminates, the `left` pointer will **always** point to the correct insertion index!

*(Note: In C++, this is exactly what `std::lower_bound` does!)*

## Optimal Approach (Binary Search)
**Detailed explanation:**
1. Initialize `left = 0`, `right = nums.size() - 1`.
2. Loop while `left <= right`:
   - `mid = left + (right - left) / 2`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, set `left = mid + 1`.
   - If `nums[mid] > target`, set `right = mid - 1`.
3. If the loop finishes, the target wasn't found. Return `left`.

**Time Complexity:** $O(\log n)$
**Space Complexity:** $O(1)$

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid; // Target found
            } else if (nums[mid] < target) {
                left = mid + 1; // Target must be to the right
            } else {
                right = mid - 1; // Target must be to the left
            }
        }
        
        // If target is not found, 'left' will naturally point to the correct insertion index
        return left;
    }
};

/*
// Alternative 1-line solution using C++ STL (Good to know, but interviewer will want the above)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }
};
*/
```

## Dry Run
`nums = [1, 3, 5, 6], target = 2`
- `left = 0`, `right = 3`.
- `mid = 1` (`nums[1] = 3`).
- `3 > 2`. Target must be on the left. `right = mid - 1 = 0`.
- `left = 0`, `right = 0`.
- `mid = 0` (`nums[0] = 1`).
- `1 < 2`. Target must be on the right. `left = mid + 1 = 1`.
- Loop breaks because `left (1) > right (0)`.
- Return `left`, which is `1`. (Correct!).

## Common Mistakes
- **Returning `mid` outside the loop:** `mid` is usually scoped inside the `while` loop. Even if you declared it outside, returning `mid` at the end is wrong because `mid` is just the last element checked, not necessarily the insertion point. `left` is the mathematically proven insertion point.
- **Handling Edge Cases Manually:** Writing `if (target > nums.back()) return nums.size();` at the beginning is unnecessary. The binary search elegantly handles all out-of-bounds targets automatically!

## Similar Problems
- Find First and Last Position of Element in Sorted Array
- First Bad Version
