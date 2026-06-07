# Problem 2: Implement Bubble Sort

## Problem Statement
Given an array `arr` of size `N`, sort the array in ascending order using the **Bubble Sort** algorithm.

## Input Format
- An array of integers `arr`.

## Output Format
- The same array sorted in ascending order.

## Constraints
- `1 <= N <= 1000`
- `0 <= arr[i] <= 10^5`

---

## Approach: Bubble Sort

**Core Idea:** Repeatedly swap adjacent elements if they are in the wrong order. This causes the largest elements to "bubble up" to the end of the array.

1. Start an outer loop `i` from `N-1` down to `1`. This represents the end boundary of the unsorted part.
2. For each `i`, run an inner loop `j` from `0` to `i-1`.
3. Compare `arr[j]` and `arr[j+1]`. If `arr[j] > arr[j+1]`, swap them.
4. **Optimization:** If no two elements were swapped in the inner loop, it means the array is already sorted. We can break early.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void bubbleSort(vector<int>& arr) {
        int n = arr.size();
        
        for (int i = n - 1; i >= 1; i--) {
            bool swapped = false; // Optimization
            
            for (int j = 0; j <= i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }
            
            // If no swaps occurred, the array is sorted
            if (!swapped) {
                break;
            }
        }
    }
};

int main() {
    Solution sol;
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    sol.bubbleSort(arr);
    
    cout << "Sorted Array: ";
    for (int x : arr) cout << x << " "; // Expected: 11 12 22 25 34 64 90
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** 
  - **Worst & Average Case:** `O(N^2)` (Array is reverse sorted or randomly sorted).
  - **Best Case:** `O(N)` (Array is already sorted, optimization catches it on the first pass).
- **Space Complexity:** `O(1)`. In-place sorting.
- **Stability:** Stable. Equal elements do not swap past each other.
