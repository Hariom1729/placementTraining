# Merge Sort

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP (Often as a foundation or follow-up)
Similar Companies: Amazon, Microsoft

## Topic
Sorting / Divide and Conquer

## Pattern
Divide and Conquer

## Problem Statement
Given an array of integers `nums`, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in $O(n \log n)$ time complexity and with the smallest space complexity possible.

*Note: Merge Sort is the classic $O(N \log N)$ stable sorting algorithm.*

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Input
- `nums` vector of integers.

## Output
- Return the sorted vector.

## Sample Test Cases

**Example 1:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2:**
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

## Edge Cases
- Array is already sorted.
- Array is sorted in reverse order.
- Array has all identical elements.

## Intuition
Merge Sort is a **Divide and Conquer** algorithm.
The core idea is incredibly simple:
1. Divide the array perfectly in half.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. **Merge** the two sorted halves back together into a single sorted array.

The base case for the recursion is when the array has 1 or 0 elements, because an array of size 1 is naturally already sorted!

The heavy lifting is done entirely in the `merge` step. How do you merge two sorted arrays `L` and `R`?
You put a pointer `i` at the start of `L` and a pointer `j` at the start of `R`. You compare `L[i]` and `R[j]`. Whichever is smaller gets placed into a temporary array, and you advance that pointer. Once one array is exhausted, you just dump the rest of the other array into the temporary array. Then, you copy the temporary array back into the original array.

## Optimal Approach (Merge Sort)
**Detailed explanation:**
1. Create a `mergeSort` function that takes `(nums, left, right)`.
2. Base case: If `left >= right`, return.
3. Find `mid = left + (right - left) / 2`.
4. Call `mergeSort(nums, left, mid)`.
5. Call `mergeSort(nums, mid + 1, right)`.
6. Call `merge(nums, left, mid, right)`.
7. `merge` function:
   - Create a temporary vector `temp` of size `right - left + 1`.
   - `i = left`, `j = mid + 1`, `k = 0`.
   - While `i <= mid` and `j <= right`:
     - If `nums[i] <= nums[j]`, `temp[k++] = nums[i++]`.
     - Else, `temp[k++] = nums[j++]`.
   - While `i <= mid`, copy remaining `nums[i]`.
   - While `j <= right`, copy remaining `nums[j]`.
   - Copy `temp` back into `nums` from `left` to `right`.

**Time Complexity:** $O(N \log N)$ in all cases (Best, Average, Worst). We divide the array $\log N$ times, and merging takes $O(N)$ time.
**Space Complexity:** $O(N)$ because we need a temporary array to hold the merged elements before copying them back. (This is Merge Sort's biggest weakness compared to Quick Sort).

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
private:
    void merge(vector<int>& nums, int left, int mid, int right) {
        // Create a temporary array to store the merged result
        vector<int> temp(right - left + 1);
        
        int i = left;      // Pointer for left half
        int j = mid + 1;   // Pointer for right half
        int k = 0;         // Pointer for temp array
        
        // Merge the two halves while both have elements
        while (i <= mid && j <= right) {
            // Use <= to maintain stability (preserve relative order of duplicates)
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }
        
        // Copy any remaining elements from the left half
        while (i <= mid) {
            temp[k++] = nums[i++];
        }
        
        // Copy any remaining elements from the right half
        while (j <= right) {
            temp[k++] = nums[j++];
        }
        
        // Copy the merged elements back into the original array
        for (int p = 0; p < temp.size(); p++) {
            nums[left + p] = temp[p];
        }
    }
    
    void mergeSort(vector<int>& nums, int left, int right) {
        if (left >= right) {
            return; // Base case: Array of size 1 is already sorted
        }
        
        int mid = left + (right - left) / 2; // Prevent integer overflow
        
        // Divide and sort left half
        mergeSort(nums, left, mid);
        
        // Divide and sort right half
        mergeSort(nums, mid + 1, right);
        
        // Merge the sorted halves
        merge(nums, left, mid, right);
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
};
```

## Dry Run
`nums = [5, 2, 3, 1]`
- `mergeSort(0, 3)` -> `mid = 1`.
  - `mergeSort(0, 1)` -> `mid = 0`.
    - `mergeSort(0, 0)` -> returns (base case).
    - `mergeSort(1, 1)` -> returns (base case).
    - `merge([5, 2], 0, 0, 1)` -> `temp` becomes `[2, 5]`. `nums` becomes `[2, 5, 3, 1]`.
  - `mergeSort(2, 3)` -> `mid = 2`.
    - `mergeSort(2, 2)` -> returns.
    - `mergeSort(3, 3)` -> returns.
    - `merge([3, 1], 2, 2, 3)` -> `temp` becomes `[1, 3]`. `nums` becomes `[2, 5, 1, 3]`.
  - `merge([2, 5, 1, 3], 0, 1, 3)`
    - `i=0 (2)`, `j=2 (1)`. 1 < 2. `temp[0] = 1`. `j++`.
    - `i=0 (2)`, `j=3 (3)`. 2 < 3. `temp[1] = 2`. `i++`.
    - `i=1 (5)`, `j=3 (3)`. 3 < 5. `temp[2] = 3`. `j++`. Right exhausted.
    - Copy remaining left: `temp[3] = 5`.
    - Copy temp back to nums: `[1, 2, 3, 5]`.

## Common Mistakes
- **Using `left + right / 2`:** This can cause integer overflow if `left` and `right` are large. Always use `left + (right - left) / 2`.
- **Not using `<` vs `<=`: ** Using `<` instead of `<=` in `if (nums[i] <= nums[j])` will break the **Stability** of the sort.

## Similar Problems
- Quick Sort
- Count Inversions (Uses the exact same merge logic, but you increment an inversion counter when `nums[i] > nums[j]`)
