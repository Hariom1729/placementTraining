# Problem 10: Find the Missing Number in an Array

## Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the missing number.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`

---

## Approach

There are multiple ways to solve this, but the mathematical approach using the sum of the first N natural numbers is the most optimal.

**Approach 1: Sum Formula (Optimal)**
1. The sum of the first `N` numbers is given by the formula: `Sum = (N * (N + 1)) / 2`.
2. Calculate this theoretical sum.
3. Calculate the actual sum of all elements present in the array.
4. The missing number will simply be: `Theoretical Sum - Actual Sum`.

*(Alternatively, you can use the XOR approach which avoids potential integer overflow).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        
        // Calculate expected sum using formula
        int expectedSum = (n * (n + 1)) / 2;
        
        // Calculate actual sum
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        
        // The difference is the missing number
        return expectedSum - actualSum;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {3, 0, 1};
    cout << "Missing number: " << sol.missingNumber(nums) << endl; // Expected: 2
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We iterate through the array once to calculate the sum.
- **Space Complexity:** `O(1)`. We only use a few integer variables.
