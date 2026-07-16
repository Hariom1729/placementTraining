# Number of Islands

## Difficulty
Medium

## Asked In
Infosys SP (L2, L3)
Year: 2022
Frequency: High

---

## Problem Statement
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

---

## Optimal Approach (DFS / BFS)
**Detailed explanation:**
Iterate through each cell in the matrix. When you find a `'1'`, increment the island counter, and trigger a DFS (or BFS) to sink the entire island (convert all connected `'1'`s to `'0'`s). This prevents counting the same island twice.

**Complexity:**
- **Time Complexity:** $O(M \times N)$ where $M$ is rows and $N$ is columns.
- **Space Complexity:** $O(M \times N)$ in the worst case for the DFS recursion stack.

---

## C++ Solution
```cpp
#include <vector>
using namespace std;

void dfs(vector<vector<char>>& grid, int r, int c) {
    int nr = grid.size();
    int nc = grid[0].size();
    
    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
        return;
    }
    
    // Sink the island
    grid[r][c] = '0';
    
    // Explore 4 directions
    dfs(grid, r - 1, c); // UP
    dfs(grid, r + 1, c); // DOWN
    dfs(grid, r, c - 1); // LEFT
    dfs(grid, r, c + 1); // RIGHT
}

int numIslands(vector<vector<char>>& grid) {
    if (grid.empty()) return 0;
    
    int num_islands = 0;
    for (int r = 0; r < grid.size(); r++) {
        for (int c = 0; c < grid[0].size(); c++) {
            if (grid[r][c] == '1') {
                num_islands++;
                dfs(grid, r, c);
            }
        }
    }
    
    return num_islands;
}
```
