# Problem 16: Maximum Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the maximum subarray sum.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach

The most famous and optimal solution for this problem is **Kadane's Algorithm**.
1. Initialize two variables: `sum = 0` and `max_val = nums[0]`.
2. Iterate through the array.
3. For each element, add it to `sum`: `sum += nums[i]`.
4. Update `max_val` if the current `sum` is greater than `max_val`.
5. If at any point the `sum` becomes negative (`sum < 0`), reset `sum` to `0`. A negative sum will only decrease the value of any future contiguous subarrays, so it's better to start a new subarray from the next element.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int max_val = nums[0]; // Initialize with first element to handle all-negative arrays
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            if (sum > max_val) {
                max_val = sum;
            }
            
            // If sum becomes negative, reset it
            if (sum < 0) {
                sum = 0;
            }
        }
        
        return max_val;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Maximum Subarray Sum: " << sol.maxSubArray(nums) << endl; // Expected: 6 (from [4, -1, 2, 1])
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We perform a single traversal.
- **Space Complexity:** `O(1)`. Only two variables are used.
