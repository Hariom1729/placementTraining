# Subarray Sum Equals K

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Microsoft

## Topic
Hashing / Arrays / Prefix Sum

## Pattern
Prefix Sum with Hash Map

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return an integer representing the count of valid subarrays.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1, 1] from index 0 to 1, and [1, 1] from index 1 to 2.
```

**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1, 2] from index 0 to 1, and [3] at index 2.
```

## Edge Cases
- Subarray contains negative numbers, meaning a sum can decrease and then increase back to `k`. (This breaks standard Sliding Window, requiring Prefix Sums).
- Array elements are 0.

## Intuition
Normally, if all numbers are positive, we can use a Sliding Window to find subarrays. BUT, because `nums` can contain **negative numbers**, a Sliding Window fails completely! We must use **Prefix Sums**.
The sum of a subarray from index `i` to `j` is:
`Sum(i, j) = PrefixSum[j] - PrefixSum[i-1]`

We want to find subarrays where `Sum(i, j) == k`.
Therefore, we are looking for: `PrefixSum[j] - PrefixSum[i-1] == k`.
Rearranging this mathematically:
`PrefixSum[i-1] = PrefixSum[j] - k`.

This is incredible! It means as we iterate through the array and calculate our `currentSum` (which is `PrefixSum[j]`), we just need to look back and see if we have EVER seen a prefix sum equal to `currentSum - k`!
How do we instantly check what prefix sums we have seen in the past? A **Hash Map**!
`unordered_map<int, int>` will store `{PrefixSum : How many times we've seen it}`.

## Brute Force Approach
**Explanation:** For every possible starting index `i`, loop to every possible ending index `j`, calculate the sum, and check if it equals `k`.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Optimal Approach (Prefix Sum + Hash Map)
**Detailed explanation:**
1. Create an `unordered_map<int, int> prefixCounts`.
2. **Crucial Base Case:** `prefixCounts[0] = 1`. This handles the case where the `currentSum` exactly equals `k` right from the very beginning of the array! (i.e. `currentSum - k = 0`).
3. Initialize `currentSum = 0` and `count = 0`.
4. Iterate through `num` in `nums`:
   - `currentSum += num`.
   - Check if `currentSum - k` exists in our map.
   - If it does, add its frequency to `count`: `count += prefixCounts[currentSum - k]`.
   - Add the new `currentSum` to our map: `prefixCounts[currentSum]++`.
5. Return `count`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the hash map.

## C++ Solution

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // Map to store the frequency of each prefix sum seen so far
        unordered_map<int, int> prefixCounts;
        
        // Base case: A prefix sum of 0 has occurred exactly 1 time (before we start)
        prefixCounts[0] = 1;
        
        int currentSum = 0;
        int count = 0;
        
        for (int num : nums) {
            currentSum += num;
            
            // If (currentSum - k) exists in the map, it means there is a subarray
            // ending at the current index which sums exactly to k!
            int target = currentSum - k;
            if (prefixCounts.count(target)) {
                count += prefixCounts[target];
            }
            
            // Add the current prefix sum to the map for future indices to use
            prefixCounts[currentSum]++;
        }
        
        return count;
    }
};
```

## Dry Run
`nums = [1, 2, 3], k = 3`
- `prefixCounts = {0: 1}`. `currSum = 0`, `count = 0`.
- `i=0 (1)`: `currSum = 1`. `target = 1 - 3 = -2`. Not in map. `prefixCounts[1] = 1`. Map: `{0:1, 1:1}`.
- `i=1 (2)`: `currSum = 3`. `target = 3 - 3 = 0`. In map! (Value is 1). `count += 1`. `prefixCounts[3] = 1`. Map: `{0:1, 1:1, 3:1}`.
- `i=2 (3)`: `currSum = 6`. `target = 6 - 3 = 3`. In map! (Value is 1). `count += 1` -> 2. `prefixCounts[6] = 1`.
- Return `count = 2`.

## Common Mistakes
- **Forgetting `prefixCounts[0] = 1`:** If you forget this base case, you will fail to count any valid subarray that starts at index 0. (e.g. if the first element is `3` and `k=3`, `currSum=3`, target=0. If `0` is not in the map, you miss it!).
- **Using a Sliding Window:** You CANNOT use left/right pointers because negative numbers mean the sum doesn't monotonically increase. Expanding the window might DECREASE the sum.

## Similar Problems
- Subarray Sums Divisible by K
- Contiguous Array
