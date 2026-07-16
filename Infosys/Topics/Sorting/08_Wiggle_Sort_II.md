# Wiggle Sort II

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Google, Amazon

## Topic
Sorting / Array

## Pattern
Virtual Indexing / Sorting

## Problem Statement
Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`
You may assume the input array always has a valid answer.

**Follow up:** Can you do it in $O(n)$ time and/or **in-place** with $O(1)$ extra space?

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input `nums`.

## Input
- `nums` vector of integers.

## Output
- Modify the vector in-place. Return nothing.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
```

**Example 2:**
```
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
```

## Edge Cases
- Many duplicate elements, particularly exactly half the array being duplicates. (If we just interleave from left to right, we might place duplicates next to each other, violating the strictly `<` / `>` rule).

## Intuition
The problem asks us to arrange the array into "peaks" and "valleys".
Valleys: even indices `0, 2, 4...`
Peaks: odd indices `1, 3, 5...`

**The $O(N \log N)$ Sorting Approach:**
1. Sort the array. Now all the small numbers are on the left half, and all the large numbers are on the right half.
2. We want to place the small numbers in the valleys (even indices) and large numbers in the peaks (odd indices).
3. To avoid putting identical numbers next to each other (e.g., if the median element is duplicated and spans both the end of the left half and start of the right half), we must pull from the **REVERSE** of the halves!
   - Fill valleys by pulling from the middle down to the start.
   - Fill peaks by pulling from the end down to the middle.

This approach requires an extra array to hold the sorted values, taking $O(N)$ space and $O(N \log N)$ time.
*(Note: the $O(N)$ time / $O(1)$ space follow-up requires Quickselect and Dutch National Flag with Virtual Indexing, which is notoriously considered one of the hardest LeetCode problems of all time. We will provide the highly accepted Sorting approach as it is perfectly sufficient for 99% of interviews).*

## Optimal Approach (Sorting + Reverse Interleaving)
**Detailed explanation:**
1. Create a copy of the array and sort it: `vector<int> sorted(nums); sort(sorted.begin(), sorted.end());`
2. We need to fill `nums`. Let `n = nums.size()`.
3. Set two pointers on the `sorted` array:
   - `left = (n - 1) / 2`: Points to the end of the smaller half (the median).
   - `right = n - 1`: Points to the end of the larger half.
4. Iterate `i` from `0` to `n - 1` through `nums`:
   - If `i` is EVEN (it's a valley): `nums[i] = sorted[left--]`.
   - If `i` is ODD (it's a peak): `nums[i] = sorted[right--]`.

**Time Complexity:** $O(N \log N)$ for sorting.
**Space Complexity:** $O(N)$ for the copy array.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Create a sorted copy of the array
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        
        int n = nums.size();
        
        // Pointers starting from the END of their respective halves
        // This prevents median duplicates from clashing
        int left = (n - 1) / 2; // End of the smaller half
        int right = n - 1;      // End of the larger half
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                // Even indices are valleys: pull from smaller half
                nums[i] = sorted[left];
                left--;
            } else {
                // Odd indices are peaks: pull from larger half
                nums[i] = sorted[right];
                right--;
            }
        }
    }
};
```

## Dry Run
`nums = [1, 5, 1, 1, 6, 4]`
- `sorted = [1, 1, 1, 4, 5, 6]`. `n = 6`.
- `left = (6-1)/2 = 2` (points to `1`).
- `right = 5` (points to `6`).
- Loop `i`:
  - `i=0 (even)`: `nums[0] = sorted[2]` -> `1`. `left = 1`.
  - `i=1 (odd)`: `nums[1] = sorted[5]` -> `6`. `right = 4`.
  - `i=2 (even)`: `nums[2] = sorted[1]` -> `1`. `left = 0`.
  - `i=3 (odd)`: `nums[3] = sorted[4]` -> `5`. `right = 3`.
  - `i=4 (even)`: `nums[4] = sorted[0]` -> `1`. `left = -1`.
  - `i=5 (odd)`: `nums[5] = sorted[3]` -> `4`. `right = 2`.
- Final `nums`: `[1, 6, 1, 5, 1, 4]`.
- Validation: `1 < 6 > 1 < 5 > 1 < 4`. Perfect!

## Common Mistakes
- **Pulling from left-to-right:** If `sorted = [4, 5, 5, 6]` and you take `left=0`, `right=2` (moving forwards), you get:
  - `nums[0] = 4`, `nums[1] = 5`, `nums[2] = 5`, `nums[3] = 6`.
  - Result: `[4, 5, 5, 6]`. `5 > 5` is FALSE! The duplicates clashed because they were right next to each other at the middle of the sorted array. Pulling backwards solves this!

## Similar Problems
- Wiggle Sort (Easier version where `nums[i] <= nums[i+1] >= nums[i+2]`, solved in 1 pass by swapping).
