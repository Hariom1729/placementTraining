# Number of Good Pairs

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon

## Topic
Hashing / Math

## Pattern
Frequency Map Combinatorics

## Problem Statement
Given an array of integers `nums`, return the number of **good pairs**.
A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Input
- `nums` vector of integers.

## Output
- Return an integer (number of good pairs).

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs: (0,3), (0,4), (3,4), (2,5). (0-indexed).
```

**Example 2:**
```
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is good. (4 * 3) / 2 = 6.
```

**Example 3:**
```
Input: nums = [1,2,3]
Output: 0
```

## Edge Cases
- All elements are the same.
- All elements are unique.

## Intuition
If we know that a number (e.g., `1`) appears $n$ times in the array, how many pairs can we form using just that number?
Mathematically, this is "$n$ choose 2", which is computed as:
$n \times (n - 1) / 2$

So, the optimal strategy is to just use a **Hash Map** (or frequency array) to count how many times each number appears.
Then, we iterate through the values in our map. If a number appeared `c` times, we add `c * (c - 1) / 2` to our total answer!

*Bonus 1-Pass Trick:* As we iterate through the array, if we see the number `1` and our map says we've already seen it `2` times before, we can instantly form `2` NEW pairs using this newly discovered `1`! So we can just do `total += count[num]` and *then* `count[num]++`.

## Brute Force Approach
**Explanation:** Nested loops checking `nums[i] == nums[j]`.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Optimal Approach (Frequency Array / 1-Pass)
**Detailed explanation:**
1. Since constraints say `1 <= nums[i] <= 100`, we can use an array `int count[101] = {0}` as our extremely fast Hash Map.
2. Initialize `goodPairs = 0`.
3. Iterate `num` in `nums`:
   - `goodPairs += count[num]` (Add a new pair for every previous occurrence we've seen).
   - `count[num]++` (Record this occurrence for future numbers).
4. Return `goodPairs`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ (Array of size 101).

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count[101] = {0};
        int goodPairs = 0;
        
        for (int num : nums) {
            // If we've seen 'num' 3 times before, this new 'num' can form
            // 3 entirely new pairs!
            goodPairs += count[num];
            
            // Increment the count of 'num'
            count[num]++;
        }
        
        return goodPairs;
    }
};
```

## Dry Run
`nums = [1, 2, 3, 1, 1, 3]`
- `num=1`: `goodPairs += count[1]` (0). `count[1]=1`.
- `num=2`: `goodPairs += count[2]` (0). `count[2]=1`.
- `num=3`: `goodPairs += count[3]` (0). `count[3]=1`.
- `num=1`: `goodPairs += count[1]` (1). `count[1]=2`. (`goodPairs = 1`).
- `num=1`: `goodPairs += count[1]` (2). `count[1]=3`. (`goodPairs = 3`).
- `num=3`: `goodPairs += count[3]` (1). `count[3]=2`. (`goodPairs = 4`).
- Return 4.

## Common Mistakes
- **Using $O(N^2)$ for small constraints:** Since $N \le 100$, the $O(N^2)$ brute force actually passes on LeetCode. But in an interview setting, the interviewer will ask you to optimize it for $N = 10^5$. Using the frequency map is required.

## Similar Problems
- Subarray Sum Equals K
- Two Sum
