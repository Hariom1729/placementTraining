# Inorder Successor in BST

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees / BST

## Pattern
Binary Search Traversal

## Problem Statement
Given the `root` of a binary search tree and a node `p` in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return `null`.
The successor of a node `p` is the node with the smallest key greater than `p.val`.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- All Nodes will have unique values.

## Input
- `root` pointer of the Binary Search Tree.
- `p` pointer to the target node.

## Output
- Return the `TreeNode*` pointing to the inorder successor.

## Sample Test Cases

**Example 1:**
```
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
```

## Edge Cases
- Target node is the maximum value in the BST (returns null).
- Target node has no right child. The successor lies somewhere above it.

## Intuition
The brute force way is to do a full inorder traversal, find `p`, and return the node immediately after it. But that takes $O(N)$ time.
Since it's a BST, we can use binary search!
We want the smallest node that is strictly greater than `p`.
- If `root->val <= p->val`, then this root cannot be the successor. The successor MUST be in the right subtree. So we move `root = root->right`.
- If `root->val > p->val`, then this root is a *potential* successor! We record it (`successor = root`). However, there might be an even smaller valid successor in the left subtree. So we move `root = root->left` to try and find a better one.

## Brute Force Approach
**Explanation:** Do an inorder traversal, store all nodes in an array. Loop through the array to find `p`, and return `array[i+1]`.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Optimal Approach (Iterative BST Search)
**Detailed explanation:**
1. Initialize a pointer `successor = nullptr`.
2. Loop `while (root != nullptr)`:
   - If `p->val >= root->val`: We are looking for a value strictly greater than `p`, so we must go right. `root = root->right`.
   - If `p->val < root->val`: The current node is greater than `p`. It might be the successor! Update `successor = root`. We then explore the left subtree to see if there's an even tighter (smaller) successor: `root = root->left`.
3. Return `successor`.

**Time Complexity:** $O(H)$ where $H$ is the height of the tree. This is $O(\log N)$ on average.
**Space Complexity:** $O(1)$ auxiliary space.

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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* successor = nullptr;
        
        while (root != nullptr) {
            // If p's value is greater than or equal to current root, 
            // the successor must be in the right subtree.
            if (p->val >= root->val) {
                root = root->right;
            } 
            // If p's value is less than current root, this root is a POTENTIAL successor.
            // Record it, then try to find a smaller one in the left subtree.
            else {
                successor = root;
                root = root->left;
            }
        }
        
        return successor;
    }
};
```

## Dry Run
Tree: `[5, 3, 6, 2, 4, 1]`, `p = 3`
- `successor = null`. `root = 5`.
- `p (3) < root (5)`. `successor = 5`. Go left: `root = 3`.
- `p (3) >= root (3)`. Go right: `root = 4`.
- `p (3) < root (4)`. `successor = 4`. Go left: `root = null`.
- Loop breaks. Returns `4`.

## Common Mistakes
- **Only checking `p->right`:** A common misunderstanding is thinking the successor is *always* the leftmost child of `p->right`. This is true ONLY if `p` has a right child! If `p` doesn't have a right child, the successor is the lowest ancestor of `p` whose left child is also an ancestor of `p`. The binary search method cleanly handles both cases automatically.

## Similar Problems
- Inorder Predecessor in BST (Exact same logic, just reverse the inequalities)
- Binary Search Tree Iterator
