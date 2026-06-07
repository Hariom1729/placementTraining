# Problem 18: Find the City With the Smallest Number of Neighbors at a Threshold Distance

## Problem Statement
There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where `edges[i] = [from_i, to_i, weight_i]` represents a bidirectional and weighted edge between cities `from_i` and `to_i`, and given the integer `distanceThreshold`.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most `distanceThreshold`. If there are multiple such cities, return the city with the **greatest number**.

## Constraints
- `2 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= from_i < to_i < n`
- `1 <= weight_i, distanceThreshold <= 10^4`

---

## Approach: Floyd-Warshall Algorithm (All-Pairs Shortest Path)

The problem asks us to find the shortest distance between EVERY pair of nodes to see how many nodes are reachable within the threshold from each node.
Since `n` is very small (`n <= 100`), an `O(N^3)` algorithm like **Floyd-Warshall** is perfect here.

1. Create a `dist` matrix of size `n x n`, initialized to infinity. Set `dist[i][i] = 0`.
2. Populate the `dist` matrix with the given edges. Since the graph is undirected, `dist[u][v] = w` and `dist[v][u] = w`.
3. Apply Floyd-Warshall:
   - For every intermediate node `k` from `0` to `n-1`:
     - For every source `i` from `0` to `n-1`:
       - For every destination `j` from `0` to `n-1`:
         - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.
4. Count reachable cities for each city. For city `i`, count how many `j` (where `i != j`) have `dist[i][j] <= distanceThreshold`.
5. Keep track of the city with the minimum reachable cities. If there's a tie, choose the city with the larger index.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Initialize distance matrix with infinity
        vector<vector<int>> dist(n, vector<int>(n, 1e9));
        for (int i = 0; i < n; i++) dist[i][i] = 0;
        
        // Populate edges
        for (auto it : edges) {
            dist[it[0]][it[1]] = it[2];
            dist[it[1]][it[0]] = it[2]; // Undirected
        }
        
        // Floyd-Warshall Algorithm
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] == 1e9 || dist[k][j] == 1e9) continue;
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
        
        int minReachable = n;
        int ansCity = -1;
        
        // Check for each city
        for (int i = 0; i < n; i++) {
            int reachable = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] <= distanceThreshold) {
                    reachable++;
                }
            }
            
            // We want the city with the smallest reachable cities.
            // If equal, we want the city with the greatest index (so we use <=).
            if (reachable <= minReachable) {
                minReachable = reachable;
                ansCity = i;
            }
        }
        
        return ansCity;
    }
};

int main() {
    Solution sol;
    int n = 4;
    vector<vector<int>> edges = {
        {0, 1, 3}, {1, 2, 1}, {1, 3, 4}, {2, 3, 1}
    };
    int distanceThreshold = 4;
    
    cout << "City with smallest number of neighbors: " << sol.findTheCity(n, edges, distanceThreshold) << endl; 
    // Expected: 3 
    // (City 0 reaches 1, 2. City 1 reaches 0, 2, 3. City 2 reaches 0, 1, 3. City 3 reaches 1, 2)
    // City 0 and 3 both reach 2 cities. We return the larger index, which is 3.

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^3)` for Floyd-Warshall algorithm. Since `N <= 100`, `N^3 = 1,000,000` operations, which is well within time limits.
- **Space Complexity:** `O(N^2)` to store the distance matrix.
