# Problem 3: Implement Insertion Sort

## Problem Statement
Given an array `arr` of size `N`, sort the array in ascending order using the **Insertion Sort** algorithm.

## Input Format
- An array of integers `arr`.

## Output Format
- The same array sorted in ascending order.

## Constraints
- `1 <= N <= 1000`
- `0 <= arr[i] <= 10^5`

---

## Approach: Insertion Sort

**Core Idea:** Builds the final sorted array one item at a time. It works the way you sort playing cards in your hands.

1. Assume the first element (`arr[0]`) is already sorted.
2. Start an outer loop `i` from `1` to `N-1`. This is the element we want to "insert" into the sorted part.
3. Save `arr[i]` into a temporary variable (let's call it `key` or just swap).
4. Run an inner loop `j` starting from `i` down to `1`.
5. As long as `j > 0` and `arr[j-1] > arr[j]`, swap them to shift the larger element to the right.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void insertionSort(vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 1; i < n; i++) {
            int j = i;
            
            // Shift elements to the right to create position for insertion
            while (j > 0 && arr[j - 1] > arr[j]) {
                swap(arr[j - 1], arr[j]);
                j--;
            }
        }
    }
};

int main() {
    Solution sol;
    vector<int> arr = {12, 11, 13, 5, 6};
    sol.insertionSort(arr);
    
    cout << "Sorted Array: ";
    for (int x : arr) cout << x << " "; // Expected: 5 6 11 12 13
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** 
  - **Worst & Average Case:** `O(N^2)` (Array is reverse sorted).
  - **Best Case:** `O(N)` (Array is already sorted, the `while` loop never executes).
- **Space Complexity:** `O(1)`. In-place sorting.
- **Stability:** Stable. Equal elements do not cross each other.
