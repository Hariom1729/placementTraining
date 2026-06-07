# Problem 1: Find the Largest Element in an Array

## Problem Statement
Given an array, find the maximum element in it.

## Input Format
- An array of integers `arr`.

## Output Format
- An integer representing the largest element.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Approach

1. Initialize a variable `max_val` with the first element of the array.
2. Iterate through the array starting from the second element.
3. Compare the current element with `max_val`. If it's greater, update `max_val`.
4. Return `max_val` after the loop finishes.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findLargest(vector<int>& arr) {
        int max_val = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] > max_val) {
                max_val = arr[i];
            }
        }
        return max_val;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {2, 5, 1, 3, 0};
    cout << "Largest element is: " << sol.findLargest(arr) << endl; // Expected: 5
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the size of the array. We visit each element exactly once.
- **Space Complexity:** `O(1)`. We only use a single integer variable `max_val`.

---

## Interview Notes
- In an actual interview, you might be asked if `std::max_element` is allowed. Always provide the manual `O(N)` loop implementation first, then mention `*max_element(arr.begin(), arr.end())` as an alternative.
