# Problem 3: Check if an Array is Sorted

## Problem Statement
Given an array of integers, check if the array is sorted in ascending order.
Return `true` if it is sorted, otherwise return `false`.

## Input Format
- A vector of integers `arr`.

## Output Format
- Boolean `true` or `false`.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Approach

1. Start a loop from index `1` to `N-1`.
2. Compare the current element `arr[i]` with the previous element `arr[i - 1]`.
3. If at any point `arr[i] < arr[i - 1]`, it means the ascending order is broken. Return `false` immediately.
4. If the loop successfully completes without returning `false`, the array is sorted. Return `true`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isSorted(vector<int>& arr) {
        if (arr.size() <= 1) return true;
        
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    vector<int> arr1 = {1, 2, 3, 4, 5};
    cout << (sol.isSorted(arr1) ? "true" : "false") << endl; // Expected: true
    
    vector<int> arr2 = {5, 4, 6, 7, 8};
    cout << (sol.isSorted(arr2) ? "true" : "false") << endl; // Expected: false
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. In the worst case (the array is sorted or fails at the last element), we iterate `N-1` times.
- **Space Complexity:** `O(1)`. No extra space is required.
