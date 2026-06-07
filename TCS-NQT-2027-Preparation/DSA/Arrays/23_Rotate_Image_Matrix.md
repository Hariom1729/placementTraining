# Problem 23: Rotate Image (Matrix) by 90 Degrees

## Problem Statement
You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

## Input Format
- An `n x n` 2D array of integers `matrix`.

## Output Format
- The `matrix` modified in-place.

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## Approach

The most mathematical and optimal way to rotate an `n x n` matrix by 90 degrees clockwise in-place is to perform two operations:
1. **Transpose the Matrix:** Swap `matrix[i][j]` with `matrix[j][i]`. This turns rows into columns.
2. **Reverse each Row:** Iterate through each row and reverse its elements using `std::reverse`.

*(Note: If you needed to rotate counter-clockwise, you would first reverse every row, and THEN transpose).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // Step 1: Transpose the matrix
        for (int i = 0; i < n; i++) {
            // j starts from i to avoid swapping twice and undoing the transpose
            for (int j = i; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};

int main() {
    Solution sol;
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    sol.rotate(matrix);
    
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    // Expected output:
    // 7 4 1
    // 8 5 2
    // 9 6 3
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` where `N` is the number of rows/columns. Transposing takes roughly `N^2/2` operations, and reversing takes `N^2/2`. Total is `O(N^2)`.
- **Space Complexity:** `O(1)`. All operations are performed in-place.
