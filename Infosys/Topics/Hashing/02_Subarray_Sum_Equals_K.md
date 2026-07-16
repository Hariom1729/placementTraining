# Subarray Sum Equals K

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2022
Frequency: Medium

---

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

---

## Input Format
- First line: `N` (size of array).
- Second line: `N` space-separated integers.
- Third line: `k`.

---

## Output Format
- Return a single integer representing the count of subarrays.

---

## Constraints
- $1 \le nums.length \le 2 \times 10^4$
- $-1000 \le nums[i] \le 1000$
- $-10^7 \le k \le 10^7$

---

## Examples

### Example 1
**Input:** 
```
3
1 1 1
2
```
**Output:** 
```
2
```
**Explanation:** The subarrays [1, 1] (index 0,1) and [1, 1] (index 1,2) sum to 2.

### Example 2
**Input:** 
```
3
1 2 3
3
```
**Output:** 
```
2
```

---

## Brute Force Approach
Generate all possible subarrays using two nested loops. Find the sum of each subarray and if it matches `k`, increment a counter.

**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$.

---

## Optimal Approach (Prefix Sum + Hash Map)
**Detailed explanation:**
If the cumulative sum up to index `i` is `S_i`, and we want a subarray ending at `i` with sum `k`, then there must be some earlier cumulative sum `S_j` such that `S_i - S_j = k`.
Rearranging the formula: `S_j = S_i - k`.

So, as we iterate, we maintain a `prefixSum`. We check if `(prefixSum - k)` has been seen before in our Hash Map. If yes, it means there are one or more subarrays ending at current index that sum to `k`. We add their frequency to our total count.

*Crucial initialization:* We must initialize the map with `{0: 1}` to handle cases where the subarray starts from index 0.

**Dry Run:**
`nums = [1, 1, 1]`, `k = 2`
- Map: `{0: 1}`, `prefix = 0`, `count = 0`
- `i=0` (1): `prefix=1`. `prefix - k = 1 - 2 = -1`. Not in map. Add `1` to map: `{0:1, 1:1}`.
- `i=1` (1): `prefix=2`. `prefix - k = 2 - 2 = 0`. In map! Frequency is 1. `count = 1`. Add `2` to map: `{0:1, 1:1, 2:1}`.
- `i=2` (1): `prefix=3`. `prefix - k = 3 - 2 = 1`. In map! Frequency is 1. `count = 2`. Add `3` to map.
- Total `count = 2`.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for Hash Map.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixCounts;
    prefixCounts[0] = 1; // Base case for subarray starting at index 0
    
    int currentSum = 0;
    int count = 0;
    
    for (int num : nums) {
        currentSum += num;
        
        // If (currentSum - k) exists, it means we found a valid subarray
        if (prefixCounts.find(currentSum - k) != prefixCounts.end()) {
            count += prefixCounts[currentSum - k];
        }
        
        // Add current sum to map
        prefixCounts[currentSum]++;
    }
    
    return count;
}

int main() {
    vector<int> nums = {1, 1, 1};
    cout << "Count: " << subarraySum(nums, 2) << endl; // Output: 2
    return 0;
}
```

---

## Common Mistakes
- **Sliding Window Trap:** Because the array can contain *negative* numbers, the standard Sliding Window (Two Pointers) technique will FAIL. The window cannot reliably expand or shrink. You MUST use Prefix Sum + Hash Map.
- **Forgetting `{0: 1}`:** If the valid subarray starts from index 0, `currentSum - k` will be `0`. If `0` is not in the map, it will miss counting it.

---

## Pattern Recognition
**Identify this when:** Asking for subarrays (contiguous) with a specific sum, **especially when negative numbers are involved**. 
Prefix Sum + Hash Map is the universal solution for "Subarray Sum Equals X".
