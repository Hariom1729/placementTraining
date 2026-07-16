# Sorting

This module covers **Sorting Algorithms** and **Sorting-Based Techniques**. While you rarely need to implement sorting algorithms from scratch in modern production code, Infosys SP and DSE rounds frequently test your understanding of:

- $O(N \log N)$ sorting foundations (Merge Sort, Quick Sort)
- $O(N)$ sorting foundations (Counting Sort, Bucket Sort)
- Custom comparators
- Using sorting as a prerequisite step for Two Pointers, Greedy algorithms, or interval merging

## Key Concepts
- **Stability:** A stable sort preserves the relative order of equal elements. (Merge Sort is stable, Quick Sort is usually not).
- **In-Place:** Uses $O(1)$ or $O(\log N)$ extra space. (Quick Sort is in-place, Merge Sort is not).
- **Custom Sort (`std::sort` in C++):** You must be extremely comfortable writing lambda comparators to sort complex objects.

## Table of Contents
1. Merge Sort (Foundation)
2. Quick Sort (Foundation)
3. Sort Colors (Dutch National Flag Algorithm)
4. Kth Largest Element in an Array (Quickselect)
5. Top K Frequent Elements (Bucket Sort)
... (More to come)
