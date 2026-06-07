# Problem 2: DFS of Graph

## Problem Statement
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the `0`th vertex from left to right according to the graph.

## Constraints
- `1 <= V, E <= 10^4`

---

## Approach: Recursion + Visited Array

Depth-First Search (DFS) explores as far as possible along each branch before backtracking. It uses a **Stack** (implicitly via the recursive call stack).
Just like BFS, we need a `visited` array to prevent infinite loops.

1. Create a `visited` array of size `V` initialized to `false`.
2. Write a recursive function `dfsHelper(node)`:
   - Mark `node` as visited.
   - Add `node` to the result array.
   - Iterate through all adjacent nodes of `node`.
   - If an adjacent node is not visited, recursively call `dfsHelper(neighbor)`.
3. Call `dfsHelper(0)` to start the traversal.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    void dfsHelper(int node, vector<int> adj[], vector<bool>& visited, vector<int>& dfs) {
        // Mark the current node as visited and add it to result
        visited[node] = true;
        dfs.push_back(node);
        
        // Visit all unvisited neighbors
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfsHelper(neighbor, adj, visited, dfs);
            }
        }
    }

public:
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        vector<int> dfs;
        vector<bool> visited(V, false);
        
        // Start DFS from node 0
        dfsHelper(0, adj, visited, dfs);
        
        return dfs;
    }
};

int main() {
    int V = 5;
    vector<int> adj[V];
    
    // Creating graph: 0-1, 0-2, 0-4, 4-3
    adj[0] = {1, 2, 4};
    adj[1] = {0};
    adj[2] = {0};
    adj[4] = {0, 3};
    adj[3] = {4};
    
    Solution sol;
    vector<int> res = sol.dfsOfGraph(V, adj);
    
    cout << "DFS Traversal: ";
    for (int x : res) cout << x << " ";
    cout << endl;
    // Expected: 0 1 2 4 3
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`. Every vertex is visited once, and every edge is checked once.
- **Space Complexity:** `O(V)` for the visited array, result array, and the recursive call stack.
