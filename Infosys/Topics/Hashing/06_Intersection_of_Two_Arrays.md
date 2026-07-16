# Intersection of Two Arrays

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook

## Topic
Hashing / Arrays

## Pattern
Hash Set Lookups

## Problem Statement
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be **unique** and you may return the result in **any order**.

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Input
- `nums1` vector of integers.
- `nums2` vector of integers.

## Output
- Return a vector of integers.

## Sample Test Cases

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Explanation: The only common element is 2. Result elements must be unique.
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

## Edge Cases
- No intersection between the two arrays (return empty array).
- One array is completely contained within the other.

## Intuition
We need to find elements that exist in BOTH arrays. But the problem specifically asks for **unique** elements in the output.
This means if an array has `[2,2,2]` and the other has `[2,2]`, the intersection is just `[2]`.
A **Hash Set** (`unordered_set`) is specifically designed to store unique elements!
1. Convert `nums1` into a Hash Set. This instantly removes all duplicates from `nums1` and gives us $O(1)$ lookups.
2. Iterate through `nums2`. For every number, check if it exists in the Hash Set.
3. If it DOES exist, we found a common element! We add it to our result array.
4. IMPORTANT: To prevent adding the same common element twice (if `nums2` has duplicates), we must **remove** it from the Hash Set as soon as we add it to our result array!

## Brute Force Approach
**Explanation:** For every element in `nums1`, run a loop over `nums2` to see if it exists. If it does, add to a result set to ensure uniqueness.
**Time Complexity:** $O(N \times M)$
**Space Complexity:** $O(\min(N, M))$ for result.

## Optimal Approach (Hash Set)
**Detailed explanation:**
1. Create an `unordered_set<int> set1` from `nums1`.
   `unordered_set<int> set1(nums1.begin(), nums1.end());`
2. Create a `vector<int> result` to hold the output.
3. Iterate `num` through `nums2`:
   - If `set1.count(num) > 0`:
     - Add `num` to `result`.
     - Remove `num` from `set1` (`set1.erase(num)`) so we don't add it again if `num` appears again in `nums2`.
4. Return `result`.

*Alternative approach: Since the constraints say `0 <= nums[i] <= 1000`, we can use a boolean array of size 1001 instead of a Hash Set for ultra-fast performance.*

## C++ Solution (Hash Set)

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // Convert nums1 to a set to remove duplicates and allow O(1) lookups
        unordered_set<int> set1(nums1.begin(), nums1.end());
        vector<int> result;
        
        for (int num : nums2) {
            // If the number exists in set1
            if (set1.count(num)) {
                result.push_back(num);
                // Erase it from the set so we don't add it again for duplicate values in nums2
                set1.erase(num);
            }
        }
        
        return result;
    }
};
```

## C++ Solution (Frequency Array - Optimal for constrained values)
```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        bool seen[1001] = {false};
        for (int num : nums1) {
            seen[num] = true;
        }
        
        vector<int> result;
        for (int num : nums2) {
            if (seen[num]) {
                result.push_back(num);
                seen[num] = false; // Mark as false to avoid duplicates
            }
        }
        
        return result;
    }
};
```

## Dry Run
`nums1 = [4,9,5], nums2 = [9,4,9,8,4]`
- `set1 = {4, 9, 5}`.
- `num = 9` (from nums2): In `set1`? Yes! `result.push(9)`. `set1.erase(9)`. `set1 = {4, 5}`.
- `num = 4` (from nums2): In `set1`? Yes! `result.push(4)`. `set1.erase(4)`. `set1 = {5}`.
- `num = 9` (from nums2): In `set1`? No (we erased it).
- `num = 8` (from nums2): In `set1`? No.
- `num = 4` (from nums2): In `set1`? No.
- Return `[9, 4]`.

## Common Mistakes
- **Forgetting to handle duplicates in `nums2`:** If you just push to the result array without erasing from the set, `nums2 = [2,2]` will result in `[2, 2]`, which fails the uniqueness constraint.

## Similar Problems
- Intersection of Two Arrays II (Allowing duplicates)
- Minimum Common Value
