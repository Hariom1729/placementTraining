# Minimum Absolute Difference in BST

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google

## Topic
Trees / BST

## Pattern
Inorder Traversal

## Problem Statement
Given the `root` of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

## Constraints
- The number of nodes in the tree is in the range `[2, 10^4]`.
- `0 <= Node.val <= 10^5`

## Input
- `root` pointer of the Binary Search Tree.

## Output
- Return an integer representing the minimum absolute difference.

## Sample Test Cases

**Example 1:**
```
Input: root = [4,2,6,1,3]
Output: 1
```

**Example 2:**
```
Input: root = [1,0,48,null,null,12,49]
Output: 1
```

## Edge Cases
- The tree has exactly 2 nodes.
- Difference could be 0 if the BST allowed duplicates (though constraints usually imply unique values).

## Intuition
To find the minimum difference between *any* two numbers in an array, you would first sort the array, and then check the differences between **adjacent elements**.
Why adjacent elements? Because the smallest difference between numbers in a sorted list MUST be between two neighbors.
In a BST, the **Inorder Traversal** naturally visits the nodes in sorted order!
So, we just perform an Inorder traversal, keep track of the `prev` node we visited, and constantly update `minDiff = min(minDiff, curr->val - prev->val)`.

## Brute Force Approach
**Explanation:** For every node, calculate the difference with EVERY other node using nested traversals.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(H)$

## Optimal Approach (Inorder Traversal)
**Detailed explanation:**
1. Initialize a global/member variable `minDiff = INT_MAX`.
2. Initialize a global/member pointer `prev = nullptr`.
3. Create `inorder(TreeNode* root)`.
4. **Base Case:** If `root == nullptr`, return.
5. Traverse left: `inorder(root->left)`.
6. **Process Node:**
   - If `prev != nullptr`, calculate the difference: `diff = root->val - prev->val`.
   - Update `minDiff = min(minDiff, diff)`.
   - Update `prev = root`.
7. Traverse right: `inorder(root->right)`.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(H)$ for the recursion stack.

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

class Solution {
private:
    int minDiff = INT_MAX;
    TreeNode* prev = nullptr;
    
    void inorder(TreeNode* root) {
        if (root == nullptr) return;
        
        inorder(root->left);
        
        // Process node
        if (prev != nullptr) {
            minDiff = min(minDiff, root->val - prev->val);
        }
        prev = root;
        
        inorder(root->right);
    }
    
public:
    int getMinimumDifference(TreeNode* root) {
        inorder(root);
        return minDiff;
    }
};
```

## Dry Run
Tree: `[4, 2, 6, 1, 3]`
Inorder traversal visits: 1, 2, 3, 4, 6.
- Visit 1: `prev=null`. `prev=1`.
- Visit 2: `prev=1`. Diff = `2 - 1 = 1`. `minDiff = min(INF, 1) = 1`. `prev=2`.
- Visit 3: `prev=2`. Diff = `3 - 2 = 1`. `minDiff = min(1, 1) = 1`. `prev=3`.
- Visit 4: `prev=3`. Diff = `4 - 3 = 1`. `minDiff = min(1, 1) = 1`. `prev=4`.
- Visit 6: `prev=4`. Diff = `6 - 4 = 2`. `minDiff = min(1, 2) = 1`. `prev=6`.
Result: 1.

## Common Mistakes
- **Using `abs()` unnecessarily:** Since Inorder traversal is strictly increasing, `root->val` will ALWAYS be greater than or equal to `prev->val`. You don't actually need to call `abs()`, just `root->val - prev->val` is guaranteed to be positive.
- **Comparing root with left/right children only:** The minimum difference might be between a node and its grandparent. Inorder traversal correctly checks neighbors in sorted order, completely avoiding this pitfall.

## Similar Problems
- Minimum Distance Between BST Nodes (Exact same problem, different name)
- Kth Smallest Element in a BST
