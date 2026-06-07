# Problem 16: Path With Minimum Effort

## Problem Statement
You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)`. You can move up, down, left, or right.

A route's **effort** is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

## Constraints
- `rows == heights.length`
- `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 10^6`

---

## Approach: Dijkstra's Algorithm (Minimax Path)

This is a variation of Dijkstra's algorithm. Instead of summing up edge weights to find the shortest path, we are keeping track of the **maximum difference** encountered along a path, and we want to **minimize this maximum difference**.

1. Use a `dist` array initialized to infinity. `dist[r][c]` will store the minimum effort to reach `(r, c)`.
2. `dist[0][0] = 0`.
3. Use a min-heap `priority_queue<pair<int, pair<int, int>>>` storing `{effort, {row, col}}`.
4. Pop the cell with the smallest effort.
5. If we reach the bottom-right cell, return the effort.
6. Check all 4 neighbors. For a neighbor `(nr, nc)`:
   - Calculate the effort to move there: `newEffort = max(currentEffort, abs(heights[r][c] - heights[nr][nc]))`.
   - If `newEffort < dist[nr][nc]`:
     - Update `dist[nr][nc] = newEffort`.
     - Push `{newEffort, {nr, nc}}` to the min-heap.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        
        // Min-heap: {effort, {row, col}}
        priority_queue<pair<int, pair<int, int>>, 
                       vector<pair<int, pair<int, int>>>, 
                       greater<pair<int, pair<int, int>>>> pq;
                       
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        
        dist[0][0] = 0;
        pq.push({0, {0, 0}});
        
        int dRow[] = {-1, 1, 0, 0};
        int dCol[] = {0, 0, -1, 1};
        
        while (!pq.empty()) {
            int effort = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();
            
            // If we reached the destination
            if (r == m - 1 && c == n - 1) return effort;
            
            // If we found a path with more effort than recorded, skip
            if (effort > dist[r][c]) continue;
            
            for (int d = 0; d < 4; d++) {
                int nr = r + dRow[d];
                int nc = c + dCol[d];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    // Effort to go to neighbor
                    int newEffort = max(effort, abs(heights[r][c] - heights[nr][nc]));
                    
                    if (newEffort < dist[nr][nc]) {
                        dist[nr][nc] = newEffort;
                        pq.push({newEffort, {nr, nc}});
                    }
                }
            }
        }
        
        return 0; // Should not reach here
    }
};

int main() {
    Solution sol;
    vector<vector<int>> heights = {
        {1, 2, 2},
        {3, 8, 2},
        {5, 3, 5}
    };
    
    cout << "Minimum Effort: " << sol.minimumEffortPath(heights) << endl; 
    // Expected: 2 (Path: 1 -> 3 -> 5 -> 3 -> 5)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(M * N \log (M * N))`. There are `M * N` nodes, and each insertion into the priority queue takes logarithmic time.
- **Space Complexity:** `O(M * N)` for the `dist` array and priority queue.
