# Problem 10: Course Schedule II

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`

---

## Approach: Topological Sort (Kahn's Algorithm)

This is a direct extension of Course Schedule I. Instead of just returning `true` or `false`, we need to return the actual topological ordering.

1. Construct the Adjacency List `adj` and the `inDegree` array.
2. Push all nodes with `inDegree == 0` into a queue.
3. Maintain a `result` vector.
4. While queue is not empty:
   - Pop a `node`. 
   - Add it to the `result` vector.
   - Iterate over its neighbors. For each neighbor, decrement its `inDegree`.
   - If a neighbor's `inDegree` becomes `0`, push it to the queue.
5. If `result.size() == numCourses`, return `result`.
6. Otherwise, return an empty array (cycle detected).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> adj[numCourses];
        vector<int> inDegree(numCourses, 0);
        
        // Build graph: prereq -> course
        for (auto it : prerequisites) {
            adj[it[1]].push_back(it[0]);
            inDegree[it[0]]++;
        }
        
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            result.push_back(node);
            
            for (int neighbor : adj[node]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        if (result.size() == numCourses) {
            return result;
        }
        return {}; // Cycle detected
    }
};

int main() {
    Solution sol;
    int numCourses = 4;
    vector<vector<int>> prerequisites = {{1,0}, {2,0}, {3,1}, {3,2}};
    
    vector<int> order = sol.findOrder(numCourses, prerequisites);
    
    cout << "Course Order: ";
    if (order.empty()) {
        cout << "Impossible";
    } else {
        for (int x : order) cout << x << " ";
    }
    cout << endl;
    // Expected: 0 1 2 3 (or 0 2 1 3)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`.
- **Space Complexity:** `O(V + E)`.
