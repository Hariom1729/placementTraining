# Median of Two Sorted Arrays

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Google, Facebook

## Topic
Searching / Arrays

## Pattern
Binary Search on smaller array (Partitioning)

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be $O(\log(m+n))$.

## Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Input
- `nums1` vector of integers.
- `nums2` vector of integers.

## Output
- Return a double (the median).

## Sample Test Cases

**Example 1:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Edge Cases
- One array is empty.
- Arrays do not overlap in value at all (e.g., `[1, 2]` and `[3, 4]`).

## Intuition
The naive approach is to merge the two arrays into one large array of size `m+n` and then return the middle element. But that takes $O(m+n)$ time, which fails the $O(\log(m+n))$ requirement!

To get logarithmic time, we must use **Binary Search**. But binary search on what?
We want to find a **Partition** point that splits BOTH arrays such that:
1. The left half of the combined arrays has the exact same number of elements as the right half.
2. Every element on the left half is $\le$ every element on the right half.

If we can find this partition perfectly, the median is just the maximum of the left half (and possibly the minimum of the right half, if the total elements are even).

Since we know the total number of elements `total = m + n`, the left half must always contain `(total + 1) / 2` elements.
If we place a partition in `nums1` at index `i`, then we MUST place the partition in `nums2` at index `j = (total + 1) / 2 - i` so that the left halves sum up to the correct amount!
Therefore, we only need to Binary Search on the smaller array (`nums1`) to find the perfect `i`!

The partition is perfectly valid when:
- `Left1 <= Right2` (The largest element on the left of nums1 is smaller than the smallest on the right of nums2)
- `Left2 <= Right1` (The largest element on the left of nums2 is smaller than the smallest on the right of nums1)

If `Left1 > Right2`, our partition in `nums1` is too far to the right. Move left!
If `Left2 > Right1`, our partition in `nums1` is too far to the left. Move right!

## Brute Force Approach
**Explanation:** Merge the two arrays using Two Pointers, then find the middle index.
**Time Complexity:** $O(N + M)$
**Space Complexity:** $O(N + M)$ (or $O(1)$ if we just keep a counter and don't physically build the array).

## Optimal Approach (Binary Search on Partitions)
**Detailed explanation:**
1. Ensure `nums1` is the smaller array (if not, swap them). This guarantees our binary search takes $O(\log(\min(M, N)))$.
2. Initialize `left = 0`, `right = nums1.size()`.
3. Loop while `left <= right`:
   - `i = left + (right - left) / 2` (Partition index for nums1).
   - `j = (total + 1) / 2 - i` (Partition index for nums2).
   - Define the boundary elements:
     - `left1 = (i == 0) ? INT_MIN : nums1[i - 1]`
     - `right1 = (i == nums1.size()) ? INT_MAX : nums1[i]`
     - `left2 = (j == 0) ? INT_MIN : nums2[j - 1]`
     - `right2 = (j == nums2.size()) ? INT_MAX : nums2[j]`
   - If `left1 <= right2` AND `left2 <= right1`: We found the perfect partition!
     - If `total % 2 != 0`: Return `max(left1, left2)`. (Odd total)
     - Else: Return `(max(left1, left2) + min(right1, right2)) / 2.0`. (Even total)
   - Else if `left1 > right2`: We went too far right in `nums1`. `right = i - 1`.
   - Else: We went too far left in `nums1`. `left = i + 1`.

**Time Complexity:** $O(\log(\min(M, N)))$. Extremely fast.
**Space Complexity:** $O(1)$

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // We must perform binary search on the smaller array to prevent out of bounds
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        
        int left = 0;
        int right = m; // Notice right is 'm', not 'm - 1', because a partition can be at the very end
        
        while (left <= right) {
            int i = left + (right - left) / 2; // Partition for nums1
            int j = (total + 1) / 2 - i;       // Corresponding partition for nums2
            
            // Handle edge cases where partition is at the extreme ends
            int left1 = (i == 0) ? INT_MIN : nums1[i - 1];
            int right1 = (i == m) ? INT_MAX : nums1[i];
            
            int left2 = (j == 0) ? INT_MIN : nums2[j - 1];
            int right2 = (j == n) ? INT_MAX : nums2[j];
            
            // Check if the partition is perfectly valid
            if (left1 <= right2 && left2 <= right1) {
                // If total elements are odd, the median is just the max of the left halves
                if (total % 2 != 0) {
                    return max(left1, left2);
                } 
                // If even, it's the average of the max of the left halves and min of the right halves
                else {
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
                }
            }
            // Partition in nums1 is too far right
            else if (left1 > right2) {
                right = i - 1;
            } 
            // Partition in nums1 is too far left
            else {
                left = i + 1;
            }
        }
        
        return 0.0;
    }
};
```

## Dry Run
`nums1 = [1, 3], nums2 = [2]`
- Smaller is `nums1`. `m = 2`, `n = 1`, `total = 3`.
- `left = 0`, `right = 2`.
- `i = 1`. `j = (3 + 1)/2 - 1 = 1`.
- `left1 = nums1[0] = 1`. `right1 = nums1[1] = 3`.
- `left2 = nums2[0] = 2`. `right2 = nums2[1]` (out of bounds) -> `INT_MAX`.
- Is `1 <= INT_MAX`? Yes.
- Is `2 <= 3`? Yes. Perfect partition!
- Total is 3 (odd). Return `max(left1, left2)` = `max(1, 2) = 2.0`.

## Common Mistakes
- **Searching on the larger array:** If you try to binary search on the larger array, the formula `j = (total + 1) / 2 - i` can yield a **negative index** for `j`, completely crashing your program. You MUST ensure `nums1` is the smaller array so `j` is mathematically guaranteed to be $\ge 0$.

## Similar Problems
- Find K-th Smallest Pair Distance
