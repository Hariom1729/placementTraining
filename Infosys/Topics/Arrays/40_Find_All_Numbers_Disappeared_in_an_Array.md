# Find All Numbers Disappeared in an Array

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Related Companies: Google, Amazon, Microsoft

## Topic
Arrays

## Pattern
In-place Hashing / Cycle Sort

## Problem Statement
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

You must do this without extra space and in $O(n)$ runtime. You may assume the returned list does not count as extra space.

## Constraints
- $n == nums.length$
- $1 \le n \le 10^5$
- $1 \le nums[i] \le n$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a 1D array of missing integers.

## Sample Input
```
8
4 3 2 7 8 2 3 1
```

## Sample Output
```
5 6
```

## Edge Cases
- No numbers are missing (array has 1 to N exactly).
- Only one number is missing.
- Array is composed of a single number repeated `n` times.

## Approach 1
Brute Force (Hash Set)
**Explanation:** Add all elements to a Hash Set. Loop `1` to `N` and check if the element exists in the Set. If not, add to result.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ (Fails the extra space constraint).

## Approach 2
Optimal Approach (State Negation)
**Explanation:** 
Because the values in the array map perfectly to indices in the array (value `x` corresponds to index `x - 1`), we can use the array itself to store boolean state.
For every number `x` we encounter, we calculate its index mapping: `abs(x) - 1`.
We then go to that index, and multiply the number sitting there by `-1` (if it isn't negative already).
After iterating through the whole array, any index `i` that contains a **positive** number means that we *never encountered the value `i + 1`*!
1. Iterate through array. For each `val`, set `nums[abs(val) - 1] = -1 * abs(nums[abs(val) - 1])`.
2. Iterate through array again. If `nums[i] > 0`, it means `i + 1` was never seen. Add `i + 1` to result list.

**Dry Run:**
`[4, 3, 2, 7, 8, 2, 3, 1]`
- Pass 1:
  - 4 -> make index 3 negative -> `[4, 3, 2, -7, 8, 2, 3, 1]`
  - 3 -> make index 2 negative -> `[4, 3, -2, -7, 8, 2, 3, 1]`
  - 2 -> make index 1 negative -> `[4, -3, -2, -7, 8, 2, 3, 1]`
  - 7 -> make index 6 negative -> `[4, -3, -2, -7, 8, 2, -3, 1]`
  - 8 -> make index 7 negative -> `[4, -3, -2, -7, 8, 2, -3, -1]`
  - 2 -> make index 1 negative -> (already negative)
  - 3 -> make index 2 negative -> (already negative)
  - 1 -> make index 0 negative -> `[-4, -3, -2, -7, 8, 2, -3, -1]`
- Pass 2:
  - `nums[4]` is positive (8). Missing: 5.
  - `nums[5]` is positive (2). Missing: 6.
Return `[5, 6]`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ (Result array does not count).

## Java Solution
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                res.add(i + 1);
            }
        }
        
        return res;
    }
}
```

## Python Solution
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
                
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                
        return res
```

## C++ Solution
```cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                res.push_back(i + 1);
            }
        }
        
        return res;
    }
};
```

## Common Mistakes
- **Forgetting `Math.abs()` on the first pass:** Because elements are turned negative in real time, if you pull `nums[i]` on iteration 5, it might have been turned negative during iteration 1. You MUST take the absolute value of `nums[i]` before mapping it to an index, or you will get a Negative Array Index Out of Bounds Exception.

## Similar Questions
- Find All Duplicates in an Array
- First Missing Positive
