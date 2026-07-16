# Maximum Depth of Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Google

## Topic
Trees

## Pattern
DFS / Postorder Traversal

## Problem Statement
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return an integer representing the maximum depth.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**
```
Input: root = [1,null,2]
Output: 2
```

**Example 3:**
```
Input: root = []
Output: 0
```

## Edge Cases
- An empty tree (root is `nullptr`). Should return 0.
- A tree with only one node (root). Should return 1.
- A highly skewed tree (e.g., essentially a linked list). Should not crash due to stack overflow in normal constraints, but good to be aware of.

## Intuition
The depth of a tree starting at the root is essentially `1` (for the root itself) plus the maximum depth of its left subtree and right subtree. This perfectly fits a recursive, bottom-up (postorder) strategy. If we ask the left child for its depth, and the right child for its depth, we just take the max of those two and add 1.

## Brute Force Approach
N/A - The optimal recursive approach explores every node exactly once, which is the definition of the most efficient approach for this problem.

## Optimal Approach
**Detailed explanation:**
We use a Depth First Search (DFS).
1. **Base Case:** If the current node is `nullptr`, the depth is `0`.
2. **Recursive Step:** 
   - Recursively call the function for the `left` child to get `leftDepth`.
   - Recursively call the function for the `right` child to get `rightDepth`.
3. **Return Value:** Return `1 + max(leftDepth, rightDepth)`.

This is a bottom-up approach because the actual calculations (`max` + 1) happen *after* the recursive calls return (Postorder traversal).

**Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree. We visit every node exactly once.
**Space Complexity:** $O(H)$ where $H$ is the height of the tree. This is for the recursive call stack. In the worst case (skewed tree), $H = N$. In the best case (balanced tree), $H = \log N$.

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

#include <algorithm>
using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: If the node is null, its depth is 0.
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the depth of the left subtree
        int leftDepth = maxDepth(root->left);
        
        // Recursively find the depth of the right subtree
        int rightDepth = maxDepth(root->right);
        
        // The maximum depth of the current node is 1 (for itself) 
        // plus the maximum of its children's depths.
        return 1 + max(leftDepth, rightDepth);
    }
};
```

## Dry Run
Given Tree: `[3, 9, 20, null, null, 15, 7]`
- `maxDepth(3)`
  - `leftDepth` = `maxDepth(9)`
    - `maxDepth(9)` -> children are null, returns `1 + max(0, 0) = 1`
  - `rightDepth` = `maxDepth(20)`
    - `maxDepth(20)` calls `maxDepth(15)` and `maxDepth(7)`
      - `maxDepth(15)` returns 1
      - `maxDepth(7)` returns 1
    - `maxDepth(20)` returns `1 + max(1, 1) = 2`
  - `maxDepth(3)` returns `1 + max(1, 2) = 3`.
Result: 3.

## Common Mistakes
- Forgetting the base case `if (root == nullptr) return 0;` which leads to a Segmentation Fault / Null Pointer Exception.
- Writing redundant code by passing a `depth` parameter down the tree (Top-Down approach). While valid, the Bottom-Up approach is cleaner and easier to reason about.

## Similar Problems
- Minimum Depth of Binary Tree
- Balanced Binary Tree

## Infosys Variations
- You might be asked to implement this iteratively using BFS (Level Order Traversal) to avoid stack overflow on very deep trees. In BFS, the depth is simply the number of levels you traverse before the queue is empty.
