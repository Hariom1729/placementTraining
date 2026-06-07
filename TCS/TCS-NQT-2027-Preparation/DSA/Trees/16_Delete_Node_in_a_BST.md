# Problem 16: Delete Node in a BST

## Problem Statement
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a unique value.
- `-10^5 <= key <= 10^5`

---

## Approach: Recursive Search and Replace

When we find the node to delete, there are 3 cases:
1. **Node is a leaf:** Simply delete it and return `NULL`.
2. **Node has one child:** Return the non-null child to the parent so it takes the place of the deleted node.
3. **Node has two children:** We can't simply delete it. We must find its **Inorder Successor** (the smallest value in its right subtree) or **Inorder Predecessor**. Let's use the successor.
   - Replace the node's value with the successor's value.
   - Recursively delete the successor in the right subtree.

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
    TreeNode* findMin(TreeNode* root) {
        while (root->left != NULL) {
            root = root->left;
        }
        return root;
    }

public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == NULL) return NULL; // Not found
        
        // 1. Search for the node
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } 
        // 2. Node found
        else {
            // Case 1 & 2: Node with only one child or no child
            if (root->left == NULL) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == NULL) {
                TreeNode* temp = root->left;
                delete root;
                return temp;
            }
            
            // Case 3: Node with two children
            // Get the inorder successor (smallest in the right subtree)
            TreeNode* temp = findMin(root->right);
            
            // Copy the inorder successor's content to this node
            root->val = temp->val;
            
            // Delete the inorder successor
            root->right = deleteNode(root->right, temp->val);
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
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->right->right = new TreeNode(7);

    Solution sol;
    cout << "Original Inorder: "; inorderPrint(root); cout << "\n";
    
    root = sol.deleteNode(root, 3);
    
    cout << "Inorder after deleting 3: "; inorderPrint(root); cout << "\n";
    // Expected: 2 4 5 6 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(H)` where `H` is the height of the tree.
- **Space Complexity:** `O(H)` for the recursive call stack.
