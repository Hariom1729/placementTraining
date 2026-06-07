# Problem 14: Search a 2D Matrix

## Problem Statement
You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.
You must write a solution in `O(log(m * n))` time complexity.

## Input Format
- A 2D array of integers `matrix`.
- An integer `target`.

## Output Format
- A boolean representing whether the target is found.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`

---

## Approach

If we flatten this 2D matrix into a 1D array, it would be strictly sorted.
We map the 1D indices `[0` to `(m*n)-1]` to 2D coordinates: `row = i / columns`, `col = i % columns`.
1. Set `low = 0` and `high = (m * n) - 1`.
2. Do standard Binary Search.
3. Access the element using `matrix[mid / n][mid % n]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int low = 0;
        int high = m * n - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            int row = mid / n;
            int col = mid % n;
            
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
};
```
