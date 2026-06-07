# Problem 8: Linear Search

## Problem Statement
Given an array `arr` and an integer `key`, find if `key` is present in the array. If present, return its index. If not present, return `-1`.

## Input Format
- An array of integers `arr`.
- An integer `key`.

## Output Format
- An integer representing the index, or `-1`.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Approach

This is the most basic searching algorithm. Since the array is not guaranteed to be sorted, we must check every element.
1. Iterate through the array from index `0` to `N-1`.
2. Compare each element with the `key`.
3. If `arr[i] == key`, return `i`.
4. If the loop finishes without finding the `key`, return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& arr, int key) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {10, 20, 30, 40, 50};
    int key = 30;
    
    cout << "Index of " << key << ": " << sol.search(arr, key) << endl; // Expected: 2
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. In the worst case, the key is at the end of the array or not present.
- **Space Complexity:** `O(1)`.
