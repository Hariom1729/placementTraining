# Problem 1: Count Frequencies of Array Elements

## Problem Statement
Given an array `arr` of size `N`, count the frequency of each element in the array and print them.

## Input Format
- An array of integers `arr`.

## Output Format
- Print each unique element and its frequency.

## Constraints
- `1 <= N <= 10^5`
- `1 <= arr[i] <= 10^9`

---

## Approach

Since `arr[i]` can be up to `10^9`, we cannot use a fixed-size frequency array (it would exceed memory limits). We must use a Hash Map.
To achieve `O(N)` time complexity, we use `std::unordered_map`.

1. Initialize an `unordered_map<int, int> freqMap`.
2. Iterate through the array `arr`. For each element `x`, increment its count in the map: `freqMap[x]++`.
3. Iterate through the map to print the elements and their frequencies.
*(Note: If the problem asks you to print them in the order they appear in the array, you should iterate through the array again and check the map, instead of iterating through the map directly, because `unordered_map` does not maintain insertion order).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    void countFrequencies(vector<int>& arr) {
        unordered_map<int, int> freqMap;
        
        // Count frequencies
        for (int i = 0; i < arr.size(); i++) {
            freqMap[arr[i]]++;
        }
        
        // Print frequencies
        for (auto it : freqMap) {
            cout << "Element " << it.first << " occurs " << it.second << " times" << endl;
        }
    }
};

int main() {
    Solution sol;
    vector<int> arr = {10, 5, 10, 15, 10, 5};
    sol.countFrequencies(arr);
    
    // Expected output (order may vary due to unordered_map):
    // Element 10 occurs 3 times
    // Element 5 occurs 2 times
    // Element 15 occurs 1 times
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Inserting into an `unordered_map` takes `O(1)` on average. We do this `N` times.
- **Space Complexity:** `O(N)` in the worst case if all elements in the array are unique.
