# Spiral Matrix

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Microsoft, Amazon, Apple

## Topic
Arrays (Matrix)

## Pattern
Simulation / Matrix Traversal

## Problem Statement
Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

## Constraints
- $m == matrix.length$
- $n == matrix[i].length$
- $1 \le m, n \le 10$
- $-100 \le matrix[i][j] \le 100$

## Input Format
- First line: `M N` (Rows and Columns)
- Next `M` lines: Each containing `N` space-separated integers.

## Output Format
- Return a 1D array/list of integers in spiral order.

## Sample Input
```
3 3
1 2 3
4 5 6
7 8 9
```

## Sample Output
```
1 2 3 6 9 8 7 4 5
```

## Edge Cases
- $1 \times 1$ matrix.
- Single row or single column matrices (e.g., $1 \times N$ or $M \times 1$).

## Approach 1
Optimal Approach (Layer-by-Layer Simulation)
**Explanation:** 
We use four boundary pointers: `top`, `bottom`, `left`, and `right`.
We loop until the boundaries cross:
1. Traverse from `left` to `right` along the `top` row. Increment `top`.
2. Traverse from `top` to `bottom` along the `right` column. Decrement `right`.
3. Check if `top <= bottom`. If so, traverse from `right` to `left` along the `bottom` row. Decrement `bottom`.
4. Check if `left <= right`. If so, traverse from `bottom` to `top` along the `left` column. Increment `left`.

**Dry Run:**
Matrix:
`1 2 3`
`4 5 6`
`7 8 9`
- `top=0, bottom=2, left=0, right=2`
- Step 1: Add (0,0), (0,1), (0,2) -> `[1,2,3]`. `top = 1`.
- Step 2: Add (1,2), (2,2) -> `[1,2,3,6,9]`. `right = 1`.
- Step 3 (bottom): Add (2,1), (2,0) -> `[...9,8,7]`. `bottom = 1`.
- Step 4 (left): Add (1,0) -> `[...7,4]`. `left = 1`.
- Loop again: `top=1, bottom=1, left=1, right=1`.
- Step 1: Add (1,1) -> `[...4,5]`. `top = 2`.
- `top > bottom`. Loop terminates.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(1)$ auxiliary (excluding the output array).

## Java Solution
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return result;
        
        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;
        
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;
            
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }
            
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }
        
        return result;
    }
}
```

## Python Solution
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.empty()) return res;
        
        int top = 0, bottom = matrix.size() - 1;
        int left = 0, right = matrix[0].size() - 1;
        
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) res.push_back(matrix[top][i]);
            top++;
            
            for (int i = top; i <= bottom; i++) res.push_back(matrix[i][right]);
            right--;
            
            if (top <= bottom) {
                for (int i = right; i >= left; i--) res.push_back(matrix[bottom][i]);
                bottom--;
            }
            
            if (left <= right) {
                for (int i = bottom; i >= top; i--) res.push_back(matrix[i][left]);
                left++;
            }
        }
        
        return res;
    }
};
```

## Common Mistakes
- **Missing Boundary Checks:** Failing to re-check `if (top <= bottom)` before traversing from right to left, or `if (left <= right)` before traversing bottom to top. Without this, single row/column matrices will print duplicate numbers traversing backward.

## Interview Tips
- Mentioning how Matrix traversal scales memory-wise is a bonus point.

## Similar Questions
- Spiral Matrix II
- Spiral Matrix III
