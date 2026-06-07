# Problem 8: Lowest Common Ancestor of a Binary Tree

## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q` in the tree.
The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

---

## Approach: Recursive DFS

We can search for `p` and `q` starting from the root.
1. **Base Case:** If the current `root` is `NULL`, return `NULL`.
2. **Found Node:** If `root` is equal to `p` or `root` is equal to `q`, return `root` (this acts as a signal that we found one of the targets in this subtree).
3. **Recursive Search:** Recursively search the `left` subtree and the `right` subtree. Let the results be `leftLCA` and `rightLCA`.
4. **Determine LCA:**
   - If both `leftLCA` and `rightLCA` are NOT `NULL`, it means `p` is in one subtree and `q` is in the other. Thus, the current `root` MUST be the LCA. Return `root`.
   - If only one of them is NOT `NULL`, return that non-null value (passing the found signal up the tree).
   - If both are `NULL`, return `NULL`.

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
        // Base case
        if (root == NULL || root == p || root == q) {
            return root;
        }
        
        // Search left and right subtrees
        TreeNode* leftLCA = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightLCA = lowestCommonAncestor(root->right, p, q);
        
        // If both return non-null, this root is the LCA
        if (leftLCA != NULL && rightLCA != NULL) {
            return root;
        }
        
        // Otherwise return the non-null child (or NULL if both are NULL)
        if (leftLCA != NULL) return leftLCA;
        return rightLCA;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(8);
    root->left->right->left = new TreeNode(7);
    root->left->right->right = new TreeNode(4);

    Solution sol;
    TreeNode* p = root->left; // Node 5
    TreeNode* q = root->right; // Node 1
    
    TreeNode* lca = sol.lowestCommonAncestor(root, p, q);
    cout << "LCA of 5 and 1 is: " << lca->val << endl; // Expected: 3
    
    q = root->left->right->right; // Node 4
    lca = sol.lowestCommonAncestor(root, p, q);
    cout << "LCA of 5 and 4 is: " << lca->val << endl; // Expected: 5

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We visit each node at most once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the height of the tree.
