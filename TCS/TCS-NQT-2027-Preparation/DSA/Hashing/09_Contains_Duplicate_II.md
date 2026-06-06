# Problem 9: Contains Duplicate II

## Problem Statement
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- A boolean representing whether the condition is met.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

---

## Approach: Hash Map for Indices

We need to check if duplicate values exist within a sliding window of size `k`.

1. Use an `unordered_map<int, int> map` where the key is the number and the value is the last seen index of that number.
2. Iterate through the array:
   - If `nums[i]` is already in the map:
     - Check if the difference between the current index `i` and the stored index `map[nums[i]]` is `<= k`.
     - If yes, return `true`.
   - Update the map with the current index: `map[nums[i]] = i`. (We always want the most recent index to minimize `abs(i - j)` for future checks).
3. If the loop completes without finding a valid pair, return `false`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map; // Number -> Last Seen Index
        
        for (int i = 0; i < nums.size(); i++) {
            if (map.find(nums[i]) != map.end()) {
                // Duplicate found, check distance
                if (i - map[nums[i]] <= k) {
                    return true;
                }
            }
            // Always update to the latest index
            map[nums[i]] = i;
        }
        
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1, 2, 3, 1};
    int k1 = 3;
    cout << "Contains duplicate within 3? " << (sol.containsNearbyDuplicate(nums1, k1) ? "Yes" : "No") << endl; // Expected: Yes

    vector<int> nums2 = {1, 2, 3, 1, 2, 3};
    int k2 = 2;
    cout << "Contains duplicate within 2? " << (sol.containsNearbyDuplicate(nums2, k2) ? "Yes" : "No") << endl; // Expected: No
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` since we traverse the array once and hash map lookups are `O(1)`.
- **Space Complexity:** `O(N)` in the worst case where all elements are unique.
