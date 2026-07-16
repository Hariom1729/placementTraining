# Find Peak Element

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Facebook

## Topic
Searching / Arrays

## Pattern
Binary Search (Hill Climbing)

## Problem Statement
A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = -∞` and `nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in $O(\log n)$ time.

## Constraints
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Input
- `nums` vector of integers.

## Output
- Return an integer index.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 1 where the peak element is 2, or index 5 where the peak element is 6.
```

## Edge Cases
- Array is strictly increasing (`[1, 2, 3]`). Peak is at the very end.
- Array is strictly decreasing (`[3, 2, 1]`). Peak is at the very beginning.
- Array has 1 element.

## Intuition
Normally, Binary Search requires a sorted array. However, we can use Binary Search here because we are trying to follow an **increasing slope** to find a peak!
Imagine you are blindfolded on a mountain range. You check your current altitude (`nums[mid]`), and then take one step to the right (`nums[mid+1]`).
- If the altitude went UP (`nums[mid] < nums[mid+1]`), you are walking up a slope! If you keep walking up this slope, you are GUARANTEED to hit a peak eventually (even if the peak is just the boundary of the array dropping off to $-\infty$). So, search the right half!
- If the altitude went DOWN (`nums[mid] > nums[mid+1]`), you are on a downward slope. This means the peak you just passed is to your LEFT. Search the left half!

By constantly moving towards the higher altitude, we will quickly converge on a peak in $O(\log n)$ time.

## Optimal Approach (Binary Search)
**Detailed explanation:**
1. Initialize `left = 0`, `right = nums.size() - 1`.
2. Loop while `left < right`:
   - `mid = left + (right - left) / 2`.
   - If `nums[mid] < nums[mid + 1]`:
     - We are climbing UP the mountain. The peak must be to the right of `mid`.
     - `left = mid + 1`.
   - Else (`nums[mid] > nums[mid + 1]`):
     - We are climbing DOWN the mountain. The peak must be to the left (or it IS `mid` itself!).
     - `right = mid`. (Do not do `mid - 1` because `mid` could be the peak!).
3. When the loop terminates, `left == right`, and it will point to a peak. Return `left`.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // Check the slope between mid and mid+1
            if (nums[mid] < nums[mid + 1]) {
                // Slope is rising, peak is to the right
                left = mid + 1;
            } else {
                // Slope is falling, peak is to the left (or could be mid itself)
                right = mid;
            }
        }
        
        // left and right converge on the peak element
        return left;
    }
};
```

## Dry Run
`nums = [1, 2, 1, 3, 5, 6, 4]`
- `left = 0`, `right = 6`. `mid = 3` (`nums[3] = 3`).
- `nums[3] (3) < nums[4] (5)`. We are going UP! Search right. `left = mid + 1 = 4`.
- `left = 4`, `right = 6`. `mid = 5` (`nums[5] = 6`).
- `nums[5] (6) > nums[6] (4)`. We are going DOWN! Search left. `right = mid = 5`.
- `left = 4`, `right = 5`. `mid = 4` (`nums[4] = 5`).
- `nums[4] (5) < nums[5] (6)`. We are going UP! Search right. `left = mid + 1 = 5`.
- Loop breaks because `left (5) == right (5)`.
- Return `5`. (Value is 6, which is a peak!).

## Common Mistakes
- **Handling Out of Bounds:** Some candidates try to check `nums[mid-1]` and `nums[mid+1]` explicitly. This requires messy edge case checks (e.g., `if (mid == 0)`). Checking ONLY `nums[mid]` vs `nums[mid+1]` avoids all out-of-bounds issues entirely because `mid` will never equal the last index as long as `left < right`!

## Similar Problems
- Find Peak Element II (2D Matrix version)
- Peak Index in a Mountain Array
