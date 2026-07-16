# Same Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Trees

## Pattern
DFS / Postorder Traversal

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Constraints
- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Input
- `p` pointer of the first Binary Tree.
- `q` pointer of the second Binary Tree.

## Output
- Return a boolean: `true` if they are identical, `false` otherwise.

## Sample Test Cases

**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Edge Cases
- Both trees are empty (`nullptr`). Should return `true`.
- One tree is empty and the other is not. Should return `false`.

## Intuition
To determine if two trees are identical, we must verify that:
1. The current nodes have the same value.
2. Their left subtrees are identical.
3. Their right subtrees are identical.

This naturally leads to a recursive DFS approach where we traverse both trees simultaneously and compare their nodes at every step.

## Brute Force Approach
N/A - The optimal approach checks every corresponding pair of nodes exactly once, which is the most efficient way possible.

## Optimal Approach
**Detailed explanation:**
We use simultaneous DFS on both trees.
1. **Base Cases:**
   - If both `p` and `q` are `nullptr`, they are identical at this position, return `true`.
   - If one of them is `nullptr` and the other is not, they mismatch, return `false`.
   - If their values do not match (`p->val != q->val`), return `false`.
2. **Recursive Step:**
   - Recursively check if the left subtrees are identical: `isSameTree(p->left, q->left)`.
   - Recursively check if the right subtrees are identical: `isSameTree(p->right, q->right)`.
3. Return `true` only if both recursive checks return `true`.

**Time Complexity:** $O(\min(N, M))$ where $N$ and $M$ are the number of nodes in trees `p` and `q`. The algorithm terminates as soon as a mismatch is found, or visits all nodes if they are identical.
**Space Complexity:** $O(\min(H1, H2))$ where $H1$ and $H2$ are the heights of the trees. This represents the recursive call stack space.

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // If both nodes are null, they are identical up to this leaf path
        if (p == nullptr && q == nullptr) {
            return true;
        }
        
        // If one is null and the other is not, they are structurally different
        if (p == nullptr || q == nullptr) {
            return false;
        }
        
        // If the values differ, they are not the same tree
        if (p->val != q->val) {
            return false;
        }
        
        // Both current nodes are identical, now recursively check left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

## Dry Run
Tree 1: `p = [1, 2]`
Tree 2: `q = [1, null, 2]`
- `isSameTree(node 1, node 1)`
  - Values match (1 == 1). Proceed to check children.
  - `isSameTree(node 2, null)`
    - `p` is not null, `q` is null. Returns `false`.
  - The left check returned `false`. `false && ...` is `false`.
- Returns `false`.

## Common Mistakes
- Writing `if (p == nullptr && q != nullptr)` and `if (p != nullptr && q == nullptr)` as two separate checks. It is much cleaner to write `if (p == nullptr || q == nullptr)` after you have already checked that they aren't *both* null.

## Similar Problems
- Symmetric Tree
- Subtree of Another Tree

## Infosys Variations
- They may ask you to implement this iteratively using two queues (BFS). You would enqueue pairs of nodes and compare them level by level.
