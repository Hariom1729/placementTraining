# Find All Duplicates in an Array

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft

## Topic
Hashing / Arrays

## Pattern
In-Place Hashing (Cyclic Sort logic)

## Problem Statement
Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **once** or **twice**, return an array of all the integers that appears **twice**.

You must write an algorithm that runs in $O(n)$ time and uses only **constant extra space**.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once** or **twice**.

## Input
- `nums` vector of integers.

## Output
- Return a vector of integers.

## Sample Test Cases

**Example 1:**
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

**Example 2:**
```
Input: nums = [1,1,2]
Output: [1]
```

**Example 3:**
```
Input: nums = [1]
Output: []
```

## Edge Cases
- No duplicates exist.
- Array elements are out of bounds? (Guaranteed by constraints to be in `[1, n]`).

## Intuition
This problem is a classic **In-Place Hashing** trick.
The constraints explicitly state: `1 <= nums[i] <= n`.
This is a massive hint! It means every number in the array can perfectly map to a valid **index** in the array (if we subtract 1).
If we see the number `4`, we know it "belongs" at index `3`.
To track that we have "seen" the number `4`, we can go to index `3` and mark the number sitting there as **negative**!
- We read `abs(nums[i])`. Let this be `x`.
- We go to `nums[x - 1]`.
- If `nums[x - 1]` is ALREADY negative, it means we have visited this index before! That means `x` is a duplicate!
- If `nums[x - 1]` is positive, we make it negative: `nums[x - 1] *= -1`.

By using the signs of the array itself to store boolean "seen" flags, we achieve Hash Set functionality with exactly $O(1)$ extra space!

## Brute Force Approach
**Explanation:** Sort the array $O(N \log N)$ and find adjacent duplicates, or use a Hash Set $O(N)$ space.
**Time Complexity:** $O(N)$ with $O(N)$ space using Hash Set.
**Space Complexity:** $O(N)$ space using Hash Set. (Fails the follow-up constraints).

## Optimal Approach (In-Place Array Negation)
**Detailed explanation:**
1. Initialize `vector<int> result`.
2. Iterate `i` from `0` to `n - 1`:
   - Get the true value of the current element: `int val = abs(nums[i])`.
   - Calculate the index this value maps to: `int index = val - 1`.
   - Check the sign of `nums[index]`:
     - If `nums[index] < 0`, we have seen `val` before! `result.push_back(val)`.
     - Else, it's the first time seeing it. Mark it as seen by negating it: `nums[index] = -nums[index]`.
3. Return `result`.

**Time Complexity:** $O(N)$ as we do a single pass through the array.
**Space Complexity:** $O(1)$ constant space (the result array does not count towards extra space constraints).

## C++ Solution

```cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        
        for (int i = 0; i < nums.size(); i++) {
            // Get the absolute value because the number might have been negated already
            int val = abs(nums[i]);
            
            // Map the value to an array index (1 to n maps to 0 to n-1)
            int index = val - 1;
            
            // If the value at that index is already negative, we've seen 'val' before!
            if (nums[index] < 0) {
                result.push_back(val);
            } else {
                // Otherwise, mark it as seen by negating the value at that index
                nums[index] = -nums[index];
            }
        }
        
        return result;
    }
};
```

## Dry Run
`nums = [4, 3, 2, 7, 8, 2, 3, 1]`
- `i=0 (4)`: `val=4`, `idx=3`. `nums[3]` is `7` (positive). Set `nums[3] = -7`.
  - Array: `[4, 3, 2, -7, 8, 2, 3, 1]`
- `i=1 (3)`: `val=3`, `idx=2`. `nums[2]` is `2` (pos). Set `nums[2] = -2`.
  - Array: `[4, 3, -2, -7, 8, 2, 3, 1]`
- `i=2 (-2)`: `val=2`, `idx=1`. `nums[1]` is `3` (pos). Set `nums[1] = -3`.
  - Array: `[4, -3, -2, -7, 8, 2, 3, 1]`
- `i=3 (-7)`: `val=7`, `idx=6`. Set `nums[6] = -3`.
- `i=4 (8)`: `val=8`, `idx=7`. Set `nums[7] = -1`.
- `i=5 (2)`: `val=2`, `idx=1`. `nums[1]` is `-3` (NEGATIVE!). We found a duplicate! Push `2`.
- `i=6 (-3)`: `val=3`, `idx=2`. `nums[2]` is `-2` (NEGATIVE!). Duplicate! Push `3`.
- `i=7 (-1)`: `val=1`, `idx=0`. Set `nums[0] = -4`.

Result: `[2, 3]`.

## Common Mistakes
- **Not using `abs()`:** Since you are mutating the array as you go, you might read `nums[i]` *after* another number negated it! If you use a negative number to calculate an array index `index = nums[i] - 1`, you will get a segfault for accessing a negative array index. Always take `abs(nums[i])`.

## Similar Problems
- Find All Numbers Disappeared in an Array
- Set Mismatch
