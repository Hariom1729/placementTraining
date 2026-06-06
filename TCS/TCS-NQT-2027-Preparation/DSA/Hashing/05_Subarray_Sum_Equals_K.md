# Problem 5: Subarray Sum Equals K

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An integer representing the total count of valid subarrays.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

---

## Approach: Prefix Sum + Hashing

This is very similar to the "Longest Subarray" problem, but instead of tracking the *earliest index* to maximize length, we need to track the **frequency** of each prefix sum to count the total number of occurrences.

1. Maintain a running `sum = 0` and a `count = 0`.
2. Create an `unordered_map<int, int> map` to store the frequencies of prefix sums. `map[prefix_sum] = frequency`.
3. **Crucial Base Case:** Initialize `map[0] = 1`. This handles the case where the running prefix sum exactly equals `k` right from the beginning of the array.
4. Iterate through the array:
   - Add `nums[i]` to `sum`.
   - The logic: If `sum - k` exists in our map, it means there are previously seen prefix sums that we can "chop off" to leave a subarray ending at `i` with exactly sum `k`.
   - We add the frequency of `sum - k` from the map to our `count`.
   - Finally, add the current `sum` to the map (increment its frequency).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixMap;
        prefixMap[0] = 1; // Base case: one way to have a sum of 0 (empty subarray)
        
        int sum = 0;
        int count = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            // If (sum - k) exists, add its frequency to the total count
            int requiredPrefix = sum - k;
            if (prefixMap.find(requiredPrefix) != prefixMap.end()) {
                count += prefixMap[requiredPrefix];
            }
            
            // Increment the frequency of the current prefix sum
            prefixMap[sum]++;
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1, 1};
    int k = 2;
    cout << "Count of subarrays: " << sol.subarraySum(nums, k) << endl; // Expected: 2 ([1,1] and [1,1])
    
    vector<int> nums2 = {1, 2, 3};
    int k2 = 3;
    cout << "Count of subarrays: " << sol.subarraySum(nums2, k2) << endl; // Expected: 2 ([1,2] and [3])
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once, performing `O(1)` map lookups and insertions.
- **Space Complexity:** `O(N)`. The map can store up to `N` different prefix sums.
