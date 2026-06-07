# Problem 1: Inorder, Preorder, Postorder Traversals

## Problem Statement
Given the `root` of a binary tree, return the inorder, preorder, and postorder traversals of its nodes' values.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Approach: Recursive Traversals

The most straightforward way to traverse a tree is using recursion.
1. **Preorder (Root, Left, Right):** Visit the current node, then recursively traverse the left subtree, then the right subtree.
2. **Inorder (Left, Root, Right):** Recursively traverse the left subtree, then visit the current node, then the right subtree.
3. **Postorder (Left, Right, Root):** Recursively traverse the left subtree, then the right subtree, then visit the current node.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    void preorder(TreeNode* root, vector<int>& res) {
        if (root == NULL) return;
        res.push_back(root->val);      // Root
        preorder(root->left, res);     // Left
        preorder(root->right, res);    // Right
    }

    void inorder(TreeNode* root, vector<int>& res) {
        if (root == NULL) return;
        inorder(root->left, res);      // Left
        res.push_back(root->val);      // Root
        inorder(root->right, res);     // Right
    }

    void postorder(TreeNode* root, vector<int>& res) {
        if (root == NULL) return;
        postorder(root->left, res);    // Left
        postorder(root->right, res);   // Right
        res.push_back(root->val);      // Root
    }

public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder(root, res);
        return res;
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        return res;
    }

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorder(root, res);
        return res;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

    Solution sol;
    
    vector<int> pre = sol.preorderTraversal(root);
    vector<int> in = sol.inorderTraversal(root);
    vector<int> post = sol.postorderTraversal(root);

    cout << "Preorder: "; for(int x : pre) cout << x << " "; cout << "\n"; // 1 2 3
    cout << "Inorder: "; for(int x : in) cout << x << " "; cout << "\n";   // 1 3 2
    cout << "Postorder: "; for(int x : post) cout << x << " "; cout << "\n"; // 3 2 1

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` for each traversal, where `N` is the number of nodes. We visit each node exactly once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the height of the tree. In the worst case (skewed tree), `O(N)`. In the best case (balanced tree), `O(\log N)`.
