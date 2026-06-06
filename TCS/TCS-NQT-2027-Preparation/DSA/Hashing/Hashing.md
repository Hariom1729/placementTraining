# Hashing & Hash Maps

## 1. Theory & Core Concepts

Hashing is a technique used to uniquely identify a specific object from a group of similar objects. In competitive programming and interviews, it is primarily used for **fast data retrieval** (lookups), counting frequencies, and storing visited states.

### Hash Tables vs Arrays
- If you need to count frequencies of numbers between `0` and `10^5`, you can use a simple array `freq[100000]`. This is called **Direct Hashing**.
- If the numbers can be very large (e.g., up to `10^9`) or if the keys are strings, you cannot use an array. You must use a **Hash Map** or **Hash Set**.

### C++ STL Maps and Sets

In C++, there are two primary types of Hash Maps/Sets based on their underlying data structure:

1. **`std::map` / `std::set` (Ordered)**
   - Implemented using a **Red-Black Tree** (Self-balancing Binary Search Tree).
   - Keys are stored in sorted order.
   - Time Complexity for Insert/Search/Delete: **`O(log N)`**.
   - Use when you need the keys to be sorted (e.g., printing frequencies in alphabetical order).

2. **`std::unordered_map` / `std::unordered_set` (Unordered)**
   - Implemented using a **Hash Table**.
   - Keys are stored in no particular order.
   - Time Complexity for Insert/Search/Delete: **`O(1)`** (Average case), **`O(N)`** (Worst case, due to collisions, though rare).
   - Use this 95% of the time in coding interviews because `O(1)` lookups are essential for optimal time complexity.

---

## 2. Common Patterns

1. **Counting Frequencies:** Using an `unordered_map<int, int>` to count how many times an element appears in an array.
2. **Finding Pairs (Two Sum):** Storing elements we've seen so far to instantly check if the complement `(target - current_element)` exists.
3. **Prefix Sum + Hashing:** A very powerful pattern for subarray problems (e.g., finding a subarray with sum `K`, or finding the longest subarray with sum `0`).

---

## 3. Problem List

*   `01_Count_Frequencies.md`
*   `02_Find_Highest_Lowest_Frequency.md`
*   `03_Two_Sum.md`
*   `04_Longest_Subarray_Given_Sum.md`
*   `05_Subarray_Sum_Equals_K.md`
