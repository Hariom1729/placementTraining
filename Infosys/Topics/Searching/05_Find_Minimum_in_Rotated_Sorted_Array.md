# Find Minimum in Rotated Sorted Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Searching / Arrays

## Pattern
Modified Binary Search

## Problem Statement
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the **minimum element** of this array.

You must write an algorithm that runs in $O(\log n)$ time.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Input
- `nums` vector of integers.

## Output
- Return an integer (the minimum element).

## Sample Test Cases

**Example 1:**
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3:**
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times (which is exactly back to sorted).
```

## Edge Cases
- Array is not rotated at all (returns the first element).
- Array has 1 or 2 elements.

## Intuition
Just like *Search in Rotated Sorted Array*, we know one half is perfectly sorted and the other half contains the "pivot" (the drop-off point where the array resets from maximum back to minimum).
The **minimum element ALWAYS resides in the unsorted half** (because that's where the drop-off happens!), UNLESS the entire current range is perfectly sorted, in which case the minimum is simply the first element!

Let's look at `mid` and compare it to `right`:
- If `nums[mid] > nums[right]`: The right half is "broken" (unsorted). For example `[4, 5, 6, 7, 0, 1, 2]`, mid is `7`, right is `2`. `7 > 2`. The drop-off MUST be on the right side! So the minimum is on the right. `left = mid + 1`.
- If `nums[mid] <= nums[right]`: The right half is perfectly sorted. For example `[7, 0, 1, 2, 4, 5, 6]`, mid is `2`, right is `6`. `2 <= 6`. Because the right half is perfectly sorted, the minimum element CANNOT be to the right of `mid`. However, `mid` itself *might* be the minimum element! So the minimum is on the left, but we must *include* mid: `right = mid`.

By repeating this, `left` and `right` will quickly converge onto the exact minimum element!

## Optimal Approach (Binary Search)
**Detailed explanation:**
1. Initialize `left = 0`, `right = nums.size() - 1`.
2. Loop while `left < right`:
   - `mid = left + (right - left) / 2`.
   - If `nums[mid] > nums[right]`:
     - The minimum MUST be strictly to the right of `mid`.
     - `left = mid + 1`.
   - Else (`nums[mid] <= nums[right]`):
     - The minimum is at `mid` or strictly to its left.
     - `right = mid`. (DO NOT do `mid - 1` because `mid` itself could be the answer!).
3. When the loop breaks, `left == right`, and it will point to the minimum element. Return `nums[left]`.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        
        // Loop terminates when left == right, which will be our minimum
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If mid is greater than the rightmost element, the drop-off MUST be on the right.
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // If mid is less than or equal to the rightmost element, the right side is perfectly sorted.
            // Therefore, the minimum cannot be to the right of mid. It must be mid or to the left of mid.
            else {
                right = mid;
            }
        }
        
        return nums[left];
    }
};
```

## Dry Run
`nums = [4, 5, 6, 7, 0, 1, 2]`
- `left=0`, `right=6`. `mid=3 (7)`.
- `nums[3] (7) > nums[6] (2)`. The right half is broken! Drop-off is there. `left = mid + 1 = 4`.
- `left=4`, `right=6`. `mid=5 (1)`.
- `nums[5] (1) <= nums[6] (2)`. The right half is sorted! Minimum cannot be to the right. `right = mid = 5`.
- `left=4`, `right=5`. `mid=4 (0)`.
- `nums[4] (0) <= nums[5] (1)`. Right half sorted! `right = mid = 4`.
- Loop breaks because `left (4) == right (4)`.
- Return `nums[4]` which is `0`. Perfect!

## Common Mistakes
- **Using `while (left <= right)`:** If you use `<=`, you will enter an infinite loop when `left == right` because `right = mid` will continuously set `right` to itself. By using `left < right`, the loop naturally exits the exact moment the two pointers land on the target.
- **`right = mid - 1`:** If `nums = [3, 1, 2]` and `mid` lands on `1`, doing `right = mid - 1` will move `right` to `3`, completely skipping the minimum element! You must do `right = mid` to keep the potential minimum element in the search space.

## Similar Problems
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array II (Handles duplicates)
