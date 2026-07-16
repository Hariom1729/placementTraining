# Two Sum II - Input Array Is Sorted

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Apple, Google

## Topic
Two Pointers / Arrays

## Pattern
Opposite Ends (Collision)

## Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Input
- `numbers` vector of integers.
- `target` integer.

## Output
- Return a vector of two integers.

## Sample Test Cases

**Example 1:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

## Edge Cases
- Negative numbers involved.
- Duplicates in array (e.g., `[0, 0]`, target `0`).

## Intuition
Normally, Two Sum uses a Hash Map to achieve $O(N)$ time, but that requires $O(N)$ space.
Here, the array is **already sorted** and the problem explicitly demands **constant extra space**.

Since the array is sorted, we can use the **Two Pointers** technique.
We place one pointer at the extreme left (`left = 0`) and one pointer at the extreme right (`right = n - 1`).
We calculate the sum: `sum = numbers[left] + numbers[right]`.
- If `sum == target`: We found our pair!
- If `sum > target`: The sum is too large. Since the array is sorted, the only way to DECREASE the sum is to move the `right` pointer to the left! (`right--`).
- If `sum < target`: The sum is too small. Since the array is sorted, the only way to INCREASE the sum is to move the `left` pointer to the right! (`left++`).

Because the array is sorted, this logic is mathematically guaranteed to find the solution if it exists.

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. Initialize `left = 0`, `right = numbers.size() - 1`.
2. Loop while `left < right`:
   - `sum = numbers[left] + numbers[right]`.
   - If `sum == target`, return `{left + 1, right + 1}` (1-indexed).
   - If `sum > target`, `right--`.
   - If `sum < target`, `left++`.
3. The problem guarantees a solution, so no need for a fallback return, but you can return `{}` at the end to satisfy compiler warnings.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        
        while (left < right) {
            int currentSum = numbers[left] + numbers[right];
            
            if (currentSum == target) {
                // The problem requires 1-based indexing
                return {left + 1, right + 1};
            } else if (currentSum > target) {
                // Sum is too large, decrease it by moving right pointer to the left
                right--;
            } else {
                // Sum is too small, increase it by moving left pointer to the right
                left++;
            }
        }
        
        return {}; // Will never reach here due to guaranteed solution
    }
};
```

## Dry Run
`numbers = [2, 7, 11, 15], target = 9`
- `left = 0 (2)`, `right = 3 (15)`. `sum = 17`.
- `17 > 9`. Move right pointer. `right--` -> `2`.
- `left = 0 (2)`, `right = 2 (11)`. `sum = 13`.
- `13 > 9`. Move right pointer. `right--` -> `1`.
- `left = 0 (2)`, `right = 1 (7)`. `sum = 9`.
- `9 == 9`. Return `{0 + 1, 1 + 1}` = `[1, 2]`.

## Common Mistakes
- **Using a Hash Map:** While a Hash Map gives $O(N)$ time, it completely ignores the "sorted array" hint and violates the $O(1)$ space requirement. In an interview, using a Hash Map for this specific problem variation is considered a failure to recognize the optimal algorithmic pattern.

## Similar Problems
- 3Sum
- 4Sum
