# Problem 11: Is Graph Bipartite?

## Problem Statement
There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to.
A graph is bipartite if the nodes can be partitioned into two independent sets `A` and `B` such that every edge in the graph connects a node in set `A` and a node in set `B`.
Return `true` if and only if it is bipartite.

## Constraints
- `graph.length == n`
- `1 <= n <= 100`
- `0 <= graph[u].length < n`
- `0 <= graph[u][i] <= n - 1`
- `graph[u]` does not contain `u`.
- All the values of `graph[u]` are unique.
- If `graph[u]` contains `v`, then `graph[v]` contains `u`.

---

## Approach: Graph Coloring (BFS or DFS)

A graph is Bipartite if it can be colored using exactly 2 colors such that no two adjacent nodes have the same color.
If a graph has a cycle of **odd length**, it CANNOT be bipartite. If it has no cycles or only even length cycles, it IS bipartite.

We can solve this using BFS (or DFS).
1. Create a `color` array of size `n` initialized to `-1` (uncolored).
2. Since the graph might not be fully connected, iterate over all nodes `0` to `n-1`.
3. If `color[i] == -1` (uncolored), start BFS:
   - Push `i` to queue and color it `0`.
   - While queue is not empty:
     - Pop `node`.
     - For each `neighbor` of `node`:
       - If `color[neighbor] == -1`: assign the opposite color `1 - color[node]` and push to queue.
       - Else if `color[neighbor] == color[node]`: Two adjacent nodes have the same color! Return `false`.
4. If BFS completes for all components without issues, return `true`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
private:
    bool checkBipartite(int start, vector<vector<int>>& graph, vector<int>& color) {
        queue<int> q;
        q.push(start);
        color[start] = 0; // Assign color 0
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (int neighbor : graph[node]) {
                // If uncolored, color with opposite color and push
                if (color[neighbor] == -1) {
                    color[neighbor] = 1 - color[node];
                    q.push(neighbor);
                } 
                // If colored with same color, not bipartite
                else if (color[neighbor] == color[node]) {
                    return false;
                }
            }
        }
        return true;
    }

public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                if (!checkBipartite(i, graph, color)) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> graph = {{1,2,3}, {0,2}, {0,1,3}, {0,2}};
    // Graph has edges 0-1, 0-2, 0-3, 1-2, 2-3
    // Triangle 0-1-2 is odd cycle, so not bipartite
    
    cout << "Is Bipartite? " << (sol.isBipartite(graph) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`. Every node is colored once, and every edge is checked once.
- **Space Complexity:** `O(V)` for the color array and queue.
