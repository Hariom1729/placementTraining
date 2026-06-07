# Trees (Binary Trees & Binary Search Trees)

## 1. Theory & Core Concepts

A **Tree** is a hierarchical data structure consisting of nodes connected by edges. The top node is called the **Root**.
A **Binary Tree** is a tree where each node has at most two children (left child and right child).

A **Binary Search Tree (BST)** is a special type of Binary Tree with the following properties:
1. The left subtree of a node contains only nodes with keys lesser than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. The left and right subtrees must also be binary search trees.

### Tree Node Structure in C++
```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
```

### Common Interview Patterns
1. **Traversals:** 
   - **DFS (Depth-First Search):** Preorder (Root, Left, Right), Inorder (Left, Root, Right), Postorder (Left, Right, Root). *Note: Inorder traversal of a BST yields a sorted array.*
   - **BFS (Breadth-First Search):** Level Order Traversal (using a Queue).
2. **Recursion:** Most tree problems are solved elegantly using recursion. Always think about base cases (e.g., `if (!root) return;`).
3. **Paths:** Finding paths from root to leaf, or between any two nodes.
4. **Lowest Common Ancestor (LCA):** Finding the lowest node that has both `p` and `q` as descendants.
5. **Views:** Top view, Bottom view, Left view, Right view.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Inorder_Preorder_Postorder_Traversals.md`
*   `02_Level_Order_Traversal.md`
*   `03_Maximum_Depth_of_Binary_Tree.md`
*   `04_Diameter_of_Binary_Tree.md`
*   `05_Check_if_Tree_is_Balanced.md`
*   *(... and 15 more)*
