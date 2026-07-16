# Maximum Product Subarray

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: LinkedIn, Amazon, Google

## Topic
Arrays

## Pattern
Kadane's Variation (Prefix & Suffix Products)

## Problem Statement
Given an integer array `nums`, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

## Constraints
- $1 \le nums.length \le 2 \times 10^4$
- $-10 \le nums[i] \le 10$
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a single integer representing the maximum product.

## Sample Input
```
4
2 3 -2 4
```

## Sample Output
```
6
```

## Edge Cases
- All negative numbers (e.g., `[-2, -3, -4]`).
- Array containing zeroes, which resets the product.
- Single element array.

## Approach 1
Brute Force
**Explanation:** Use two nested loops to calculate the product of every possible subarray and keep track of the maximum.
**Time Complexity:** $O(N^2)$ (TLE)
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Prefix and Suffix Products)
**Explanation:** 
Unlike Kadane's for sums, Kadane's for products is tricky because a negative number multiplied by another negative number becomes positive.
Instead of tracking max/min locally, a mathematically elegant observation solves this:
1. If the array has no zeroes, the maximum product will either be the prefix product of the entire array, or the suffix product of the entire array. (This is because if there's an even number of negatives, the whole array is the max. If there's an odd number of negatives, the max is either everything before the last negative, or everything after the first negative).
2. If we encounter a zero, the prefix/suffix product is broken. We simply reset our running prefix/suffix to 1 and continue.

Algorithm:
1. Maintain `prefix = 1`, `suffix = 1`, and `ans = INT_MIN`.
2. Iterate from `0` to `N-1`.
3. If `prefix == 0`, reset `prefix = 1`. If `suffix == 0`, reset `suffix = 1`.
4. `prefix *= nums[i]`
5. `suffix *= nums[N - 1 - i]`
6. `ans = max(ans, max(prefix, suffix))`

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int ans = Integer.MIN_VALUE;
        int prefix = 1;
        int suffix = 1;
        
        for (int i = 0; i < n; i++) {
            if (prefix == 0) prefix = 1;
            if (suffix == 0) suffix = 1;
            
            prefix *= nums[i];
            suffix *= nums[n - 1 - i];
            
            ans = Math.max(ans, Math.max(prefix, suffix));
        }
        
        return ans;
    }
}
```

## Python Solution
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        prefix, suffix = 1, 1
        
        for i in range(n):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            
            ans = max(ans, prefix, suffix)
            
        return ans
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int ans = INT_MIN;
        int prefix = 1;
        int suffix = 1;
        
        for (int i = 0; i < n; i++) {
            if (prefix == 0) prefix = 1;
            if (suffix == 0) suffix = 1;
            
            prefix *= nums[i];
            suffix *= nums[n - 1 - i];
            
            ans = max(ans, max(prefix, suffix));
        }
        
        return ans;
    }
};
```

## Common Mistakes
- **Forgetting to check for zero BEFORE multiplying:** If you multiply first and then check for zero, you will reset it for the next iteration, but you'll incorrectly evaluate `0` against `ans` during the current iteration. Always check and reset before multiplying.

## Interview Tips
- There is another optimal solution that involves tracking `current_max` and `current_min` variables locally. The Prefix/Suffix observation approach is generally much easier to explain and trace during an interview without tripping over negative value swap logic.

## Similar Questions
- Maximum Subarray
- Maximum Product of Three Numbers
