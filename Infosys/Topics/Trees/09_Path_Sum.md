# Path Sum

## Difficulty
Easy / Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Microsoft, Amazon, Oracle

## Topic
Trees

## Pattern
DFS / Top-Down Recursion

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.
A leaf is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Input
- `root` pointer of the Binary Tree.
- `targetSum` integer.

## Output
- Return a boolean.

## Sample Test Cases

**Example 1:**
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path 5 -> 4 -> 11 -> 2 sums to 22.
```

**Example 2:**
```
Input: root = [1,2,3], targetSum = 5
Output: false
```

**Example 3:**
```
Input: root = [], targetSum = 0
Output: false
```

## Edge Cases
- Empty tree. Should return `false`.
- A tree with a single node. True if `node.val == targetSum`.
- Negative numbers in the tree. We cannot short-circuit the search if our sum exceeds `targetSum` because a negative number could bring it back down.

## Intuition
This is a classic top-down DFS problem.
As we travel down the tree from the root to a leaf, we can subtract the current node's value from the `targetSum`. 
When we reach a leaf node, we check if the *remaining* `targetSum` exactly equals the leaf node's value. If it does, we found a valid path!
If we reach a null node, it's not a path, return `false`.

## Brute Force Approach
N/A - Standard DFS is optimal.

## Optimal Approach
**Detailed explanation:**
1. **Base Case 1:** If `root == nullptr`, return `false`.
2. **Base Case 2 (Leaf Node Check):** A node is a leaf if BOTH its left and right children are null. If `root->left == nullptr && root->right == nullptr`, check if `targetSum == root->val`. Return `true` if it matches, `false` otherwise.
3. **Recursive Step:** We haven't reached a leaf yet.
   - Subtract `root->val` from `targetSum`.
   - Recursively call the function for the left child: `hasPathSum(root->left, targetSum - root->val)`.
   - Recursively call the function for the right child: `hasPathSum(root->right, targetSum - root->val)`.
   - If *either* the left path OR the right path returns `true`, then a valid path exists. (Use the logical OR `||` operator).

**Time Complexity:** $O(N)$ where $N$ is the number of nodes. We visit each node at most once.
**Space Complexity:** $O(H)$ where $H$ is the height of the tree. This accounts for the recursive call stack.

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        // If the tree is empty, no path exists
        if (root == nullptr) {
            return false;
        }
        
        // If we reach a leaf node, check if the remaining targetSum equals the leaf's value
        if (root->left == nullptr && root->right == nullptr) {
            return targetSum == root->val;
        }
        
        // Recursively check the left and right subtrees with the updated targetSum
        int remainingSum = targetSum - root->val;
        
        return hasPathSum(root->left, remainingSum) || hasPathSum(root->right, remainingSum);
    }
};
```

## Dry Run
Tree: `[1, 2, 3]`, `targetSum = 5`
- `hasPathSum(1, 5)`
  - Not a leaf. `remaining = 5 - 1 = 4`.
  - Calls `hasPathSum(2, 4)`
    - Node 2 is a leaf. Is `4 == 2`? No. Returns `false`.
  - Calls `hasPathSum(3, 4)`
    - Node 3 is a leaf. Is `4 == 3`? No. Returns `false`.
  - Returns `false || false` = `false`.

## Common Mistakes
- **Checking for `targetSum == 0` when `root == nullptr`:** If you do this, a tree like `[1, 2]` with target `1` will fail. Why?
  - `hasPathSum(1, 1)` -> calls `left(2, 0)` and `right(null, 0)`.
  - The `right(null, 0)` will hit the base case `targetSum == 0` and return `true`! But the path `1 -> null` is NOT a root-to-leaf path. A leaf must have NO children. You MUST check the sum exactly AT the leaf node, not at the null node below it.

## Similar Problems
- Path Sum II (Return all paths)
- Path Sum III (Path doesn't have to start at root or end at leaf)

## Infosys Variations
- Infosys SP often asks **Path Sum II**, which requires you to return the actual nodes in the path using a `vector<vector<int>>` and standard backtracking (pushing to a `currentPath` vector, recursing, and popping).
