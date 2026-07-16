# Continuous Subarray Sum

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys DSE
Similar Companies: Facebook, Amazon, Apple

## Topic
Hashing / Prefix Sum / Math

## Pattern
Prefix Sum Modulo Hashing

## Problem Statement
Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.
A **good subarray** is a subarray where:
- its length is **at least two**, and
- the sum of the elements of the subarray is a multiple of `k`.

Note that:
- A subarray is a contiguous part of the array.
- An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is always a multiple of `k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
```

**Example 2:**
```
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
```

**Example 3:**
```
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

## Edge Cases
- Prefix sum becomes extremely large (must use `long long` for running sum or apply modulo at every step to prevent overflow).
- Zeros in the array (`[0, 0]`, `k=2` is valid because `0` is a multiple of `2`).

## Intuition
This problem is a direct evolution of **Subarray Sum Equals K**, but instead of finding an *exact sum*, we need to find a sum that is a *multiple* of `k`.
Recall the prefix sum formula: `Sum(i, j) = PrefixSum[j] - PrefixSum[i-1]`.
We want `Sum(i, j) % k == 0`.
Therefore: `(PrefixSum[j] - PrefixSum[i-1]) % k == 0`.
By modular arithmetic properties:
`PrefixSum[j] % k == PrefixSum[i-1] % k` !!!

This is the magic realization: **If two prefix sums have the EXACT SAME REMAINDER when divided by `k`, the subarray between them must sum to a multiple of `k`!**

Example: 
- `k = 6`
- Prefix sum at index `i-1` is `14`. `14 % 6 = 2`.
- Prefix sum at index `j` is `38`. `38 % 6 = 2`.
- The subarray sum is `38 - 14 = 24`. And `24` is perfectly divisible by `6`!

Algorithm:
1. Maintain a running sum, and take modulo `k` at each step to get the remainder.
2. Use an `unordered_map<int, int>` to store `{remainder : index_where_it_first_occurred}`. (We need the index because the problem requires the subarray length to be **at least 2**).
3. If we see a remainder that is already in the map, we check the distance between the current index and the stored index. If it's $\ge 2$, return `true`!

## Brute Force Approach
**Explanation:** Check every subarray of length $\ge 2$ and calculate the sum.
**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$

## Optimal Approach (Prefix Sum + Modulo Hashing)
**Detailed explanation:**
1. Create `unordered_map<int, int> remainderMap`.
2. **Crucial Base Case:** `remainderMap[0] = -1`. This ensures that if the prefix sum from the very beginning of the array perfectly divides by `k`, the distance calculation `i - (-1)` works properly!
3. Initialize `sum = 0`.
4. Iterate `i` from `0` to `nums.size() - 1`:
   - `sum += nums[i]`.
   - `int remainder = sum % k`.
   - If `remainderMap.count(remainder)`:
     - Check distance: `if (i - remainderMap[remainder] >= 2)`, return `true`.
   - Else:
     - Store the FIRST occurrence of this remainder: `remainderMap[remainder] = i`. (We don't overwrite it if it exists because we want to maximize distance to ensure length $\ge 2$).
5. Return `false`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(\min(N, k))$ for the Hash Map.

## C++ Solution

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        // Map stores {remainder : first_index_seen}
        unordered_map<int, int> remainderMap;
        
        // Base case: Remainder 0 at index -1
        // Handles cases where a valid subarray starts from index 0
        remainderMap[0] = -1;
        
        long long sum = 0; // Prevent overflow on massive arrays
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            // Apply modulo math
            int remainder = sum % k;
            
            // If we've seen this remainder before
            if (remainderMap.count(remainder)) {
                // Check if the subarray length is at least 2
                if (i - remainderMap[remainder] >= 2) {
                    return true;
                }
            } else {
                // IMPORTANT: Only store the first occurrence of the remainder
                // This maximizes the distance between indices
                remainderMap[remainder] = i;
            }
        }
        
        return false;
    }
};
```

## Dry Run
`nums = [23, 2, 4, 6, 7], k = 6`
- `remainderMap = {0: -1}`
- `i=0 (23)`: `sum=23`, `rem=5`. Map: `{0:-1, 5:0}`.
- `i=1 (2)`: `sum=25`, `rem=1`. Map: `{0:-1, 5:0, 1:1}`.
- `i=2 (4)`: `sum=29`, `rem=5`. `5` is in map! Index is `0`.
  - Distance = `2 - 0 = 2`. Length is $\ge 2$. Valid!
- Return `true`.

## Common Mistakes
- **Overwriting the remainder index:** If the map already contains `rem`, DO NOT do `remainderMap[rem] = i`. You want the earliest possible index to ensure the length `>= 2` condition is satisfied.
- **Forgetting the base case `remainderMap[0] = -1`:** If `nums = [23, 1]` and `k = 12`, sum is 24, `rem = 0`. Without `-1`, the distance check might fail or you'll completely miss that the entire array from index 0 is valid.

## Similar Problems
- Subarray Sum Equals K
- Subarray Sums Divisible by K
