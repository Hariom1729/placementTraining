# Valid Sudoku

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Apple, Microsoft

## Topic
Hashing / Matrix

## Pattern
Multi-State Validation Tracking

## Problem Statement
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Input
- `board`: a vector of vector of chars.

## Output
- Return `true` if valid, `false` otherwise.

## Sample Test Cases

**Example 1:**
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

## Edge Cases
- Invalid values hiding inside a grid.
- A completely empty board (returns `true` because there are no rule violations!).

## Intuition
To validate the Sudoku board, we must check 3 rules for every single cell: Row uniqueness, Column uniqueness, and 3x3 Box uniqueness.
We can check this in one single pass using **Hash Sets** (or arrays tracking seen states).
As we iterate through the `9x9` board, if we find a digit at `board[r][c]`:
1. We check if we have seen it in row `r` before.
2. We check if we have seen it in column `c` before.
3. We check if we have seen it in the specific 3x3 box before.

The trickiest part is: **How do we identify which 3x3 box a cell belongs to?**
We can give each of the 9 boxes a unique ID from `0` to `8`.
The mathematical formula for the box ID given row `r` and column `c` is:
`boxIndex = (r / 3) * 3 + (c / 3)`
With this, we can maintain 3 arrays of Hash Sets (or just simple integer arrays since the digits are only 1-9) to store what we've seen so far!

## Brute Force Approach
N/A - Checking row/col/box is inherently $O(1)$ per cell.

## Optimal Approach (Arrays of HashSets / Booleans)
**Detailed explanation:**
1. Create three 2D boolean arrays (or integer arrays) to act as super-fast HashSets:
   - `bool rows[9][9] = {false}` (represents `[row_index][digit 1-9]`)
   - `bool cols[9][9] = {false}`
   - `bool boxes[9][9] = {false}`
2. Iterate `r` from 0 to 8:
   - Iterate `c` from 0 to 8:
     - `char val = board[r][c]`
     - If `val == '.'`, skip.
     - `int num = val - '1'` (to 0-index the digit for our arrays).
     - `int boxIndex = (r / 3) * 3 + (c / 3)`.
     - Check if it exists in ANY of the tracking arrays:
       - If `rows[r][num] || cols[c][num] || boxes[boxIndex][num]`, return `false`! We found a duplicate!
     - Otherwise, mark it as seen:
       - `rows[r][num] = true`
       - `cols[c][num] = true`
       - `boxes[boxIndex][num] = true`
3. If the loop completes without issue, return `true`.

**Time Complexity:** $O(1)$ because the board size is ALWAYS exactly `9x9`. (Technically $O(R \times C)$ if generalized).
**Space Complexity:** $O(1)$ since our boolean arrays are always exactly size `3 x 9 x 9` = 243 bytes.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Boolean arrays to act as extremely fast O(1) hash sets
        // dimensions are [index of row/col/box][number 0-8 representing digits 1-9]
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                // Convert digit '1'-'9' to index 0-8
                int num = board[r][c] - '1';
                
                // Calculate which of the 9 boxes this cell belongs to
                int boxIndex = (r / 3) * 3 + (c / 3);
                
                // Check if the number has already been seen in this row, col, or box
                if (rows[r][num] || cols[c][num] || boxes[boxIndex][num]) {
                    return false; // Invalid Sudoku!
                }
                
                // Mark the number as seen
                rows[r][num] = true;
                cols[c][num] = true;
                boxes[boxIndex][num] = true;
            }
        }
        
        return true; // Completely valid
    }
};
```

## Dry Run
`r = 0, c = 0`, `val = '5'`
- `num = 4`. `boxIndex = (0/3)*3 + (0/3) = 0`.
- Not seen. Set `rows[0][4] = T`, `cols[0][4] = T`, `boxes[0][4] = T`.
`r = 0, c = 1`, `val = '3'`
- `num = 2`. `boxIndex = 0`.
- Not seen. Mark all as `T`.
`r = 1, c = 3`, `val = '1'`
- `num = 0`. `boxIndex = (1/3)*3 + (3/3) = 0 + 1 = 1`. (Belongs to top-middle box).
- Not seen. Mark all as `T`.
... Loop finishes successfully. Returns `true`.

## Common Mistakes
- **Failing to calculate `boxIndex`:** Many people try to write incredibly complex nested loops traversing 3x3 chunks manually. The formula `(r / 3) * 3 + (c / 3)` completely avoids this by mathematically determining the box in $O(1)$ time.

## Similar Problems
- Sudoku Solver
