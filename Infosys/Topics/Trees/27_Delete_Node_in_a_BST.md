# Delete Node in a BST

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Uber, Google

## Topic
Trees / BST

## Pattern
BST Modification

## Problem Statement
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a unique value.
- `root` is a valid binary search tree.
- `-10^5 <= key <= 10^5`

## Input
- `root` pointer of the Binary Search Tree.
- `key` integer to delete.

## Output
- Return the `TreeNode*` pointing to the root of the modified tree.

## Sample Test Cases

**Example 1:**
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Another valid answer is [5,2,6,null,4,null,7].
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

**Example 3:**
```
Input: root = [], key = 0
Output: []
```

## Edge Cases
- Deleting the root of the tree.
- Node to be deleted is a leaf (no children).
- Node to be deleted has exactly one child.
- Node to be deleted has two children (hardest case).

## Intuition
When we find the node to delete, we face 3 scenarios:
1. **Node is a leaf:** Simply remove it (return null to parent).
2. **Node has one child:** Return the non-null child to the parent (effectively bypassing the deleted node).
3. **Node has two children:** This is tricky. We need to replace the node's value with a value that preserves the BST structure, and then delete that replaced value.
   - We can either find the **Inorder Predecessor** (the maximum value in the left subtree).
   - Or the **Inorder Successor** (the minimum value in the right subtree).
   - Let's use the Inorder Successor. We copy the successor's value to the current node, and then recursively delete the successor node from the right subtree.

Alternatively, there is a **pointer restructuring** method where we take the entire left subtree and attach it to the leftmost node of the right subtree, then return the right subtree. We will implement this $O(1)$ space restructuring method.

## Optimal Approach (Restructuring)
**Detailed explanation:**
We recursively search for the key. Once found (`root->val == key`):
1. If `root->left == nullptr`, we return `root->right`.
2. If `root->right == nullptr`, we return `root->left`.
3. If both children exist:
   - We find the leftmost node in the right subtree (this is the inorder successor).
   - We attach the deleted node's left subtree to the left of this inorder successor.
   - We return the deleted node's right child (which now acts as the root of this sub-branch).

**Time Complexity:** $O(H)$ where $H$ is the height of the tree. Finding the node takes $O(H)$, and finding the leftmost node of the right subtree takes $O(H)$. Overall $O(H)$.
**Space Complexity:** $O(H)$ for the recursive stack.

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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // Step 1: Search for the node
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } 
        else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } 
        else {
            // Step 2: Node found. Handle the 3 cases.
            
            // Case 1 & 2: Node has 0 or 1 child
            if (root->left == nullptr) {
                TreeNode* temp = root->right;
                delete root; // Prevent memory leak
                return temp;
            } 
            else if (root->right == nullptr) {
                TreeNode* temp = root->left;
                delete root;
                return temp;
            }
            
            // Case 3: Node has 2 children.
            // Find the inorder successor (smallest in the right subtree)
            // Or alternatively, attach the left subtree to the leftmost node of the right subtree.
            
            TreeNode* rightSubtree = root->right;
            TreeNode* leftMostOfRight = rightSubtree;
            
            // Go as far left as possible in the right subtree
            while (leftMostOfRight->left != nullptr) {
                leftMostOfRight = leftMostOfRight->left;
            }
            
            // Attach the deleted node's left subtree here
            leftMostOfRight->left = root->left;
            
            // Return the right subtree to replace the deleted node
            TreeNode* temp = root->right;
            delete root;
            return temp;
        }
        
        return root;
    }
};
```

## Dry Run
Tree: `[5, 3, 6, 2, 4, null, 7]`, `key = 3`
- `delete(5, 3)`. `3 < 5`, so `5->left = delete(3, 3)`.
- `delete(3, 3)`. Key found!
  - 3 has left(2) and right(4).
  - `rightSubtree = 4`.
  - `leftMostOfRight = 4`. `4->left` is null, loop doesn't run.
  - `leftMostOfRight->left = root->left` -> `4->left = 2`.
  - Return `temp = 4`.
- Back to 5: `5->left = 4`. (Node 4 now has left child 2).
Result Tree: `[5, 4, 6, 2, null, null, 7]`.

## Common Mistakes
- **Forgetting to update parent pointers:** You MUST use the return value of the recursive calls to update the parent: `root->left = deleteNode(root->left, key)`. Simply calling `deleteNode` without assignment will not modify the tree structure correctly.
- **Memory Leaks:** In C++, you must explicitly `delete root;` after re-arranging the pointers, otherwise you leak memory.

## Similar Problems
- Insert into a Binary Search Tree
- Split BST
