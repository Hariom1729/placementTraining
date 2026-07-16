# Symmetric Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees

## Pattern
DFS / Simultaneous Traversal

## Problem Statement
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a boolean: `true` if symmetric, `false` otherwise.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

**Example 2:**
```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Edge Cases
- Tree with a single node (is symmetric).
- Asymmetric trees where structure matches but values differ.
- Asymmetric trees where values match but structure differs (Example 2).

## Intuition
A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
This is heavily related to the "Same Tree" problem, but instead of checking if `Tree A == Tree B` identically, we check if `Tree A` is a MIRROR of `Tree B`.
Therefore, when we traverse, we must compare the **left** child of the left subtree with the **right** child of the right subtree, and the **right** child of the left subtree with the **left** child of the right subtree.

## Brute Force Approach
N/A - Checking corresponding nodes is the most optimal way.

## Optimal Approach
**Detailed explanation:**
We use a helper function that takes two nodes (representing the roots of the subtrees to compare).
1. **Base Cases:**
   - If both nodes are `nullptr`, they are symmetric (return `true`).
   - If one is `nullptr` and the other is not, they are asymmetric (return `false`).
   - If their values do not match, they are asymmetric (return `false`).
2. **Recursive Step:**
   - For a mirror image, the `left` child of node 1 must match the `right` child of node 2.
   - The `right` child of node 1 must match the `left` child of node 2.
   - We recursively return `checkSymmetry(n1->left, n2->right) && checkSymmetry(n1->right, n2->left)`.

**Time Complexity:** $O(N)$ because we potentially visit every node in the tree once.
**Space Complexity:** $O(H)$ for the recursion stack space, where $H$ is the height of the tree.

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

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        // An empty tree or single node tree is symmetric
        if (root == nullptr) return true;
        
        // Start the simultaneous mirrored traversal
        return checkSymmetry(root->left, root->right);
    }
    
private:
    bool checkSymmetry(TreeNode* leftNode, TreeNode* rightNode) {
        // If both are null, it's symmetric at this leaf
        if (leftNode == nullptr && rightNode == nullptr) {
            return true;
        }
        
        // If one is null but the other isn't, structurally asymmetric
        if (leftNode == nullptr || rightNode == nullptr) {
            return false;
        }
        
        // Values must match for symmetry
        if (leftNode->val != rightNode->val) {
            return false;
        }
        
        // Recursive check:
        // Left child of left tree MUST MATCH Right child of right tree
        // Right child of left tree MUST MATCH Left child of right tree
        return checkSymmetry(leftNode->left, rightNode->right) && 
               checkSymmetry(leftNode->right, rightNode->left);
    }
};
```

## Dry Run
Tree: `[1, 2, 2, 3, 4, 4, 3]`
- `isSymmetric(1)` calls `checkSymmetry(2, 2)`
- `checkSymmetry(2, 2)`:
  - Values match (2 == 2).
  - Checks outer pair: `checkSymmetry(2->left(3), 2->right(3))`
    - Values match (3 == 3). Children are null. Returns `true`.
  - Checks inner pair: `checkSymmetry(2->right(4), 2->left(4))`
    - Values match (4 == 4). Children are null. Returns `true`.
- Both checks return `true`. Overall result is `true`.

## Common Mistakes
- Using exactly the same code as "Same Tree" without swapping `left` and `right`. If you do `check(n1->left, n2->left)`, you are checking if the subtrees are *identical*, not *symmetric*.

## Similar Problems
- Same Tree
- Invert Binary Tree

## Infosys Variations
- Just like Same Tree, Infosys might ask for an Iterative approach. You can push pairs of nodes into a standard Queue, pop them two at a time, check if they mirror each other, and then push their children in mirrored order: `(node1->left, node2->right)` and `(node1->right, node2->left)`.
