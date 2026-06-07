# Problem 13: Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Constraints
- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.

---

## Approach: Hash Map + Recursion

1. **Preorder:** The first element is ALWAYS the root of the tree.
2. **Inorder:** The root splits the inorder array into two halves: the left subtree elements and the right subtree elements.
3. We can use a Hash Map to store the indices of elements in the `inorder` array so we can find the root's position in `O(1)` time.
4. We build a recursive function `buildTree(preorder, preStart, preEnd, inorder, inStart, inEnd, inMap)`.
   - The root is `preorder[preStart]`.
   - Find this root in `inMap` to get its index `inRoot`.
   - The number of elements in the left subtree is `numsLeft = inRoot - inStart`.
   - Recursively build the left child: `preStart + 1` to `preStart + numsLeft`.
   - Recursively build the right child: `preStart + numsLeft + 1` to `preEnd`.
   - Return the root.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    TreeNode* buildTreeHelper(vector<int>& preorder, int preStart, int preEnd,
                              vector<int>& inorder, int inStart, int inEnd,
                              unordered_map<int, int>& inMap) {
        
        if (preStart > preEnd || inStart > inEnd) return NULL;
        
        // Root is the first element in current preorder segment
        TreeNode* root = new TreeNode(preorder[preStart]);
        
        // Find root in inorder to split left and right subtrees
        int inRoot = inMap[root->val];
        int numsLeft = inRoot - inStart;
        
        // Recursive calls
        root->left = buildTreeHelper(preorder, preStart + 1, preStart + numsLeft, 
                                     inorder, inStart, inRoot - 1, inMap);
                                     
        root->right = buildTreeHelper(preorder, preStart + numsLeft + 1, preEnd, 
                                      inorder, inRoot + 1, inEnd, inMap);
                                      
        return root;
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inMap;
        for (int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }
        
        return buildTreeHelper(preorder, 0, preorder.size() - 1, 
                               inorder, 0, inorder.size() - 1, inMap);
    }
};

void inorderPrint(TreeNode* root) {
    if (!root) return;
    inorderPrint(root->left);
    cout << root->val << " ";
    inorderPrint(root->right);
}

int main() {
    Solution sol;
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};
    
    TreeNode* root = sol.buildTree(preorder, inorder);
    
    cout << "Inorder of constructed tree: ";
    inorderPrint(root);
    cout << "\n"; // Expected: 9 3 15 20 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` to build the Hash Map, and `O(N)` to construct the tree because we visit each node exactly once. Overall `O(N)`.
- **Space Complexity:** `O(N)` for the Hash Map and `O(H)` for the recursive stack.
