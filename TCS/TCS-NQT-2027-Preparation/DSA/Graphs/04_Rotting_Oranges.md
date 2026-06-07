# Problem 4: Rotting Oranges

## Problem Statement
You are given an `m x n` `grid` where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

---

## Approach: Multi-source BFS

This problem requires finding the shortest time for an infection to spread. Shortest path/time on an unweighted grid implies **BFS**. Since there can be multiple rotten oranges initially, we must start the BFS from ALL rotten oranges simultaneously (Multi-source BFS).

1. Initialize a queue `q` storing pairs of `(row, col)`.
2. Iterate over the grid.
   - If a cell is `2` (rotten), push its coordinates into `q`.
   - If a cell is `1` (fresh), increment a `freshCount`.
3. If `freshCount == 0`, return `0` (no fresh oranges to rot).
4. Do standard BFS level by level. Use an array `directions = {{-1,0}, {1,0}, {0,-1}, {0,1}}`.
5. For each level (minute):
   - Pop nodes, check their 4 neighbors.
   - If a neighbor is `1` (fresh), make it `2` (rotten), decrement `freshCount`, and push it to the queue.
6. Return `minutes` if `freshCount == 0`. Otherwise, return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        queue<pair<int, int>> q;
        int freshCount = 0;
        
        // 1. Add all initially rotten oranges to queue, and count fresh oranges
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }
        
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        int dRow[] = {-1, 1, 0, 0};
        int dCol[] = {0, 0, -1, 1};
        
        // 2. Multi-source BFS
        while (!q.empty()) {
            int size = q.size();
            bool rottedAny = false;
            
            for (int i = 0; i < size; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();
                
                // Check 4 neighbors
                for (int d = 0; d < 4; d++) {
                    int nr = r + dRow[d];
                    int nc = c + dCol[d];
                    
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Make it rotten
                        freshCount--;
                        q.push({nr, nc});
                        rottedAny = true;
                    }
                }
            }
            if (rottedAny) minutes++;
        }
        
        return freshCount == 0 ? minutes : -1;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {
        {2, 1, 1},
        {1, 1, 0},
        {0, 1, 1}
    };
    
    cout << "Minutes required: " << sol.orangesRotting(grid) << endl; 
    // Expected: 4
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M)` where `N` and `M` are the grid dimensions. We visit each cell at most a few times.
- **Space Complexity:** `O(N * M)` for the queue in the worst-case scenario.
