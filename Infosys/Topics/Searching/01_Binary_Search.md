# Binary Search

## Difficulty
Easy

## Asked In
Infosys DSE
Frequency: Very High

---

## Problem Statement
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with $O(\log N)$ runtime complexity.

---

## Input Format
- First line: `N`
- Second line: `N` space-separated sorted integers.
- Third line: `target`.

---

## Optimal Approach (Binary Search)
**Detailed explanation:**
Since the array is sorted, we don't need to check every element. We can check the middle element.
- If it is the target, we are done.
- If it is less than the target, we can discard the left half of the search space.
- If it is greater than the target, we can discard the right half.

**Complexity:**
- **Time Complexity:** $O(\log N)$
- **Space Complexity:** $O(1)$

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] < target) {
            left = mid + 1; // Discard left half
        }
        else {
            right = mid - 1; // Discard right half
        }
    }
    
    return -1; // Target not found
}
```

---

## Common Mistakes
- **Loop Condition:** Using `while (left < right)` instead of `while (left <= right)` will cause the loop to terminate prematurely, potentially missing the target if it happens to be at the exact `left == right` index.
- **Midpoint Overflow:** `(left + right) / 2` can overflow.

---

## Pattern Recognition
**Identify this when:** The problem mentions a "sorted array" and requires a $O(\log N)$ search time. Binary search isn't just for finding elements; it's heavily used in Infosys SP for "Binary Search on Answer" problems (like Koko Eating Bananas or Allocate Minimum Pages).
