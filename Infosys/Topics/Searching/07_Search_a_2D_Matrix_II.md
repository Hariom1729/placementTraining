# Search a 2D Matrix II

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Apple

## Topic
Searching / Matrix

## Pattern
Staircase Search / Top-Right Elimination

## Problem Statement
Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:
1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the integers in each row are **sorted** in ascending order.
- All the integers in each column are **sorted** in ascending order.
- `-10^9 <= target <= 10^9`

## Input
- `matrix` vector of vectors of integers.
- `target` integer.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

**Example 2:**
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

## Edge Cases
- Target is smaller than top-left or larger than bottom-right.
- Matrix is 1x1.

## Intuition
Unlike *Search a 2D Matrix I*, the rows are NOT sequentially sorted (i.e. the start of row 2 is NOT necessarily greater than the end of row 1). If you lay the matrix flat, it is NOT a strictly increasing 1D array. So we CANNOT use standard 1D binary search.

However, the matrix has a very specific property: every row is sorted left-to-right, and every column is sorted top-to-bottom.
If we start our search at the **Top-Right** corner of the matrix, we get a magical property similar to a Binary Search Tree!
Let the current element be `matrix[row][col]`.
- If `matrix[row][col] == target`, we found it!
- If `matrix[row][col] > target`: Because the column is sorted top-to-bottom, everything below this element is even LARGER! We can safely eliminate this **entire column**. We move left: `col--`.
- If `matrix[row][col] < target`: Because the row is sorted left-to-right, everything to the left of this element is even SMALLER! We can safely eliminate this **entire row**. We move down: `row++`.

We repeat this process until we either find the target or fall off the matrix (meaning it doesn't exist).
*(Note: You can also start from the Bottom-Left corner and achieve the exact same logic moving up and right).*

## Brute Force Approach
**Explanation:** Nested loops iterating through every cell.
**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(1)$

## Optimal Approach (Staircase Search)
**Detailed explanation:**
1. Initialize `row = 0` (top) and `col = matrix[0].size() - 1` (right).
2. Loop while `row < matrix.size()` AND `col >= 0`:
   - If `matrix[row][col] == target`, return `true`.
   - If `matrix[row][col] > target`:
     - Target must be to the left, so `col--`.
   - Else (`matrix[row][col] < target`):
     - Target must be below, so `row++`.
3. If loop finishes, return `false`.

**Time Complexity:** $O(M + N)$. In the worst case, we start at top-right and walk all the way to bottom-left, taking at most $M$ steps down and $N$ steps left.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // Start from the top-right corner
        int r = 0;
        int c = cols - 1;
        
        while (r < rows && c >= 0) {
            int current = matrix[r][c];
            
            if (current == target) {
                return true; // Target found
            } else if (current > target) {
                // Since column is sorted top-down, everything below 'current' is even larger.
                // Eliminate the entire column.
                c--;
            } else {
                // Since row is sorted left-right, everything left of 'current' is even smaller.
                // Eliminate the entire row.
                r++;
            }
        }
        
        // Fell off the matrix, target does not exist
        return false;
    }
};
```

## Dry Run
`matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 5`
- `r = 0`, `c = 2`. `current = matrix[0][2] = 7`.
- `7 > 5`. Eliminate column 2. `c--` -> `c = 1`.
- `r = 0`, `c = 1`. `current = matrix[0][1] = 4`.
- `4 < 5`. Eliminate row 0. `r++` -> `r = 1`.
- `r = 1`, `c = 1`. `current = matrix[1][1] = 5`.
- `5 == 5`. Return `true`!

## Common Mistakes
- **Starting at Top-Left or Bottom-Right:** If you start at `[0][0]`, and the target is larger, you don't know whether to move Right or Down, because BOTH directions contain larger numbers! The logic only works if one direction is smaller and the other is larger (which is only true for Top-Right and Bottom-Left corners).

## Similar Problems
- Search a 2D Matrix I
