# Problem 1: Implement Selection Sort

## Problem Statement
Given an array `arr` of size `N`, sort the array in ascending order using the **Selection Sort** algorithm.

## Input Format
- An array of integers `arr`.

## Output Format
- The same array sorted in ascending order.

## Constraints
- `1 <= N <= 1000`
- `0 <= arr[i] <= 10^5`

---

## Approach: Selection Sort

**Core Idea:** Repeatedly find the minimum element from the unsorted part and put it at the beginning.

1. The array has two parts: a sorted subarray (built up from left to right) and an unsorted subarray (the rest).
2. Start with an outer loop `i` from `0` to `N-2` (representing the position we want to fill with the minimum).
3. Assume `arr[i]` is the minimum. Set `minIndex = i`.
4. Start an inner loop `j` from `i+1` to `N-1` to search the unsorted part.
5. If `arr[j] < arr[minIndex]`, update `minIndex = j`.
6. After the inner loop, swap `arr[i]` with `arr[minIndex]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void selectionSort(vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in unsorted array
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // Swap the found minimum element with the first element
            if (minIndex != i) {
                swap(arr[i], arr[minIndex]);
            }
        }
    }
};

int main() {
    Solution sol;
    vector<int> arr = {64, 25, 12, 22, 11};
    sol.selectionSort(arr);
    
    cout << "Sorted Array: ";
    for (int x : arr) cout << x << " "; // Expected: 11 12 22 25 64
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` for all cases (Best, Worst, and Average). We do `N` scans regardless of whether the array is sorted or not.
- **Space Complexity:** `O(1)`. In-place sorting.
- **Stability:** Not Stable. Swapping can change the relative order of identical elements.
