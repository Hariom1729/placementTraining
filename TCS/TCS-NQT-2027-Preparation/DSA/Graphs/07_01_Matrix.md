# Problem 7: 01 Matrix

## Problem Statement
Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.
The distance between two adjacent cells is `1`.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.

---

## Approach: Multi-source BFS

Instead of finding the distance from every `1` to the nearest `0` (which is `O((NM)^2)`), it is much faster to start a Multi-source BFS from **ALL `0`s simultaneously**.

1. Create a `dist` matrix initialized to `infinity` (or `-1`), and a `queue<pair<int, int>> q`.
2. Iterate over the grid. For every `mat[i][j] == 0`, set `dist[i][j] = 0` and push `{i, j}` into `q`.
3. Perform standard BFS:
   - Pop `{r, c}`.
   - For each of the 4 neighbors `{nr, nc}`:
     - If the neighbor is within bounds and `dist[nr][nc]` is infinity (not visited yet):
       - `dist[nr][nc] = dist[r][c] + 1`
       - Push `{nr, nc}` to `q`.
4. Return `dist` matrix.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<int>> dist(m, vector<int>(n, -1));
        queue<pair<int, int>> q;
        
        // Add all 0s to queue and mark distance as 0
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    dist[i][j] = 0;
                    q.push({i, j});
                }
            }
        }
        
        int dRow[] = {-1, 1, 0, 0};
        int dCol[] = {0, 0, -1, 1};
        
        // Multi-source BFS
        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            
            for (int d = 0; d < 4; d++) {
                int nr = r + dRow[d];
                int nc = c + dCol[d];
                
                // If within bounds and not visited
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }
        
        return dist;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> mat = {
        {0, 0, 0},
        {0, 1, 0},
        {1, 1, 1}
    };
    
    vector<vector<int>> res = sol.updateMatrix(mat);
    
    cout << "Distance Matrix:\n";
    for (auto row : res) {
        for (int x : row) cout << x << " ";
        cout << "\n";
    }
    // Expected:
    // 0 0 0 
    // 0 1 0 
    // 1 2 1 

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M)`. Each cell is added to the queue at most once.
- **Space Complexity:** `O(N * M)` for the `dist` array and queue.
