# Lowest Common Ancestor of a Binary Search Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Microsoft

## Topic
Trees / BST

## Pattern
Binary Search Traversal

## Problem Statement
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

## Input
- `root` pointer of the Binary Search Tree.
- `p` pointer to the first target node.
- `q` pointer to the second target node.

## Output
- Return the `TreeNode*` pointing to the lowest common ancestor.

## Sample Test Cases

**Example 1:**
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

**Example 2:**
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

## Edge Cases
- One node is the direct parent or ancestor of the other (e.g., Example 2).
- The root itself is the LCA.

## Intuition
This problem is significantly easier and faster than finding the LCA in a normal Binary Tree.
Because this is a **Binary Search Tree**, we know that for any node `curr`:
- If both `p` and `q` are **less than** `curr->val`, then both nodes are located strictly in the left subtree. We can ignore the right subtree and move left.
- If both `p` and `q` are **greater than** `curr->val`, then both nodes are located strictly in the right subtree. We can ignore the left subtree and move right.
- What if one is smaller and one is larger? Or what if `curr` is exactly equal to `p` or `q`? **This means a split has occurred!** The moment `p` and `q` diverge (one goes left, one goes right), the current node `curr` is mathematically guaranteed to be the Lowest Common Ancestor. We can immediately return it.

## Brute Force Approach
**Explanation:** Use the same $O(N)$ DFS algorithm used for normal Binary Trees. This works perfectly fine but is suboptimal because it doesn't utilize the BST properties.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(H)$

## Optimal Approach (Iterative BST Traversal)
**Detailed explanation:**
1. Use an iterative loop `while (root != nullptr)`.
2. Compare the values of `root`, `p`, and `q`.
3. If `root->val > p->val` AND `root->val > q->val`, it means both targets are on the left. Set `root = root->left`.
4. Else if `root->val < p->val` AND `root->val < q->val`, it means both targets are on the right. Set `root = root->right`.
5. Else, we have found the split point (or `root` equals one of the targets). This `root` is the LCA. Return `root`.

**Time Complexity:** $O(H)$ where $H$ is the height of the tree. This is $O(\log N)$ on average, and $O(N)$ in the worst case (skewed tree). This is much faster than the standard Binary Tree LCA which always takes $O(N)$ in the worst case and explores the whole tree.
**Space Complexity:** $O(1)$ auxiliary space since we are doing this iteratively.

## C++ Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Iterate down the tree
        while (root != nullptr) {
            
            // If both p and q are smaller than root, LCA must be in the left subtree
            if (p->val < root->val && q->val < root->val) {
                root = root->left;
            }
            // If both p and q are greater than root, LCA must be in the right subtree
            else if (p->val > root->val && q->val > root->val) {
                root = root->right;
            }
            // Otherwise, we have found the split point (or one of the nodes is the root).
            // This is the LCA.
            else {
                return root;
            }
        }
        
        return nullptr; // Should not be reached based on constraints
    }
};
```

## Recursive Solution
```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) return nullptr;
        
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        return root; // Split point
    }
};
```

## Dry Run
Tree: `[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]`, `p = 2`, `q = 4`
- Start at root = `6`.
- `p=2` is less than 6. `q=4` is less than 6. Both are smaller! Move left.
- `root = 2`.
- `p=2` is NOT less than 2. `p=2` is NOT greater than 2. (It is equal).
- The `else` block executes. Returns node `2`.
Correct! `2` is the LCA of `2` and `4`.

## Common Mistakes
- **Using the normal Binary Tree LCA algorithm:** While it gets accepted on platforms like LeetCode, interviewers will deduct points because you failed to optimize time and space complexity using the given BST properties.
- **Forgetting that `p` might be greater than `q`:** The conditions `p->val < root->val && q->val < root->val` automatically handle this, but if you try to manually check ranges like `p->val < root->val < q->val`, you must account for the fact that `p` could be larger than `q`.

## Similar Problems
- Lowest Common Ancestor of a Binary Tree
- Insert into a Binary Search Tree
