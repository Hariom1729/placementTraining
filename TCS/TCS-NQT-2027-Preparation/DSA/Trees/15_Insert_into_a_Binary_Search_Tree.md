# Problem 15: Insert into a Binary Search Tree

## Problem Statement
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

## Constraints
- The number of nodes in the tree will be in the range `[0, 10^4]`.
- `-10^8 <= Node.val <= 10^8`
- All the values `Node.val` are unique.
- `-10^8 <= val <= 10^8`
- It's guaranteed that `val` does not exist in the original BST.

---

## Approach: Iterative Traversal

We can traverse the BST according to its properties (go left if value is smaller, go right if value is greater) until we hit a `NULL` pointer. We insert the new node at that `NULL` position.

1. If `root == NULL`, return a new `TreeNode(val)`.
2. Keep a `curr` pointer starting at `root`.
3. Loop infinitely (`while(true)`):
   - If `val < curr->val`:
     - If `curr->left != NULL`, move `curr = curr->left`.
     - Else, `curr->left = new TreeNode(val)`, and `break`.
   - If `val > curr->val`:
     - If `curr->right != NULL`, move `curr = curr->right`.
     - Else, `curr->right = new TreeNode(val)`, and `break`.
4. Return `root`.

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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (root == NULL) return new TreeNode(val);
        
        TreeNode* curr = root;
        
        while (true) {
            if (curr->val <= val) { // Target is greater, go right
                if (curr->right != NULL) {
                    curr = curr->right;
                } else {
                    curr->right = new TreeNode(val);
                    break;
                }
            } else { // Target is smaller, go left
                if (curr->left != NULL) {
                    curr = curr->left;
                } else {
                    curr->left = new TreeNode(val);
                    break;
                }
            }
        }
        
        return root;
    }
};

void inorderPrint(TreeNode* root) {
    if (!root) return;
    inorderPrint(root->left);
    cout << root->val << " ";
    inorderPrint(root->right);
}

int main() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);

    Solution sol;
    root = sol.insertIntoBST(root, 5);
    
    cout << "Inorder after insertion: ";
    inorderPrint(root);
    cout << "\n"; // Expected: 1 2 3 4 5 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(H)` where `H` is the height of the BST. In worst case (skewed tree), it's `O(N)`. In a balanced BST, it's `O(\log N)`.
- **Space Complexity:** `O(1)` as we only use a few pointers.
