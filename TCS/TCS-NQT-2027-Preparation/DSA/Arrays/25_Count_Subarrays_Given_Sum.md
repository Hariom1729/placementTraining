# Problem 25: Count Subarrays with Given Sum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- An integer representing the count of valid subarrays.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

---

## Approach

This problem cannot be solved with the Sliding Window Two-Pointers method because the array contains negative numbers (meaning the sum can fluctuate up and down). We must use the **Prefix Sum + Hashing** pattern.

1. Maintain a running `sum` and a `count` of valid subarrays.
2. Create an `unordered_map<int, int> map` to store the frequencies of prefix sums we've seen so far.
3. Crucially, initialize `map[0] = 1`. This handles the case where a prefix sum itself is exactly equal to `k`.
4. Iterate through the array:
   - Add `nums[i]` to `sum`.
   - The logic: If `sum - k` exists in our map, it means there is a previous subarray ending somewhere before `i` that we can "chop off" to leave a subarray ending at `i` with exactly sum `k`.
   - Add the frequency of `sum - k` from the map to our `count`.
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
        unordered_map<int, int> map;
        map[0] = 1; // Base case
        
        int sum = 0, count = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            // Check if we have seen the required prefix sum
            if (map.count(sum - k)) {
                count += map[sum - k];
            }
            
            // Add current prefix sum to the map
            map[sum]++;
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1, 1};
    int k = 2;
    cout << "Count: " << sol.subarraySum(nums, k) << endl; // Expected: 2 (from [1,1] twice)
    
    vector<int> nums2 = {1, 2, 3};
    int k2 = 3;
    cout << "Count: " << sol.subarraySum(nums2, k2) << endl; // Expected: 2 (from [1,2] and [3])
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. The unordered map lookups take `O(1)` average time.
- **Space Complexity:** `O(N)`. The map can store up to `N` different prefix sums in the worst case.
