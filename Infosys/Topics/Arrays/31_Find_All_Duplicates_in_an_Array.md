# Find All Duplicates in an Array

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Microsoft, Amazon, Google

## Topic
Arrays

## Pattern
In-place Hashing / Cycle Sort

## Problem Statement
Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **once** or **twice**, return an array of all the integers that appears **twice**.

You must write an algorithm that runs in $O(n)$ time and uses only constant extra space.

## Constraints
- $n == nums.length$
- $1 \le n \le 10^5$
- $1 \le nums[i] \le n$
- Each element in `nums` appears once or twice.

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a 1D array of duplicate integers.

## Sample Input
```
8
4 3 2 7 8 2 3 1
```

## Sample Output
```
2 3
```

## Edge Cases
- No duplicates exist (return `[]`).
- The entire array is made of pairs (e.g., `[2, 2, 1, 1]`).

## Approach 1
Brute Force
**Explanation:** Sort the array. Iterate and check if `nums[i] == nums[i+1]`.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Hash Set)
**Explanation:** Iterate over the array. Add to a Set. If the element is already in the set, add it to the result array.
**Complexity:** $O(N)$ time, $O(N)$ space.

## Approach 3
Optimal Approach (In-place Hashing / State Negation)
**Explanation:** 
Since the numbers are strictly in the range `[1, n]`, we can use the array itself to track which numbers we have seen!
For every number `x = abs(nums[i])`:
- Since `x` is between `1` and `n`, `x - 1` is a valid array index.
- We go to the index `x - 1` and multiply the number sitting there by `-1`. This negative sign acts as a "visited" flag for the number `x`.
- If we encounter another `x` later, we will go to index `x - 1` and see that the number is *already negative*. This means we have seen `x` before! We add `x` to our duplicates result list.

**Dry Run:**
`[4, 3, 2, 7, 8, 2, 3, 1]`
- `i=0` (4): target index `4-1=3`. `nums[3]` is 7. Make it -7. Array: `[4, 3, 2, -7, 8, 2, 3, 1]`
- `i=1` (3): target index `3-1=2`. `nums[2]` is 2. Make it -2. Array: `[4, 3, -2, -7, 8, 2, 3, 1]`
- `i=2` (-2): `abs(-2)` = 2. Target index 1. `nums[1]` is 3. Make it -3.
- `i=3` (-7): `abs(-7)` = 7. Target index 6. `nums[6]` is 3. Make it -3.
- `i=4` (8): `abs(8)` = 8. Target index 7. `nums[7]` is 1. Make it -1.
- `i=5` (2): `abs(2)` = 2. Target index 1. `nums[1]` is -3. It's ALREADY NEGATIVE! This means 2 is a duplicate. Add `2` to result.
- `i=6` (-3): `abs(-3)` = 3. Target index 2. `nums[2]` is -2. ALREADY NEGATIVE! Add `3` to result.
- `i=7` (-1): `abs(-1)` = 1. Target index 0. `nums[0]` is 4. Make it -4.
Result: `[2, 3]`

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ (Result array does not count towards extra space).

## Java Solution
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            
            if (nums[index] < 0) {
                res.add(Math.abs(nums[i]));
            } else {
                nums[index] = -nums[index];
            }
        }
        
        return res;
    }
}
```

## Python Solution
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] *= -1
                
        return res
```

## C++ Solution
```cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            
            if (nums[index] < 0) {
                res.push_back(abs(nums[i]));
            } else {
                nums[index] = -nums[index];
            }
        }
        
        return res;
    }
};
```

## Common Mistakes
- **Forgetting to take absolute value:** Because we are mutating the array by turning elements negative, when we process an element, it might have already been turned negative by a previous step. You MUST take `abs(nums[i])` to calculate the correct index, otherwise you will get an Out of Bounds index error.

## Similar Questions
- Find All Numbers Disappeared in an Array
- First Missing Positive
