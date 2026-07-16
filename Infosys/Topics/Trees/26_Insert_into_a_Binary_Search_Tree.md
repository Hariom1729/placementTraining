# Insert into a Binary Search Tree

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, LinkedIn

## Topic
Trees / BST

## Pattern
Binary Search Traversal

## Problem Statement
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

## Constraints
- The number of nodes in the tree will be in the range `[0, 10^4]`.
- `-10^8 <= Node.val <= 10^8`
- All the values `Node.val` are unique.
- `-10^8 <= val <= 10^8`
- It's guaranteed that `val` does not exist in the original BST.

## Input
- `root` pointer of the Binary Search Tree.
- `val` integer to insert.

## Output
- Return the `TreeNode*` pointing to the root of the modified tree.

## Sample Test Cases

**Example 1:**
```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

**Example 2:**
```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

**Example 3:**
```
Input: root = [], val = 5
Output: [5]
```

## Edge Cases
- Empty tree. We must return a newly created node as the root.

## Intuition
The easiest way to insert a node into a BST while maintaining the BST properties is to insert it as a **leaf node**.
We can traverse the tree exactly like we do in a BST search.
- If the new value is less than the current node, we must go left. If the left child is null, we have found our insertion point! We attach the new node to the left.
- If the new value is greater than the current node, we must go right. If the right child is null, we attach the new node to the right.

This can be done elegantly using both iteration and recursion. Iteration uses $O(1)$ space.

## Brute Force Approach
N/A - Standard BST traversal is optimal.

## Optimal Approach (Iterative)
**Detailed explanation:**
1. If `root == nullptr`, the tree is empty. Return a new `TreeNode(val)`.
2. Use a pointer `curr = root` to traverse the tree.
3. Start an infinite loop `while(true)`:
   - If `val < curr->val`:
     - If `curr->left != nullptr`, we keep moving left: `curr = curr->left`.
     - If `curr->left == nullptr`, we found the empty spot. `curr->left = new TreeNode(val)`. Break the loop.
   - If `val > curr->val`:
     - If `curr->right != nullptr`, we keep moving right: `curr = curr->right`.
     - If `curr->right == nullptr`, we found the empty spot. `curr->right = new TreeNode(val)`. Break the loop.
4. Return the original `root`.

**Time Complexity:** $O(H)$ where $H$ is the height of the tree. In average case $O(\log N)$, worst case $O(N)$ for skewed trees.
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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        // Edge case: empty tree
        if (root == nullptr) {
            return new TreeNode(val);
        }
        
        TreeNode* curr = root;
        
        while (true) {
            // Target is smaller, go left
            if (val < curr->val) {
                if (curr->left != nullptr) {
                    curr = curr->left;
                } else {
                    curr->left = new TreeNode(val);
                    break;
                }
            } 
            // Target is larger, go right
            else {
                if (curr->right != nullptr) {
                    curr = curr->right;
                } else {
                    curr->right = new TreeNode(val);
                    break;
                }
            }
        }
        
        return root;
    }
};
```

## Recursive Solution
```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (root == nullptr) {
            return new TreeNode(val);
        }
        
        if (val < root->val) {
            root->left = insertIntoBST(root->left, val);
        } else {
            root->right = insertIntoBST(root->right, val);
        }
        
        return root;
    }
};
```

## Dry Run
Tree: `[4, 2, 7, 1, 3]`, `val = 5`
- `curr = 4`.
- `5 > 4`, go right. `curr->right` is 7. `curr` becomes 7.
- `curr = 7`.
- `5 < 7`, go left. `curr->left` is null.
- Spot found! `curr->left = new TreeNode(5)`. Break.
- Returns root (4).

## Common Mistakes
- **Overcomplicating the insertion:** Some candidates try to insert the node in the middle of the tree and shift existing nodes down. This is extremely complicated and completely unnecessary since inserting as a leaf is mathematically guaranteed to preserve BST rules.
- **Forgetting to return the root:** Always return the original root pointer after modifying the tree.

## Similar Problems
- Search in a Binary Search Tree
- Delete Node in a BST
