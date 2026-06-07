# Problem 14: Shortest Path in Binary Matrix

## Problem Statement
Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return `-1`.
A clear path is a path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)` such that:
- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected.
The length of a clear path is the number of visited cells of this path.

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

---

## Approach: BFS (Dijkstra's with edge weight 1)

Since all edges (moves between valid adjacent cells) have the same weight (length `1`), we can use standard BFS. This is essentially Dijkstra's algorithm where the priority queue is replaced by a standard queue because all weights are equal.

1. If `grid[0][0] == 1` or `grid[n-1][n-1] == 1`, return `-1`.
2. Use a `queue<pair<int, int>> q` and a `dist` matrix.
3. Push `{0, 0}` to `q` and set `dist[0][0] = 1`.
4. While `q` is not empty:
   - Pop `{r, c}`.
   - If `r == n-1` and `c == n-1`, return `dist[r][c]`.
   - Explore all 8 directions.
   - If a neighbor `(nr, nc)` is within bounds, is a `0`, and its current distance is greater than `dist[r][c] + 1` (or if it's not visited):
     - `dist[nr][nc] = dist[r][c] + 1`
     - Push `{nr, nc}` to `q`.
5. If we exit the loop, return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        
        queue<pair<int, int>> q;
        q.push({0, 0});
        
        // Instead of a visited array, we can modify the grid or use a dist array.
        // Let's modify the grid to store distances to save space.
        grid[0][0] = 1;
        
        // 8 directions
        int dRow[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dCol[] = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            int dist = grid[r][c];
            q.pop();
            
            if (r == n - 1 && c == n - 1) return dist;
            
            for (int d = 0; d < 8; d++) {
                int nr = r + dRow[d];
                int nc = c + dCol[d];
                
                // If within bounds and is '0' (unvisited open cell)
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = dist + 1; // Mark visited with distance
                    q.push({nr, nc});
                }
            }
        }
        
        return -1;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {
        {0, 0, 0},
        {1, 1, 0},
        {1, 1, 0}
    };
    
    cout << "Shortest Path Length: " << sol.shortestPathBinaryMatrix(grid) << endl; 
    // Expected: 4

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` where `N` is the dimension of the grid. Each cell is added to the queue at most once.
- **Space Complexity:** `O(N^2)` for the queue in the worst case.
