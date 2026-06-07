# Problem 8: Surrounded Regions

## Problem Statement
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`.
A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

---

## Approach: Boundary DFS/BFS

Any `'O'` that is connected to the boundary of the board CANNOT be captured, because it is not completely surrounded.
Therefore, all `'O'`s that are connected to boundary `'O'`s are safe. All other `'O'`s must be flipped to `'X'`.

1. Traverse the 4 boundaries (first row, last row, first col, last col).
2. If you find an `'O'`, start a DFS/BFS from it.
3. During the DFS, mark the visited `'O'`s as a special character (e.g., `'#'`) indicating they are safe.
4. After traversing all boundaries, go through the entire board:
   - If you see an `'O'`, it means it was not connected to the boundary. Flip it to `'X'`.
   - If you see a `'#'`, it means it is safe. Revert it back to `'O'`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    void dfs(int r, int c, vector<vector<char>>& board, int m, int n) {
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') {
            return;
        }
        
        // Mark as safe
        board[r][c] = '#';
        
        // DFS in 4 directions
        dfs(r - 1, c, board, m, n);
        dfs(r + 1, c, board, m, n);
        dfs(r, c - 1, board, m, n);
        dfs(r, c + 1, board, m, n);
    }

public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        if (m == 0) return;
        int n = board[0].size();
        
        // 1. Traverse first and last column boundaries
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(i, 0, board, m, n);
            if (board[i][n - 1] == 'O') dfs(i, n - 1, board, m, n);
        }
        
        // 2. Traverse first and last row boundaries
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') dfs(0, j, board, m, n);
            if (board[m - 1][j] == 'O') dfs(m - 1, j, board, m, n);
        }
        
        // 3. Flip remaining 'O' to 'X' and '#' back to 'O'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};

int main() {
    Solution sol;
    vector<vector<char>> board = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}
    };
    
    sol.solve(board);
    
    cout << "Board after solving:\n";
    for (auto row : board) {
        for (char c : row) cout << c << " ";
        cout << "\n";
    }
    // Expected:
    // X X X X 
    // X X X X 
    // X X X X 
    // X O X X 
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M)`. Worst case, we visit every cell a constant number of times.
- **Space Complexity:** `O(N * M)` for the recursion stack in the worst case (all 'O's).
