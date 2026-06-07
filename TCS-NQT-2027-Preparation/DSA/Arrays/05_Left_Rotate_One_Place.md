# Problem 5: Left Rotate an Array by One Place

## Problem Statement
Given an array `arr` of integers, left rotate the array by exactly one position. The first element of the array should be moved to the last position.

## Input Format
- An array of integers `arr`.

## Output Format
- The modified array `arr`.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Approach

1. Store the first element of the array in a temporary variable, e.g., `temp = arr[0]`.
2. Iterate from index `1` up to `N-1`.
3. Shift each element one position to the left: `arr[i - 1] = arr[i]`.
4. Finally, assign the value stored in `temp` to the last position of the array: `arr[N - 1] = temp`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotateOne(vector<int>& arr) {
        if (arr.empty()) return;
        
        int temp = arr[0];
        
        for (int i = 1; i < arr.size(); i++) {
            arr[i - 1] = arr[i];
        }
        
        arr[arr.size() - 1] = temp;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 2, 3, 4, 5};
    sol.rotateOne(arr);
    
    cout << "Rotated array: ";
    for (int x : arr) {
        cout << x << " "; // Expected: 2 3 4 5 1
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` because we iterate through the array once to shift the elements.
- **Space Complexity:** `O(1)` as we are doing the shifting in-place, using only a single temporary variable.
