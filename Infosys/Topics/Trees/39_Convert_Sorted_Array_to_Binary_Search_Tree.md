# Convert Sorted Array to Binary Search Tree

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Airbnb, Apple

## Topic
Trees / BST / Divide and Conquer

## Pattern
Binary Search Traversal

## Problem Statement
Given an integer array `nums` where the elements are sorted in ascending order, convert it to a **height-balanced** binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Constraints
- $1 \le nums.length \le 10^4$
- $-10^4 \le nums[i] \le 10^4$
- `nums` is sorted in a strictly increasing order.

## Input
- `nums` vector of integers.

## Output
- Return the `TreeNode*` pointing to the root of the constructed BST.

## Sample Test Cases

**Example 1:**
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.
```

**Example 2:**
```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## Edge Cases
- Array with one element.
- Array with two elements. (One node will be the root, the other will be a child. Still balanced).

## Intuition
To create a height-balanced BST from a sorted array, the root node must be the **middle element** of the array. This ensures that the left half of the array (which becomes the left subtree) and the right half of the array (which becomes the right subtree) have roughly the exact same number of elements!
Once we pick the middle element as the root, we recursively do the exact same thing for the left subarray and the right subarray.
This is identical to the logic of Binary Search.

## Brute Force Approach
N/A - The binary search method is the standard and only logical way.

## Optimal Approach (Divide and Conquer)
**Detailed explanation:**
1. Create a helper recursive function `build(nums, left, right)`.
2. **Base Case:** If `left > right`, it means the subarray is empty. Return `nullptr`.
3. Find the middle index: `mid = left + (right - left) / 2`.
4. Create the root node: `TreeNode* root = new TreeNode(nums[mid])`.
5. Recursively build the left subtree using the left half of the array: 
   `root->left = build(nums, left, mid - 1)`.
6. Recursively build the right subtree using the right half of the array:
   `root->right = build(nums, mid + 1, right)`.
7. Return `root`.

**Time Complexity:** $O(N)$ because we create exactly one node for every element in the array.
**Space Complexity:** $O(\log N)$ since the tree is perfectly height-balanced, the recursion stack will only go $\log N$ deep.

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
using namespace std;

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums, 0, nums.size() - 1);
    }
    
private:
    TreeNode* build(vector<int>& nums, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        
        // Find the middle element to ensure height balance
        int mid = left + (right - left) / 2;
        
        // Create root from the middle element
        TreeNode* root = new TreeNode(nums[mid]);
        
        // Recursively build left and right subtrees
        root->left = build(nums, left, mid - 1);
        root->right = build(nums, mid + 1, right);
        
        return root;
    }
};
```

## Dry Run
`nums = [-10, -3, 0, 5, 9]`
- `build(0, 4)`: `mid = 2`. `nums[2] = 0`. `root = 0`.
  - `root->left = build(0, 1)`
    - `mid = 0`. `nums[0] = -10`. `root = -10`.
    - `root->left = build(0, -1)` -> null.
    - `root->right = build(1, 1)`
      - `mid = 1`. `nums[1] = -3`. `root = -3`.
      - returns `-3`.
    - Returns `-10` with right child `-3`.
  - `root->right = build(3, 4)`
    - `mid = 3`. `nums[3] = 5`. `root = 5`.
    - `root->left = build(3, 2)` -> null.
    - `root->right = build(4, 4)`
      - `mid = 4`. `nums[4] = 9`. `root = 9`.
      - returns `9`.
    - Returns `5` with right child `9`.
- Returns `0` with left child `-10` and right child `5`.

## Common Mistakes
- **Passing vectors by value:** If you slice the vector `vector<int>(nums.begin(), nums.begin() + mid)` for the recursive calls, you will use $O(N \log N)$ time and $O(N \log N)$ space. ALWAYS pass the vector by reference and use `left` and `right` indices!
- **Using `mid = (left + right) / 2`:** While this works for this specific problem due to small constraints ($10^4$), it's a bad habit that can cause integer overflow in larger arrays. Use `left + (right - left) / 2` instead.

## Similar Problems
- Convert Sorted List to Binary Search Tree
