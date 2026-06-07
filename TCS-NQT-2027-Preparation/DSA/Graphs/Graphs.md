# Graphs

## 1. Theory & Core Concepts

A **Graph** is a non-linear data structure consisting of **Nodes (or Vertices)** and **Edges** that connect these nodes.
Graphs can be:
- **Directed or Undirected:** Edges have a direction or are bidirectional.
- **Weighted or Unweighted:** Edges have a cost/weight or all edges cost the same (typically 1).
- **Cyclic or Acyclic:** Contains cycles or does not. A Directed Acyclic Graph is called a **DAG**.

### Graph Representation in C++
There are two main ways to represent a graph:
1. **Adjacency Matrix:** A 2D array `adj[V][V]`. `adj[i][j] = 1` if there is an edge between `i` and `j`. Uses `O(V^2)` space.
2. **Adjacency List:** An array of vectors `vector<int> adj[V]`. `adj[i]` contains all nodes connected to `i`. Uses `O(V + E)` space. **(Most common and efficient)**.

```cpp
// Building an Adjacency List for an Undirected Graph
vector<int> adj[V];
for(int i=0; i<E; i++){
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u); // Remove this line for a Directed Graph
}
```

### Common Interview Patterns
1. **Traversals:** 
   - **BFS (Breadth-First Search):** Uses a Queue. Good for finding the shortest path in unweighted graphs.
   - **DFS (Depth-First Search):** Uses Recursion (Call Stack). Good for exploring all paths, cycle detection, and topological sorting.
2. **Connected Components:** Finding groups of nodes that are connected to each other but isolated from the rest of the graph.
3. **Cycle Detection:** Checking if a graph has a cycle using BFS or DFS.
4. **Topological Sort:** Ordering of nodes in a DAG such that for every directed edge `u -> v`, `u` comes before `v`. (Kahn's Algorithm).
5. **Shortest Paths:**
   - **Dijkstra's Algorithm:** Shortest path from a single source to all other nodes (no negative weights).
   - **Bellman-Ford Algorithm:** Single source shortest path, handles negative weights.
   - **Floyd-Warshall Algorithm:** All-pairs shortest path.
6. **Minimum Spanning Tree (MST):** Prim's Algorithm or Kruskal's Algorithm.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_BFS_of_Graph.md`
*   `02_DFS_of_Graph.md`
*   `03_Number_of_Provinces.md`
*   `04_Rotting_Oranges.md`
*   `05_Detect_Cycle_in_Undirected_Graph.md`
*   *(... and 15 more)*
