# Maximum Gap

## Difficulty
Hard (But frequently asked in SP to test Bucket Sort)

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Apple, Google

## Topic
Sorting / Arrays

## Pattern
Bucket Sort / Pigeonhole Principle

## Problem Statement
Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in **linear time** and uses **linear extra space**.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Input
- `nums` vector of integers.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
```

**Example 2:**
```
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

## Edge Cases
- All elements are identical.
- Array length is `< 2`.
- Massive numbers causing integer overflow (numbers are up to $10^9$, differences fit in 32-bit int).

## Intuition
If we could sort the array in $O(N \log N)$, finding the max difference would be trivial (just loop through adjacent elements). But the problem mandates **$O(N)$ time**.
How can we sort an array with numbers up to $10^9$ in $O(N)$ time? Radix Sort or Bucket Sort!

Let's use **Bucket Sort** relying on the **Pigeonhole Principle**.
1. Find the minimum (`minVal`) and maximum (`maxVal`) values in the array.
2. The maximum possible gap cannot be smaller than `(maxVal - minVal) / (N - 1)`. Why? If you have numbers from 1 to 10 spread across 4 elements, the most evenly you can spread them is 1, 4, 7, 10. The gap is $(10-1)/(4-1) = 3$. If they are less evenly spread, at least one gap MUST be larger than 3!
3. Therefore, if we set our "Bucket Size" to `ceil((maxVal - minVal) / (N - 1))`, we are GUARANTEED that the maximum gap will **never** occur between two numbers within the SAME bucket! The max gap must occur between the **Max of Bucket A** and the **Min of Bucket B**!
4. So we create $N$ buckets. For each bucket, we only need to track the `min` and `max` value inside it.
5. We place every number into a bucket using the formula: `idx = (num - minVal) / bucketSize`.
6. Finally, we iterate through the buckets. The gap is simply `currentBucket.min - previousBucket.max`. We find the largest such gap.

## Brute Force Approach
**Explanation:** Sort the array $O(N \log N)$ and compare adjacent elements.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$

## Optimal Approach (Bucket Sort / Pigeonhole Principle)
**Detailed explanation:**
1. If `N < 2`, return 0.
2. Find `minVal` and `maxVal`. If `minVal == maxVal`, return 0.
3. Calculate `bucketSize = ceil((double)(maxVal - minVal) / (N - 1))`. Or using integer math: `(maxVal - minVal) / (N - 1)`. If it's 0, make it 1.
4. Calculate number of buckets: `(maxVal - minVal) / bucketSize + 1`.
5. Create two arrays: `bucketMin` initialized to `INT_MAX`, and `bucketMax` initialized to `INT_MIN`.
6. Iterate through `num` in `nums`:
   - `idx = (num - minVal) / bucketSize`.
   - `bucketMin[idx] = min(bucketMin[idx], num)`.
   - `bucketMax[idx] = max(bucketMax[idx], num)`.
7. Iterate through buckets to find max gap:
   - `maxGap = 0`, `prevMax = minVal`.
   - For each bucket:
     - If bucket is empty (i.e. `bucketMin[i] == INT_MAX`), skip it.
     - `maxGap = max(maxGap, bucketMin[i] - prevMax)`.
     - `prevMax = bucketMax[i]`.
8. Return `maxGap`.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        
        int minVal = *min_element(nums.begin(), nums.end());
        int maxVal = *max_element(nums.begin(), nums.end());
        
        if (minVal == maxVal) return 0; // All elements are identical
        
        // Calculate bucket size and count
        // We use ceil to ensure we have enough buckets. Integer math: (a + b - 1) / b
        int bucketSize = max(1, (maxVal - minVal) / (n - 1)); 
        int bucketCount = (maxVal - minVal) / bucketSize + 1;
        
        vector<int> bucketMin(bucketCount, INT_MAX);
        vector<int> bucketMax(bucketCount, INT_MIN);
        
        // Place numbers into buckets
        for (int num : nums) {
            int idx = (num - minVal) / bucketSize;
            bucketMin[idx] = min(bucketMin[idx], num);
            bucketMax[idx] = max(bucketMax[idx], num);
        }
        
        // Calculate max gap between buckets
        int maxGap = 0;
        int previousMax = minVal;
        
        for (int i = 0; i < bucketCount; i++) {
            // Skip empty buckets
            if (bucketMin[i] == INT_MAX) continue;
            
            // The gap is the current bucket's min minus the previous bucket's max
            maxGap = max(maxGap, bucketMin[i] - previousMax);
            previousMax = bucketMax[i];
        }
        
        return maxGap;
    }
};
```

## Dry Run
`nums = [3, 6, 9, 1]`
- `n = 4`. `minVal = 1`, `maxVal = 9`.
- `bucketSize = (9 - 1) / 3 = 2`.
- `bucketCount = (9 - 1) / 2 + 1 = 5`.
- Buckets: `bMin[5]`, `bMax[5]`.
- Place numbers:
  - `3`: `idx = (3 - 1) / 2 = 1`. `bMin[1]=3`, `bMax[1]=3`.
  - `6`: `idx = (6 - 1) / 2 = 2`. `bMin[2]=6`, `bMax[2]=6`.
  - `9`: `idx = (9 - 1) / 2 = 4`. `bMin[4]=9`, `bMax[4]=9`.
  - `1`: `idx = (1 - 1) / 2 = 0`. `bMin[0]=1`, `bMax[0]=1`.
- Calculate gap:
  - `prev = 1`.
  - `i=0`: `bMin[0]=1`. `gap = max(0, 1 - 1) = 0`. `prev = 1`.
  - `i=1`: `bMin[1]=3`. `gap = max(0, 3 - 1) = 2`. `prev = 3`.
  - `i=2`: `bMin[2]=6`. `gap = max(2, 6 - 3) = 3`. `prev = 6`.
  - `i=3`: empty, skip.
  - `i=4`: `bMin[4]=9`. `gap = max(3, 9 - 6) = 3`. `prev = 9`.
- Return `3`.

## Common Mistakes
- **Failing `bucketSize` integer math:** If `(maxVal - minVal) / (N - 1)` results in 0 due to integer truncation, division by zero will crash the program when doing `(num - minVal) / bucketSize`. Always do `max(1, ...)` or properly use `ceil`.

## Similar Problems
- Contains Duplicate III
