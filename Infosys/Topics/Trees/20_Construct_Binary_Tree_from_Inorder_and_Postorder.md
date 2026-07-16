# Construct Binary Tree from Inorder and Postorder Traversal

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Trees

## Pattern
Tree Construction / Divide and Conquer

## Problem Statement
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

## Constraints
- $1 \le inorder.length \le 3000$
- $postorder.length == inorder.length$
- $-3000 \le inorder[i], postorder[i] \le 3000$
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is guaranteed to be the inorder traversal of the tree.
- `postorder` is guaranteed to be the postorder traversal of the tree.

## Input
- `inorder` vector of integers.
- `postorder` vector of integers.

## Output
- Return the `root` pointer of the constructed Binary Tree.

## Sample Test Cases

**Example 1:**
```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**
```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

## Edge Cases
- Arrays with a single element.
- Highly skewed trees where the left or right subtree sizes are 0.

## Intuition
**Postorder (Left -> Right -> Root):** The very LAST element is ALWAYS the root of the tree.
**Inorder (Left -> Root -> Right):** If we find the root element in the `inorder` array, everything to the left of it forms the left subtree, and everything to the right of it forms the right subtree!

This is almost identical to constructing a tree from Preorder, but instead of the root being at the beginning of the array, it's at the end of the `postorder` subarray.
1. Pop the last element from the current `postorder` segment to create the root.
2. Find the index of this root in the `inorder` array.
3. The number of elements to the left of the root in `inorder` gives us the size of the left subtree (`numsLeft`).
4. Recursively build the `left` child using the left portion of the arrays.
5. Recursively build the `right` child using the right portion of the arrays.

To speed up the "Find the index" step, we hash the `inorder` array into a map mapping `value -> index`.

## Brute Force Approach
N/A - The recursive boundary method is standard.

## Optimal Approach
**Detailed explanation:**
1. Create a `unordered_map<int, int> inMap` to store the values of `inorder` and their indices.
2. Create a recursive function `buildTree(postorder, postStart, postEnd, inorder, inStart, inEnd, inMap)`.
3. **Base Case:** If `postStart > postEnd` or `inStart > inEnd`, return `nullptr`.
4. The root value is `postorder[postEnd]`. Create a new `TreeNode` with this value.
5. Find the root's index in `inorder` using the hash map: `inRoot = inMap[root->val]`.
6. Calculate the number of nodes in the left subtree: `numsLeft = inRoot - inStart`.
7. **Recursive Calls:**
   - **Left Subtree:** The postorder bounds will be from `postStart` to `postStart + numsLeft - 1`.
   - **Right Subtree:** The postorder bounds will be from `postStart + numsLeft` to `postEnd - 1`.
8. Return `root`.

**Time Complexity:** $O(N)$ because finding the root index takes $O(1)$ with the hash map, and we build $N$ nodes.
**Space Complexity:** $O(N)$ for the hash map and the recursion stack.

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
#include <unordered_map>
using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> inMap;
        // Hash the inorder array to achieve O(1) lookups
        for (int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }
        
        return build(postorder, 0, postorder.size() - 1,
                     inorder, 0, inorder.size() - 1, 
                     inMap);
    }
    
private:
    TreeNode* build(vector<int>& postorder, int postStart, int postEnd,
                    vector<int>& inorder, int inStart, int inEnd,
                    unordered_map<int, int>& inMap) {
        
        // Base case: no elements left to process
        if (postStart > postEnd || inStart > inEnd) {
            return nullptr;
        }
        
        // The last element in the current postorder segment is the root
        TreeNode* root = new TreeNode(postorder[postEnd]);
        
        // Find the index of this root in the inorder array
        int inRoot = inMap[root->val];
        
        // Number of elements in the left subtree
        int numsLeft = inRoot - inStart;
        
        // Recursively build the left subtree
        root->left = build(postorder, postStart, postStart + numsLeft - 1, 
                           inorder, inStart, inRoot - 1, inMap);
                           
        // Recursively build the right subtree
        root->right = build(postorder, postStart + numsLeft, postEnd - 1, 
                            inorder, inRoot + 1, inEnd, inMap);
                            
        return root;
    }
};
```

## Dry Run
`inorder = [9, 3, 15, 20, 7]`, `postorder = [9, 15, 7, 20, 3]`
- Map: `{9:0, 3:1, 15:2, 20:3, 7:4}`
- `build(post(0..4), in(0..4))`
  - Root: `post[4] = 3`. `inRoot = map[3] = 1`. `numsLeft = 1 - 0 = 1`.
  - Left Call: `build(post(0..0), in(0..0))`
    - Root: `post[0] = 9`. Returns `TreeNode(9)`.
  - Right Call: `build(post(1..3), in(2..4))`
    - Root: `post[3] = 20`. `inRoot = map[20] = 3`. `numsLeft = 3 - 2 = 1`.
    - Left Call: `build(post(1..1), in(2..2))` -> returns `TreeNode(15)`.
    - Right Call: `build(post(2..2), in(4..4))` -> returns `TreeNode(7)`.
    - Returns `TreeNode(20)` with children 15 and 7.
- Root 3 returns with left child 9 and right child 20.

## Common Mistakes
- **Mixing up index calculations:** It's extremely easy to get `postStart + numsLeft - 1` wrong. Always remember that the length of the left postorder chunk MUST exactly equal `numsLeft`.
  - Length of `[postStart, postStart + numsLeft - 1]` = `(postStart + numsLeft - 1) - postStart + 1 = numsLeft`. This confirms the math is correct!

## Similar Problems
- Construct Binary Tree from Preorder and Inorder Traversal
