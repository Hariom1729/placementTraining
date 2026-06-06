# Problem 5: Implement Quick Sort

## Problem Statement
Given an array `arr` of size `N`, sort the array in ascending order using the **Quick Sort** algorithm.

## Input Format
- An array of integers `arr`.

## Output Format
- The same array sorted in ascending order.

## Constraints
- `1 <= N <= 10^5`
- `0 <= arr[i] <= 10^9`

---

## Approach: Quick Sort

**Core Idea:** Divide and Conquer. Pick a "pivot" element, place it in its correct sorted position, and partition the array around it (smaller elements to the left, larger to the right). Recursively do this for the left and right subarrays.

1. **`quickSort(arr, low, high)`:**
   - Base Condition: If `low >= high`, return.
   - Call `partitionIndex = partition(arr, low, high)`.
   - Recursively call `quickSort(arr, low, partitionIndex - 1)`.
   - Recursively call `quickSort(arr, partitionIndex + 1, high)`.
2. **`partition(arr, low, high)`:**
   - Choose the first element as the `pivot = arr[low]`.
   - Use two pointers: `i = low` and `j = high`.
   - Loop `while (i < j)`:
     - Increment `i` as long as `arr[i] <= pivot` and `i <= high - 1`.
     - Decrement `j` as long as `arr[j] > pivot` and `j >= low + 1`.
     - If `i < j`, swap `arr[i]` and `arr[j]`.
   - Swap `arr[low]` (the pivot) with `arr[j]`. Now the pivot is in its correct place.
   - Return `j`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int partition(vector<int>& arr, int low, int high) {
        int pivot = arr[low];
        int i = low;
        int j = high;

        while (i < j) {
            // Find the first element greater than the pivot
            while (arr[i] <= pivot && i <= high - 1) {
                i++;
            }
            // Find the first element smaller than or equal to the pivot
            while (arr[j] > pivot && j >= low + 1) {
                j--;
            }
            // Swap if they haven't crossed
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }
        
        // Put the pivot in its correct sorted position
        swap(arr[low], arr[j]);
        return j; // Return the partition index
    }

    void quickSortHelper(vector<int>& arr, int low, int high) {
        if (low < high) {
            int partitionIndex = partition(arr, low, high);
            quickSortHelper(arr, low, partitionIndex - 1);
            quickSortHelper(arr, partitionIndex + 1, high);
        }
    }

public:
    void quickSort(vector<int>& arr) {
        quickSortHelper(arr, 0, arr.size() - 1);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {10, 80, 30, 90, 40, 50, 70};
    sol.quickSort(arr);
    
    cout << "Sorted Array: ";
    for (int x : arr) cout << x << " "; // Expected: 10 30 40 50 70 80 90
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:**
  - **Average & Best Case:** `O(N log N)`.
  - **Worst Case:** `O(N^2)` (Occurs when the array is already sorted or reverse sorted, and we pick the first element as pivot. Choosing a random pivot prevents this).
- **Space Complexity:** `O(log N)` auxiliary space for the recursive call stack. In-place sorting.
- **Stability:** Unstable.
