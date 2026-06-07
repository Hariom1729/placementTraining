# Problem 5: Check if Tree is Balanced

## Problem Statement
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

---

## Approach: DFS (Modified Max Depth)

Similar to the Diameter problem, we can avoid an `O(N^2)` solution by checking for balance *while* computing the height.
We can write a recursive function `checkHeight(node)`:
- If `node == NULL`, return `0`.
- Get the height of the left subtree: `lh = checkHeight(node->left)`.
  - If `lh == -1` (meaning the left subtree is unbalanced), return `-1` to propagate the failure up.
- Get the height of the right subtree: `rh = checkHeight(node->right)`.
  - If `rh == -1` (meaning the right subtree is unbalanced), return `-1`.
- If the absolute difference between `lh` and `rh` is greater than 1, it means the current node is unbalanced. Return `-1`.
- Otherwise, return the height of the current node: `1 + max(lh, rh)`.

If the final call to `checkHeight(root)` returns `-1`, the tree is unbalanced; otherwise, it is balanced.

---

## C++ Solution

```cpp
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    int checkHeight(TreeNode* root) {
        if (root == NULL) return 0;
        
        int lh = checkHeight(root->left);
        if (lh == -1) return -1; // Left subtree is unbalanced
        
        int rh = checkHeight(root->right);
        if (rh == -1) return -1; // Right subtree is unbalanced
        
        // If current node is unbalanced
        if (abs(lh - rh) > 1) return -1;
        
        return 1 + max(lh, rh); // Return height
    }

public:
    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution sol;
    cout << "Is Balanced? " << (sol.isBalanced(root) ? "Yes" : "No") << endl; 
    // Expected: Yes

    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->left->left = new TreeNode(3);
    root2->left->left->left = new TreeNode(4);
    cout << "Is Balanced? " << (sol.isBalanced(root2) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` because we visit every node exactly once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the height of the tree.
