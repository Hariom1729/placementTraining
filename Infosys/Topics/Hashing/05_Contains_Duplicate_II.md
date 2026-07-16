# Contains Duplicate II

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Palantir

## Topic
Hashing / Sliding Window

## Pattern
Hash Map Index Tracking

## Problem Statement
Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Input
- `nums` vector of integers.
- `k` integer distance limit.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] == nums[3], and abs(0 - 3) = 3 <= 3.
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: nums[2] == nums[3], and abs(2 - 3) = 1 <= 1.
```

**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: The only duplicate of 1 is at index 3. abs(0 - 3) = 3. 3 > 2, so it's false.
```

## Edge Cases
- `k = 0`. Since `i` and `j` must be distinct (`abs(i-j) > 0`), it's impossible to satisfy. Return `false`.
- A number appears many times, but only the 4th and 5th appearances are close enough.

## Intuition
This builds directly on `Contains Duplicate`. But this time, just knowing that a duplicate *exists* isn't enough; we need to know exactly **WHERE** we saw it last, so we can calculate the distance `abs(i - j)`.
Because we need to map a **value** to its **last seen index**, we should upgrade our `unordered_set` to an `unordered_map<int, int>`!
- Keys will be the numbers in the array.
- Values will be the highest index where we last saw that number.

As we iterate through the array at index `i`:
- We check if `nums[i]` is in our hash map.
- If it IS in the hash map, we grab its last seen index `last_i = map[nums[i]]`.
- We check if `i - last_i <= k`.
  - If YES: We found it! Return `true`.
  - If NO: We update `map[nums[i]] = i` so that future duplicates can use this new, closer index!
- If it is NOT in the hash map, we just insert it: `map[nums[i]] = i`.

## Brute Force Approach
**Explanation:** For every element `i`, run a nested loop `j` from `i+1` to `i+k` checking if `nums[i] == nums[j]`.
**Time Complexity:** $O(N \times k)$
**Space Complexity:** $O(1)$

## Optimal Approach (Hash Map)
**Detailed explanation:**
1. Initialize an `unordered_map<int, int> seen`.
2. Loop `i` from `0` to `nums.size() - 1`:
   - If `seen.count(nums[i]) > 0`:
     - If `i - seen[nums[i]] <= k`, return `true`.
   - (Regardless of whether it was there or not, or if it failed the distance check) Update the map with the latest index: `seen[nums[i]] = i`.
3. Return `false`.

**Time Complexity:** $O(N)$ because checking and updating an `unordered_map` is $O(1)$ on average.
**Space Complexity:** $O(N)$ for the hash map to store unique values.

*(Note: You can also solve this strictly as a Sliding Window using an `unordered_set` of size `k`, which caps space at $O(k)$).*

## C++ Solution (Hash Map)

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Map to store {value : last seen index}
        unordered_map<int, int> seen;
        
        for (int i = 0; i < nums.size(); i++) {
            // If the number exists in the map
            if (seen.count(nums[i])) {
                // Check the distance constraint
                if (i - seen[nums[i]] <= k) {
                    return true;
                }
            }
            
            // Unconditionally update the index to the most recent one
            // (If it failed the distance check, we want to store this closer index for future checks)
            seen[nums[i]] = i;
        }
        
        return false;
    }
};
```

## Dry Run
`nums = [1, 2, 3, 1, 2, 3], k = 2`
- `i=0, num=1`: Map empty. Add `seen[1] = 0`.
- `i=1, num=2`: Add `seen[2] = 1`.
- `i=2, num=3`: Add `seen[3] = 2`.
- `i=3, num=1`: `1` is in map! `last_i = seen[1] = 0`. `3 - 0 = 3`. `3 <= 2` is FALSE.
  - Update `seen[1] = 3`. (Map now stores index 3 instead of 0).
- `i=4, num=2`: `2` is in map! `last_i = seen[2] = 1`. `4 - 1 = 3`. `3 <= 2` is FALSE.
  - Update `seen[2] = 4`.
- `i=5, num=3`: `last_i = 2`. `5 - 2 = 3`. FALSE.
  - Update `seen[3] = 5`.
- Loop finishes. Returns `false`.

## Common Mistakes
- **Failing to overwrite the index on a failed check:** If `nums[i]` is in the map but `i - seen[nums[i]] > k`, some candidates do nothing and just `continue`. This is WRONG! You must update `seen[nums[i]] = i`. The new occurrence is much closer to the rest of the array, so it is a much better candidate for matching with future duplicates!

## Similar Problems
- Contains Duplicate
- Contains Duplicate III (Uses a balanced BST / `std::set` in C++ for range queries)
