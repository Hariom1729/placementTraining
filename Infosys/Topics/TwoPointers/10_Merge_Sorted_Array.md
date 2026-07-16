# Merge Sorted Array

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Facebook, Microsoft, Amazon, Google

## Topic
Two Pointers / Arrays / Sorting

## Pattern
Two Pointers (Backwards)

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Input
- `nums1` vector of integers.
- `m` integer.
- `nums2` vector of integers.
- `n` integer.

## Output
- Modify `nums1` in-place. Return nothing.

## Sample Test Cases

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].
```

**Example 2:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Example 3:**
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

## Edge Cases
- `nums1` is completely empty initially (`m=0`). We must overwrite the zeros with all of `nums2`.
- `nums2` is empty (`n=0`). The array `nums1` is already correct.

## Intuition
The naive approach is to copy all elements of `nums2` into the zeros at the end of `nums1`, and then sort `nums1`. This takes $O((m+n) \log(m+n))$ time.

Since both arrays are ALREADY sorted, we can merge them in $O(m+n)$ time using **Two Pointers**.
Normally, to merge two arrays, we start at the beginning of both arrays, compare elements, and place the smaller one into a NEW array. But we aren't allowed extra space; we MUST place them in `nums1`.

If we start comparing from the left, placing the smaller element into `nums1[0]` might overwrite an existing element in `nums1` before we've had a chance to evaluate it!
**The Trick: Merge BACKWARDS!**
Since the end of `nums1` is filled with zeroes (empty space), we can safely start placing the LARGEST elements at the very back of `nums1`!
We place pointers at the end of the valid elements in `nums1` (`p1 = m - 1`) and `nums2` (`p2 = n - 1`), and a third pointer `p = m + n - 1` at the very end of the array.
We compare `nums1[p1]` and `nums2[p2]`. We place the larger one at `nums1[p]` and decrement the pointers.
This completely avoids overwriting any unsorted elements!

## Optimal Approach (Backwards Two Pointers)
**Detailed explanation:**
1. Initialize `p1 = m - 1` (pointer for valid elements in nums1).
2. Initialize `p2 = n - 1` (pointer for elements in nums2).
3. Initialize `p = m + n - 1` (pointer for the insertion index).
4. Loop while `p1 >= 0` AND `p2 >= 0`:
   - If `nums1[p1] > nums2[p2]`:
     - Place `nums1[p1]` at `nums1[p]`.
     - `p1--`, `p--`.
   - Else:
     - Place `nums2[p2]` at `nums1[p]`.
     - `p2--`, `p--`.
5. If `p2 >= 0` (meaning there are still elements left in `nums2`), we must copy them over.
   - Loop while `p2 >= 0`: `nums1[p] = nums2[p2]`; `p2--`; `p--`.
6. (If `p1 >= 0`, we don't need to do anything because they are already perfectly in place in `nums1`!).

**Time Complexity:** $O(M + N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Pointers for the last valid elements
        int p1 = m - 1;
        int p2 = n - 1;
        
        // Pointer for the insertion position (from the back)
        int p = m + n - 1;
        
        // Compare elements from the back and place the largest at 'p'
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p] = nums1[p1];
                p1--;
            } else {
                nums1[p] = nums2[p2];
                p2--;
            }
            p--;
        }
        
        // If there are any elements left in nums2, copy them
        // (No need to copy nums1, because they are already in place!)
        while (p2 >= 0) {
            nums1[p] = nums2[p2];
            p2--;
            p--;
        }
    }
};
```

## Dry Run
`nums1 = [1, 2, 3, 0, 0, 0], m = 3`
`nums2 = [2, 5, 6], n = 3`
- `p1 = 2` (val=3), `p2 = 2` (val=6), `p = 5`.
- `3 < 6`. `nums1[5] = 6`. `p2 = 1`, `p = 4`.
- `p1 = 2` (val=3), `p2 = 1` (val=5).
- `3 < 5`. `nums1[4] = 5`. `p2 = 0`, `p = 3`.
- `p1 = 2` (val=3), `p2 = 0` (val=2).
- `3 > 2`. `nums1[3] = 3`. `p1 = 1`, `p = 2`.
- `p1 = 1` (val=2), `p2 = 0` (val=2).
- `2 == 2`. `nums1[2] = 2`. `p2 = -1`, `p = 1`.
- `p2 < 0`. Main loop breaks!
- Second loop is skipped because `p2 = -1`.
- Array is `[1, 2, 2, 3, 5, 6]`. Perfect!

## Common Mistakes
- **Forgetting the second `while (p2 >= 0)` loop:** If `nums1 = [4, 5, 6, 0, 0, 0]` and `nums2 = [1, 2, 3]`, all elements of `nums1` will be placed at the end. `p1` will reach `-1`, and the main loop will break. `nums1` will look like `[4, 5, 6, 4, 5, 6]`. You MUST have the second loop to copy the remaining `[1, 2, 3]` from `nums2` into the front!

## Similar Problems
- Merge Two Sorted Lists (Linked list variation)
- Squares of a Sorted Array (Also solved via backwards placement)
