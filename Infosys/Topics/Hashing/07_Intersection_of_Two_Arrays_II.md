# Intersection of Two Arrays II

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Hashing / Arrays / Two Pointers

## Pattern
Frequency Maps

## Problem Statement
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

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
Output: [2,2]
Explanation: Since 2 appears twice in both arrays, it must appear twice in the result.
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
```

## Edge Cases
- No intersection.
- One array is completely identical to the other.

## Intuition
Unlike `Intersection of Two Arrays I`, we cannot just use a Hash Set (which destroys duplicates). We need to track exactly **how many times** each number appears!
This calls for a **Hash Map** (`unordered_map`) to store frequencies.
1. Iterate through `nums1` and count the frequency of each number.
2. Iterate through `nums2`. For every number, check if its frequency in our map is $> 0$.
3. If it is, we found a match! We add it to our result array.
4. We must then **decrement** the frequency in the map! This ensures that if `nums2` has three `2`s but `nums1` only had two `2`s, we only push two `2`s to our result array.

*Follow-up question:* What if the given arrays are already sorted?
If they are sorted, we can use a **Two Pointers** approach which uses $O(1)$ extra space!

## Optimal Approach 1 (Hash Map)
**Detailed explanation:**
1. Create an `unordered_map<int, int> counts`.
2. For each `num` in `nums1`: `counts[num]++`.
3. Create a `vector<int> result`.
4. For each `num` in `nums2`:
   - If `counts[num] > 0`:
     - `result.push_back(num)`.
     - `counts[num]--`.
5. Return `result`.

**Time Complexity:** $O(N + M)$
**Space Complexity:** $O(\min(N, M))$ (You should hash the smaller array to save space).

## Optimal Approach 2 (Two Pointers - Follow up for Sorted Arrays)
**Detailed explanation:**
1. `sort(nums1.begin(), nums1.end())` and `sort(nums2.begin(), nums2.end())`.
2. Initialize `i = 0` (for `nums1`) and `j = 0` (for `nums2`).
3. While `i < nums1.size()` and `j < nums2.size()`:
   - If `nums1[i] < nums2[j]`, increment `i` (catch up).
   - Else if `nums1[i] > nums2[j]`, increment `j` (catch up).
   - Else (they are equal!):
     - `result.push_back(nums1[i])`.
     - `i++`, `j++`.
4. Return `result`.

**Time Complexity:** $O(N \log N + M \log M)$ to sort. If already sorted, $O(N + M)$.
**Space Complexity:** $O(1)$ ignoring the result array.

## C++ Solution (Hash Map)

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        // Optimize: Hash the smaller array to save space
        if (nums1.size() > nums2.size()) {
            return intersect(nums2, nums1);
        }
        
        unordered_map<int, int> counts;
        for (int num : nums1) {
            counts[num]++;
        }
        
        vector<int> result;
        for (int num : nums2) {
            // If the number exists and has a remaining count > 0
            if (counts[num] > 0) {
                result.push_back(num);
                counts[num]--; // Decrement the available count
            }
        }
        
        return result;
    }
};
```

## Dry Run
`nums1 = [1,2,2,1], nums2 = [2,2]`
- Map for `nums1`: `{1: 2, 2: 2}`.
- `num = 2` (nums2): `counts[2]` is 2. `result.push(2)`. `counts[2] = 1`.
- `num = 2` (nums2): `counts[2]` is 1. `result.push(2)`. `counts[2] = 0`.
- Result: `[2, 2]`.

## Common Mistakes
- **Erasing the key instead of decrementing:** If you use `counts.erase(num)`, you will fail test cases where multiple duplicates should match. You must decrement `counts[num]--`.

## Similar Problems
- Intersection of Two Arrays I
- Find Common Characters
