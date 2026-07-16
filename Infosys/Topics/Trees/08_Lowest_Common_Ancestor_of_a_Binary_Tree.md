# Lowest Common Ancestor of a Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google, Microsoft

## Topic
Trees

## Pattern
DFS / Postorder Traversal

## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Input
- `root` pointer of the Binary Tree.
- `p` and `q` pointers to the target nodes.

## Output
- Return the pointer to the LCA node.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

## Edge Cases
- One of the target nodes is the root. The root is automatically the LCA.
- One node is a direct descendant of the other. The higher node (the ancestor) is the LCA.

## Intuition
When traversing a tree, if we find `p` or `q`, we should immediately return that node up to its parent. 
If a parent receives a non-null return from its **left** child AND a non-null return from its **right** child, it means `p` is on one side and `q` is on the other. This makes the parent the Lowest Common Ancestor!
If a parent only receives a non-null return from one side, it means both `p` and `q` are on that side, so it just passes that non-null return further up the chain.

## Brute Force Approach
**Explanation:** Find the path from the root to `p`, and store it in an array. Find the path from the root to `q`, and store it in another array. Compare the two arrays to find the last common node.
**Time Complexity:** $O(N)$ to find the paths.
**Space Complexity:** $O(N)$ for the arrays storing the paths. (Actually, $O(H)$ for height, but $O(N)$ in worst case).

## Optimal Approach
**Detailed explanation:**
We use a single-pass DFS recursion.
1. **Base Case:** If `root` is `nullptr`, return `nullptr`. If `root == p` or `root == q`, return `root`.
2. **Recursive Step:**
   - Search the left subtree: `TreeNode* left = lowestCommonAncestor(root->left, p, q);`
   - Search the right subtree: `TreeNode* right = lowestCommonAncestor(root->right, p, q);`
3. **Logic:**
   - If both `left` and `right` are NOT null, this means one target was found in the left subtree and the other in the right subtree. The current `root` is the LCA. Return `root`.
   - If `left` is NOT null but `right` IS null, both nodes must be located in the left subtree (or one node was found and the other is further down). Return `left`.
   - If `right` is NOT null but `left` IS null, return `right`.
   - If both are null, return `nullptr`.

**Time Complexity:** $O(N)$ where $N$ is the number of nodes. In the worst case, we might visit all nodes.
**Space Complexity:** $O(H)$ for the recursive stack space.

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
        // Base case: if we hit a null node, or find one of our target nodes
        if (root == nullptr || root == p || root == q) {
            return root;
        }
        
        // Search left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
        // If both left and right return a non-null node, it means 
        // p and q are in different subtrees. Therefore, root is the LCA.
        if (left != nullptr && right != nullptr) {
            return root;
        }
        
        // Otherwise, if only one side returned a node, pass it up.
        // If both are null, this will correctly return nullptr.
        return (left != nullptr) ? left : right;
    }
};
```

## Dry Run
Tree: `[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]`
`p = 5`, `q = 4`
- `LCA(3)`
  - `left = LCA(5)`. Since `5 == p`, returns `5` instantly. (It doesn't search under 5 yet).
  - `right = LCA(1)`.
    - searches left(0) -> returns null.
    - searches right(8) -> returns null.
    - `LCA(1)` returns null.
  - Back at `LCA(3)`: `left = 5`, `right = null`.
  - Returns `5`.
Wait, how did it find `4`? It didn't! Because `p` and `q` are guaranteed to exist, if we found `5` and never found `4` in the other branch, `4` MUST be a descendant of `5`. Thus, `5` is the correct LCA.

## Common Mistakes
- **Wasting time searching descendants:** Once you find `p`, you DO NOT need to search `p`'s children for `q`. Just return `p`. If `q` is under `p`, then `p` is the LCA anyway. If `q` is not under `p`, it will be found in another branch and the parent will resolve it.

## Similar Problems
- Lowest Common Ancestor of a Binary Search Tree (Much easier, $O(H)$ time)
- Step-By-Step Directions From a Binary Tree Node to Another

## Infosys Variations
- Sometimes they ask for LCA in an N-ary tree, or LCA when the nodes don't necessarily exist in the tree. If they might not exist, you CANNOT return early upon finding `p`; you must search the whole tree to verify both actually exist.
