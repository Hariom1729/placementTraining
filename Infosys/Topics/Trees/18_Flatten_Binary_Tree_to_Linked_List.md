# Flatten Binary Tree to Linked List

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees

## Pattern
DFS / Morris Traversal

## Problem Statement
Given the `root` of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **pre-order traversal** of the binary tree.

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Modify the tree in-place. Do not return anything.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Example 2:**
```
Input: root = []
Output: []
```

## Edge Cases
- Empty tree.
- Tree that is already perfectly flattened to the right.
- Tree that is completely skewed to the left.

## Intuition
The flattened tree must follow the **Preorder** (Root -> Left -> Right) traversal.
If we think backwards, the **Reverse Postorder** traversal (Right -> Left -> Root) visits the nodes in the exact opposite order of the flattened list (6 -> 5 -> 4 -> 3 -> 2 -> 1).
If we traverse in Reverse Postorder, we can keep track of the previously visited node in a global variable `prev`. 
When we are at the `Root` node, its right child should point to `prev`, and its left child should become `null`. Then, we update `prev = Root` and move up!

## Brute Force Approach
**Explanation:** Run a standard Preorder traversal and store all node pointers in a `vector<TreeNode*>`. Iterate through the vector, setting `left = null` and `right = vector[i+1]`.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the vector and recursion stack.

## Optimal Approach (Reverse Postorder)
**Detailed explanation:**
1. Maintain a global or member variable `TreeNode* prev = nullptr`.
2. Define a recursive function `flatten(root)`.
3. Base case: If `root == nullptr`, return.
4. Recursively flatten the right subtree: `flatten(root->right)`.
5. Recursively flatten the left subtree: `flatten(root->left)`.
6. Attach the current node to the flattened list:
   - `root->right = prev;`
   - `root->left = nullptr;`
7. Move the `prev` pointer to the current node: `prev = root;`

**Time Complexity:** $O(N)$ because every node is visited exactly once.
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
    TreeNode* prev = nullptr;
    
public:
    void flatten(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        
        // Reverse Postorder: Right -> Left -> Root
        flatten(root->right);
        flatten(root->left);
        
        // Process current node
        root->right = prev;
        root->left = nullptr;
        
        // Move prev to current node
        prev = root;
    }
};
```

## Advanced Optimal Approach (Morris Traversal $O(1)$ Space)
If the interviewer insists on $O(1)$ space (no recursion stack):
For every node `curr`, if it has a left child:
1. Find the rightmost node in the left subtree.
2. Connect that rightmost node's right pointer to `curr->right`.
3. Move `curr->left` to `curr->right` and set `curr->left = nullptr`.
4. Move `curr = curr->right`.

```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* curr = root;
        while (curr != nullptr) {
            if (curr->left != nullptr) {
                // Find rightmost node of left subtree
                TreeNode* prev = curr->left;
                while (prev->right != nullptr) {
                    prev = prev->right;
                }
                
                // Thread the rightmost node to curr's right subtree
                prev->right = curr->right;
                
                // Move left subtree to the right
                curr->right = curr->left;
                curr->left = nullptr;
            }
            // Move to the next node on the right
            curr = curr->right;
        }
    }
};
```

## Dry Run (Reverse Postorder)
Tree: `[1, 2, 5, 3, 4, null, 6]`
- `prev = null`
- `flatten(6)` -> leaves. `6->right = null, 6->left = null`. `prev = 6`.
- `flatten(5)` -> visits right(6). returns. visits left(null).
  - `5->right = 6`, `5->left = null`. `prev = 5`.
- `flatten(4)` -> leaves. `4->right = 5`, `4->left = null`. `prev = 4`.
- `flatten(3)` -> leaves. `3->right = 4`, `3->left = null`. `prev = 3`.
- `flatten(2)` -> visits right(4). visits left(3).
  - `2->right = 3`, `2->left = null`. `prev = 2`.
- `flatten(1)` -> visits right(5). visits left(2).
  - `1->right = 2`, `1->left = null`. `prev = 1`.
Final Tree: 1 -> 2 -> 3 -> 4 -> 5 -> 6.

## Common Mistakes
- **Doing a standard Preorder traversal:** If you do `root->right = root->left`, you instantly overwrite and LOSE the original `root->right` pointer, causing you to lose half the tree!
- **Not setting `left = nullptr`:** Forgetting this causes the resulting structure to fail the "linked list" definition and creates a tangled graph.

## Similar Problems
- Flatten a Multilevel Doubly Linked List
- Convert Binary Search Tree to Sorted Doubly Linked List
