# Problem 4: Longest Subarray with Given Sum K

## Problem Statement
Given an array containing `N` integers and an integer `K`, your task is to find the length of the longest subarray with the sum of the elements equal to the given value `K`.

## Input Format
- An array of integers `arr`.
- An integer `K`.

## Output Format
- An integer representing the length of the longest subarray.

## Constraints
- `1 <= N <= 10^5`
- `-10^4 <= arr[i] <= 10^4`
- `-10^9 <= K <= 10^9`

---

## Approach: Prefix Sum + Hashing

Because the array can contain negative numbers, the Sliding Window (Two Pointers) approach will fail (as the sum can fluctuate up and down). We must use Hashing.

1. Maintain a running sum `prefixSum = 0` and the `maxLength = 0`.
2. Create an `unordered_map<int, int> prefixMap` to store the `(prefixSum, index)` where that sum was FIRST seen. We only store it the FIRST time because we want the *longest* subarray, which means we want to subtract the earliest possible prefix sum.
3. Iterate through the array:
   - Add `arr[i]` to `prefixSum`.
   - **Case 1:** If `prefixSum == K`, it means the subarray from index `0` to `i` has sum `K`. The length is `i + 1`. `maxLength = max(maxLength, i + 1)`.
   - **Case 2:** Check if `(prefixSum - K)` exists in `prefixMap`. If it does, it means there is a previous prefix sum that we can "chop off" to leave a subarray of sum `K`.
     - Let the index of that previous prefix sum be `prevIndex`.
     - The length of this valid subarray is `i - prevIndex`.
     - `maxLength = max(maxLength, i - prevIndex)`.
   - Finally, if `prefixSum` is NOT already in the map, add it: `prefixMap[prefixSum] = i`. *(We only add it if it doesn't exist because we want to keep the earliest index).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubarrayWithSumK(vector<int>& arr, int k) {
        unordered_map<long long, int> prefixMap;
        long long prefixSum = 0;
        int maxLength = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            prefixSum += arr[i];
            
            // Case 1: The prefix itself is equal to K
            if (prefixSum == k) {
                maxLength = max(maxLength, i + 1);
            }
            
            // Case 2: We have seen (prefixSum - k) before
            long long requiredPrefix = prefixSum - k;
            if (prefixMap.find(requiredPrefix) != prefixMap.end()) {
                int len = i - prefixMap[requiredPrefix];
                maxLength = max(maxLength, len);
            }
            
            // Add prefixSum to map ONLY IF it doesn't exist already
            // This ensures we keep the earliest index for maximum length
            if (prefixMap.find(prefixSum) == prefixMap.end()) {
                prefixMap[prefixSum] = i;
            }
        }
        
        return maxLength;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {10, 5, 2, 7, 1, 9};
    int k = 15;
    cout << "Longest Subarray Length: " << sol.longestSubarrayWithSumK(arr, k) << endl; // Expected: 4 (from [5, 2, 7, 1])
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once. The `unordered_map` lookup and insertion take `O(1)` on average.
- **Space Complexity:** `O(N)`. In the worst case, all prefix sums are unique and stored in the map.
