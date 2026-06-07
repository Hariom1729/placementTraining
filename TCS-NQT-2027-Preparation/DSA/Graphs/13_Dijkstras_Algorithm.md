# Problem 13: Dijkstra's Algorithm

## Problem Statement
Given a weighted, undirected and connected graph of `V` vertices and an adjacency list `adj` where `adj[i]` is a list of lists containing two integers where the first integer of each list `j` denotes there is edge between `i` and `j`, second integers corresponds to the weight of that edge.
Find the shortest distance of all the vertex's from the source vertex `S`.

## Constraints
- `1 <= V <= 1000`
- `0 <= adj[i][j] <= 1000`
- `1 <= adj.length() <= 1000`
- `0 <= S < V`

---

## Approach: Priority Queue (Min-Heap)

Dijkstra's Algorithm finds the shortest path from a source node to all other nodes in a graph with non-negative edge weights.

1. Create a `dist` array of size `V`, initialized to infinity, except for `dist[S] = 0`.
2. Use a `priority_queue` (min-heap) that stores `{distance, node}`.
3. Push `{0, S}` into the min-heap.
4. While min-heap is not empty:
   - Pop the top element `{d, u}`. This gives the node `u` with the smallest known distance `d`.
   - Iterate over all neighbors `{v, weight}` of `u`.
   - If `d + weight < dist[v]`:
     - Update `dist[v] = d + weight`.
     - Push `{dist[v], v}` into the min-heap.
5. Return the `dist` array.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> dijkstra(int V, vector<vector<int>> adj[], int S) {
        // Min-heap: {distance, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        // Distance array initialized to infinity
        vector<int> dist(V, 1e9);
        
        dist[S] = 0;
        pq.push({0, S});
        
        while (!pq.empty()) {
            int dis = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            // Traverse neighbors
            for (auto it : adj[node]) {
                int edgeWeight = it[1];
                int adjNode = it[0];
                
                // Relaxation
                if (dis + edgeWeight < dist[adjNode]) {
                    dist[adjNode] = dis + edgeWeight;
                    pq.push({dist[adjNode], adjNode});
                }
            }
        }
        
        return dist;
    }
};

int main() {
    int V = 3;
    vector<vector<int>> adj[V];
    
    // Graph: 0-1 (weight 1), 0-2 (weight 6), 1-2 (weight 3)
    adj[0] = {{1, 1}, {2, 6}};
    adj[1] = {{0, 1}, {2, 3}};
    adj[2] = {{0, 6}, {1, 3}};
    
    Solution sol;
    vector<int> res = sol.dijkstra(V, adj, 2);
    
    cout << "Shortest distances from node 2: ";
    for (int x : res) cout << x << " ";
    cout << endl;
    // Expected: 4 3 0
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(E \log V)` where `E` is the number of edges and `V` is the number of vertices. Priority Queue operations take `O(\log V)`.
- **Space Complexity:** `O(V + E)` for the adjacency list and priority queue.
