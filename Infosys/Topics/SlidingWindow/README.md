# Sliding Window

This module covers the **Sliding Window** technique, an essential algorithmic pattern derived from Two Pointers. It is heavily tested in Infosys SP and DSE rounds because it is the most efficient way to solve problems involving contiguous subarrays or substrings, reducing time complexities from $O(N^2)$ to $O(N)$.

## Key Patterns
- **Fixed Size Window:** The window size `k` remains constant. You add one element to the right and remove one from the left at every step. (e.g., Maximum Average Subarray).
- **Variable Size Window:** The window expands and contracts dynamically based on a condition. You expand the `right` pointer to gather elements, and when a condition is broken, you shrink the `left` pointer until the condition is met again. (e.g., Longest Substring Without Repeating Characters).
- **Count/Frequency Maps:** Often combined with hash maps or frequency arrays to track characters inside the current window (e.g., Minimum Window Substring).

## Table of Contents
1. Maximum Average Subarray I (Fixed Window)
2. Max Consecutive Ones III (Variable Window)
3. Longest Substring Without Repeating Characters (Variable Window)
4. Longest Repeating Character Replacement (Variable Window)
5. Minimum Window Substring (Hard Variable Window)
... (More to come)
