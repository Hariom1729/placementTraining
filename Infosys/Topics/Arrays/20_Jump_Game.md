# Jump Game

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Amazon, Microsoft, ByteDance

## Topic
Arrays

## Pattern
Greedy

## Problem Statement
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
Return `true` if you can reach the last index, or `false` otherwise.

## Constraints
- $1 \le nums.length \le 10^4$
- $0 \le nums[i] \le 10^5$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a boolean (`true` or `false`).

## Sample Input
```
5
2 3 1 1 4
```

## Sample Output
```
true
```

## Edge Cases
- Array of size 1. (Already at the last index, return true).
- Elements are 0. If `nums[0] = 0` and size > 1, immediately return false.

## Approach 1
Brute Force / DFS
**Explanation:** From every index, try all possible jumps from `1` to `nums[i]`. Recursively check if any path reaches the end.
**Time Complexity:** $O(2^N)$ (Will TLE).
**Space Complexity:** $O(N)$ for recursion stack.

## Approach 2
Dynamic Programming (Memoization)
**Explanation:** Cache the results of the DFS. An array `dp[i]` stores whether it's possible to reach the end from index `i`.
**Complexity:** $O(N^2)$ time, $O(N)$ space. (Can still TLE on tight $O(N)$ constraints).

## Approach 3
Optimal Approach (Greedy)
**Explanation:** 
Instead of looking forward to see where we can go, we maintain the `maximum_reachable_index`.
1. Initialize `maxReach = 0`.
2. Iterate through the array up to `n-1`.
3. If the current index `i` is greater than `maxReach`, it means we cannot even reach the current index, let alone the end. Return `false`.
4. Update `maxReach = max(maxReach, i + nums[i])`.
5. If `maxReach >= n - 1` at any point, return `true`.

**Dry Run:**
`nums = [3, 2, 1, 0, 4]`
- `i=0` (3): `maxReach = max(0, 0 + 3) = 3`.
- `i=1` (2): `maxReach = max(3, 1 + 2) = 3`.
- `i=2` (1): `maxReach = max(3, 2 + 1) = 3`.
- `i=3` (0): `maxReach = max(3, 3 + 0) = 3`.
- `i=4` (4): Wait, `i=4` is > `maxReach (3)`. The loop triggers `i > maxReach`. Returns `false`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;
            }
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }
        
        return true;
    }
}
```

## Python Solution
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
                
        return True
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            if (i > maxReach) {
                return false;
            }
            maxReach = max(maxReach, i + nums[i]);
            if (maxReach >= n - 1) {
                return true;
            }
        }
        
        return true;
    }
};
```

## Common Mistakes
- **Confusing with Jump Game II:** This problem just asks *if* it's possible. Jump Game II asks for the *minimum number of jumps*, which requires maintaining a current window boundary and counting steps. The logic here is much simpler.

## Similar Questions
- Jump Game II
- Jump Game III
- Minimum Number of Taps to Open to Water a Garden
