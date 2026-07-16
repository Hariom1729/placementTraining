# Lowest Common Ancestor of a Binary Tree

## Difficulty
Medium

## Asked In
Infosys SP (L2, L3)
Infosys DSE
Year: 2021, 2023
Frequency: Very High

---

## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

---

## Optimal Approach (DFS / Recursion)
**Detailed explanation:**
Traverse the tree using Post-order DFS.
If the current node is `null`, return `null`.
If the current node is `p` or `q`, return the current node.
Recursively find the LCA in the left and right subtrees.
- If both left and right return a non-null node, it means `p` is in one subtree and `q` is in the other. Thus, the current node is the LCA!
- If only one subtree returns a non-null node, return that non-null node upwards.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(H)$ where $H$ is the height of the tree (recursion stack).

---

## C++ Solution
```cpp
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    // Base Case
    if (root == NULL || root == p || root == q) {
        return root;
    }
    
    // Look for keys in left and right subtrees
    TreeNode* left_lca = lowestCommonAncestor(root->left, p, q);
    TreeNode* right_lca = lowestCommonAncestor(root->right, p, q);
    
    // If both return non-null, this node is the LCA
    if (left_lca != NULL && right_lca != NULL) {
        return root;
    }
    
    // Otherwise, return the non-null child
    return (left_lca != NULL) ? left_lca : right_lca;
}
```
