# Problem 3: Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Input Format
- An array of integers `nums`.
- An integer `target`.

## Output Format
- An array containing the two indices.

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

---

## Approach: Hashing

We need to find two numbers, `a` and `b`, such that `a + b = target`. 
If we are currently at `a`, we need to check if we have already seen `b = target - a` previously in the array.

1. Initialize an `unordered_map<int, int> seen`. This will map a number to its index: `seen[number] = index`.
2. Iterate through the array.
3. For each element `nums[i]`:
   - Calculate the `complement = target - nums[i]`.
   - Check if `complement` exists in our `seen` map.
   - If it does exist, we have found our pair! Return `{seen[complement], i}`.
   - If it does not exist, add the current element to the map: `seen[nums[i]] = i`.

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
        unordered_map<int, int> seen;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // If complement exists in map, return the indices
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            
            // Otherwise, add the current element and its index to the map
            seen[nums[i]] = i;
        }
        
        return {}; // Should not reach here if there is exactly one solution
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> res = sol.twoSum(nums, target);
    cout << "Indices: [" << res[0] << ", " << res[1] << "]" << endl; // Expected: [0, 1]
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once. The `unordered_map` provides `O(1)` average time complexity for lookups and insertions.
- **Space Complexity:** `O(N)`. In the worst case, we might store `N-1` elements in the map before finding the pair.
