# Problem 5: Detect Cycle in an Undirected Graph

## Problem Statement
Given an undirected graph with `V` vertices and `E` edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where `adj[i]` contains all the nodes `i`th node is having edge with.

## Constraints
- `1 <= V, E <= 10^5`

---

## Approach: BFS or DFS

A cycle exists in an undirected graph if we reach a node that is already visited AND that visited node is NOT the parent of the current node.

**Using BFS:**
1. Create a `visited` array.
2. For each connected component, push `{node, parent}` into a queue. Start with `{0, -1}`.
3. Mark `0` as visited.
4. While queue is not empty:
   - Pop `{node, parent}`.
   - For each adjacent `neighbor` of `node`:
     - If `neighbor` is not visited: mark as visited and push `{neighbor, node}`.
     - Else if `neighbor != parent`: we found a cycle! Return `true`.
5. Return `false` if no cycle is found.

---

## C++ Solution (BFS)

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
private:
    bool checkForCycle(int src, int V, vector<int> adj[], vector<bool>& visited) {
        visited[src] = true;
        // Queue stores {node, parent}
        queue<pair<int, int>> q;
        q.push({src, -1});
        
        while (!q.empty()) {
            int node = q.front().first;
            int parent = q.front().second;
            q.pop();
            
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push({neighbor, node});
                } else if (neighbor != parent) {
                    // Visited and not the parent -> Cycle detected!
                    return true;
                }
            }
        }
        return false;
    }

public:
    bool isCycle(int V, vector<int> adj[]) {
        vector<bool> visited(V, false);
        
        // Handle disconnected components
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (checkForCycle(i, V, adj, visited)) return true;
            }
        }
        return false;
    }
};

int main() {
    int V = 5;
    vector<int> adj[V];
    
    // Graph with cycle: 0-1, 1-2, 2-3, 3-4, 4-1
    adj[0] = {1};
    adj[1] = {0, 2, 4};
    adj[2] = {1, 3};
    adj[3] = {2, 4};
    adj[4] = {1, 3};
    
    Solution sol;
    cout << "Contains Cycle? " << (sol.isCycle(V, adj) ? "Yes" : "No") << endl; 
    // Expected: Yes

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`.
- **Space Complexity:** `O(V)` for the queue and visited array.
