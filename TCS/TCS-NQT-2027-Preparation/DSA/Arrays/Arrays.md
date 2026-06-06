# Arrays in Data Structures & Algorithms

## 1. Theory & Core Concepts

An **Array** is a linear data structure that stores a collection of elements of the same data type in contiguous memory locations. Because the memory addresses are contiguous, we can easily calculate the address of any element using its index.

### Key Characteristics:
- **Fixed Size:** In C++, the size of a standard array (`int arr[10];`) is fixed at the time of declaration. 
- **Dynamic Arrays:** C++ provides `std::vector` from the STL (Standard Template Library), which automatically resizes itself when elements are added or removed.
- **Zero-Indexed:** The first element is at index `0`.
- **Random Access:** You can access any element in `O(1)` time using its index.

### Memory Allocation:
- In C++, static arrays (e.g., inside a function) are allocated on the stack, while dynamic arrays (`new int[10]`) or vectors are allocated on the heap.
- Because elements are contiguous, arrays are highly cache-friendly.

---

## 2. Complexity Analysis

| Operation | Best Case | Average Case | Worst Case | Space Complexity |
| :--- | :---: | :---: | :---: | :---: |
| **Accessing Element** | `O(1)` | `O(1)` | `O(1)` | `O(1)` |
| **Searching (Unsorted)** | `O(1)` | `O(N)` | `O(N)` | `O(1)` |
| **Searching (Sorted - Binary)** | `O(1)` | `O(log N)` | `O(log N)` | `O(1)` |
| **Insertion (At End)** | `O(1)` | `O(1)` amortized | `O(N)` | `O(1)` |
| **Insertion (At Beginning)** | `O(N)` | `O(N)` | `O(N)` | `O(1)` |
| **Deletion (At End)** | `O(1)` | `O(1)` | `O(1)` | `O(1)` |
| **Deletion (At Beginning)** | `O(N)` | `O(N)` | `O(N)` | `O(1)` |

---

## 3. Common Patterns in Array Problems

When preparing for TCS NQT (Ninja/Digital/Prime), almost every array problem falls into one of these patterns:

1. **Two Pointers:** Used heavily for sorted arrays (e.g., Two Sum) or for operations at both ends.
2. **Sliding Window:** Used for problems asking for "maximum/minimum/longest/shortest contiguous subarray".
3. **Prefix Sum / Suffix Sum:** Used for fast range queries.
4. **Hashing (`std::unordered_map` / `std::unordered_set`):** Used when we need to check for frequencies, duplicates, or find complements in `O(1)` average time.
5. **Kadane’s Algorithm:** The standard approach for the "Maximum Subarray Sum" problem.
6. **Dutch National Flag Algorithm:** Used for sorting arrays containing only 3 distinct elements.
7. **Tortoise and Hare (Floyd’s Cycle Detection):** Used in arrays where values point to indexes.

---

## 4. Problem List

To keep study materials organized and easy to digest, each coding problem has been placed into its own dedicated Markdown file.

*   `01_Largest_Element.md`
*   `02_Second_Largest_Element.md`
*   `03_Check_Array_Sorted.md`
*   `04_Remove_Duplicates.md`
*   `05_Left_Rotate_One_Place.md`
*(...and more)*
