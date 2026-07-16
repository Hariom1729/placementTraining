# Construct Binary Search Tree from Preorder Traversal

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, ByteDance, Microsoft

## Topic
Trees / BST

## Pattern
Preorder Construction / Range Bounds

## Problem Statement
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

## Constraints
- $1 \le preorder.length \le 100$
- $1 \le preorder[i] \le 10^8$
- All the values of `preorder` are unique.

## Input
- `preorder` vector of integers.

## Output
- Return the `TreeNode*` pointing to the root of the constructed BST.

## Sample Test Cases

**Example 1:**
```
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

**Example 2:**
```
Input: preorder = [1,3]
Output: [1,null,3]
```

## Edge Cases
- Skewed trees: e.g., `preorder = [1, 2, 3, 4]`. The entire tree will just be a chain of right children.

## Intuition
Unlike constructing a normal Binary Tree (where we need both Preorder and Inorder), constructing a BST only requires one traversal! This is because the Inorder traversal of a BST is simply the sorted version of the Preorder array.
So one immediate solution is: Sort `preorder` to get `inorder`, then use the $O(N)$ algorithm for "Construct Tree from Preorder and Inorder". But this takes $O(N \log N)$ time to sort.

Can we do it in $O(N)$ directly?
Yes! We can use the concept of an **Upper Bound**.
As we iterate through the `preorder` array, the very first element is the root.
When we build the left subtree, the elements MUST be smaller than the root. So the root's value becomes the `upperBound` for the left subtree.
When we build the right subtree, it is bound by whatever bounded its parent.
We can pass this `upperBound` recursively. If the next element in the array is greater than the `upperBound`, we know it doesn't belong in the current subtree, so we return `nullptr` and let the parent handle it.

## Brute Force Approach
**Explanation:** For every element in the array, run the standard `insertIntoBST(root, val)` algorithm.
**Time Complexity:** $O(N^2)$ in the worst case (skewed tree).
**Space Complexity:** $O(H)$

## Optimal Approach (Upper Bound Recursion)
**Detailed explanation:**
1. Create a reference integer `i = 0` to iterate through the array.
2. Create a recursive function `build(preorder, i, bound)`.
3. **Base Case:** If `i == preorder.size()` (we reached the end of the array), or if `preorder[i] > bound`, return `nullptr`.
4. **Process Node:** The current value `preorder[i]` is valid. Create a new `TreeNode* root = new TreeNode(preorder[i])` and increment `i++`.
5. **Recursive Steps:**
   - Build the left subtree. The new bound is `root->val`, because all nodes in the left subtree must be strictly less than the root.
     `root->left = build(preorder, i, root->val)`
   - Build the right subtree. The bound remains the same as the parent's bound.
     `root->right = build(preorder, i, bound)`
6. Return `root`.

**Time Complexity:** $O(N)$ since we visit every element in the array exactly once.
**Space Complexity:** $O(N)$ for the recursion stack in the worst case (skewed tree).

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

#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i = 0;
        // Start with the maximum possible upper bound
        return build(preorder, i, INT_MAX);
    }
    
private:
    TreeNode* build(vector<int>& preorder, int& i, int bound) {
        // Base case: array exhausted OR current element violates the bound
        if (i == preorder.size() || preorder[i] > bound) {
            return nullptr;
        }
        
        // Construct the root and increment the pointer
        TreeNode* root = new TreeNode(preorder[i++]);
        
        // Left subtree bound strictly by root's value
        root->left = build(preorder, i, root->val);
        
        // Right subtree bounded by the parent's bound
        root->right = build(preorder, i, bound);
        
        return root;
    }
};
```

## Dry Run
`preorder = [8, 5, 1, 7, 10, 12]`
- `build(i=0, bound=INF)`
  - `root = 8`, `i = 1`.
  - `root->left = build(i=1, bound=8)`
    - `preorder[1] = 5 < 8`. Valid. `root = 5`, `i = 2`.
    - `5->left = build(i=2, bound=5)`
      - `preorder[2] = 1 < 5`. Valid. `root = 1`, `i = 3`.
      - `1->left = build(i=3, bound=1)`. `pre[3]=7 > 1`. Returns `null`.
      - `1->right = build(i=3, bound=5)`. `pre[3]=7 > 5`. Returns `null`.
      - Returns `TreeNode(1)`.
    - `5->right = build(i=3, bound=8)`
      - `preorder[3] = 7 < 8`. Valid. `root = 7`, `i = 4`.
      - `7->left = build(i=4, bound=7)`. `pre[4]=10 > 7`. Returns `null`.
      - `7->right = build(i=4, bound=8)`. `pre[4]=10 > 8`. Returns `null`.
      - Returns `TreeNode(7)`.
    - Returns `TreeNode(5)` with children 1 and 7.
  - `root->right = build(i=4, bound=INF)`
    - `preorder[4] = 10 < INF`. Valid. `root = 10`, `i = 5`.
    - ...
- Returns `TreeNode(8)`.

## Common Mistakes
- **Passing `i` by value instead of reference:** If you do `int i` instead of `int& i` in the recursive function, `i` will not increment globally across the recursive calls, leading to an infinite loop and completely wrong tree structure.
- **Checking both upper and lower bounds:** While theoretically correct, checking `minBound` is completely unnecessary because the preorder array structure naturally handles the left bounds as we process elements linearly.

## Similar Problems
- Construct Binary Tree from Preorder and Inorder Traversal
- Serialize and Deserialize BST
