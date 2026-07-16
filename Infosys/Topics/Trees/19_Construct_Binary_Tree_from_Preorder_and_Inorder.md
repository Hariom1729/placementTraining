# Construct Binary Tree from Preorder and Inorder Traversal

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Bloomberg

## Topic
Trees

## Pattern
Tree Construction / Divide and Conquer

## Problem Statement
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Constraints
- $1 \le preorder.length \le 3000$
- $inorder.length == preorder.length$
- $-3000 \le preorder[i], inorder[i] \le 3000$
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

## Input
- `preorder` vector of integers.
- `inorder` vector of integers.

## Output
- Return the `root` pointer of the constructed Binary Tree.

## Sample Test Cases

**Example 1:**
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**
```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Edge Cases
- Arrays with a single element.
- Highly skewed trees where the left or right subtree sizes are 0.

## Intuition
**Preorder (Root -> Left -> Right):** The very first element is ALWAYS the root of the tree.
**Inorder (Left -> Root -> Right):** If we find the root element in the `inorder` array, everything to the left of it forms the left subtree, and everything to the right of it forms the right subtree!

Using this property, we can recursively divide and conquer:
1. Pop the first element from `preorder` to create the current root.
2. Find the index of this root in the `inorder` array.
3. The number of elements to the left of the root in `inorder` gives us the size of the left subtree.
4. Recursively build the `left` child using the left portion of the arrays.
5. Recursively build the `right` child using the right portion of the arrays.

To speed up the "Find the index" step, we can hash the `inorder` array into a map mapping `value -> index` beforehand.

## Brute Force Approach
N/A - The recursive boundary method is standard.

## Optimal Approach
**Detailed explanation:**
1. Create a `unordered_map<int, int> inMap` to store the values of `inorder` and their indices.
2. Create a recursive function `buildTree(preorder, preStart, preEnd, inorder, inStart, inEnd, inMap)`.
3. **Base Case:** If `preStart > preEnd` or `inStart > inEnd`, return `nullptr`.
4. The root value is `preorder[preStart]`. Create a new `TreeNode` with this value.
5. Find the root's index in `inorder` using the hash map: `inRoot = inMap[root->val]`.
6. Calculate the number of nodes in the left subtree: `numsLeft = inRoot - inStart`.
7. **Recursive Calls:**
   - `root->left = buildTree(..., preStart + 1, preStart + numsLeft, ..., inStart, inRoot - 1, ...)`
   - `root->right = buildTree(..., preStart + numsLeft + 1, preEnd, ..., inRoot + 1, inEnd, ...)`
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inMap;
        // Hash the inorder array to achieve O(1) lookups
        for (int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }
        
        return build(preorder, 0, preorder.size() - 1,
                     inorder, 0, inorder.size() - 1, 
                     inMap);
    }
    
private:
    TreeNode* build(vector<int>& preorder, int preStart, int preEnd,
                    vector<int>& inorder, int inStart, int inEnd,
                    unordered_map<int, int>& inMap) {
        
        // Base case: no elements left to process
        if (preStart > preEnd || inStart > inEnd) {
            return nullptr;
        }
        
        // The first element in the current preorder segment is the root
        TreeNode* root = new TreeNode(preorder[preStart]);
        
        // Find the index of this root in the inorder array
        int inRoot = inMap[root->val];
        
        // Number of elements in the left subtree
        int numsLeft = inRoot - inStart;
        
        // Recursively build the left subtree
        root->left = build(preorder, preStart + 1, preStart + numsLeft, 
                           inorder, inStart, inRoot - 1, inMap);
                           
        // Recursively build the right subtree
        root->right = build(preorder, preStart + numsLeft + 1, preEnd, 
                            inorder, inRoot + 1, inEnd, inMap);
                            
        return root;
    }
};
```

## Dry Run
`preorder = [3, 9, 20, 15, 7]`, `inorder = [9, 3, 15, 20, 7]`
- Map: `{9:0, 3:1, 15:2, 20:3, 7:4}`
- `build(pre(0..4), in(0..4))`
  - Root: `pre[0] = 3`. `inRoot = map[3] = 1`. `numsLeft = 1 - 0 = 1`.
  - Left Call: `build(pre(1..1), in(0..0))`
    - Root: `pre[1] = 9`. `inRoot = map[9] = 0`. `numsLeft = 0`.
    - Returns `TreeNode(9)` with null children.
  - Right Call: `build(pre(2..4), in(2..4))`
    - Root: `pre[2] = 20`. `inRoot = map[20] = 3`. `numsLeft = 3 - 2 = 1`.
    - Left Call: `build(pre(3..3), in(2..2))` -> returns `TreeNode(15)`.
    - Right Call: `build(pre(4..4), in(4..4))` -> returns `TreeNode(7)`.
    - Returns `TreeNode(20)` with children 15 and 7.
- Root 3 returns with left child 9 and right child 20.

## Common Mistakes
- **Passing array copies instead of indices:** If you use vector slicing/copying (e.g., `vector(preorder.begin() + 1, ...)`) for every recursive call, your time complexity degrades to $O(N^2)$ and memory usage explodes. ALWAYS pass by reference and use `start` and `end` indices.
- **Calculating `preStart` and `preEnd` incorrectly:** Memorize that the end of the left subarray in preorder is `preStart + numsLeft`. The right subarray naturally starts at `preStart + numsLeft + 1`.

## Similar Problems
- Construct Binary Tree from Inorder and Postorder Traversal
- Serialize and Deserialize Binary Tree
