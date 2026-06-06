# Problem 10: Count Pairs with Given Sum

## Problem Statement
Given an array of integers `arr`, and an integer `K`, find the number of pairs of elements in the array whose sum is equal to `K`.

Notice that this is different from Two Sum: we need to find the total **count** of all valid pairs, not just the indices of one pair. `arr[i] + arr[j] == K` (where `i < j`).

## Input Format
- An array of integers `arr`.
- An integer `K`.

## Output Format
- An integer representing the count of valid pairs.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^5`
- `1 <= K <= 10^5`

---

## Approach

Since we need the total count of pairs, we can't just use a map to store seen elements as `true/false`; we need to store their **frequencies**.

1. Create an `unordered_map<int, int> freqMap` to store the frequency of numbers seen *so far*.
2. Initialize `count = 0`.
3. Iterate through `arr`:
   - For the current element `arr[i]`, we need `complement = K - arr[i]`.
   - If `complement` exists in our map, it means there are `freqMap[complement]` numbers previously in the array that can form a valid pair with `arr[i]`. Add this frequency to `count`.
   - Increment the frequency of the current element: `freqMap[arr[i]]++`.
4. Return `count`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int getPairsCount(vector<int>& arr, int k) {
        unordered_map<int, int> freqMap;
        int count = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            int complement = k - arr[i];
            
            // If complement exists, add its frequency to total count
            if (freqMap.find(complement) != freqMap.end()) {
                count += freqMap[complement];
            }
            
            // Add current element to the map
            freqMap[arr[i]]++;
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 5, 7, 1};
    int k = 6;
    cout << "Pairs count for sum 6: " << sol.getPairsCount(arr, k) << endl; // Expected: 2 (1+5 and 5+1)

    vector<int> arr2 = {1, 1, 1, 1};
    int k2 = 2;
    cout << "Pairs count for sum 2: " << sol.getPairsCount(arr2, k2) << endl; // Expected: 6 (all combinations)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` since we traverse the array once and perform `O(1)` map operations.
- **Space Complexity:** `O(N)` to store frequencies in the hash map.
