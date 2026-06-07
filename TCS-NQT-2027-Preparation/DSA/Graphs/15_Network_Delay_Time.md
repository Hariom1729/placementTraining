# Problem 15: Network Delay Time

## Problem Statement
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.
We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- `0 <= w_i <= 100`

---

## Approach: Dijkstra's Algorithm

The problem asks for the time it takes for a signal to reach *all* nodes from a source node `k`. This means we need the shortest path from `k` to all other nodes. The answer is simply the **maximum** of all these shortest paths (the time the signal reaches the farthest node). If any node is unreachable (distance is infinity), return `-1`.

We use Dijkstra's Algorithm because weights are non-negative.
1. Build an adjacency list: `adj[u] = {v, w}`.
2. Initialize `dist` array of size `n + 1` with infinity. `dist[k] = 0`.
3. Use a min-heap `priority_queue<pair<int, int>>` storing `{distance, node}`.
4. Run standard Dijkstra.
5. After the loop, find the maximum value in the `dist` array (ignoring index 0). If the maximum is infinity, return `-1`. Else return the maximum.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<pair<int, int>> adj[n + 1]; // 1-based indexing
        for (auto it : times) {
            adj[it[0]].push_back({it[1], it[2]});
        }
        
        vector<int> dist(n + 1, 1e9);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        dist[k] = 0;
        pq.push({0, k});
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            
            // Optimization: if we already found a shorter path, skip
            if (d > dist[node]) continue;
            
            for (auto it : adj[node]) {
                int adjNode = it.first;
                int weight = it.second;
                
                if (d + weight < dist[adjNode]) {
                    dist[adjNode] = d + weight;
                    pq.push({dist[adjNode], adjNode});
                }
            }
        }
        
        int mx = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == 1e9) return -1;
            mx = max(mx, dist[i]);
        }
        
        return mx;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> times = {
        {2, 1, 1},
        {2, 3, 1},
        {3, 4, 1}
    };
    int n = 4, k = 2;
    
    cout << "Network Delay Time: " << sol.networkDelayTime(times, n, k) << endl; 
    // Expected: 2 (Signal goes to 1 and 3 in time 1, then from 3 to 4 in time 2)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(E \log V)` where `E` is the number of edges (`times.length`) and `V` is the number of nodes `n`.
- **Space Complexity:** `O(V + E)` for the adjacency list and priority queue.
