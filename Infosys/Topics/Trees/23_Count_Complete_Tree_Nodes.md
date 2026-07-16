# Count Complete Tree Nodes

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees

## Pattern
Binary Search / Tree Traversal

## Problem Statement
Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between $1$ and $2^h$ nodes inclusive at the last level $h$.

Design an algorithm that runs in less than $O(N)$ time complexity.

## Constraints
- The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
- `0 <= Node.val <= 5 * 10^4`
- The tree is guaranteed to be complete.

## Input
- `root` pointer of the Binary Tree.

## Output
- Return an integer representing the count of nodes.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,4,5,6]
Output: 6
```

**Example 2:**
```
Input: root = []
Output: 0
```

**Example 3:**
```
Input: root = [1]
Output: 1
```

## Edge Cases
- Empty tree.
- Tree that is perfectly balanced (last level is completely full).

## Intuition
If we do a standard DFS or BFS, it takes $O(N)$ time. The problem specifically asks for less than $O(N)$, meaning we MUST utilize the "complete" property of the tree.
A complete tree is perfectly balanced everywhere except potentially the bottom right.
If a subtree is *perfect* (i.e., the extreme left depth is equal to the extreme right depth), we can mathematically calculate its total nodes using the formula: $2^h - 1$, where $h$ is the height. This takes $O(1)$ time if we already know the height!
If a subtree is *not perfect*, we recursively count its left and right children and add 1 for the root: `1 + countNodes(left) + countNodes(right)`.

## Brute Force Approach
**Explanation:** Standard DFS. `if (!root) return 0; return 1 + count(left) + count(right);`
**Time Complexity:** $O(N)$
**Space Complexity:** $O(H)$

## Optimal Approach
**Detailed explanation:**
1. Check the height of the extreme left path (`leftHeight`).
2. Check the height of the extreme right path (`rightHeight`).
3. If `leftHeight == rightHeight`, the subtree is a Perfect Binary Tree. Return `(1 << leftHeight) - 1`. (Note: `1 << h` is equivalent to $2^h$).
4. If they are not equal, the tree is complete but not perfect. We cannot use the math formula on the entire tree, but we can recurse! Return `1 + countNodes(root->left) + countNodes(root->right)`.

Because the tree is complete, at EVERY level, at least one of the two subtrees (left or right) will ALWAYS be a perfect binary tree! Thus, the recursion will quickly hit the $O(1)$ math formula instead of traversing all nodes.

**Time Complexity:** $O((\log N)^2)$. We calculate the height which takes $O(\log N)$ time, and we do this at most $\log N$ times (the depth of the tree).
**Space Complexity:** $O(\log N)$ for the recursion stack.

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
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        
        int lh = getLeftHeight(root);
        int rh = getRightHeight(root);
        
        // If left height and right height are equal, it is a perfect binary tree.
        // Total nodes = 2^h - 1
        if (lh == rh) {
            return (1 << lh) - 1; // 1 << lh is 2^lh
        }
        
        // If not perfect, recurse on left and right children.
        // Due to completeness, one of them will always be perfect and return instantly.
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
    
private:
    int getLeftHeight(TreeNode* node) {
        int height = 0;
        while (node != nullptr) {
            height++;
            node = node->left;
        }
        return height;
    }
    
    int getRightHeight(TreeNode* node) {
        int height = 0;
        while (node != nullptr) {
            height++;
            node = node->right;
        }
        return height;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, 6]` (Left depth is 3, Right depth is 2)
- `countNodes(1)`
  - `lh = 3` (nodes 1->2->4)
  - `rh = 2` (nodes 1->3)
  - Not equal. Return `1 + count(2) + count(3)`.
  
- `countNodes(2)`
  - `lh = 2` (nodes 2->4)
  - `rh = 2` (nodes 2->5)
  - Equal! Returns `(1 << 2) - 1 = 4 - 1 = 3`. (Node 2, 4, 5). No further recursion!
  
- `countNodes(3)`
  - `lh = 2` (nodes 3->6)
  - `rh = 1` (nodes 3)
  - Not equal. Return `1 + count(6) + count(null)`.
  
  - `countNodes(6)` -> lh=1, rh=1. Returns `(1 << 1) - 1 = 1`.
  - `countNodes(null)` -> Returns 0.
  - Subtree 3 returns `1 + 1 + 0 = 2`.

- Total = `1 + 3 + 2 = 6`.

## Common Mistakes
- **Using `pow(2, h)` instead of bit shifting:** `pow()` returns a double and can cause precision issues or slower execution time. Bitwise shift `(1 << h)` is exactly what you want for powers of 2 in C++.
- **Miscalculating height:** The height should represent the number of nodes in the path (starting at 1 for the root itself), otherwise the formula $2^h - 1$ will be off by a factor of 2.

## Similar Problems
- Closest Binary Search Tree Value
