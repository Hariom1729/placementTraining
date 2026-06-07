# Problem 4: Implement Merge Sort

## Problem Statement
Given an array `arr` of size `N`, sort the array in ascending order using the **Merge Sort** algorithm.

## Input Format
- An array of integers `arr`.

## Output Format
- The same array sorted in ascending order.

## Constraints
- `1 <= N <= 10^5`
- `0 <= arr[i] <= 10^9`

---

## Approach: Merge Sort

**Core Idea:** Divide and Conquer. Divide the array into two halves, recursively sort them, and then merge the two sorted halves.

1. **`mergeSort(arr, low, high)`:**
   - Base Condition: If `low >= high`, return.
   - Find `mid = low + (high - low) / 2`.
   - Recursively call `mergeSort(arr, low, mid)`.
   - Recursively call `mergeSort(arr, mid + 1, high)`.
   - Call `merge(arr, low, mid, high)`.
2. **`merge(arr, low, mid, high)`:**
   - Create a temporary array `temp`.
   - Use two pointers: `left = low` and `right = mid + 1`.
   - While `left <= mid` and `right <= high`, compare `arr[left]` and `arr[right]`. Push the smaller one into `temp` and increment the respective pointer.
   - If elements are left in the left half, push them all to `temp`.
   - If elements are left in the right half, push them all to `temp`.
   - Copy the elements from `temp` back into the original `arr` from index `low` to `high`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    void merge(vector<int>& arr, int low, int mid, int high) {
        vector<int> temp; 
        int left = low;      
        int right = mid + 1;   

        // Merge two sorted halves
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.push_back(arr[left]);
                left++;
            } else {
                temp.push_back(arr[right]);
                right++;
            }
        }

        // Copy remaining elements of left half
        while (left <= mid) {
            temp.push_back(arr[left]);
            left++;
        }

        // Copy remaining elements of right half
        while (right <= high) {
            temp.push_back(arr[right]);
            right++;
        }

        // Transfer from temporary vector to original array
        for (int i = low; i <= high; i++) {
            arr[i] = temp[i - low];
        }
    }

    void mergeSortHelper(vector<int>& arr, int low, int high) {
        if (low >= high) return; // Base case
        
        int mid = low + (high - low) / 2;
        mergeSortHelper(arr, low, mid);  // Sort left half
        mergeSortHelper(arr, mid + 1, high); // Sort right half
        merge(arr, low, mid, high);  // Merge them
    }

public:
    void mergeSort(vector<int>& arr) {
        mergeSortHelper(arr, 0, arr.size() - 1);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    sol.mergeSort(arr);
    
    cout << "Sorted Array: ";
    for (int x : arr) cout << x << " "; // Expected: 3 9 10 27 38 43 82
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N log N)` for Best, Worst, and Average cases. The array is always divided into half (`log N`) and merging takes linear time (`N`).
- **Space Complexity:** `O(N)`. We need a temporary array `temp` of size `N` to perform the merge operation.
- **Stability:** Stable.
