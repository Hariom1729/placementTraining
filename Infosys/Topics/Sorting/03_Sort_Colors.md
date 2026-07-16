# Sort Colors

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google

## Topic
Sorting / Two Pointers / Arrays

## Pattern
Dutch National Flag Algorithm

## Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Input
- `nums` vector of integers.

## Output
- Return nothing. Modify the vector in-place.

## Sample Test Cases

**Example 1:**
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:**
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Edge Cases
- All elements are the same color.
- Array contains only two of the three colors.

## Intuition
This problem famously asks for a 1-pass, $O(N)$ time, $O(1)$ space solution.
Because there are only 3 distinct values (`0`, `1`, `2`), this is the textbook use-case for the **Dutch National Flag Algorithm** proposed by Edsger Dijkstra.

We maintain three pointers:
- `low`: Where the next `0` should go.
- `mid`: The current element we are inspecting.
- `high`: Where the next `2` should go.

The logic is simple. We scan the array with `mid`:
- If `nums[mid] == 0`: We swap it with `nums[low]`. Since we know `nums[low]` (if it wasn't the same as `mid`) was a `1` that got pushed aside, we can safely increment BOTH `low` and `mid`.
- If `nums[mid] == 1`: It's already in the correct middle section. Just increment `mid`.
- If `nums[mid] == 2`: We swap it with `nums[high]`. We decrement `high`. **Crucially, we DO NOT increment `mid`!** Why? Because the element we just swapped in from the end of the array is completely unknown to us! We must evaluate it on the next loop iteration.

## Brute Force Approach
**Explanation:** Any standard sorting algorithm like Merge Sort or Quick Sort.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$ for Quick Sort.

## Intermediate Approach (Counting Sort / 2-Pass)
**Explanation:** Count the number of 0s, 1s, and 2s in a frequency map. Then rewrite the array.
**Time Complexity:** $O(N)$ (but requires 2 passes).
**Space Complexity:** $O(1)$.

## Optimal Approach (Dutch National Flag / 1-Pass)
**Detailed explanation:**
1. Initialize `low = 0`, `mid = 0`, `high = nums.size() - 1`.
2. Loop while `mid <= high`:
   - If `nums[mid] == 0`:
     - `swap(nums[low], nums[mid])`.
     - `low++`, `mid++`.
   - Else if `nums[mid] == 1`:
     - `mid++`.
   - Else if `nums[mid] == 2`:
     - `swap(nums[mid], nums[high])`.
     - `high--`. (Do not increment mid!).

**Time Complexity:** $O(N)$ as we process each element exactly once.
**Space Complexity:** $O(1)$ strictly in-place.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                // If it's 0, swap it to the left partition
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                // If it's 1, it's already in the middle partition
                mid++;
            } else if (nums[mid] == 2) {
                // If it's 2, swap it to the right partition
                swap(nums[mid], nums[high]);
                high--;
                // Note: We don't increment mid here because the element we swapped
                // from 'high' hasn't been checked yet. It could be a 0!
            }
        }
    }
};
```

## Dry Run
`nums = [2, 0, 2, 1, 1, 0]`
- `low=0`, `mid=0`, `high=5`.
- `mid=0 (2)`: `swap(mid, high)`. `nums = [0, 0, 2, 1, 1, 2]`. `high = 4`. `mid=0`.
- `mid=0 (0)`: `swap(low, mid)`. `nums = [0, 0, 2, 1, 1, 2]`. `low = 1`, `mid = 1`.
- `mid=1 (0)`: `swap(low, mid)`. `nums = [0, 0, 2, 1, 1, 2]`. `low = 2`, `mid = 2`.
- `mid=2 (2)`: `swap(mid, high)`. `nums = [0, 0, 1, 1, 2, 2]`. `high = 3`. `mid = 2`.
- `mid=2 (1)`: `mid = 3`.
- `mid=3 (1)`: `mid = 4`.
- `mid=4 > high(3)`. Loop terminates!
- Result: `[0, 0, 1, 1, 2, 2]`.

## Common Mistakes
- **Incrementing `mid` when swapping a `2`:** If you do this, you might swap a `0` from the back of the array into the `mid` position, and then immediately skip over it! This leaves a `0` trapped in the middle of your `1`s.
- **Using `mid < high` instead of `mid <= high`:** If you don't use `<=`, the loop terminates one step too early, leaving the final element un-evaluated.

## Similar Problems
- Move Zeroes
- Sort Array By Parity
