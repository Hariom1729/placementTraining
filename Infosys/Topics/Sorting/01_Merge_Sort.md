# Merge Sort

## Difficulty
Medium

## Asked In
Infosys SP
Year: 2020, 2023
Frequency: High

---

## Problem Statement
Given an array of integers `nums`, sort the array in ascending order using the Merge Sort algorithm and return it.
You must solve the problem without using any built-in functions in $O(N \log N)$ time complexity.

---

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

---

## Output Format
- Return the sorted array.

---

## Constraints
- $1 \le nums.length \le 5 \times 10^4$
- $-5 \times 10^4 \le nums[i] \le 5 \times 10^4$

---

## Optimal Approach (Divide and Conquer)
**Detailed explanation:**
Merge Sort is a classic Divide and Conquer algorithm.
1. **Divide:** Find the midpoint of the array and recursively split it into two halves until each half contains a single element.
2. **Conquer/Merge:** Merge the two sorted halves back together by using two pointers to compare elements from both halves and placing the smaller element into a temporary array.

**Complexity:**
- **Time Complexity:** $O(N \log N)$ in all cases (Worst, Average, Best).
- **Space Complexity:** $O(N)$ for the temporary array during merging.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Create temporary vectors
    vector<int> L(n1), R(n2);
    
    // Copy data to temp vectors
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    
    // Merge the temp vectors back into arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Copy remaining elements
    while (i < n1) {
        arr[k] = L[i];
        i++; k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++; k++;
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

vector<int> sortArray(vector<int>& nums) {
    mergeSort(nums, 0, nums.size() - 1);
    return nums;
}
```

---

## Common Mistakes
- **Midpoint calculation overflow:** Always use `mid = left + (right - left) / 2` instead of `(left + right) / 2` to prevent integer overflow.
- **Base case:** Forgetting `if (left >= right) return;` leads to infinite recursion.

---

## Interview Tips
- Mention that Merge Sort is a **stable** sort (maintains the relative order of equal elements), whereas Quick Sort is typically unstable. This is why Java's `Arrays.sort` uses a variant of Merge Sort for Objects.
