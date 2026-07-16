# Range Sum Query 2D - Immutable

## Difficulty
Medium-Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Related Companies: Amazon, Google, Palantir

## Topic
Arrays (Matrix)

## Pattern
2D Prefix Sum

## Problem Statement
Given a 2D matrix `matrix`, handle multiple queries of the following type:
- Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

Implement the `NumMatrix` class:
- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

You must design an algorithm where `sumRegion` works on $O(1)$ time complexity.

## Constraints
- $m == matrix.length$
- $n == matrix[i].length$
- $1 \le m, n \le 200$
- $-10^4 \le matrix[i][j] \le 10^4$
- $0 \le row1 \le row2 < m$
- $0 \le col1 \le col2 < n$
- At most $10^4$ calls will be made to `sumRegion`.

## Input Format
- This is a system design/class implementation question.

## Edge Cases
- Rectangle is a single cell (`row1 == row2` and `col1 == col2`).
- Rectangle touches the top or left borders of the matrix (where index-out-of-bounds errors usually occur).

## Approach 1
Brute Force
**Explanation:** For every `sumRegion` call, iterate over the sub-grid from `row1` to `row2` and `col1` to `col2`, adding the elements.
**Time Complexity:** Constructor is $O(1)$. `sumRegion` is $O(M \times N)$.
**Space Complexity:** $O(1)$.
*Note: Fails the $O(1)$ time requirement for queries.*

## Approach 2
Optimal Approach (2D Prefix Sum)
**Explanation:** 
We can precompute the sum of the rectangle from the top-left corner `(0,0)` to every cell `(i,j)`. Let's call this `prefix[i][j]`.
To construct the 2D prefix array easily without bounds checking, we allocate it as `prefix[m+1][n+1]` with an extra row and column of zeros.
- `prefix[r+1][c+1] = matrix[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]`
  - Meaning: Current cell + Sum above + Sum to the left - Sum of the top-left diagonal (which was added twice).

To query any rectangle from `(r1, c1)` to `(r2, c2)` in $O(1)$ time:
- `Sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`
  - Meaning: Total sum from `(0,0)` to `(r2,c2)`, minus the rectangle sitting directly above it, minus the rectangle sitting directly to the left, plus the top-left corner which was subtracted twice.

**Time Complexity:** Constructor is $O(M \times N)$ for precomputation. `sumRegion` is $O(1)$.
**Space Complexity:** $O(M \times N)$ for the prefix sum matrix.

## Java Solution
```java
class NumMatrix {
    private int[][] prefix;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        
        int m = matrix.length;
        int n = matrix[0].length;
        prefix = new int[m + 1][n + 1];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1];
    }
}
```

## Python Solution
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                self.prefix[i + 1][j + 1] = (matrix[i][j] 
                                           + self.prefix[i][j + 1] 
                                           + self.prefix[i + 1][j] 
                                           - self.prefix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] 
              - self.prefix[row1][col2 + 1] 
              - self.prefix[row2 + 1][col1] 
              + self.prefix[row1][col1])
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class NumMatrix {
private:
    vector<vector<int>> prefix;
    
public:
    NumMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return;
        
        int m = matrix.size();
        int n = matrix[0].size();
        prefix = vector<vector<int>>(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1];
    }
};
```

## Common Mistakes
- **Not padding the array:** If you construct the prefix array with size `[m][n]`, you will be forced to write 4 separate `if` conditions inside your loops and `sumRegion` function to prevent Out Of Bounds exceptions when `row1 == 0` or `col1 == 0`. Constructing `prefix[m+1][n+1]` with zeroes completely bypasses all bounds-checking logic and makes the code beautifully concise.

## Similar Questions
- Range Sum Query - Immutable (1D Array)
