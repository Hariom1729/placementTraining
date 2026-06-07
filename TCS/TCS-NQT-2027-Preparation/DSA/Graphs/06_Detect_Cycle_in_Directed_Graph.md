# Problem 6: Detect Cycle in a Directed Graph

## Problem Statement
Given a Directed Graph with `V` vertices (Numbered from `0` to `V-1`) and `E` edges, check whether it contains any cycle or not.

## Constraints
- `1 <= V, E <= 10^5`

---

## Approach: DFS with Path Visited Array

In an undirected graph, checking if a node is visited and not the parent is enough. However, in a directed graph, finding an already visited node doesn't necessarily mean there's a cycle (it could just be a cross edge).
A cycle in a directed graph exists **if and only if there's a back-edge**. A back-edge points to a node that is currently in the recursion stack (i.e., currently being explored).

1. Maintain two boolean arrays: `visited` and `pathVisited`.
2. When performing DFS on a node:
   - Mark it as `visited[node] = true` and `pathVisited[node] = true`.
   - Iterate through its neighbors.
     - If the neighbor is not visited, recursively call DFS. If that returns true, return true.
     - If the neighbor IS visited AND `pathVisited[neighbor]` is true, we found a cycle!
   - When backtracking (returning from the DFS call), set `pathVisited[node] = false`.

*(Alternatively, this can be solved using Kahn's Algorithm / BFS Topological Sort).*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    bool dfsCheck(int node, vector<int> adj[], vector<bool>& visited, vector<bool>& pathVisited) {
        visited[node] = true;
        pathVisited[node] = true; // Add to current path
        
        for (int neighbor : adj[node]) {
            // When the node is not visited
            if (!visited[neighbor]) {
                if (dfsCheck(neighbor, adj, visited, pathVisited)) return true;
            } 
            // If visited and currently on the same path
            else if (pathVisited[neighbor]) {
                return true; // Cycle detected
            }
        }
        
        pathVisited[node] = false; // Backtrack
        return false;
    }

public:
    bool isCyclic(int V, vector<int> adj[]) {
        vector<bool> visited(V, false);
        vector<bool> pathVisited(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfsCheck(i, adj, visited, pathVisited)) return true;
            }
        }
        
        return false;
    }
};

int main() {
    int V = 4;
    vector<int> adj[V];
    
    // Cycle: 0->1, 1->2, 2->3, 3->1
    adj[0] = {1};
    adj[1] = {2};
    adj[2] = {3};
    adj[3] = {1}; // Back edge to 1
    
    Solution sol;
    cout << "Contains Cycle? " << (sol.isCyclic(V, adj) ? "Yes" : "No") << endl; 
    // Expected: Yes

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`.
- **Space Complexity:** `O(V)` for visited arrays and recursion stack.
