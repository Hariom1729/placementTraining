# Problem 1: Climbing Stairs

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Constraints
- `1 <= n <= 45`

---

## Approach: 1D DP / Fibonacci Sequence

To reach step `i`, you could have come from either:
- step `i - 1` (taking a 1-step jump)
- step `i - 2` (taking a 2-step jump)

Therefore, the total number of ways to reach step `i` is the sum of ways to reach step `i - 1` and step `i - 2`.
`dp[i] = dp[i-1] + dp[i-2]`
This is exactly the Fibonacci sequence.

Instead of an array, we can just keep track of the last two values to achieve `O(1)` space complexity.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        
        int prev2 = 1; // Ways to reach step 1
        int prev1 = 2; // Ways to reach step 2
        
        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};

int main() {
    Solution sol;
    cout << "Ways to climb 5 stairs: " << sol.climbStairs(5) << endl; 
    // Expected: 8
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`. We iterate from `3` to `n`.
- **Space Complexity:** `O(1)`. We only use a few integer variables.
