# Longest Consecutive Sequence

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Google, Amazon, Microsoft, Facebook

## Topic
Hashing / Arrays

## Pattern
Hash Set Lookups

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **$O(n)$** time.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Input
- `nums` vector of integers.

## Output
- Return an integer length.

## Sample Test Cases

**Example 1:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].
```

## Edge Cases
- Empty array (return 0).
- Array with all duplicates (return 1).

## Intuition
The obvious solution is to sort the array and count the longest streak. But sorting takes $O(N \log N)$ time, and the problem STRICTLY requires $O(N)$ time!
To achieve $O(N)$, we must use a **Hash Set**.
If we dump all elements into a Hash Set, we can look up any number in $O(1)$ time.
But how do we avoid counting the same sequence multiple times? (e.g. if we have `1,2,3`, we don't want to count starting from `1`, then count starting from `2`, then count starting from `3`).

**The Trick:**
We only want to start counting a sequence if it is the **START** of a sequence.
How do we know if a number `x` is the start of a sequence?
If `x - 1` does NOT exist in the set!
If `x - 1` exists, `x` is just the middle of a sequence, so we skip it!

So, for every number `x` in the array:
- If `x - 1` is NOT in the set: this is a start! We loop to see if `x + 1`, `x + 2`, `x + 3`... exist in the set, and count the maximum streak!

## Brute Force Approach
**Explanation:** Sort the array $O(N \log N)$ and iterate through it checking `nums[i] == nums[i-1] + 1`.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$

## Optimal Approach (Hash Set)
**Detailed explanation:**
1. If `nums.empty()`, return 0.
2. Dump all `nums` into an `unordered_set<int> numSet`.
3. Initialize `maxLength = 0`.
4. Iterate through `num` in `numSet`:
   - Check if this is the start of a sequence: `if (!numSet.count(num - 1))`
   - If it IS the start:
     - Initialize `currentNum = num` and `currentStreak = 1`.
     - While `numSet.count(currentNum + 1)`:
       - `currentNum++`
       - `currentStreak++`
     - `maxLength = max(maxLength, currentStreak)`
5. Return `maxLength`.

**Time Complexity:** $O(N)$. Even though there is a `while` loop inside a `for` loop, the `while` loop ONLY runs for the start of a sequence. Each number in the array is visited at most TWICE (once in the outer loop, once in the inner loop). $O(N) + O(N) = O(N)$.
**Space Complexity:** $O(N)$ for the Hash Set.

## C++ Solution

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        unordered_set<int> numSet(nums.begin(), nums.end());
        int maxLength = 0;
        
        for (int num : numSet) {
            // Check if it's the start of a sequence
            // If num - 1 exists, then num is not the start, skip it!
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentStreak = 1;
                
                // Keep looking for the next consecutive numbers
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum++;
                    currentStreak++;
                }
                
                maxLength = max(maxLength, currentStreak);
            }
        }
        
        return maxLength;
    }
};
```

## Dry Run
`nums = [100, 4, 200, 1, 3, 2]`
- `numSet = {100, 4, 200, 1, 3, 2}`
- `num = 100`: Is `99` in set? No. Start!
  - `101` in set? No. Streak = 1. `maxLength = 1`.
- `num = 4`: Is `3` in set? Yes. Skip!
- `num = 200`: Is `199` in set? No. Start!
  - `201` in set? No. Streak = 1. `maxLength = 1`.
- `num = 1`: Is `0` in set? No. Start!
  - `2` in set? Yes. `curr = 2`, `streak = 2`.
  - `3` in set? Yes. `curr = 3`, `streak = 3`.
  - `4` in set? Yes. `curr = 4`, `streak = 4`.
  - `5` in set? No. Stop. `maxLength = 4`.
- `num = 3`: Is `2` in set? Yes. Skip!
- `num = 2`: Is `1` in set? Yes. Skip!
Result: `4`.

## Common Mistakes
- **Failing to use the `if (!numSet.count(num - 1))` check:** If you run the inner while loop for EVERY number, the worst-case time complexity becomes $O(N^2)$ (e.g., if the array is already sorted `1,2,3,4,5`). The check is mandatory to achieve $O(N)$.

## Similar Problems
- Find all Numbers Disappeared in an Array
- Missing Number
