# Problem 22: Set Matrix Zeros

## Problem Statement
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.
You must do it in place.

## Input Format
- A 2D array (vector of vectors) of integers `matrix`.

## Output Format
- The `matrix` modified in-place.

## Constraints
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## Approach

**Optimal Approach (O(1) space):**
We can use the first row and first column of the matrix itself to keep track of which rows and columns need to be zeroed.
1. We need one extra variable, `col0 = 1`, to track if the first column needs to be zeroed (since `matrix[0][0]` will represent the first row).
2. **First pass:** Iterate through the matrix. If `matrix[i][j] == 0`:
   - Set `matrix[i][0] = 0` (marking the row).
   - If `j == 0`, set `col0 = 0`. Else, set `matrix[0][j] = 0` (marking the column).
3. **Second pass:** Iterate backwards from the bottom-right `(m-1, n-1)` to `(0, 1)` (skipping the first row and col for now).
   - If either `matrix[i][0] == 0` OR `matrix[0][j] == 0`, set `matrix[i][j] = 0`.
4. **Fix first row:** If `matrix[0][0] == 0`, set the entire first row to 0.
5. **Fix first column:** If `col0 == 0`, set the entire first column to 0.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int col0 = 1, rows = matrix.size(), cols = matrix[0].size();

        for (int i = 0; i < rows; i++) {
            if (matrix[i][0] == 0) col0 = 0;
            for (int j = 1; j < cols; j++)
                if (matrix[i][j] == 0)
                    matrix[i][0] = matrix[0][j] = 0;
        }

        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 1; j--)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            if (col0 == 0) matrix[i][0] = 0;
        }
    }
};

int main() {
    Solution sol;
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };
    
    sol.setZeroes(matrix);
    
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    // Expected output:
    // 1 0 1
    // 0 0 0
    // 1 0 1
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M)` where `N` is rows and `M` is columns. We traverse the matrix roughly twice.
- **Space Complexity:** `O(1)`. All markings are done inside the input matrix itself.
