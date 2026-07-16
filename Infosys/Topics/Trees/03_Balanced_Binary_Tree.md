# Balanced Binary Tree

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Google, Bloomberg

## Topic
Trees

## Pattern
DFS / Tree DP

## Problem Statement
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
> a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a boolean: `true` if balanced, `false` otherwise.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**
```
Input: root = []
Output: true
```

## Edge Cases
- An empty tree is considered balanced.
- A tree with one node is balanced.
- A completely skewed tree of 3 nodes (e.g., node -> left -> left) is unbalanced.

## Intuition
To check if a tree is balanced at a specific node, we need the height of its left subtree and right subtree. If the absolute difference is greater than 1, it's unbalanced.
However, *every* node in the tree must be balanced.
We can reuse the logic from finding the Maximum Depth. While calculating the depth, we can simultaneously check the balance condition. If we find an imbalance deep in the tree, we can propagate a "failure signal" up to the root to instantly terminate further checks.

## Brute Force Approach
**Explanation:** For every node, calculate the height of its left and right subtrees (using a standard $O(N)$ height function). If `abs(left - right) <= 1`, recursively check if `node->left` and `node->right` are balanced.
**Time Complexity:** $O(N^2)$ because we calculate the height repeatedly for the same nodes.
**Space Complexity:** $O(H)$ for recursion stack.

## Optimal Approach
**Detailed explanation:**
We use a bottom-up DFS (Postorder Traversal).
We modify our standard "find depth" function. Instead of just returning the depth, we return `-1` if we ever detect that a subtree is unbalanced.
1. Define `checkHeight(node)`.
2. Base case: If `node == nullptr`, return `0`.
3. Recursively call `checkHeight(node->left)`. If it returns `-1`, immediately return `-1` (propagate failure).
4. Recursively call `checkHeight(node->right)`. If it returns `-1`, immediately return `-1`.
5. Now, we have the valid heights of both subtrees. Check if `abs(leftHeight - rightHeight) > 1`.
   - If true (unbalanced), return `-1`.
   - If false (balanced), return the actual height: `1 + max(leftHeight, rightHeight)`.
6. Finally, in the main function, check if `checkHeight(root) != -1`.

**Time Complexity:** $O(N)$. We visit every node at most once. The failure propagation prevents unnecessary work.
**Space Complexity:** $O(H)$ for the recursive call stack.

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
#include <cmath>
using namespace std;

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // If checkHeight returns -1, the tree is unbalanced.
        return checkHeight(root) != -1;
    }
    
private:
    int checkHeight(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        int leftHeight = checkHeight(node->left);
        // If left subtree is unbalanced, instantly propagate the failure
        if (leftHeight == -1) return -1;
        
        int rightHeight = checkHeight(node->right);
        // If right subtree is unbalanced, instantly propagate the failure
        if (rightHeight == -1) return -1;
        
        // If current node is unbalanced, return -1
        if (abs(leftHeight - rightHeight) > 1) {
            return -1;
        }
        
        // Otherwise, return the height of the current subtree
        return 1 + max(leftHeight, rightHeight);
    }
};
```

## Dry Run
Tree: `[1, 2, null, 3]` (Skewed left)
- `checkHeight(1)`
  - calls `checkHeight(2)`
    - calls `checkHeight(3)`
      - calls `checkHeight(null)` -> returns 0
      - calls `checkHeight(null)` -> returns 0
      - diff is 0, returns `1 + max(0,0) = 1`
    - calls right child of 2 (null) -> returns 0
    - diff between left(1) and right(0) is 1. returns `1 + max(1,0) = 2`
  - calls right child of 1 (null) -> returns 0
  - diff between left(2) and right(0) is 2. `2 > 1`, so returns `-1`.
- `checkHeight(1)` returns `-1`.
Result: `isBalanced` returns `false`.

## Common Mistakes
- **Doing a top-down $O(N^2)$ approach:** While it passes many basic test cases, it gets completely destroyed on large inputs or skewed trees, resulting in Time Limit Exceeded (TLE) errors. Always use the bottom-up approach to guarantee $O(N)$.
- **Using a boolean class member variable without resetting it:** Some candidates use a global `bool isBal = true;` variable. This is fine, but returning `-1` directly through the recursion tree is mathematically cleaner and avoids side-effect bugs in multi-threaded test environments.

## Similar Problems
- Maximum Depth of Binary Tree
- Minimum Depth of Binary Tree

## Infosys Variations
- You might be asked to prove the time complexity of the $O(N^2)$ approach vs the $O(N)$ approach. Be ready to explain why calculating depth repeatedly causes quadratic time on skewed trees.
