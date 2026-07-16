# Search in Rotated Sorted Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google

## Topic
Searching / Arrays

## Pattern
Modified Binary Search

## Problem Statement
There is an integer array `nums` sorted in ascending order (with **distinct** values).
Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). 
For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Input
- `nums` vector of integers.
- `target` integer.

## Output
- Return an integer index.

## Sample Test Cases

**Example 1:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**
```
Input: nums = [1], target = 0
Output: -1
```

## Edge Cases
- Array is NOT rotated at all (e.g., `[1, 2, 3, 4, 5]`).
- Array size is 1 or 2.

## Intuition
The array is rotated, which means a standard binary search will fail because the array is no longer strictly increasing.
HOWEVER, if you take any rotated array and cut it perfectly in half, **AT LEAST ONE of the halves MUST be perfectly sorted!**
Look at `[4, 5, 6, 7, 0, 1, 2]`. Mid is `7`.
- Left half: `[4, 5, 6, 7]` (Perfectly sorted!).
- Right half: `[7, 0, 1, 2]` (Rotated).

This observation is the key to $O(\log n)$ time.
At every step:
1. Find `mid`.
2. Check which half is perfectly sorted by comparing `nums[left]` with `nums[mid]`.
3. If the **Left Half** is sorted:
   - Is our `target` mathematically located inside this sorted range? (i.e., `nums[left] <= target < nums[mid]`).
   - If yes, target MUST be on the left. `right = mid - 1`.
   - If no, target MUST be on the right. `left = mid + 1`.
4. If the **Right Half** is sorted:
   - Is our `target` mathematically located inside this sorted range? (i.e., `nums[mid] < target <= nums[right]`).
   - If yes, target MUST be on the right. `left = mid + 1`.
   - If no, target MUST be on the left. `right = mid - 1`.

## Optimal Approach (Modified Binary Search)
**Detailed explanation:**
1. Initialize `left = 0`, `right = nums.size() - 1`.
2. Loop while `left <= right`:
   - `mid = left + (right - left) / 2`.
   - If `nums[mid] == target`, return `mid`.
   - Check if left half is sorted: `if (nums[left] <= nums[mid])`
     - If `nums[left] <= target && target < nums[mid]`, target is in the left half: `right = mid - 1`.
     - Else, it's in the right half: `left = mid + 1`.
   - Else (right half must be sorted):
     - If `nums[mid] < target && target <= nums[right]`, target is in the right half: `left = mid + 1`.
     - Else, it's in the left half: `right = mid - 1`.
3. Return `-1`.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$

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
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // Check if the LEFT half is perfectly sorted
            if (nums[left] <= nums[mid]) {
                // Is the target mathematically within this sorted left half?
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1; // It is! Search left.
                } else {
                    left = mid + 1;  // It's not! Search right.
                }
            } 
            // Otherwise, the RIGHT half MUST be perfectly sorted
            else {
                // Is the target mathematically within this sorted right half?
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;  // It is! Search right.
                } else {
                    right = mid - 1; // It's not! Search left.
                }
            }
        }
        
        return -1;
    }
};
```

## Dry Run
`nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
- `left = 0`, `right = 6`. `mid = 3` (`nums[3] = 7`).
- Is `nums[left] <= nums[mid]`? `4 <= 7`. YES! Left half is sorted.
- Is `target` (0) between `4` and `7`? NO! `0` is not `>= 4`.
- Therefore, target must be in the right half! `left = mid + 1 = 4`.
- `left = 4`, `right = 6`. `mid = 5` (`nums[5] = 1`).
- Is `nums[left] <= nums[mid]`? `0 <= 1`. YES! Left half is sorted.
- Is `target` (0) between `0` and `1`? `0 <= 0` and `0 < 1`. YES!
- Therefore, target must be in the left half! `right = mid - 1 = 4`.
- `left = 4`, `right = 4`. `mid = 4` (`nums[4] = 0`).
- `nums[4] == 0`. We found the target! Return `4`.

## Common Mistakes
- **Using `<` instead of `<=` when checking `nums[left] <= nums[mid]`:** If `left` and `mid` point to the exact same element (which happens when the search space shrinks to size 1 or 2), the left half technically IS sorted (an array of size 1 is sorted). If you omit the `=`, the logic falls into the `else` block and fails.

## Similar Problems
- Search in Rotated Sorted Array II (Handles duplicates)
- Find Minimum in Rotated Sorted Array
