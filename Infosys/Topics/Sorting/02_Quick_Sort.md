# Quick Sort

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP (Extremely common algorithm question)
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Sorting / Divide and Conquer

## Pattern
Partitioning

## Problem Statement
Given an array of integers `nums`, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in $O(n \log n)$ time complexity and with $O(\log n)$ space complexity.

*Note: Quick Sort is the classic $O(N \log N)$ in-place sorting algorithm.*

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
- Array is already sorted (Worst case for naive pivot choice!).
- Array is sorted in reverse order.
- Array has all identical elements.

## Intuition
Quick Sort is a **Divide and Conquer** algorithm, but unlike Merge Sort, it does the heavy lifting *before* the recursive calls!
The core idea is **Partitioning**:
1. Pick an element from the array to be the **Pivot**.
2. Rearrange the array so that all elements **smaller** than the pivot are on the left, and all elements **greater** than the pivot are on the right.
3. Now, the pivot is in its **exact, final sorted position**!
4. Recursively apply this to the sub-array on the left of the pivot and the sub-array on the right of the pivot.

**The Pivot Problem:**
If you always pick the *last* element as the pivot, and the array is already sorted, you will partition an array of size $N$ into sizes $N-1$ and $0$. This causes $O(N^2)$ worst-case time complexity!
To fix this, we pick a **Random Pivot** (or the middle element) and swap it with the last element before partitioning. This guarantees $O(N \log N)$ on average.

## Optimal Approach (Quick Sort with Lomuto Partition Scheme)
**Detailed explanation:**
1. Create a `quickSort(nums, low, high)` function.
2. Base case: If `low >= high`, return.
3. **Partitioning step:**
   - Pick a random pivot index between `low` and `high`. Swap `nums[pivotIndex]` with `nums[high]`.
   - Now the pivot value is at the end: `pivot = nums[high]`.
   - Maintain a pointer `i = low - 1`. (This points to the end of the "smaller than pivot" section).
   - Loop `j` from `low` to `high - 1`:
     - If `nums[j] < pivot`, increment `i` and `swap(nums[i], nums[j])`.
   - After the loop, swap the pivot into its correct place: `swap(nums[i + 1], nums[high])`.
   - Return `i + 1` (the final index of the pivot).
4. Let the returned index be `pi`.
5. Recursively call `quickSort(nums, low, pi - 1)`.
6. Recursively call `quickSort(nums, pi + 1, high)`.

**Time Complexity:** Average $O(N \log N)$. Worst Case $O(N^2)$ (extremely rare with random pivot).
**Space Complexity:** $O(\log N)$ auxiliary space for the recursion stack. It is **In-Place** because it modifies the array directly without temporary arrays (unlike Merge Sort).

## C++ Solution

```cpp
#include <vector>
#include <cstdlib> // for rand()
#include <algorithm> // for swap
using namespace std;

class Solution {
private:
    int partition(vector<int>& nums, int low, int high) {
        // Random pivot to avoid O(N^2) worst case on sorted arrays
        int randomIndex = low + rand() % (high - low + 1);
        swap(nums[randomIndex], nums[high]);
        
        int pivot = nums[high];
        int i = low - 1; // Index of smaller element
        
        for (int j = low; j < high; j++) {
            // If current element is smaller than the pivot
            if (nums[j] < pivot) {
                i++; // Expand the smaller section
                swap(nums[i], nums[j]);
            }
        }
        
        // Place the pivot in its correct sorted position
        swap(nums[i + 1], nums[high]);
        
        // Return the partitioning index
        return i + 1;
    }
    
    void quickSort(vector<int>& nums, int low, int high) {
        if (low < high) {
            // pi is the partitioning index, nums[pi] is now at right place
            int pi = partition(nums, low, high);
            
            // Recursively sort elements before and after partition
            quickSort(nums, low, pi - 1);
            quickSort(nums, pi + 1, high);
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
};
```

## Dry Run
`nums = [5, 2, 3, 1]`
- `quickSort(0, 3)`.
- `partition(0, 3)`: Let's assume random pivot picks index 2 (value `3`).
  - Swap index 2 and 3: `nums = [5, 2, 1, 3]`. Pivot is `3`.
  - `i = -1`.
  - `j=0 (5)`: Not `< 3`.
  - `j=1 (2)`: `< 3`! `i=0`. Swap `nums[0]` and `nums[1]`. `nums = [2, 5, 1, 3]`.
  - `j=2 (1)`: `< 3`! `i=1`. Swap `nums[1]` and `nums[2]`. `nums = [2, 1, 5, 3]`.
  - Loop ends. Swap pivot `nums[i+1]` (index 2) with `nums[high]` (index 3).
  - `nums = [2, 1, 3, 5]`. Returns `pi = 2`.
- Notice how `3` is in its final sorted position! Everything left is `< 3`, everything right is `> 3`.
- `quickSort(0, 1)` -> sorts `[2, 1]` into `[1, 2]`.
- `quickSort(3, 3)` -> base case.
- Result: `[1, 2, 3, 5]`.

## Common Mistakes
- **Forgetting the Random Pivot:** If you always use `pivot = nums[high]`, and LeetCode gives you an array of 50,000 elements sorted in ascending order, you will hit maximum recursion depth or Time Limit Exceeded (TLE) because it becomes $O(N^2)$.
- **Using `<` in recursion:** Always do `low < high` for the base case, not `low <= high`. A 1-element array is trivially sorted and attempting to partition it is wasted work.

## Similar Problems
- Merge Sort
- Kth Largest Element in an Array (Quickselect uses the exact same partition logic)
