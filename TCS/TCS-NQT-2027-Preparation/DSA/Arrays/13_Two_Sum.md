# Problem 13: Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## Input Format
- An array of integers `nums`.
- An integer `target`.

## Output Format
- An array of two integers representing the indices.

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## Approach

**Approach: Hashing (Optimal for Unsorted Arrays)**
1. Use an `unordered_map<int, int>` to store the numbers we've seen so far and their indices.
2. Iterate through the array. For each element `nums[i]`:
3. Calculate the `complement` needed to reach the target: `complement = target - nums[i]`.
4. Check if the `complement` exists in the map.
5. If it exists, we have found our pair. Return `{map[complement], i}`.
6. If it does not exist, insert the current number and its index into the map.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // If the complement exists in the map, return indices
            if (map.count(complement)) {
                return {map[complement], i};
            }
            
            // Store current number and index in the map
            map[nums[i]] = i;
        }
        
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> res = sol.twoSum(nums, target);
    cout << "Indices: " << res[0] << ", " << res[1] << endl; // Expected: 0, 1
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once. The `unordered_map` operations (insert and lookup) take `O(1)` time on average.
- **Space Complexity:** `O(N)`. In the worst case, we might store `N-1` elements in the map.
