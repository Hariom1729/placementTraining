# Maximum Subarray (Kadane's Algorithm)

## Problem
Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Difficulty
Medium

## Companies
Infosys SP
Infosys DSE
Other companies: Amazon, Microsoft, Google

## Frequency
Very High

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

## Constraints
- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## Input
- First line: `N`
- Second line: `N` space-separated integers.

## Output
- A single integer representing the maximum subarray sum.

## Sample Test Cases

### Example 1
**Input:** 
```
9
-2 1 -3 4 -1 2 1 -5 4
```
**Output:** 
```
6
```
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

### Example 2
**Input:** 
```
1
1
```
**Output:** 
```
1
```

## Edge Cases
- All negative numbers: Should return the single maximum negative number.
- Single element array.

## Brute Force
**Explanation:** Iterate through all possible starting points `i` and ending points `j`. For each pair, calculate the sum and keep track of the maximum.
**Complexity:** $O(N^2)$ time, $O(1)$ space. Will TLE.

## Better Solution
There is no "better" intermediate solution between $O(N^2)$ and $O(N)$. We jump straight to the optimal.

## Optimal Solution (Kadane's Algorithm)
**Explanation:** 
As we iterate through the array, we maintain a `current_sum`. If `current_sum` becomes negative, it means that this particular prefix of the array will only drag down any future subarray sums. Therefore, if `current_sum < 0`, we reset it to `0`. We constantly update `max_sum` with `current_sum`.

**Dry Run:**
`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- `i=0` (-2): `cur=-2`. `max=-2`. `cur < 0` so `cur=0`.
- `i=1` (1): `cur=1`. `max=1`.
- `i=2` (-3): `cur=-2`. `max=1`. `cur < 0` so `cur=0`.
- `i=3` (4): `cur=4`. `max=4`.
- `i=4` (-1): `cur=3`. `max=4`.
- `i=5` (2): `cur=5`. `max=5`.
- `i=6` (1): `cur=6`. `max=6`.
- `i=7` (-5): `cur=1`. `max=6`.
- `i=8` (4): `cur=5`. `max=6`.
Return 6.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int max_sum = nums[0];
    int current_sum = 0;
    
    for (int i = 0; i < nums.size(); i++) {
        current_sum += nums[i];
        
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
        
        if (current_sum < 0) {
            current_sum = 0;
        }
    }
    
    return max_sum;
}
```

## Common Mistakes
- **Initializing max_sum to 0:** If the array contains ONLY negative numbers (e.g., `[-3, -5]`), initializing `max_sum = 0` will incorrectly return `0` instead of `-3`. Always initialize to `nums[0]` or `INT_MIN`.

## Interview Tips
- The interviewer might ask you to also return the *starting and ending indices* of the maximum subarray. You can do this by keeping track of the start index whenever `current_sum` resets to 0.

## Similar Problems
- Maximum Product Subarray
- Maximum Circular Subarray Sum

## Variations
- Return the indices of the subarray.
