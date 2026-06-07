# Problem 4: Diameter of Binary Tree

## Problem Statement
Given the `root` of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of **edges** between them.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach: DFS (Modified Max Depth)

The diameter of a tree passing through a specific node is the sum of the maximum depth of its left subtree and the maximum depth of its right subtree (in terms of nodes, edges is nodes - 1).
To find the overall diameter, we can calculate the diameter at *every* node and keep track of the maximum value found.

Instead of computing the depth separately for every node (which would be `O(N^2)`), we can modify the `maxDepth` function to compute the depth AND update the global maximum diameter in a single `O(N)` pass.

1. Maintain a global variable `max_diameter = 0`.
2. Write a recursive function `height(node)`:
   - If `node == NULL`, return `0`.
   - Compute `lh = height(node->left)` and `rh = height(node->right)`.
   - Update the global maximum: `max_diameter = max(max_diameter, lh + rh)`.
   - Return the height of the current node: `1 + max(lh, rh)`.
3. Return `max_diameter`.

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
private:
    int height(TreeNode* root, int& max_diameter) {
        if (root == NULL) {
            return 0;
        }
        
        int lh = height(root->left, max_diameter);
        int rh = height(root->right, max_diameter);
        
        // The path length passing through the current root is lh + rh (number of edges)
        max_diameter = max(max_diameter, lh + rh);
        
        // Return height of the subtree
        return 1 + max(lh, rh);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diameter = 0;
        height(root, max_diameter);
        return max_diameter;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    Solution sol;
    cout << "Diameter: " << sol.diameterOfBinaryTree(root) << endl; 
    // Expected: 3 (Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We visit each node exactly once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the tree height.
