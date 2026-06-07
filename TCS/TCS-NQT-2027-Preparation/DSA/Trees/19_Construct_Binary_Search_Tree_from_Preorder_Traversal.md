# Problem 19: Construct Binary Search Tree from Preorder Traversal

## Problem Statement
Given an array of integers preorder, which represents the `preorder` traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

## Constraints
- `1 <= preorder.length <= 100`
- `1 <= preorder[i] <= 10^8`
- All the values of `preorder` are unique.

---

## Approach: Upper Bound Recursion

A naïve approach is to insert elements one by one (`O(N \log N)` to `O(N^2)`). Another approach is to sort the preorder array to get the inorder array, then build the tree from both (`O(N \log N)`).
We can do it in `O(N)` time.

Since preorder is **Root -> Left -> Right**, the first element is the root. The subsequent elements that are smaller than the root belong to the left subtree, and the rest to the right subtree.
Instead of finding the boundary linearly, we pass down an **upper bound** constraint.
- For the left child, the upper bound is the `root->val`.
- For the right child, the upper bound is whatever the current node's upper bound was.
We maintain an index `i` that iterates through the `preorder` array.

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
    TreeNode* build(vector<int>& preorder, int& i, int upperBound) {
        if (i == preorder.size() || preorder[i] > upperBound) {
            return NULL;
        }
        
        TreeNode* root = new TreeNode(preorder[i++]);
        
        // Left subtree values must be less than the root's value
        root->left = build(preorder, i, root->val);
        
        // Right subtree values must be less than the parent's upper bound
        root->right = build(preorder, i, upperBound);
        
        return root;
    }

public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i = 0;
        return build(preorder, i, 1e9); // Pass a very large number as initial upper bound
    }
};

void inorderPrint(TreeNode* root) {
    if (!root) return;
    inorderPrint(root->left);
    cout << root->val << " ";
    inorderPrint(root->right);
}

int main() {
    vector<int> preorder = {8, 5, 1, 7, 10, 12};
    Solution sol;
    
    TreeNode* root = sol.bstFromPreorder(preorder);
    
    cout << "Inorder of constructed BST: ";
    inorderPrint(root); 
    cout << "\n"; // Expected: 1 5 7 8 10 12

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We process each element exactly once and move the pointer `i` forward.
- **Space Complexity:** `O(H)` for the recursive stack, where `H` is the height of the BST.
