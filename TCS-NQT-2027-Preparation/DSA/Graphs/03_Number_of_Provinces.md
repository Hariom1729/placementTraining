# Problem 3: Number of Provinces

## Problem Statement
There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.
A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`th city and the `j`th city are directly connected, and `isConnected[i][j] = 0` otherwise.
Return the total number of provinces.

## Constraints
- `1 <= n <= 200`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

---

## Approach: Connected Components (DFS or BFS)

The problem asks for the number of connected components in an undirected graph given as an adjacency matrix.
We can use a `visited` array and a `for` loop that checks every node from `0` to `n-1`.

1. Initialize `visited` array of size `n` with `false`.
2. Initialize `provinces = 0`.
3. Loop `i` from `0` to `n-1`:
   - If `visited[i]` is `false`, it means we found a new province.
   - Increment `provinces`.
   - Start a DFS or BFS from `i` to mark all cities connected to `i` as visited.
4. The DFS function will iterate through `isConnected[node]`. If `isConnected[node][j] == 1` and `j` is not visited, recursively call DFS for `j`.
5. Return `provinces`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    void dfs(int node, vector<vector<int>>& isConnected, vector<bool>& visited) {
        visited[node] = true;
        
        for (int j = 0; j < isConnected.size(); j++) {
            // If there is an edge and the neighbor is not visited
            if (isConnected[node][j] == 1 && !visited[j]) {
                dfs(j, isConnected, visited);
            }
        }
    }

public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int provinces = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                provinces++; // Found a new unconnected component
                dfs(i, isConnected, visited); // Traverse the entire component
            }
        }
        
        return provinces;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> isConnected = {
        {1, 1, 0},
        {1, 1, 0},
        {0, 0, 1}
    };
    
    cout << "Number of Provinces: " << sol.findCircleNum(isConnected) << endl; 
    // Expected: 2 (Province 1: cities 0,1. Province 2: city 2)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V^2)`. The adjacency matrix is of size `V x V`. The DFS traverses the entire matrix once.
- **Space Complexity:** `O(V)` for the `visited` array and recursive call stack.
