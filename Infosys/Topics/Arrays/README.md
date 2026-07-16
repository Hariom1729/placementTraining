# Arrays

## Introduction
Arrays form the bedrock of almost every online assessment. In Infosys SP (Specialist Programmer) and DSE (Digital Specialist Engineer) rounds, array problems are heavily tested in Round 1 and Round 2. You will rarely see a simple "traverse the array" problem; instead, they focus heavily on optimization patterns.

## Important Concepts
- Subarrays and Subsequences
- In-place modifications (O(1) space)
- Precomputation (Prefix Arrays, Suffix Arrays)
- 2D Arrays (Matrix Traversals)
- Hashing within Arrays

## Pattern Classification
- **Prefix Sum:** Used when querying sums of subarrays repeatedly.
- **Kadane's Algorithm:** Used for finding maximum/minimum contiguous subarray sum.
- **Sliding Window:** Used when finding the longest/shortest subarray matching a condition.
- **Two Pointers:** Used when array is sorted or when swapping opposite ends.
- **Dutch National Flag:** Three-way partitioning (e.g. Sort Colors).

## Time Complexity Table
| Operation | Complexity | Note |
| :--- | :--- | :--- |
| Access | O(1) | Random access via index |
| Search (Unsorted) | O(N) | Linear scan |
| Search (Sorted) | O(log N) | Binary Search |
| Insertion / Deletion | O(N) | Shifting elements |
| Sort | O(N log N) | Standard sort |

## Space Complexity Table
| Approach | Complexity | Note |
| :--- | :--- | :--- |
| In-place Swap | O(1) | Optimal for interviews |
| Hash Map (Frequency) | O(N) | Trading space for time |
| Prefix Array | O(N) | Storing cumulative states |

## Interview Tips
1. **Always ask about constraints:** If $N \le 10^5$, an $O(N^2)$ solution will fail.
2. **Beware of Integer Overflow:** If calculating products or sums, switch to `long` in Java/C++ or Python natively handles it.
3. **In-place requirement:** Look for swaps or negating values if $O(1)$ space is requested.

## Most Repeated Infosys Patterns
1. Prefix Sum + Hash Map (for subarray sums with negatives)
2. Kadane's Algorithm
3. Interval Merging
4. Cycle Sort (Missing numbers)
5. Greedy Array Traversals (Jump Game)

## Preparation Order
1. Two Pointers & Basic Traversals
2. Prefix & Suffix Arrays
3. Hash Map Frequency Counting
4. Kadane's & Subarrays
5. Intervals & Sorting
6. Matrices (2D Arrays)

## Revision Checklist
- [ ] Can you implement Binary Search perfectly?
- [ ] Do you know how to rotate a 2D matrix in-place?
- [ ] Can you apply Kadane's algorithm?
- [ ] Do you understand why Prefix Sum + Hash Map is used for negative numbers?

## List of All Problems

| No | Problem | Difficulty |
|----|----------|------------|
| 01 | Two Sum | Medium |
| 02 | Product of Array Except Self | Medium |
| 03 | Maximum Subarray | Medium |
| 04 | Merge Intervals | Medium |
| 05 | Next Permutation | Medium-Hard |
| 06 | Minimum Number of Jumps | Hard |
| 07 | Missing Number | Easy |
| 08 | Rotate Array | Easy |
| 09 | Second Largest | Easy |
| 10 | Find the Duplicate Number | Medium |
| 11 | Subarray Sum Equals K | Medium |
| 12 | Trapping Rain Water | Hard |
| 13 | Search in Rotated Sorted Array | Medium |
| 14 | Longest Consecutive Sequence | Medium |
| 15 | Spiral Matrix | Medium |
| 16 | Set Matrix Zeroes | Medium |
| 17 | Majority Element | Medium |
| 18 | 3Sum | Medium |
| 19 | Container With Most Water | Medium |
| 20 | Subarray Sums Divisible by K | Medium |
| 21 | Jump Game I | Medium |
| 22 | Sort Colors | Medium |
| 23 | Insert Interval | Medium |
| 24 | Next Greater Element III | Medium-Hard |
| 25 | Best Time to Buy and Sell Stock | Medium |
| 26 | Maximum Product Subarray | Medium-Hard |
| 27 | Find Minimum in Rotated Sorted Array | Medium |
| 28 | Non-overlapping Intervals | Medium |
| 29 | Meeting Rooms II | Medium-Hard |
| 30 | First Missing Positive | Hard |
| 31 | Range Sum Query 2D | Medium-Hard |
| 32 | Sliding Window Maximum | Hard |
| 33 | Find All Duplicates in an Array | Medium |
| 34 | Rotate Image | Medium |
| 35 | Kth Largest Element in an Array | Medium |
| 36 | Top K Frequent Elements | Medium |
| 37 | Subsets | Medium |
| 38 | Subsets II | Medium |
| 39 | Valid Sudoku | Medium |
| 40 | Minimum Size Subarray Sum | Medium |
