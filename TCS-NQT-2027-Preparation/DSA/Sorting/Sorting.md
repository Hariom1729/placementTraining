# Sorting Algorithms

## 1. Theory & Core Concepts

Sorting is the process of arranging elements in a specific order (usually ascending or descending). In competitive programming and interviews, knowing how to sort is essential, but knowing the *mechanics* of sorting algorithms is a frequent topic in objective tests and technical interviews.

There are broadly two categories of sorting algorithms you must know for TCS NQT:
1.  **`O(N^2)` Algorithms:** Selection Sort, Bubble Sort, Insertion Sort. (Useful for small datasets, but generally slow).
2.  **`O(N log N)` Algorithms:** Merge Sort, Quick Sort, Heap Sort. (Efficient algorithms used in standard library functions).

### Stability in Sorting
A sorting algorithm is **stable** if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.
*   **Stable:** Merge Sort, Insertion Sort, Bubble Sort.
*   **Unstable:** Quick Sort, Selection Sort, Heap Sort.

### In-Place Sorting
An **in-place** sorting algorithm requires only `O(1)` extra space (or `O(log N)` for recursive call stacks).
*   **In-Place:** Quick Sort, Selection Sort, Bubble Sort, Insertion Sort, Heap Sort.
*   **Out-of-Place:** Merge Sort (requires `O(N)` auxiliary array).

---

## 2. C++ STL for Sorting

In 99% of actual coding problems, you will NOT implement these algorithms from scratch. You will use the C++ Standard Template Library (`<algorithm>`):

*   `sort(arr.begin(), arr.end());` -> Sorts in ascending order in `O(N log N)`. Under the hood, C++ uses **IntroSort** (a hybrid of Quick Sort, Heap Sort, and Insertion Sort).
*   `sort(arr.begin(), arr.end(), greater<int>());` -> Sorts in descending order.

### Custom Comparators
When sorting pairs or complex objects, you write a custom comparator function:
```cpp
bool compare(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) return a.second > b.second;
    return a.first < b.first;
}
// Usage: sort(arr.begin(), arr.end(), compare);
```

---

## 3. Problem List (Algorithm Implementations)

*   `01_Selection_Sort.md`
*   `02_Bubble_Sort.md`
*   `03_Insertion_Sort.md`
*   `04_Merge_Sort.md`
*   `05_Quick_Sort.md`
