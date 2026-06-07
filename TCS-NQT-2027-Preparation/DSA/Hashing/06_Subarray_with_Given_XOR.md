# Problem 6: Count Subarrays with Given XOR

## Problem Statement
Given an array of integers `A` and an integer `B`.
Find the total number of subarrays having bitwise XOR of all elements equals to `B`.

## Input Format
- An array of integers `A`.
- An integer `B`.

## Output Format
- An integer representing the total count of valid subarrays.

## Constraints
- `1 <= A.length <= 10^5`
- `1 <= A[i] <= 10^5`
- `1 <= B <= 10^5`

---

## Approach: Prefix XOR + Hashing

This problem is identical in logic to "Subarray Sum Equals K", but uses the XOR operation instead of addition.
Key property of XOR: If `a ^ b = c`, then `a ^ c = b`.

1. Maintain a running `prefixXOR = 0` and `count = 0`.
2. Create an `unordered_map<int, int> map` to store the frequencies of `prefixXOR`.
3. **Base Case:** Initialize `map[0] = 1`. This handles subarrays starting from index 0 whose XOR is exactly `B`.
4. Iterate through the array:
   - Calculate current `prefixXOR ^= A[i]`.
   - The required prefix we need to chop off is `x = prefixXOR ^ B`.
   - If `x` exists in the map, add its frequency to `count`.
   - Add the current `prefixXOR` to the map (increment its frequency).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int solve(vector<int>& A, int B) {
        unordered_map<int, int> prefixMap;
        prefixMap[0] = 1; // Base case
        
        int prefixXOR = 0;
        int count = 0;
        
        for (int i = 0; i < A.size(); i++) {
            prefixXOR ^= A[i];
            
            // Check if prefixXOR ^ B exists in the map
            int requiredXOR = prefixXOR ^ B;
            if (prefixMap.find(requiredXOR) != prefixMap.end()) {
                count += prefixMap[requiredXOR];
            }
            
            // Add current prefixXOR to the map
            prefixMap[prefixXOR]++;
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> A = {4, 2, 2, 6, 4};
    int B = 6;
    cout << "Count of subarrays with XOR " << B << ": " << sol.solve(A, B) << endl; 
    // Expected: 4 ( [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6] )
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once and perform `O(1)` map lookups/insertions.
- **Space Complexity:** `O(N)`. We might store up to `N` different prefix XORs in the worst case.
