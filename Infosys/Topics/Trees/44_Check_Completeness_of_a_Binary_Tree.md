# Check Completeness of a Binary Tree

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Meta, Bloomberg

## Topic
Trees

## Pattern
Level Order Traversal / BFS

## Problem Statement
Given the `root` of a binary tree, determine if it is a complete binary tree.
In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between $1$ and $2^h$ nodes inclusive at the last level $h$.

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`.
- `1 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return `true` if it is complete, else `false`.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

**Example 2:**
```
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

## Edge Cases
- Only a root node exists.
- Tree leans entirely to the right (Not complete).

## Intuition
If we perform a standard **Level Order Traversal (BFS)**, we process nodes level by level, left to right.
In a perfectly complete binary tree, there are no "gaps" between nodes.
A gap happens when we encounter a `nullptr`, but then later in our BFS traversal, we encounter a real `TreeNode`.
Therefore, our logic is simple:
1. Traverse the tree using a Queue. Push children into the queue, **even if they are null**.
2. If we pop a `nullptr` from the queue, we raise a flag: `gapFound = true`.
3. If we continue popping and ever see a non-null node AFTER the flag is raised, it means there is a gap! The tree is NOT complete.

## Brute Force Approach
**Explanation:** Index the nodes using the formula for array representations of trees (`left = 2*i`, `right = 2*i + 1`). Find the maximum index. If the maximum index exceeds the total number of nodes, there is a gap.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ to store nodes and indices.

## Optimal Approach (BFS Null Check)
**Detailed explanation:**
1. Create a `queue<TreeNode*> q`. Push `root`.
2. Maintain a boolean variable `gapFound = false`.
3. Loop while `!q.empty()`:
   - Pop the current node `curr`.
   - If `curr == nullptr`, we set `gapFound = true`. We don't push its children because it doesn't have any.
   - If `curr != nullptr`:
     - **Crucial check:** If `gapFound == true`, return `false`. (We found a real node after a null node!)
     - Push `curr->left` into the queue (even if it's null).
     - Push `curr->right` into the queue (even if it's null).
4. If the queue empties without triggering the return condition, return `true`.

**Time Complexity:** $O(N)$ because every node (and null child) is pushed and popped exactly once.
**Space Complexity:** $O(N)$ for the queue (at the last level, the queue holds roughly $N/2$ nodes).

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

#include <queue>
using namespace std;

class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        if (root == nullptr) return true;
        
        queue<TreeNode*> q;
        q.push(root);
        
        bool gapFound = false;
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            if (curr == nullptr) {
                // We've hit a gap or the end of the tree. 
                // Any non-null node seen after this point proves the tree is not complete.
                gapFound = true;
            } else {
                // If we see a real node AFTER a gap was found, it's not a complete tree
                if (gapFound) {
                    return false;
                }
                
                // Push children unconditionally (even if they are null)
                q.push(curr->left);
                q.push(curr->right);
            }
        }
        
        return true;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, null, 7]`
- Queue: `[1]`.
- Pop 1. Push 2, 3. Queue: `[2, 3]`.
- Pop 2. Push 4, 5. Queue: `[3, 4, 5]`.
- Pop 3. Push null, 7. Queue: `[4, 5, null, 7]`.
- Pop 4. Push null, null. Queue: `[5, null, 7, null, null]`.
- Pop 5. Push null, null. Queue: `[null, 7, null, null, null, null]`.
- Pop null. `curr == nullptr`. Sets `gapFound = true`.
- Pop 7. `curr != nullptr`. Checks `gapFound`. `gapFound == true`! Returns `false`.
Correct! The tree is not complete because 7 is to the right of a missing left child of 3.

## Common Mistakes
- **Only pushing non-null children into the queue:** If you write `if (curr->left) q.push(curr->left);`, the queue simply skips over the nulls, and you lose the ability to detect horizontal gaps! You MUST push `nullptr` into the queue for this algorithm to work.

## Similar Problems
- Count Complete Tree Nodes
- Maximum Width of Binary Tree
