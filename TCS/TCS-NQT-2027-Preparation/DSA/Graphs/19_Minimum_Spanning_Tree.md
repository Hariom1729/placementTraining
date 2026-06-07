# Problem 19: Minimum Spanning Tree (Prim's Algorithm)

## Problem Statement
Given a weighted, undirected and connected graph of `V` vertices and `E` edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
(A spanning tree is a subset of Graph G, which has all the vertices covered with minimum possible number of edges. Hence, a spanning tree does not have cycles and it cannot be disconnected.)

## Constraints
- `2 <= V <= 1000`
- `V-1 <= E <= (V*(V-1))/2`
- `1 <= w <= 1000`

---

## Approach: Prim's Algorithm

Prim's algorithm builds the MST starting from any node, continuously greedily adding the edge with the lowest weight that connects the growing tree to a new node.

1. Use a Min-Heap `priority_queue<pair<int, int>>` storing `{edgeWeight, node}`.
2. Maintain a `visited` array.
3. Push `{0, 0}` to the queue (start at node 0 with edge weight 0).
4. Maintain a `sum = 0`.
5. While queue is not empty:
   - Pop `{weight, node}`.
   - If `node` is already visited, `continue`.
   - Mark `node` as visited.
   - Add `weight` to `sum`.
   - Iterate over adjacent nodes. If they are not visited, push `{adjWeight, adjNode}` to the queue.
6. Return `sum`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    // Function to find sum of weights of edges of the Minimum Spanning Tree.
    int spanningTree(int V, vector<vector<int>> adj[]) {
        // Priority queue storing {weight, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<bool> visited(V, false);
        
        int sum = 0;
        
        // Start from node 0
        pq.push({0, 0});
        
        while (!pq.empty()) {
            int weight = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            // If already visited, ignore
            if (visited[node]) continue;
            
            // Mark as visited and add to MST sum
            visited[node] = true;
            sum += weight;
            
            // Push all unvisited neighbors to PQ
            for (auto it : adj[node]) {
                int adjNode = it[0];
                int edgeWt = it[1];
                
                if (!visited[adjNode]) {
                    pq.push({edgeWt, adjNode});
                }
            }
        }
        
        return sum;
    }
};

int main() {
    int V = 3;
    vector<vector<int>> adj[V];
    
    // Graph: 0-1 (wt 5), 1-2 (wt 3), 0-2 (wt 1)
    adj[0] = {{1, 5}, {2, 1}};
    adj[1] = {{0, 5}, {2, 3}};
    adj[2] = {{1, 3}, {0, 1}};
    
    Solution sol;
    cout << "Sum of MST: " << sol.spanningTree(V, adj) << endl; 
    // Expected: 4 (Edge 0-2 (wt 1) + Edge 2-1 (wt 3))
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(E \log E)` because there are at most `E` elements in the priority queue.
- **Space Complexity:** `O(V + E)` for the priority queue and visited array.
