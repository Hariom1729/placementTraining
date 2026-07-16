# Remove Duplicates from Sorted Array

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Two Pointers / Arrays

## Pattern
Same Direction (Fast and Slow Pointers)

## Problem Statement
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following things:
- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Input
- `nums` vector of integers.

## Output
- Modify vector in-place.
- Return an integer `k`.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

## Edge Cases
- Array has only 1 element.
- All elements are the exact same (returns `k = 1`).
- All elements are already unique.

## Intuition
The array is sorted, which means all duplicates are guaranteed to be **adjacent** to each other.
Since we need to modify the array **in-place** with $O(1)$ extra space, we can't create a new array.

Instead, we use the **Fast and Slow Pointer** technique!
- `slow` pointer: Keeps track of the boundary where the "unique" elements end.
- `fast` pointer: Scans ahead to find the *next* unique element.

Since the first element `nums[0]` is always unique by definition, `slow` starts at index `1`.
`fast` also starts at index `1`.
If `nums[fast] != nums[fast - 1]`, we found a new unique element! We copy this element to `nums[slow]`, and increment `slow`.
If it's equal, we just skip it by incrementing `fast`.

At the end, `slow` will represent exactly the number of unique elements!

## Optimal Approach (Fast and Slow Pointers)
**Detailed explanation:**
1. If array is empty, return 0 (Based on constraints, it's at least 1, but good practice).
2. Initialize `slow = 1`.
3. Loop `fast` from `1` to `nums.size() - 1`:
   - If `nums[fast] != nums[fast - 1]`:
     - We found a new unique element!
     - `nums[slow] = nums[fast]`.
     - `slow++`.
4. Return `slow`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        // slow pointer indicates the index where the NEXT unique element should be placed
        int slow = 1;
        
        for (int fast = 1; fast < nums.size(); fast++) {
            // If the current element is different from the previous one, it's unique!
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        
        return slow; // slow is exactly the count of unique elements
    }
};
```

## Dry Run
`nums = [0, 0, 1, 1, 1, 2, 2, 3]`
- `slow = 1`, `fast = 1`.
- `fast=1` (0). `nums[1] == nums[0]`. Skip.
- `fast=2` (1). `nums[2] != nums[1]` (1 != 0). Unique!
  - `nums[slow] = nums[2]` -> `nums[1] = 1`.
  - `slow++` -> 2.
- `fast=3` (1). `nums[3] == nums[2]`. Skip.
- `fast=4` (1). Skip.
- `fast=5` (2). `nums[5] != nums[4]` (2 != 1). Unique!
  - `nums[slow] = nums[5]` -> `nums[2] = 2`.
  - `slow++` -> 3.
- `fast=6` (2). Skip.
- `fast=7` (3). Unique!
  - `nums[slow] = nums[7]` -> `nums[3] = 3`.
  - `slow++` -> 4.
- Returns `slow` (4). First 4 elements are `[0, 1, 2, 3]`.

## Common Mistakes
- **Erasing elements using `nums.erase()`:** Do not do `nums.erase(nums.begin() + i)`. While this passes, `vector::erase` is an $O(N)$ operation. Calling it inside a loop makes your time complexity $O(N^2)$, which is incredibly inefficient and defeats the purpose of the two-pointer optimization!

## Similar Problems
- Remove Element
- Move Zeroes
