# Problem 15: Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm that searches for a `target` value in an `m x n` integer `matrix`. The matrix has the following properties:
1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

## Input Format
- A 2D array of integers `matrix`.
- An integer `target`.

## Output Format
- A boolean representing whether the target is found.

## Constraints
- `1 <= m, n <= 300`

---

## Approach

Use a stair-case search starting from the **top-right corner** of the matrix.
1. Start at `row = 0`, `col = n - 1`.
2. If `matrix[row][col] == target`, return `true`.
3. If `matrix[row][col] > target`, target must be strictly left. Move left: `col--`.
4. If `matrix[row][col] < target`, target must be strictly below. Move down: `row++`.
5. If we step out of bounds, return `false`.

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
        
        int row = 0;
        int col = n - 1;
        
        while (row < m && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col--; 
            } else {
                row++; 
            }
        }
        return false;
    }
};
```
