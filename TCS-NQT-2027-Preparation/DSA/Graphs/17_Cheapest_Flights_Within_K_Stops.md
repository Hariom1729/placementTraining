# Problem 17: Cheapest Flights Within K Stops

## Problem Statement
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.
You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

## Constraints
- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- `1 <= price_i <= 10^4`
- `0 <= src, dst, k < n`

---

## Approach: BFS based on Stops (Bellman-Ford variant)

If we use standard Dijkstra, it prioritizes cost. However, Dijkstra might find a very cheap path that takes `k+1` stops and mark the node as visited, permanently blocking a slightly more expensive path that only takes `k` stops.
Since we need to limit the number of stops, it's better to process the graph **level by level** (by number of stops). We can use a standard Queue (BFS).

1. Queue stores `{stops, {node, cost}}`.
2. Push `{0, {src, 0}}` to the queue.
3. `dist` array stores minimum cost to reach a node. `dist[src] = 0`.
4. While queue is not empty:
   - Pop `{stops, {node, cost}}`.
   - If `stops > k`, we skip because we exceeded the stop limit.
   - For each neighbor `(adjNode, edgeWt)`:
     - If `cost + edgeWt < dist[adjNode]`:
       - Update `dist[adjNode] = cost + edgeWt`.
       - Push `{stops + 1, {adjNode, cost + edgeWt}}` to the queue.
5. Return `dist[dst]` if it's not infinity, otherwise return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int, int>> adj[n];
        for (auto it : flights) {
            adj[it[0]].push_back({it[1], it[2]});
        }
        
        // Queue: {stops, {node, cost}}
        queue<pair<int, pair<int, int>>> q;
        q.push({0, {src, 0}});
        
        vector<int> dist(n, 1e9);
        dist[src] = 0;
        
        while (!q.empty()) {
            auto it = q.front();
            q.pop();
            
            int stops = it.first;
            int node = it.second.first;
            int cost = it.second.second;
            
            if (stops > k) continue;
            
            for (auto neighbor : adj[node]) {
                int adjNode = neighbor.first;
                int edgeWt = neighbor.second;
                
                // If the new cost is strictly better, update and push
                if (cost + edgeWt < dist[adjNode] && stops <= k) {
                    dist[adjNode] = cost + edgeWt;
                    q.push({stops + 1, {adjNode, cost + edgeWt}});
                }
            }
        }
        
        if (dist[dst] == 1e9) return -1;
        return dist[dst];
    }
};

int main() {
    Solution sol;
    int n = 4;
    vector<vector<int>> flights = {
        {0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}
    };
    int src = 0, dst = 3, k = 1;
    
    cout << "Cheapest Price: " << sol.findCheapestPrice(n, flights, src, dst, k) << endl; 
    // Expected: 700 (0 -> 1 -> 3 takes 1 stop. 0 -> 1 -> 2 -> 3 takes 2 stops and costs 400 but violates k=1)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N + E \cdot K)`. In the worst case, we explore all edges up to `K` times.
- **Space Complexity:** `O(N + E)` for the adjacency list and queue.
