# Problem 3: Maximum Depth of Binary Tree

## Problem Statement
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach: Recursive DFS

The maximum depth of a tree is `1` plus the maximum of the depths of its left and right subtrees.
This can be defined recursively:
- **Base Case:** If the node is `NULL`, its depth is `0`.
- **Recursive Step:** Calculate the depth of the left subtree and the right subtree. The depth of the current node is `1 + max(left_depth, right_depth)`.

---

## C++ Solution

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        return 1 + max(leftDepth, rightDepth);
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution sol;
    cout << "Max Depth: " << sol.maxDepth(root) << endl; 
    // Expected: 3

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We visit each node exactly once.
- **Space Complexity:** `O(H)` where `H` is the height of the tree (for the recursion stack). In the worst case (skewed tree), space is `O(N)`. In a balanced tree, space is `O(\log N)`.
