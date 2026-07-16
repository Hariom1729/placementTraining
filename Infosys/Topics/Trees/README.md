# Trees

## Introduction
Trees are one of the most critical data structures asked in Infosys SP (Specialist Programmer) and DSE (Digital Specialist Engineer) coding rounds. Unlike Arrays or Strings which are linear, Trees introduce hierarchical data representations and heavily test a candidate's grasp of recursion, backtracking, and queue-based traversals. Infosys is highly likely to ask medium-to-hard level tree problems that require a solid understanding of both Depth First Search (DFS) and Breadth First Search (BFS).

## Binary Tree Basics
A Tree is a collection of nodes connected by edges. A Binary Tree is a tree where each node has at most two children, referred to as the left child and the right child.
Key terminologies:
- **Root:** The topmost node.
- **Leaf:** A node with no children.
- **Depth of a Node:** Number of edges from the root to the node.
- **Height of a Tree:** Number of edges on the longest path from root to a leaf.
- **Subtree:** A tree consisting of a node and its descendants.

## DFS vs BFS
When exploring a tree, you generally have two choices:
1. **Depth First Search (DFS):** Go deep before you go wide. Explore down a branch as far as possible before backtracking. Implemented naturally using Recursion (Call Stack) or an explicit Stack.
2. **Breadth First Search (BFS):** Go wide before you go deep. Explore all nodes at the current depth level before moving deeper. Implemented using a Queue.

## Traversal Techniques
- **Inorder (DFS):** Left -> Root -> Right (Yields sorted elements in a BST).
- **Preorder (DFS):** Root -> Left -> Right (Useful for copying a tree).
- **Postorder (DFS):** Left -> Right -> Root (Useful for deleting a tree, or bottom-up DP).
- **Level Order (BFS):** Level by level, from left to right.

## Recursive vs Iterative Solutions
- **Recursive:** Most tree problems can be solved recursively. It leads to clean, concise code. The space complexity is $O(H)$ where $H$ is the height of the tree, due to the call stack.
- **Iterative:** Sometimes required if the language has strict recursion limits or to avoid stack overflow on heavily skewed trees. Iterative DFS requires a `stack`, iterative BFS requires a `queue`. Iterative Inorder/Postorder traversals are common "Hard" variations of basic algorithms.

## Tree Patterns
- **DFS / Top-Down:** Passing state from parent down to children.
- **DFS / Bottom-Up (Tree DP):** Children return state up to the parent, and the parent computes its answer based on child results (e.g., Diameter, Maximum Path Sum).
- **BFS Level Order:** Using a queue and a size variable to process nodes level by level (e.g., Zigzag, Right View).
- **Coordinate Traversal:** Tracking horizontal distance (X) and vertical depth (Y) for Vertical Order and Top/Bottom views.
- **Serialization:** Converting a tree into a string and back to a tree.

## Complexity Table

| Operation | Average Case | Worst Case (Skewed Tree) |
|-----------|--------------|--------------------------|
| DFS Time | $O(N)$ | $O(N)$ |
| DFS Space | $O(\log N)$ | $O(N)$ |
| BFS Time | $O(N)$ | $O(N)$ |
| BFS Space | $O(W)$ (Width) | $O(N/2)$ = $O(N)$ |

## Interview Tips
- **Always check for null:** The first line of any recursive function should usually be `if (root == nullptr) return ...;`
- **Draw the recursion tree:** If you get stuck on a Tree DP problem, draw the nodes and explicitly write what the left child returns and what the right child returns.
- **Don't forget the base cases:** Leaf nodes and null nodes.
- **Understand Time/Space trade-offs:** Morris Traversal achieves $O(1)$ space by temporarily modifying the tree structure. Mention this in interviews for extra points!

## Common Mistakes
- Not realizing that the space complexity of a recursive tree algorithm is $O(H)$, where $H$ is the height of the tree. In the worst case (a linked list), $O(H)$ becomes $O(N)$.
- Modifying tree pointers carelessly and creating cycles.
- Forgetting to handle the edge case where the root itself is null.

## Most Repeated Infosys Tree Questions
1. Diameter of Binary Tree
2. Binary Tree Maximum Path Sum
3. Vertical Order Traversal
4. Lowest Common Ancestor
5. Boundary Traversal
6. Serialize and Deserialize Binary Tree

## Revision Checklist
- [ ] Understand all 3 recursive DFS traversals
- [ ] Write Iterative Preorder, Inorder, and Postorder
- [ ] Implement BFS Level Order Traversal
- [ ] Understand Top, Bottom, Left, and Right Views
- [ ] Master Tree DP (Bottom-up recursion returning multiple states)
- [ ] Understand how to track paths from Root to Node

## Preparation Roadmap
1. Start with basic Traversals and simple recursion (Max Depth, Same Tree).
2. Move to BFS problems (Level Order, Zigzag, Right View).
3. Tackle Coordinate-based problems (Vertical Order, Top/Bottom views).
4. Master Advanced Tree DP (Diameter, Max Path Sum, House Robber III).
5. Finish with Construction and Modification (Serialize/Deserialize, Flatten, Burn Tree).

## List of All Problems

| No | Problem | Difficulty |
|----|----------|------------|
|01|Maximum Depth of Binary Tree|Medium|
|02|Diameter of Binary Tree|Medium|
|03|Balanced Binary Tree|Medium|
|04|Same Tree|Medium|
|05|Symmetric Tree|Medium|
|06|Binary Tree Level Order Traversal|Medium|
|07|Zigzag Level Order Traversal|Medium|
|08|Lowest Common Ancestor of a Binary Tree|Medium|
|09|Path Sum|Medium|
|10|Binary Tree Maximum Path Sum|Hard|
|11|Boundary Traversal of Binary Tree|Medium-Hard|
|12|Vertical Order Traversal of a Binary Tree|Hard|
|13|Top View of Binary Tree|Medium|
|14|Bottom View of Binary Tree|Medium|
|15|Right View of Binary Tree|Medium|
|16|Left View of Binary Tree|Medium|
|17|Diagonal Traversal of Binary Tree|Medium-Hard|
|18|Flatten Binary Tree to Linked List|Medium-Hard|
|19|Construct Binary Tree from Preorder and Inorder|Medium-Hard|
|20|Construct Binary Tree from Inorder and Postorder|Medium-Hard|
|21|Serialize and Deserialize Binary Tree|Hard|
|22|All Nodes Distance K in Binary Tree|Hard|
|23|Minimum Time to Burn a Tree|Hard|
|24|Count Complete Tree Nodes|Medium-Hard|
|25|Check Completeness of a Binary Tree|Medium-Hard|
|26|Cousins in Binary Tree|Medium|
|27|Maximum Width of Binary Tree|Medium-Hard|
|28|Children Sum Property|Medium|
|29|Validate Binary Search Tree|Medium|
|30|Recover Binary Search Tree|Hard|
|31|Morris Traversal Inorder|Hard|
|32|Binary Tree Cameras|Hard|
|33|House Robber III|Medium-Hard|
|34|Longest Zigzag Path in a Binary Tree|Medium-Hard|
|35|Maximum Ancestor Difference|Medium|
|36|Smallest String Starting from Leaf|Medium|
|37|Binary Tree Coloring Game|Medium-Hard|
|38|Amount of Time for Binary Tree to Be Infected|Medium-Hard|
|39|Lowest Common Ancestor of a BST|Medium|
|40|Invert Binary Tree|Easy-Medium|
|41|Kth Smallest Element in a BST|Medium|
|42|Two Sum IV - Input is a BST|Medium|
