# First Missing Positive

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Amazon, Microsoft, Facebook

## Topic
Arrays

## Pattern
Cycle Sort / Hash as Index

## Problem Statement
Given an unsorted integer array `nums`, return the smallest missing positive integer.
You must implement an algorithm that runs in $O(n)$ time and uses constant extra space.

## Constraints
- $1 \le nums.length \le 10^5$
- $-2^{31} \le nums[i] \le 2^{31} - 1$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a single integer representing the first missing positive.

## Sample Input
```
4
3 4 -1 1
```

## Sample Output
```
2
```

## Edge Cases
- All negative numbers (return 1).
- Array already sorted sequentially starting from 1 (return `N + 1`).
- Array containing duplicates.

## Approach 1
Brute Force (Sorting)
**Explanation:** Sort the array. Iterate through it, looking for `1`. Increment a `target` variable as long as the array matches it.
**Time Complexity:** $O(N \log N)$ (Fails the $O(N)$ requirement).
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Hash Set)
**Explanation:** Put all elements into a Hash Set. Loop `i` from `1` to `N+1`. Check if `i` is in the Hash Set. Return the first one that isn't.
**Complexity:** $O(N)$ time, $O(N)$ space. (Fails the $O(1)$ space requirement).

## Approach 3
Optimal Approach (Cycle Sort / Hashing in-place)
**Explanation:** 
Since we want the first missing positive integer, the answer must inherently fall in the range `[1, N+1]`.
We can use the array itself as a Hash Map.
The goal is to place every number `x` where `1 <= x <= N` at the index `x - 1`. (So `1` goes to index 0, `2` goes to index 1, etc.)
1. Iterate through the array. While the current number `nums[i]` is in the valid range `[1, N]` AND it is not currently at its correct index (`nums[i] != nums[nums[i] - 1]`), swap it into its correct place.
2. After this cycle sort completes, iterate through the array again.
3. The first index `i` where `nums[i] != i + 1` is the missing number! Return `i + 1`.
4. If the loop completes without returning, it means all numbers `1` to `N` are present in perfectly sorted order. Thus, the missing positive is `N + 1`.

**Dry Run:**
`nums = [3, 4, -1, 1]`
- `i=0` (3): 3 is in range `[1,4]`. Correct index for 3 is 2. `nums[2] = -1`. Swap `nums[0]` and `nums[2]`. Array becomes `[-1, 4, 3, 1]`.
- `i=0` (-1): -1 not in range. Move to next.
- `i=1` (4): 4 is in range. Correct index is 3. `nums[3] = 1`. Swap `nums[1]` and `nums[3]`. Array becomes `[-1, 1, 3, 4]`.
- `i=1` (1): 1 is in range. Correct index is 0. Swap `nums[1]` and `nums[0]`. Array becomes `[1, -1, 3, 4]`.
- `i=1` (-1): not in range. Next.
- `i=2` (3): 3 is already at index 2. Next.
- `i=3` (4): 4 is already at index 3. Next.
Second pass on `[1, -1, 3, 4]`:
- index 0: `nums[0] == 1` (Correct)
- index 1: `nums[1] != 2` (Incorrect!). Return `1 + 1 = 2`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                // Swap
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        return n + 1;
    }
}
```

## Python Solution
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Python tuple unpacking swap
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                swap(nums[i], nums[nums[i] - 1]);
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        return n + 1;
    }
};
```

## Common Mistakes
- **Using an `if` instead of a `while` for swapping:** When you swap a number into its correct place, the number that gets swapped *back* to the current index `i` might also need to be swapped to its own correct place. You must use a `while` loop to continuously swap until the number sitting at `i` is either out of bounds, or is finally the correct number `i+1`.

## Similar Questions
- Missing Number
- Find All Numbers Disappeared in an Array
- Find the Duplicate Number
