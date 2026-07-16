# Move Zeroes

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Facebook, Amazon, Apple, Microsoft

## Topic
Two Pointers / Arrays

## Pattern
Same Direction (Fast and Slow Pointers)

## Problem Statement
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Input
- `nums` vector of integers.

## Output
- Modify vector in-place. Return nothing.

## Sample Test Cases

**Example 1:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2:**
```
Input: nums = [0]
Output: [0]
```

## Edge Cases
- Array has no zeroes (should remain unchanged).
- Array is all zeroes (should remain unchanged).
- Zeroes are already at the end.

## Intuition
This problem is fundamentally identical to **Remove Duplicates from Sorted Array** or **Remove Element**.
We want to "remove" the zeroes by shifting all the non-zero elements to the front.
Once all the non-zero elements are tightly packed at the front, we can just fill the rest of the array with zeroes!

We use **Fast and Slow Pointers**:
- `slow` pointer: Represents the boundary where the next non-zero element should be placed.
- `fast` pointer: Scans ahead to find non-zero elements.

Whenever `fast` finds a non-zero element, we place it at the `slow` index, and increment `slow`.
After `fast` finishes scanning the entire array, `slow` will be pointing exactly at the index where the zeroes should start.
We just run a simple `while` loop from `slow` to the end of the array, setting every element to `0`.

Alternatively, we can just **swap** `nums[slow]` and `nums[fast]` whenever `nums[fast] != 0`. This does it in a single pass without needing a second loop to fill zeroes!

## Optimal Approach (Fast & Slow Pointers with Swap)
**Detailed explanation:**
1. Initialize `slow = 0`.
2. Loop `fast` from `0` to `nums.size() - 1`:
   - If `nums[fast] != 0`:
     - Swap `nums[slow]` and `nums[fast]`.
     - Increment `slow`.
3. (If you don't swap, you would do `nums[slow] = nums[fast]` and then have a second loop to fill the rest with `0`s. Both are fine, swap is slightly cleaner).

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        
        for (int fast = 0; fast < nums.size(); fast++) {
            // When we find a non-zero element, swap it with the slow pointer
            if (nums[fast] != 0) {
                swap(nums[slow], nums[fast]);
                slow++;
            }
        }
    }
};

/*
// Alternative approach without swap (2 passes)
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        
        // Pass 1: Shift all non-zero elements forward
        for (int fast = 0; fast < nums.size(); fast++) {
            if (nums[fast] != 0) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        
        // Pass 2: Fill the rest with zeroes
        while (slow < nums.size()) {
            nums[slow] = 0;
            slow++;
        }
    }
};
*/
```

## Dry Run
`nums = [0, 1, 0, 3, 12]`
- `slow = 0`.
- `fast=0` (0). `nums[fast] == 0`. Skip.
- `fast=1` (1). `nums[fast] != 0`. Swap `nums[0]` and `nums[1]`.
  - Array: `[1, 0, 0, 3, 12]`.
  - `slow++` -> 1.
- `fast=2` (0). Skip.
- `fast=3` (3). `nums[fast] != 0`. Swap `nums[1]` and `nums[3]`.
  - Array: `[1, 3, 0, 0, 12]`.
  - `slow++` -> 2.
- `fast=4` (12). `nums[fast] != 0`. Swap `nums[2]` and `nums[4]`.
  - Array: `[1, 3, 12, 0, 0]`.
  - `slow++` -> 3.
- Done. Array is `[1, 3, 12, 0, 0]`.

## Common Mistakes
- **Erasing elements:** Using `nums.erase()` to remove zeroes and `nums.push_back(0)` to add them to the end is $O(N^2)$ time complexity. Avoid `erase` in vector loops.

## Similar Problems
- Remove Element
- Remove Duplicates from Sorted Array
