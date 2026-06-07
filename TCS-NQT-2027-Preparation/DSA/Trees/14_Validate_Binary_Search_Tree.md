# Problem 14: Validate Binary Search Tree

## Problem Statement
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

---

## Approach: Valid Range (Min and Max)

A common mistake is to only check if `left < root` and `right > root`. This is incorrect because a node deep in the right subtree might be smaller than the main root, which violates BST properties.
Instead, we must pass down a **valid range** `[min_val, max_val]` for every node.

1. Create a helper function `isValidBST(node, min_val, max_val)`.
2. Initial call: `isValidBST(root, LONG_MIN, LONG_MAX)`. (We use `long long` to prevent overflow with `INT_MAX/MIN`).
3. If `node == NULL`, return `true`.
4. If `node->val <= min_val` OR `node->val >= max_val`, return `false`.
5. Recursively check the left subtree with the updated max limit: `isValidBST(node->left, min_val, node->val)`.
6. Recursively check the right subtree with the updated min limit: `isValidBST(node->right, node->val, max_val)`.
7. Return `left_valid && right_valid`.

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
    bool isValidBST(TreeNode* root, long long minVal, long long maxVal) {
        if (root == NULL) return true;
        
        if (root->val <= minVal || root->val >= maxVal) {
            return false;
        }
        
        return isValidBST(root->left, minVal, root->val) 
            && isValidBST(root->right, root->val, maxVal);
    }

public:
    bool isValidBST(TreeNode* root) {
        // Use long long to handle cases where node val is INT_MIN or INT_MAX
        return isValidBST(root, -10000000000LL, 10000000000LL); 
    }
};

int main() {
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4); // Invalid, should be > 5
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(6);

    Solution sol;
    cout << "Is Valid BST? " << (sol.isValidBST(root) ? "Yes" : "No") << endl; 
    // Expected: No

    TreeNode* root2 = new TreeNode(2);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(3);
    cout << "Is Valid BST? " << (sol.isValidBST(root2) ? "Yes" : "No") << endl; 
    // Expected: Yes

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We visit each node exactly once.
- **Space Complexity:** `O(H)` for the recursive stack.
