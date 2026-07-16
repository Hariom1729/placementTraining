# Boundary Traversal of Binary Tree

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Samsung, MakeMyTrip

## Topic
Trees

## Pattern
Custom Traversal (DFS/BFS combination)

## Problem Statement
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 
1. **Left boundary nodes:** defined as the path from the root to the left-most node. If the root doesn't have a left child, then only the root is the left boundary.
2. **Leaf nodes:** all the leaf nodes in the tree from left to right.
3. **Right boundary nodes:** defined as the path from the right-most node to the root. If the root doesn't have a right child, then only the root is the right boundary.

The root node should be included exactly once. If the tree has only a root, just return the root. Do not duplicate nodes if they appear in multiple boundaries (e.g., a left-most node that is also a leaf).

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-1000 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the boundary traversal.

## Sample Test Cases

**Example 1:**
```
Input: root = [1, 2, 3, 4, 5, 6, 7, null, null, 8, 9]
Output: [1, 2, 4, 8, 9, 6, 7, 3]
```

**Example 2:**
```
Input: root = [1, null, 2, 3, 4]
Output: [1, 3, 4, 2]
```

## Edge Cases
- A tree with only the root node.
- A completely skewed left or right tree.

## Intuition
The problem clearly divides the task into three separate modular parts:
1. Extract the left boundary (excluding leaves so we don't duplicate them).
2. Extract all leaves using standard DFS (Preorder or Inorder) to guarantee left-to-right ordering.
3. Extract the right boundary (excluding leaves) and reverse it, because we need it from bottom to top.

## Brute Force Approach
N/A - The modular approach is the standard and most intuitive way to solve this.

## Optimal Approach
**Detailed explanation:**
We will use an array `ans` to store the result.
1. **Root Check:** If the root is `nullptr`, return `ans`.
2. **Handle Root:** If the root is NOT a leaf, add `root->val` to `ans`. (If it is a leaf, it will be caught by the leaf collection step).
3. **Left Boundary:** 
   - Start from `root->left`.
   - While the node is not null:
     - If it's not a leaf, add it to `ans`.
     - Move to the left child. If the left child doesn't exist, move to the right child (it is still part of the left boundary).
4. **Leaves:**
   - Use a simple DFS (Preorder) to traverse the whole tree.
   - If a node is a leaf (left and right are null), add it to `ans`.
5. **Right Boundary:**
   - Start from `root->right`.
   - Create a temporary vector `temp`.
   - While the node is not null:
     - If it's not a leaf, add it to `temp`.
     - Move to the right child. If the right child doesn't exist, move to the left child.
   - Finally, iterate `temp` backwards and add elements to `ans` (to get bottom-up order).

**Time Complexity:** $O(N)$. The left boundary takes $O(H)$, right boundary takes $O(H)$, and collecting leaves takes $O(N)$. Overall $O(N)$.
**Space Complexity:** $O(N)$ for the recursion stack during leaf collection and storing the final answer.

## C++ Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <vector>
using namespace std;

class Solution {
    bool isLeaf(TreeNode* node) {
        return node->left == nullptr && node->right == nullptr;
    }
    
    void addLeftBoundary(TreeNode* root, vector<int>& res) {
        TreeNode* curr = root->left;
        while (curr != nullptr) {
            if (!isLeaf(curr)) res.push_back(curr->val);
            if (curr->left != nullptr) curr = curr->left;
            else curr = curr->right;
        }
    }
    
    void addRightBoundary(TreeNode* root, vector<int>& res) {
        TreeNode* curr = root->right;
        vector<int> temp;
        while (curr != nullptr) {
            if (!isLeaf(curr)) temp.push_back(curr->val);
            if (curr->right != nullptr) curr = curr->right;
            else curr = curr->left;
        }
        // Add in reverse order for bottom-up
        for (int i = temp.size() - 1; i >= 0; i--) {
            res.push_back(temp[i]);
        }
    }
    
    void addLeaves(TreeNode* root, vector<int>& res) {
        if (root == nullptr) return;
        if (isLeaf(root)) {
            res.push_back(root->val);
            return;
        }
        addLeaves(root->left, res);
        addLeaves(root->right, res);
    }
    
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) return res;
        
        // Add root (if it's not a leaf)
        if (!isLeaf(root)) {
            res.push_back(root->val);
        }
        
        addLeftBoundary(root, res);
        addLeaves(root, res);
        addRightBoundary(root, res);
        
        return res;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5]` (Nodes 4, 5 are children of 2).
- Root 1 is not a leaf. `res = [1]`.
- **Left Boundary:** Start at 2. It's not a leaf. `res = [1, 2]`. Move to 4 (leaf). Break loop.
- **Leaves:** `addLeaves(1)`.
  - Goes to 2 -> 4. 4 is leaf. `res = [1, 2, 4]`.
  - Goes to 5. 5 is leaf. `res = [1, 2, 4, 5]`.
  - Goes to 3. 3 is leaf. `res = [1, 2, 4, 5, 3]`.
- **Right Boundary:** Start at 3. 3 is a leaf, break loop.
Result: `[1, 2, 4, 5, 3]`.

## Common Mistakes
- **Adding the root twice:** If the root is the ONLY node in the tree (it is a leaf), you might add it in step 1, and then again in the leaf collection step. The `if (!isLeaf(root))` check at the very beginning perfectly handles this.
- **Failing to check the alternate child in boundaries:** In the left boundary, if a node has no left child, you MUST traverse to its right child (because that right child is now part of the boundary). `if (curr->left) curr = curr->left; else curr = curr->right;` is required.

## Similar Problems
- Binary Tree Right Side View
- Zigzag Level Order Traversal
