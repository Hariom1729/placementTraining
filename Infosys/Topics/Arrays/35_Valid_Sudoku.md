# Valid Sudoku

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Related Companies: Amazon, Apple, Microsoft

## Topic
Arrays (Matrix)

## Pattern
Hash Set (Simulation)

## Problem Statement
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated.

## Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Input Format
- 9 lines, each containing 9 characters representing the board.

## Output Format
- Return a boolean (`true` or `false`).

## Sample Input
```
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

## Sample Output
```
true
```

## Approach 1
Optimal Approach (Using Hash Sets or Arrays)
**Explanation:** 
We need to check three things for every non-empty cell: is it unique in its row, unique in its col, and unique in its 3x3 box?
We can use a 2D array of booleans (or sets) to track this in a single pass.
1. `rows[9][9]`: `rows[i][num]` is true if `num` exists in row `i`.
2. `cols[9][9]`: `cols[j][num]` is true if `num` exists in col `j`.
3. `boxes[9][9]`: `boxes[k][num]` is true if `num` exists in box `k`.
   - The box index `k` can be calculated as `(i / 3) * 3 + (j / 3)`.

Loop through the `9x9` board. If the cell is not `.`:
- Extract the integer `num` (remember to convert from 1-based to 0-based index, e.g., `num - '1'`).
- Check if `rows[i][num]`, `cols[j][num]`, or `boxes[k][num]` is already true. If so, return `false`.
- Otherwise, mark them all as `true`.
If the loop finishes without returning `false`, return `true`.

**Time Complexity:** $O(1)$ because the board is always $9 \times 9$. (Technically $O(N^2)$ if generalized).
**Space Complexity:** $O(1)$ (Fixed $9 \times 9$ boolean arrays).

## Java Solution
```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    int k = (i / 3) * 3 + (j / 3);
                    
                    if (rows[i][num] || cols[j][num] || boxes[k][num]) {
                        return false;
                    }
                    
                    rows[i][num] = true;
                    cols[j][num] = true;
                    boxes[k][num] = true;
                }
            }
        }
        
        return true;
    }
}
```

## Python Solution
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    k = (i // 3) * 3 + (j // 3)
                    
                    if val in rows[i] or val in cols[j] or val in boxes[k]:
                        return False
                        
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[k].add(val)
                    
        return True
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    int k = (i / 3) * 3 + (j / 3);
                    
                    if (rows[i][num] || cols[j][num] || boxes[k][num]) {
                        return false;
                    }
                    
                    rows[i][num] = true;
                    cols[j][num] = true;
                    boxes[k][num] = true;
                }
            }
        }
        
        return true;
    }
};
```

## Common Mistakes
- **Calculating the box index incorrectly:** `k = (i / 3) * 3 + (j / 3)` is the standard mapping from 2D coordinates to 1D blocks. Forgetting the `* 3` will cause blocks in the same column to overwrite each other.

## Similar Questions
- Sudoku Solver
