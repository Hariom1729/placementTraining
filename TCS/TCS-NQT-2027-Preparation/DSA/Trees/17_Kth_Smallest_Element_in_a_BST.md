# Problem 17: Kth Smallest Element in a BST

## Problem Statement
Given the `root` of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

## Constraints
- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

---

## Approach: Inorder Traversal

A core property of a Binary Search Tree is that an **Inorder Traversal (Left, Root, Right)** visits the nodes in ascending sorted order.

1. Perform an inorder traversal.
2. Keep a counter variable. Every time we visit a node (after returning from the left subtree), increment the counter.
3. If the counter equals `k`, we have found the `k`th smallest element.
4. We can optimize by stopping the traversal once we find the element.

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
    void inorder(TreeNode* root, int k, int& count, int& result) {
        if (root == NULL || count >= k) return;
        
        // Traverse Left
        inorder(root->left, k, count, result);
        
        // Visit Root
        count++;
        if (count == k) {
            result = root->val;
            return; // Found it, stop searching further down this path
        }
        
        // Traverse Right
        inorder(root->right, k, count, result);
    }

public:
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        int result = -1;
        inorder(root, k, count, result);
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->left->left->left = new TreeNode(1);

    Solution sol;
    cout << "3rd smallest: " << sol.kthSmallest(root, 3) << endl; // Expected: 3
    cout << "1st smallest: " << sol.kthSmallest(root, 1) << endl; // Expected: 1

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(H + k)`. We go down to the leftmost leaf `O(H)` and then process `k` nodes. In the worst case (skewed tree where `k=N`), it's `O(N)`.
- **Space Complexity:** `O(H)` for the recursive call stack.
