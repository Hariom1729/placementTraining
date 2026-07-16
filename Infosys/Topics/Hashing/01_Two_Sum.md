# Two Sum

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Frequency: Very High

---

## Problem Statement
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

---

## Input Format
- First line: `N` (Size of the array)
- Second line: `N` space-separated integers.
- Third line: `target` integer.

---

## Output Format
- Return two integers representing the indices.

---

## Constraints
- $2 \le nums.length \le 10^4$
- $-10^9 \le nums[i] \le 10^9$
- $-10^9 \le target \le 10^9$

---

## Examples

### Example 1
**Input:** 
```
4
2 7 11 15
9
```
**Output:** 
```
[0, 1]
```
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

---

## Brute Force Approach
Use two nested loops. For every element `nums[i]`, check all subsequent elements `nums[j]` to see if `nums[i] + nums[j] == target`.

**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

---

## Optimal Approach (Using Hash Map)
**Detailed explanation:**
Instead of a second loop to search for the required difference (`target - nums[i]`), we can use a Hash Map. 
As we iterate through the array, we check if the difference `(target - nums[i])` already exists in the map.
- If it does, we found our pair! We return the index from the map and the current index `i`.
- If it doesn't, we add the current number and its index `i` into the map.

**Dry Run:**
`nums = [2, 7, 11, 15]`, `target = 9`
- `i = 0`, `val = 2`: difference = `9 - 2 = 7`. Is 7 in map? No. Map -> `{2: 0}`.
- `i = 1`, `val = 7`: difference = `9 - 7 = 2`. Is 2 in map? Yes! It is at index 0.
- Return `[0, 1]`.

**Complexity:**
- **Time Complexity:** $O(N)$ because hash map lookups take $O(1)$ on average.
- **Space Complexity:** $O(N)$ for the hash map.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numMap;
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // If the complement is found, return the indices
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], i};
        }
        
        // Add the current number and its index to the map
        numMap[nums[i]] = i;
    }
    
    return {};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    vector<int> res = twoSum(nums, 9);
    cout << "[" << res[0] << ", " << res[1] << "]" << endl;
    return 0;
}
```

---

## Common Mistakes
- **Populating the Map early:** If you insert all elements into the map *before* checking, you might accidentally use the same element twice (e.g., if target is 6 and the array has a 3). By checking first and then inserting, you avoid this.

---

## Similar Questions
- 3Sum (Medium)
- 4Sum (Hard)
- Subarray Sum Equals K

---

## Pattern Recognition
**Identify this when:** You need to find pairs that satisfy an arithmetic condition (sum, difference). **Hash Maps** reduce the $O(N)$ linear search to $O(1)$ lookups.
