# Rotate Image

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, Apple

## Topic
Arrays (Matrix)

## Pattern
Matrix Transposition

## Problem Statement
You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90 degrees (clockwise)**.
You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

## Constraints
- $n == matrix.length == matrix[i].length$
- $1 \le n \le 20$
- $-1000 \le matrix[i][j] \le 1000$

## Input Format
- First line: `N`
- Next `N` lines: `N` space-separated integers.

## Output Format
- Return the matrix modified in-place.

## Sample Input
```
3
1 2 3
4 5 6
7 8 9
```

## Sample Output
```
7 4 1
8 5 2
9 6 3
```

## Edge Cases
- `n = 1` (Matrix with a single element remains unchanged).

## Approach 1
Brute Force (Using extra space)
**Explanation:** Allocate a new `n x n` matrix. Iterate over the original matrix and place `matrix[i][j]` into `new_matrix[j][n - 1 - i]`. Then copy the new matrix back into the original.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(N^2)$ (Fails the in-place requirement).

## Approach 2
Optimal Approach (Transpose + Reverse)
**Explanation:** 
A mathematically elegant way to rotate a square matrix by 90 degrees clockwise is to break it down into two simpler operations:
1. **Transpose the matrix:** Swap `matrix[i][j]` with `matrix[j][i]`. This turns rows into columns and columns into rows. (Make sure you only loop `j` from `i` to `n` to avoid double-swapping and putting elements back).
2. **Reverse each row:** Iterate through each row of the transposed matrix and reverse its elements (swap `matrix[i][left]` with `matrix[i][right]`).

**Dry Run:**
Original:
`1 2 3`
`4 5 6`
`7 8 9`

Step 1: Transpose (swap across diagonal):
`1 4 7`
`2 5 8`
`3 6 9`

Step 2: Reverse each row:
Row 0: Reverse `1 4 7` -> `7 4 1`
Row 1: Reverse `2 5 8` -> `8 5 2`
Row 2: Reverse `3 6 9` -> `9 6 3`

Final:
`7 4 1`
`8 5 2`
`9 6 3`

**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        // 1. Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // 2. Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;
            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
    }
}
```

## Python Solution
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # 1. Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. Reverse rows
        for i in range(n):
            matrix[i].reverse()
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // 1. Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // 2. Reverse rows
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

## Common Mistakes
- **Transposing incorrectly:** When transposing, the inner loop for `j` MUST start from `i`. If it starts from `0`, you will swap every element twice, effectively returning the matrix to its original state.
- **Rotating Counter-Clockwise instead of Clockwise:** 
  - To rotate 90 degrees *clockwise*: Transpose, then reverse rows.
  - To rotate 90 degrees *counter-clockwise*: Reverse rows, then transpose.

## Similar Questions
- Determine Whether Matrix Can Be Obtained By Rotation
- Spiral Matrix
