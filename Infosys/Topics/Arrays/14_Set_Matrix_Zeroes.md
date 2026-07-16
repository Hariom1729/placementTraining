# Set Matrix Zeroes

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Microsoft, Amazon, Bloomberg

## Topic
Arrays (Matrix)

## Pattern
In-place Hashing / State Maintenance

## Problem Statement
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.
You must do it **in-place**.

## Constraints
- $m == matrix.length$
- $n == matrix[0].length$
- $1 \le m, n \le 200$
- $-2^{31} \le matrix[i][j] \le 2^{31} - 1$

## Input Format
- First line: `M N`
- Next `M` lines: `N` space-separated integers.

## Output Format
- Return the modified matrix.

## Sample Input
```
3 3
1 1 1
1 0 1
1 1 1
```

## Sample Output
```
1 0 1
0 0 0
1 0 1
```

## Edge Cases
- The very first element `matrix[0][0]` is 0.
- Multiple zeros in the same row/col.

## Approach 1
Brute Force
**Explanation:** When encountering a `0`, replace the row and column with a special placeholder value (e.g., `-1000000`). Then do a second pass to convert all placeholders to `0`. (Requires knowing a safe placeholder not in the matrix).
**Time Complexity:** $O((M \times N) \times (M + N))$
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Auxiliary Arrays)
**Explanation:** Keep two arrays, `row[M]` and `col[N]`. If `matrix[i][j] == 0`, mark `row[i] = 1` and `col[j] = 1`. Do a second pass over the matrix, and if `row[i]` or `col[j]` is 1, set `matrix[i][j] = 0`.
**Complexity:** $O(M \times N)$ time, $O(M + N)$ space.

## Approach 3
Optimal Approach (In-place using first row/col)
**Explanation:** 
Use the first row and first column of the matrix itself to act as the auxiliary `row` and `col` tracking arrays.
1. Determine if the first row and first column themselves contain any zeros. Store this in two boolean variables `firstRowZero` and `firstColZero`.
2. Iterate over the matrix from `i=1` and `j=1`. If `matrix[i][j] == 0`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`.
3. Iterate again from `i=1` and `j=1`. If either `matrix[i][0] == 0` or `matrix[0][j] == 0`, set `matrix[i][j] = 0`.
4. Finally, if `firstColZero` is true, zero out the first column. If `firstRowZero` is true, zero out the first row.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) firstColZero = true;
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) firstRowZero = true;
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        if (firstColZero) {
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }
        if (firstRowZero) {
            for (int j = 0; j < n; j++) matrix[0][j] = 0;
        }
    }
}
```

## Python Solution
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        bool firstRowZero = false;
        bool firstColZero = false;
        
        for(int i = 0; i < m; i++) if(matrix[i][0] == 0) firstColZero = true;
        for(int j = 0; j < n; j++) if(matrix[0][j] == 0) firstRowZero = true;
        
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        if(firstColZero) {
            for(int i = 0; i < m; i++) matrix[i][0] = 0;
        }
        if(firstRowZero) {
            for(int j = 0; j < n; j++) matrix[0][j] = 0;
        }
    }
};
```

## Common Mistakes
- **Polluting `matrix[0][0]`:** If you use a single variable for `matrix[0][0]`, you merge the state of `firstRowZero` and `firstColZero`, which causes the entire first row to become zero just because the first column had a zero. Separate booleans are cleaner and error-proof.

## Similar Questions
- Game of Life
- Number of Islands
