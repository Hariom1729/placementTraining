# Problem 9: Course Schedule

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.
Return `true` if you can finish all courses. Otherwise, return `false`.

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`

---

## Approach: Topological Sort (Kahn's Algorithm - BFS)

This problem boils down to checking if a **cycle exists in a Directed Graph**. If there's a cycle (e.g., A needs B, B needs C, C needs A), you can never finish the courses.
Topological Sorting can only be done on Directed Acyclic Graphs (DAG). Kahn's algorithm uses BFS based on **In-degree**.

1. Construct an Adjacency List from the `prerequisites`. For `[a, b]`, it's an edge `b -> a`.
2. Compute the `inDegree` for each node (number of incoming edges).
3. Push all nodes with `inDegree == 0` into a queue (these courses have no prerequisites).
4. Maintain a `count` of processed nodes.
5. While queue is not empty:
   - Pop a `node`. Increment `count`.
   - Iterate over its neighbors. For each neighbor, decrement its `inDegree`.
   - If a neighbor's `inDegree` becomes `0`, push it to the queue.
6. If `count == numCourses`, return `true` (Topological sort was possible, no cycle).
7. If `count < numCourses`, return `false` (Cycle detected).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> adj[numCourses];
        vector<int> inDegree(numCourses, 0);
        
        // Build graph and calculate in-degrees
        for (auto it : prerequisites) {
            int course = it[0];
            int prereq = it[1];
            adj[prereq].push_back(course); // prereq -> course
            inDegree[course]++;
        }
        
        queue<int> q;
        // Push all nodes with 0 in-degree
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        int count = 0;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;
            
            for (int neighbor : adj[node]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        return count == numCourses;
    }
};

int main() {
    Solution sol;
    int numCourses1 = 2;
    vector<vector<int>> prerequisites1 = {{1, 0}};
    cout << "Can Finish? " << (sol.canFinish(numCourses1, prerequisites1) ? "Yes" : "No") << endl; 
    // Expected: Yes (Take 0, then 1)
    
    int numCourses2 = 2;
    vector<vector<int>> prerequisites2 = {{1, 0}, {0, 1}};
    cout << "Can Finish? " << (sol.canFinish(numCourses2, prerequisites2) ? "Yes" : "No") << endl; 
    // Expected: No (Cycle)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(V + E)`. Building the graph takes `O(E)`. The queue processes each vertex and edge once.
- **Space Complexity:** `O(V + E)` for the adjacency list, in-degree array, and queue.
