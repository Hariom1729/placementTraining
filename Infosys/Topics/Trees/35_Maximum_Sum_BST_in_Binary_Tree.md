# Maximum Sum BST in Binary Tree

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Samsung

## Topic
Trees / BST

## Pattern
Bottom-Up Tree DP

## Problem Statement
Given a binary tree `root`, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Constraints
- The number of nodes in the tree is in the range `[1, 4 * 10^4]`.
- `-4 * 10^4 <= Node.val <= 4 * 10^4`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return an integer representing the maximum sum.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3 (3 + 2 + 5 + 4 + 6 = 20).
```

**Example 2:**
```
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
```

**Example 3:**
```
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negative. Return an empty BST (sum = 0).
```

## Edge Cases
- Tree with all negative values (return 0, because an empty BST is valid and has sum 0).
- Tree that is completely invalid as a BST, so you must find the smallest valid subtrees (leaves).

## Intuition
To verify if a tree is a BST, a node needs to know:
1. Is its left subtree a BST?
2. Is its right subtree a BST?
3. What is the maximum value in the left subtree? (Current node must be greater than this).
4. What is the minimum value in the right subtree? (Current node must be less than this).

If all these conditions are met, the current tree is a BST!
If it IS a BST, what is its sum? It's `Node.val + Sum(Left) + Sum(Right)`.

Since a parent needs information from its children to make a decision, this is a classic **Bottom-Up Postorder Traversal**.
We can create a custom `NodeValue` object/struct that returns 4 things from every recursive call:
- The minimum value in that subtree.
- The maximum value in that subtree.
- The sum of the subtree.
- Whether it is a valid BST. (We can imply this by setting max > min artificially if it fails).

## Brute Force Approach
**Explanation:** For every single node in the tree, run `isValidBST()`. If it returns true, run `calculateSum()`. Maintain a global maximum.
**Time Complexity:** $O(N^2)$ because we traverse the tree for validation repeatedly.
**Space Complexity:** $O(H)$

## Optimal Approach (Bottom-Up Postorder DP)
**Detailed explanation:**
1. Define a class `NodeValue` with `minNode`, `maxNode`, and `maxSize` (which we'll use for the sum).
2. Create a global `int maxSum = 0`.
3. Create recursive `postOrder(TreeNode* root)`.
4. **Base Case:** If `root == nullptr`, return `NodeValue(INT_MAX, INT_MIN, 0)`.
   - *Why INT_MAX for min?* So the parent's comparison `root->val > left.maxNode` will safely pass.
5. `auto left = postOrder(root->left);`
6. `auto right = postOrder(root->right);`
7. **Validation:** Check if current node is a BST: `left.maxNode < root->val && root->val < right.minNode`.
8. **If Valid:**
   - The new sum is `left.maxSize + right.maxSize + root->val`.
   - Update `maxSum = max(maxSum, newSum)`.
   - Return new `NodeValue`:
     - `minNode = min(root->val, left.minNode)`
     - `maxNode = max(root->val, right.maxNode)`
     - `maxSize = newSum`
9. **If Invalid:**
   - Return a "dummy" `NodeValue` that will purposefully fail any future parent comparisons.
   - `minNode = INT_MIN`, `maxNode = INT_MAX`, `maxSize = max(left.maxSize, right.maxSize)`. (By making min extremely small and max extremely large, the parent will never be able to satisfy the BST condition).

**Time Complexity:** $O(N)$ since every node is visited exactly once in the postorder traversal.
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

#include <algorithm>
#include <climits>
using namespace std;

class NodeValue {
public:
    int minNode, maxNode, sum;
    
    NodeValue(int minNode, int maxNode, int sum) {
        this->minNode = minNode;
        this->maxNode = maxNode;
        this->sum = sum;
    }
};

class Solution {
private:
    int maxSum = 0;
    
    NodeValue postOrder(TreeNode* root) {
        // An empty tree is a valid BST with sum 0
        if (root == nullptr) {
            return NodeValue(INT_MAX, INT_MIN, 0);
        }
        
        // Get values from left and right subtrees
        auto left = postOrder(root->left);
        auto right = postOrder(root->right);
        
        // Check if the current tree forms a valid BST
        if (left.maxNode < root->val && root->val < right.minNode) {
            
            // It is a valid BST. Calculate the sum
            int currentSum = left.sum + right.sum + root->val;
            
            // Update global maxSum
            maxSum = max(maxSum, currentSum);
            
            // Return updated info to parent
            return NodeValue(
                min(root->val, left.minNode), 
                max(root->val, right.maxNode), 
                currentSum
            );
        }
        
        // If it's NOT a valid BST, pass up dummy values that will fail all future BST checks.
        // E.g., setting min to INT_MIN means the parent can never be smaller than it.
        return NodeValue(INT_MIN, INT_MAX, max(left.sum, right.sum));
    }
    
public:
    int maxSumBST(TreeNode* root) {
        maxSum = 0;
        postOrder(root);
        // If the maxSum is negative, the problem allows returning an empty BST (0).
        return maxSum > 0 ? maxSum : 0;
    }
};
```

## Dry Run
Tree: `[4, 3, null, 1, 2]`
- `postOrder(4)`
  - `postOrder(3)`
    - `postOrder(1)` -> Leaf. `maxNode=1, minNode=1, sum=1`. Valid.
    - `postOrder(2)` -> Leaf. `maxNode=2, minNode=2, sum=2`. Valid.
    - At Node 3: `left.max(1) < 3` AND `3 < right.min(2)`. This is FALSE (`3 < 2` is false).
    - Subtree 3 is INVALID. Returns `NodeValue(INT_MIN, INT_MAX, max(1, 2) = 2)`.
  - `postOrder(null)` -> Returns `INT_MAX, INT_MIN, 0`.
  - At Node 4: `left.max(INT_MAX) < 4`. FALSE.
  - Subtree 4 is INVALID.
- Global `maxSum` was updated to `2` during the processing of leaf node `2`.
- Returns `2`.

## Common Mistakes
- **Incorrect Base Case:** Returning `INT_MIN` for `minNode` and `INT_MAX` for `maxNode` in the base case (`root == nullptr`) will ruin the logic. A null node should have an impossibly LARGE min value and an impossibly SMALL max value so that it never fails a parent's condition.

## Similar Problems
- Largest BST Subtree (Exact same logic, just keeping track of node count instead of sum)
