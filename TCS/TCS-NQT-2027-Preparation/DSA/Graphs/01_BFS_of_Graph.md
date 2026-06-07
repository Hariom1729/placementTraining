# Problem 1: BFS of graph

## Problem Statement
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from `0`.
Note: One can move from node `u` to node `v` only if there's an edge from `u` to `v`. Find the BFS traversal of the graph starting from the `0`th vertex, from left to right according to the input graph.

## Constraints
- `1 <= V, E <= 10^4`

---

## Approach: Queue + Visited Array

Breadth-First Search (BFS) explores the graph level by level. It uses a **Queue**.
To avoid visiting the same node multiple times (and getting stuck in infinite loops in cyclic graphs), we must maintain a `visited` array.

1. Create a `visited` array of size `V` initialized to `false`.
2. Create a `queue<int>`.
3. Push the starting node (`0`) into the queue and mark it as visited: `visited[0] = true`.
4. While the queue is not empty:
   - Pop the front node, add it to the result array.
   - Iterate through all adjacent nodes of the popped node.
   - If an adjacent node is **not visited**, mark it as visited and push it into the queue.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        vector<int> bfs;
        vector<bool> visited(V, false);
        queue<int> q;
        
        q.push(0);
        visited[0] = true;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            bfs.push_back(node);
            
            // Traverse all adjacent nodes
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        return bfs;
    }
};

int main() {
    int V = 5;
    vector<int> adj[V];
    
    // Creating graph: 0 -> 1, 0 -> 2, 0 -> 3, 2 -> 4
    adj[0] = {1, 2, 3};
    adj[1] = {};
    adj[2] = {4};
    adj[3] = {};
    adj[4] = {};
    
    Solution sol;
    vector<int> res = sol.bfsOfGraph(V, adj);
    
    cout << "BFS Traversal: ";
    for (int x : res) cout << x << " ";
    cout << endl;
    // Expected: 0 1 2 3 4
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)` where `V` is the number of vertices and `E` is the number of edges. Every vertex and every edge is visited exactly once.
- **Space Complexity:** `O(V)` for the queue, visited array, and result array.
