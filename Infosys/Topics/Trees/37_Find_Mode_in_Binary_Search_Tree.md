# Find Mode in Binary Search Tree

## Difficulty
Easy

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees / BST

## Pattern
Inorder Traversal

## Problem Statement
Given the `root` of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Input
- `root` pointer of the Binary Search Tree.

## Output
- Return a 1D array of integers representing the modes.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,null,2,2]
Output: [2]
```

**Example 2:**
```
Input: root = [0]
Output: [0]
```

## Edge Cases
- All elements appear the same number of times (e.g., 1 time each). All elements are modes.
- Tree has only one node.

## Intuition
**Brute Force:** Traverse the tree, store counts in an `unordered_map<int, int>`, find the maximum count, and then extract all keys with that count. This takes $O(N)$ space.
**Optimal ($O(1)$ Space):** Since this is a BST, an Inorder Traversal visits the elements in sorted order. If there are duplicates, they will be strictly adjacent to each other during the traversal! (e.g., `1 -> 2 -> 2 -> 2 -> 3`).
We just need to track the `prev` node's value. 
- If `curr->val == prev->val`, we increment the `currentCount`.
- If `curr->val != prev->val`, we reset `currentCount = 1`.
- If `currentCount == maxCount`, we add the value to our answer array.
- If `currentCount > maxCount`, we found a new strict maximum! We must clear our answer array, add this new value, and update `maxCount`.

## Brute Force Approach
**Explanation:** Map counting.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the hash map.

## Optimal Approach (Inorder Traversal)
**Detailed explanation:**
1. Initialize member variables:
   - `int maxCount = 0`
   - `int currentCount = 0`
   - `TreeNode* prev = nullptr`
   - `vector<int> ans`
2. Create `inorder(TreeNode* root)` function.
3. Traverse left: `inorder(root->left)`.
4. **Process Node:**
   - If `prev != nullptr && root->val == prev->val`, increment `currentCount++`.
   - Else, `currentCount = 1`.
   - If `currentCount > maxCount`:
     - `maxCount = currentCount`.
     - `ans.clear()`.
     - `ans.push_back(root->val)`.
   - Else if `currentCount == maxCount`:
     - `ans.push_back(root->val)`.
   - Update `prev = root`.
5. Traverse right: `inorder(root->right)`.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(1)$ auxiliary space (excluding the recursion stack and output array as per problem description).

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
private:
    int maxCount = 0;
    int currentCount = 0;
    TreeNode* prev = nullptr;
    vector<int> ans;
    
    void inorder(TreeNode* root) {
        if (root == nullptr) return;
        
        // Go Left
        inorder(root->left);
        
        // Process Node
        if (prev != nullptr && root->val == prev->val) {
            currentCount++;
        } else {
            currentCount = 1;
        }
        
        if (currentCount > maxCount) {
            maxCount = currentCount;
            ans.clear();
            ans.push_back(root->val);
        } else if (currentCount == maxCount) {
            ans.push_back(root->val);
        }
        
        prev = root;
        
        // Go Right
        inorder(root->right);
    }
    
public:
    vector<int> findMode(TreeNode* root) {
        inorder(root);
        return ans;
    }
};
```

## Dry Run
Tree: `[1, null, 2, 2]`
Inorder traversal visits: 1, 2, 2.
- Visit 1: `prev` is null. `currentCount = 1`. `maxCount` becomes 1. `ans = [1]`. `prev = 1`.
- Visit 2: `prev` is 1. Not equal. `currentCount = 1`. `currentCount == maxCount`. `ans = [1, 2]`. `prev = 2`.
- Visit 2: `prev` is 2. Equal! `currentCount = 2`. `currentCount > maxCount (1)`. 
  - `maxCount = 2`.
  - `ans.clear()`.
  - `ans = [2]`.
  - `prev = 2`.
Result: `[2]`.

## Common Mistakes
- **Forgetting to clear the answer array:** When you find a new `maxCount`, all previous entries in the array are no longer modes! You must `ans.clear()` before pushing the new value.

## Similar Problems
- Find First and Last Position of Element in Sorted Array
