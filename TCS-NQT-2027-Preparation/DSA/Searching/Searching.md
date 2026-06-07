# Searching in Data Structures & Algorithms

## 1. Theory & Core Concepts

Searching algorithms are designed to retrieve an element from any data structure where it is stored. In competitive programming and interviews (like TCS NQT), searching is almost always synonymous with **Binary Search** and its variations.

### Linear Search vs. Binary Search

| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Pre-requisite** | None. Array can be unsorted. | Array **must** be sorted. |
| **Time Complexity** | `O(N)` | `O(log N)` |
| **Space Complexity** | `O(1)` | `O(1)` (Iterative) / `O(log N)` (Recursive) |
| **Mechanism** | Checks every element one by one. | Divides the search space in half repeatedly. |

### The Binary Search Algorithm

The standard Binary Search algorithm works as follows:
1. Define a search space `[low, high]`. Initially, `low = 0` and `high = N - 1`.
2. Find the middle element `mid = low + (high - low) / 2`. *(Note: using this formula prevents integer overflow compared to `(low + high) / 2`)*.
3. If `arr[mid] == target`, you found it!
4. If `arr[mid] < target`, the target must be to the right. Update `low = mid + 1`.
5. If `arr[mid] > target`, the target must be to the left. Update `high = mid - 1`.
6. Repeat until `low > high`.

---

## 2. Common Patterns in Searching Problems

In TCS Ninja and Digital interviews, direct Binary Search is rarely asked. Instead, they ask questions where the search space is hidden or modified.

1. **Standard Binary Search on Arrays:** E.g., Find an element, find First/Last occurrence.
2. **Binary Search on Answer:** E.g., Allocate Minimum Number of Pages, Aggressive Cows, Koko Eating Bananas. This is a very common **TCS Digital/Prime** pattern. You apply binary search on the *range of possible answers* rather than indices.
3. **Binary Search on Rotated Arrays:** E.g., Search in a Rotated Sorted Array, Find Minimum in Rotated Sorted Array.
4. **Binary Search on 2D Matrices:** E.g., Search a 2D Matrix.

---

## 3. C++ STL for Searching

In C++, you don't always need to write Binary Search from scratch. The Standard Template Library (`<algorithm>`) provides highly optimized functions:

*   `binary_search(arr.begin(), arr.end(), target)`: Returns `true` if target is present, `false` otherwise. Time: `O(log N)`.
*   `lower_bound(arr.begin(), arr.end(), target)`: Returns an iterator to the **first element which does not evaluate to less than** target (i.e. `x >= target`).
*   `upper_bound(arr.begin(), arr.end(), target)`: Returns an iterator to the **first element which evaluates to greater than** target (i.e. `x > target`).

---

## 4. Problem List

*   `01_Binary_Search.md`
*   `02_Lower_Bound.md`
*   `03_Upper_Bound.md`
*   `04_Search_Insert_Position.md`
*   `05_First_and_Last_Occurrence.md`
