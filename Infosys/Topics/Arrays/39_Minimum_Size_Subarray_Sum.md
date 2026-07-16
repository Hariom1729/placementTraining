# Minimum Size Subarray Sum

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Amazon, Facebook, Bloomberg

## Topic
Arrays

## Pattern
Sliding Window / Two Pointers

## Problem Statement
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a **contiguous subarray** of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Constraints
- $1 \le target \le 10^9$
- $1 \le nums.length \le 10^5$
- $1 \le nums[i] \le 10^4$

## Input Format
- First line: `N`
- Second line: `N` space-separated positive integers.
- Third line: `Target`

## Output Format
- Return a single integer representing the minimal length.

## Sample Input
```
6
2 3 1 2 4 3
7
```

## Sample Output
```
2
```

## Edge Cases
- Entire array sum is less than `target` (return 0).
- Single element $\ge$ `target` (return 1).

## Approach 1
Brute Force
**Explanation:** For every element, start a nested loop to find the contiguous sum. Break when the sum $\ge$ target and update the minimum length.
**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Sliding Window)
**Explanation:** 
Since all numbers are positive, the sum of a window strictly increases as we expand it to the right, and strictly decreases as we shrink it from the left. This makes Sliding Window perfectly applicable.
1. Initialize `left = 0`, `current_sum = 0`, and `min_len = INT_MAX`.
2. Iterate `right` from 0 to $N-1$:
3. Add `nums[right]` to `current_sum`.
4. **Shrink Phase:** While `current_sum >= target`, it means our window is valid.
   - Record the window length: `min_len = min(min_len, right - left + 1)`.
   - Shrink from the left by subtracting `nums[left]` from `current_sum`.
   - Increment `left`.
5. Repeat until the end of the array.
6. Return `min_len` (if it was updated) or `0` (if it's still INT_MAX).

**Dry Run:**
`nums = [2, 3, 1, 2, 4, 3]`, `target = 7`
- `r=0`: sum=2.
- `r=1`: sum=5.
- `r=2`: sum=6.
- `r=3`: sum=8 (>=7). valid! len=4. `min_len=4`. Shrink: sum=6, `l=1`.
- `r=4`: sum=10 (>=7). valid! len=4. `min_len=4`. Shrink: sum=7, `l=2`.
- Still in while loop (sum=7 >= 7). valid! len=3. `min_len=3`. Shrink: sum=6, `l=3`.
- `r=5`: sum=9 (>=7). valid! len=3. `min_len=3`. Shrink: sum=7, `l=4`.
- Still in while loop (sum=7 >= 7). valid! len=2. `min_len=2`. Shrink: sum=3, `l=5`.
Return 2.

**Time Complexity:** $O(N)$ (Each element is added and removed at most once).
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int currentSum = 0;
        int minLen = Integer.MAX_VALUE;
        
        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];
            
            while (currentSum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }
        
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
```

## Python Solution
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0;
        int currentSum = 0;
        int minLen = INT_MAX;
        
        for (int right = 0; right < nums.size(); right++) {
            currentSum += nums[right];
            
            while (currentSum >= target) {
                minLen = min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }
        
        return minLen == INT_MAX ? 0 : minLen;
    }
};
```

## Common Mistakes
- **Replacing `while` with `if`:** During the shrink phase, a single right expansion might suddenly make the sum large enough that we can shrink the left side *multiple times* and still be $\ge$ target. An `if` statement will only shrink once, missing the true minimum length.
- **Applying this to arrays with negative numbers:** This sliding window logic mathematically breaks if the array contains negative numbers (because adding a number might decrease the sum). If negative numbers are present, you must use Prefix Sum + Deque or Binary Search.

## Similar Questions
- Minimum Window Substring
- Maximum Average Subarray I
