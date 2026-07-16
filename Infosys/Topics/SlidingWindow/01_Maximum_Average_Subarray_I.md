# Maximum Average Subarray I

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft

## Topic
Sliding Window / Arrays

## Pattern
Fixed Size Window

## Problem Statement
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.

## Constraints
- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return a double (the maximum average).

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

**Example 2:**
```
Input: nums = [5], k = 1
Output: 5.00000
```

## Edge Cases
- All negative numbers.
- `k` equals the size of the array (return the average of the whole array).

## Intuition
The naive approach is to calculate the sum of every possible subarray of size `k`. Since there are roughly $N$ subarrays and calculating the sum takes $O(K)$, the total time is $O(N \times K)$, which will Time Limit Exceed.

Notice that the subarray of size `k` starting at index `1` shares almost all its elements with the subarray starting at index `0`. 
Indices `[0, 1, 2, 3]`. Next is `[1, 2, 3, 4]`. 
The ONLY difference is that we lost element `0` and gained element `4`.

This perfectly describes a **Sliding Window**!
Instead of recalculating the sum from scratch, we calculate the sum of the very first window of size `k`. 
Then, as we slide the window to the right by one position, we just **subtract the element that fell out of the left side of the window** and **add the new element entering the right side of the window**.

To maximize the average of a fixed number of elements `k`, we just need to maximize the SUM! We can track the `maxSum` and only divide by `k` at the very end to avoid precision issues during comparison.

## Optimal Approach (Fixed Sliding Window)
**Detailed explanation:**
1. Initialize `currentSum = 0`.
2. Calculate the sum of the first `k` elements and set `maxSum = currentSum`.
3. Loop from index `i = k` up to `n - 1`:
   - `currentSum += nums[i]` (Add the new element on the right).
   - `currentSum -= nums[i - k]` (Subtract the old element from the left).
   - Update `maxSum = max(maxSum, currentSum)`.
4. Return `(double)maxSum / k`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int currentSum = 0;
        
        // 1. Calculate the sum of the first window of size k
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }
        
        int maxSum = currentSum;
        
        // 2. Slide the window across the rest of the array
        for (int i = k; i < nums.size(); i++) {
            // Add the new element entering the window
            currentSum += nums[i];
            
            // Remove the old element leaving the window
            currentSum -= nums[i - k];
            
            // Update the maximum sum found so far
            maxSum = max(maxSum, currentSum);
        }
        
        // Return the average
        return (double)maxSum / k;
    }
};
```

## Dry Run
`nums = [1, 12, -5, -6, 50, 3], k = 4`
- Initial Window (`i = 0` to `3`): `1 + 12 - 5 - 6 = 2`.
  - `currentSum = 2`, `maxSum = 2`.
- Slide to `i = 4` (value `50`):
  - Leaving element: `nums[4 - 4] = nums[0] = 1`.
  - `currentSum = 2 + 50 - 1 = 51`.
  - `maxSum = max(2, 51) = 51`.
- Slide to `i = 5` (value `3`):
  - Leaving element: `nums[5 - 4] = nums[1] = 12`.
  - `currentSum = 51 + 3 - 12 = 42`.
  - `maxSum = max(51, 42) = 51`.
- End of array.
- Return `51 / 4.0 = 12.75`.

## Common Mistakes
- **Calculating average inside the loop:** `maxAvg = max(maxAvg, currentSum / (double)k)` inside the loop works, but floating-point division is slow. It's much better to track the `maxSum` using integers and only divide by `k` at the very end.
- **Off-by-one errors:** The element leaving the window is always at index `i - k`.

## Similar Problems
- Subarray Sum Equals K
- Maximum Points You Can Obtain from Cards
