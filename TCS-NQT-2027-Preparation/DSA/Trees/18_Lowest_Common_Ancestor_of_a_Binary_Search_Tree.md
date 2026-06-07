# Problem 18: Lowest Common Ancestor of a Binary Search Tree

## Problem Statement
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the BST.

---

## Approach: Iterative Traversal

Because this is a BST, we don't need to do a full DFS like we did for a regular Binary Tree.
We can use the BST property:
- If both `p` and `q` are **less than** the root, the LCA must be in the **left** subtree.
- If both `p` and `q` are **greater than** the root, the LCA must be in the **right** subtree.
- If one is less and the other is greater (or if one of them is equal to the root), we have found the split point. The current root **is** the LCA.

We can do this iteratively in `O(1)` auxiliary space.

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

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while (root != NULL) {
            // Both nodes are on the left
            if (p->val < root->val && q->val < root->val) {
                root = root->left;
            }
            // Both nodes are on the right
            else if (p->val > root->val && q->val > root->val) {
                root = root->right;
            }
            // Split point found (or one of the nodes is the root)
            else {
                return root;
            }
        }
        return NULL;
    }
};

int main() {
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(2);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(4);
    root->left->right->left = new TreeNode(3);
    root->left->right->right = new TreeNode(5);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);

    Solution sol;
    TreeNode* p = root->left; // Node 2
    TreeNode* q = root->right; // Node 8
    
    TreeNode* lca = sol.lowestCommonAncestor(root, p, q);
    cout << "LCA of 2 and 8 is: " << lca->val << endl; // Expected: 6
    
    q = root->left->right; // Node 4
    lca = sol.lowestCommonAncestor(root, p, q);
    cout << "LCA of 2 and 4 is: " << lca->val << endl; // Expected: 2

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(H)` where `H` is the height of the tree. We only traverse down one path.
- **Space Complexity:** `O(1)` as we use a while loop and no extra memory.
