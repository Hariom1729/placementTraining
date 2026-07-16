# Validate Binary Search Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Google, Facebook

## Topic
Trees / BST

## Pattern
DFS / Inorder Traversal

## Problem Statement
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a boolean indicating whether it is a valid BST.

## Sample Test Cases

**Example 1:**
```
Input: root = [2,1,3]
Output: true
```

**Example 2:**
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Edge Cases
- Node values can be exactly `INT_MAX` or `INT_MIN`. We must use `long long` for our boundaries to avoid overflow during comparisons.
- Trees where the immediate children are valid, but a deeply nested child violates the overall root's boundary (e.g., `root = 5, right = 8, right->left = 4`. The 4 is less than 8, which is fine, but it is ALSO less than 5, which violates the BST rule for the root 5).

## Intuition
A binary tree is a valid BST if every node falls within a specific valid range `(minValue, maxValue)`.
When we go to the **left** child, the maximum allowed value becomes the parent's value. `(min, parent.val)`.
When we go to the **right** child, the minimum allowed value becomes the parent's value. `(parent.val, max)`.
If any node violates its allowed range, it's not a BST.

Alternatively, the **Inorder Traversal** of a valid BST is ALWAYS strictly increasing. We can do an Inorder traversal and keep track of the previously visited node's value. If the current node's value is less than or equal to the previous, it's invalid.

## Brute Force Approach
**Explanation:** For every node, recursively check if the maximum value in its left subtree is less than the node, and the minimum value in its right subtree is greater than the node.
**Time Complexity:** $O(N^2)$ because we repeatedly traverse subtrees to find min/max.
**Space Complexity:** $O(H)$

## Optimal Approach (Range Checking)
**Detailed explanation:**
1. Create a helper function `isValid(TreeNode* root, long long minVal, long long maxVal)`.
2. **Base Case:** If `root == nullptr`, return `true`.
3. Check if the current node's value is strictly within the allowed range. If `root->val <= minVal` or `root->val >= maxVal`, return `false`.
4. Recursively check the left and right subtrees:
   - For the left subtree, the new range is `(minVal, root->val)`.
   - For the right subtree, the new range is `(root->val, maxVal)`.
5. The tree is valid only if BOTH subtrees are valid, so return `isValid(left) && isValid(right)`.
6. Initially, call the helper with the absolute minimum and maximum `long long` values: `isValid(root, LONG_MIN, LONG_MAX)`.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(H)$ where $H$ is the height of the tree for the recursion stack.

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

#include <climits>
using namespace std;

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // Use LONG_MIN and LONG_MAX to handle edge cases where 
        // node values are exactly INT_MIN or INT_MAX.
        return isValid(root, LONG_MIN, LONG_MAX);
    }
    
private:
    bool isValid(TreeNode* node, long long minVal, long long maxVal) {
        if (node == nullptr) {
            return true;
        }
        
        // Check if current node violates the min/max constraints
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        // Recursively check left and right subtrees with updated constraints.
        // Left child must be smaller than current node's value (maxVal = node->val).
        // Right child must be larger than current node's value (minVal = node->val).
        return isValid(node->left, minVal, node->val) && 
               isValid(node->right, node->val, maxVal);
    }
};
```

## Alternative Optimal Approach (Inorder Traversal)
```cpp
class Solution {
    long long prev = LONG_MIN;
public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) return true;
        
        // Traverse left
        if (!isValidBST(root->left)) return false;
        
        // Process current node
        if (root->val <= prev) return false;
        prev = root->val;
        
        // Traverse right
        return isValidBST(root->right);
    }
};
```

## Dry Run
Tree: `[5, 1, 4, null, null, 3, 6]`
- `isValid(5, -INF, +INF)`
  - 5 is in range.
  - Left: `isValid(1, -INF, 5)`
    - 1 is in range.
    - Left(null) -> true. Right(null) -> true. Returns true.
  - Right: `isValid(4, 5, +INF)`
    - 4 is NOT in range (4 is not > 5).
    - Returns false.
- Returns `true && false` = false.

## Common Mistakes
- **Only checking immediate children:** `if (node->left->val < node->val && node->right->val > node->val)` is INCORRECT. A node in the right subtree might be greater than its parent but smaller than the root, which violates the BST property.
- **Using `INT_MIN` instead of `LONG_MIN`:** If a node's value is exactly `INT_MIN` (-2147483648), the condition `node->val <= minVal` will trigger incorrectly if `minVal` is also `INT_MIN`.

## Similar Problems
- Recover Binary Search Tree
- Find Mode in Binary Search Tree
