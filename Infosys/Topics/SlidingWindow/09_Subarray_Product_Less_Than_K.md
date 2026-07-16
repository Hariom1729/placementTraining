# Subarray Product Less Than K

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, LinkedIn

## Topic
Sliding Window / Arrays

## Pattern
Variable Size Window (Combinatorics)

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

**Example 2:**
```
Input: nums = [1,2,3], k = 0
Output: 0
```

## Edge Cases
- `k <= 1` (Since all `nums[i] >= 1`, it's impossible to have a product strictly less than 1. Return `0`).

## Intuition
This problem asks for the **number** of valid subarrays.
We can use a **Variable Size Sliding Window**. We maintain a window `[left, right]` where the product of all elements is strictly less than `k`.

As we expand the window by moving `right` and multiplying `product *= nums[right]`:
- If `product >= k`, our window is invalid! We must shrink it by moving `left` and dividing `product /= nums[left]` until `product < k`.

**The crucial mathematical trick:**
Once we have a valid window `[left, right]` where the product is less than `k`, how many valid subarrays does this window introduce that END at `right`?
The answer is exactly `right - left + 1`!
Why? If the valid window is `[10, 5, 2]` (indices 0 to 2), the subarrays ending at index 2 are:
- `[2]`
- `[5, 2]`
- `[10, 5, 2]`
There are exactly 3 new subarrays! And `right - left + 1` = `2 - 0 + 1` = `3`.
By adding `right - left + 1` to our `totalCount` at every step, we brilliantly count every single valid subarray exactly once!

## Optimal Approach (Sliding Window)
**Detailed explanation:**
1. If `k <= 1`, return 0.
2. Initialize `product = 1`, `left = 0`, `count = 0`.
3. Loop `right` from `0` to `nums.size() - 1`:
   - `product *= nums[right]`.
   - While `product >= k`:
     - `product /= nums[left]`.
     - `left++`.
   - `count += right - left + 1`.
4. Return `count`.

**Time Complexity:** $O(N)$. `right` moves $N$ times, `left` moves at most $N$ times.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        // Since nums[i] >= 1, product can never be less than 1.
        if (k <= 1) return 0;
        
        int product = 1;
        int left = 0;
        int count = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            product *= nums[right];
            
            // Shrink window if product is too large
            while (product >= k) {
                product /= nums[left];
                left++;
            }
            
            // Add the number of valid subarrays ENDING at 'right'
            count += right - left + 1;
        }
        
        return count;
    }
};
```

## Dry Run
`nums = [10, 5, 2, 6], k = 100`
- `right=0 (10)`: `prod = 10`. `10 < 100`. Valid.
  - `count += 0 - 0 + 1` (1). Subarray: `[10]`.
- `right=1 (5)`: `prod = 50`. `50 < 100`. Valid.
  - `count += 1 - 0 + 1` (2). Subarrays: `[5]`, `[10, 5]`. Total count = 3.
- `right=2 (2)`: `prod = 100`. `100 >= 100`. Invalid!
  - `prod /= nums[0] (10)` -> 10. `left++ -> 1`.
  - Window `[1..2]`. Valid.
  - `count += 2 - 1 + 1` (2). Subarrays: `[2]`, `[5, 2]`. Total count = 5.
- `right=3 (6)`: `prod = 60`. `60 < 100`. Valid.
  - `count += 3 - 1 + 1` (3). Subarrays: `[6]`, `[2, 6]`, `[5, 2, 6]`. Total count = 8.
- Return 8.

## Common Mistakes
- **Failing the `k <= 1` edge case:** If `k=0` and `nums=[1,2]`, `product=1`. `1 >= 0`, so we enter the while loop. We do `product /= nums[left]` -> `1 / 1 = 1`. `left++`. The loop repeats, `product` is STILL 1, `left` goes out of bounds, and the program crashes. You MUST check `if (k <= 1) return 0;`.

## Similar Problems
- Subarray Sum Equals K
- Maximum Product Subarray
