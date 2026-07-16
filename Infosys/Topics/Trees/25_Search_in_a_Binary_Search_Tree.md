# Search in a Binary Search Tree

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Adobe

## Topic
Trees / BST

## Pattern
Binary Search

## Problem Statement
You are given the `root` of a binary search tree (BST) and an integer `val`.
Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10^7`
- `root` is a valid binary search tree.
- `1 <= val <= 10^7`

## Input
- `root` pointer of the Binary Search Tree.
- `val` integer to search for.

## Output
- Return the `TreeNode*` pointing to the node with the target value, or `nullptr` if not found.

## Sample Test Cases

**Example 1:**
```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

**Example 2:**
```
Input: root = [4,2,7,1,3], val = 5
Output: []
```

## Edge Cases
- Empty tree (return null).
- Target is the root itself.
- Target is a leaf node.

## Intuition
The defining property of a Binary Search Tree is that for any given node, all values in its left subtree are smaller, and all values in its right subtree are larger.
This allows us to perform a Binary Search.
- If the target `val` is equal to the current node's value, we found it!
- If the target `val` is less than the current node's value, the target MUST be in the left subtree. We can completely ignore the right subtree.
- If the target `val` is greater than the current node's value, the target MUST be in the right subtree. We can completely ignore the left subtree.

This can be implemented either recursively or iteratively. The iterative approach is slightly better as it uses $O(1)$ space.

## Brute Force Approach
**Explanation:** Standard DFS or BFS traversing every single node.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(H)$

## Optimal Approach (Iterative)
**Detailed explanation:**
1. While `root` is not `nullptr` and `root->val != val`:
2. If `val < root->val`, the target is smaller, so move to the left child: `root = root->left`.
3. If `val > root->val`, the target is larger, so move to the right child: `root = root->right`.
4. The loop breaks either when we find the node (`root->val == val`), or when we reach a dead end (`root == nullptr`).
5. Simply return `root`.

**Time Complexity:** $O(H)$ where $H$ is the height of the tree. In a balanced BST, this is $O(\log N)$. In the worst-case skewed tree, it's $O(N)$.
**Space Complexity:** $O(1)$ auxiliary space.

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
    TreeNode* searchBST(TreeNode* root, int val) {
        // Loop until root is null or we find the value
        while (root != nullptr && root->val != val) {
            // If target is smaller, search left
            if (val < root->val) {
                root = root->left;
            } 
            // If target is larger, search right
            else {
                root = root->right;
            }
        }
        // Returns the node if found, or nullptr if not found
        return root;
    }
};
```

## Recursive Solution
```cpp
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root == nullptr || root->val == val) {
            return root;
        }
        
        if (val < root->val) {
            return searchBST(root->left, val);
        } else {
            return searchBST(root->right, val);
        }
    }
};
```

## Dry Run
Tree: `[4, 2, 7, 1, 3]`, `val = 2`
- Initial: `root = 4`. `4 != 2`.
- `2 < 4`, so `root = root->left (2)`.
- Loop condition: `root != null`, but `root->val == val` (2 == 2)! Loop breaks.
- Returns node 2.

## Common Mistakes
- **Searching both sides unnecessarily:** In a standard binary tree, you must search left and right. In a BST, you ONLY search the side dictated by the comparison. Doing `search(left) || search(right)` defeats the purpose of the BST.

## Similar Problems
- Insert into a Binary Search Tree
- Closest Binary Search Tree Value
