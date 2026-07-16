# Contains Duplicate

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Apple

## Topic
Hashing / Arrays

## Pattern
Hash Set Frequency Check

## Problem Statement
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Input
- `nums` vector of integers.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 appears at indices 0 and 3.
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Edge Cases
- Array with one element (cannot contain duplicates, return `false`).
- Massive array where the duplicate is only at the very end.

## Intuition
We need to check if we have "seen" a number before. The perfect data structure for quickly remembering what we have seen without storing redundant data is a **Hash Set** (`unordered_set` in C++).
We iterate through the array. For every number:
- We check if it is already in our `unordered_set`.
- If it is, we immediately return `true` (we found a duplicate!).
- If it isn't, we insert it into our `unordered_set` and keep looking.
If we finish the entire array without triggering a `true`, we return `false`.

*(Alternatively, you can just sort the array and check adjacent elements. It's slower $O(N \log N)$, but uses $O(1)$ space).*

## Brute Force Approach
**Explanation:** For every element, check every other element in the array to see if they match.
**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$

## Optimal Approach 1 (Hash Set)
**Detailed explanation:**
1. Initialize an `unordered_set<int> seen`.
2. Iterate `num` in `nums`:
   - If `seen.count(num)` is 1 (meaning it exists in the set):
     - Return `true`.
   - Else:
     - `seen.insert(num)`.
3. Return `false`.

**Time Complexity:** $O(N)$ because inserting and checking a hash set is $O(1)$ on average.
**Space Complexity:** $O(N)$ because the hash set can store up to $N$ elements.

## Optimal Approach 2 (Sorting - O(1) Space)
**Detailed explanation:**
1. Sort the `nums` array: `sort(nums.begin(), nums.end())`.
2. Iterate `i` from `1` to `nums.size() - 1`:
   - If `nums[i] == nums[i-1]`, return `true`.
3. Return `false`.

**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$

## C++ Solution (Hash Set)

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        
        for (int num : nums) {
            // If the number is already in the set, we found a duplicate
            if (seen.count(num)) {
                return true;
            }
            // Otherwise, add it to our set to remember we've seen it
            seen.insert(num);
        }
        
        return false;
    }
};
```

## C++ Solution (Sorting)

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
};
```

## Dry Run (Hash Set)
`nums = [1, 2, 3, 1]`
- `num = 1`: `seen` is empty. Not in set. `seen.insert(1)`. `seen = {1}`.
- `num = 2`: `2` not in set. `seen.insert(2)`. `seen = {1, 2}`.
- `num = 3`: `3` not in set. `seen.insert(3)`. `seen = {1, 2, 3}`.
- `num = 1`: `1` IS in set! Return `true`.

## Common Mistakes
- **Using an array as a frequency map:** You might be tempted to use `vector<int> count(1000)` like in string problems. However, the constraints say `-10^9 <= nums[i] <= 10^9`. You cannot create an array of size $2 \times 10^9$. You MUST use an `unordered_set`.

## Similar Problems
- Contains Duplicate II
- Contains Duplicate III
