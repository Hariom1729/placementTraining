# Problem 7: Symmetric Tree

## Problem Statement
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

---

## Approach: Recursive DFS

A tree is symmetric if its left subtree is a mirror reflection of its right subtree.
Two trees are a mirror reflection of each other if:
1. Their two roots have the same value.
2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

We can write a helper function `isMirror(node1, node2)`:
- **Base Cases:**
  1. If both are `NULL`, return `true`.
  2. If one is `NULL` and the other is not, return `false`.
  3. If values don't match, return `false`.
- **Recursive Step:** Return `isMirror(node1->left, node2->right)` AND `isMirror(node1->right, node2->left)`.

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
private:
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL && t2 == NULL) return true;
        if (t1 == NULL || t2 == NULL) return false;
        
        return (t1->val == t2->val)
            && isMirror(t1->left, t2->right)
            && isMirror(t1->right, t2->left);
    }

public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return isMirror(root->left, root->right);
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    Solution sol;
    cout << "Is Symmetric? " << (sol.isSymmetric(root) ? "Yes" : "No") << endl; 
    // Expected: Yes

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes in the tree. We visit each node exactly once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the height of the tree.
