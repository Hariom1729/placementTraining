# Binary Tree Maximum Path Sum

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, ByteDance

## Topic
Trees

## Pattern
DFS / Tree DP

## Problem Statement
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.
The **path sum** of a path is the sum of the node's values in the path.
Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

## Constraints
- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return an integer representing the maximum path sum.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:**
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## Edge Cases
- All nodes contain negative values. (The answer should be the single largest negative number, not 0, because the path must be non-empty).
- The maximum path is just a single node.

## Intuition
This problem is a direct, albeit harder, relative of the **Diameter of a Binary Tree** problem.
In the diameter problem, we wanted the longest path (number of edges). Here, we want the path with the maximum sum of values.
For any given node, the maximum path passing *through* it as the highest point (the "arch" of the path) is:
`Node.val + MaxPathSum(Left Child) + MaxPathSum(Right Child)`.

However, when this node returns its maximum path sum to its parent, it CANNOT return a branched path! A path must be a single line. Therefore, it can only return:
`Node.val + max(MaxPathSum(Left Child), MaxPathSum(Right Child))`.

Also, if the maximum path sum of a child is negative, we should ignore it entirely (treat it as 0) because adding a negative number will only decrease our current path sum.

## Brute Force Approach
**Explanation:** For every node, recursively find the maximum straight-line path downwards on the left and right, and add them together. Keep track of the global maximum.
**Time Complexity:** $O(N^2)$ due to repeated traversals.
**Space Complexity:** $O(H)$

## Optimal Approach
**Detailed explanation:**
1. Initialize a global/reference variable `maxi = INT_MIN`.
2. Create a recursive function `findMaxPath(TreeNode* node, int& maxi)`.
3. **Base Case:** If `node == nullptr`, return `0`.
4. **Recursive Step:** 
   - Calculate `leftMax = findMaxPath(node->left, maxi)`. If `leftMax` is negative, set it to `0` (we ignore negative contributions). `leftMax = max(0, leftMax)`.
   - Calculate `rightMax = findMaxPath(node->right, maxi)`. If `rightMax` is negative, set it to `0`. `rightMax = max(0, rightMax)`.
5. **Update Global Maximum:** The maximum path forming an arch through the current node is `node->val + leftMax + rightMax`. Update `maxi = max(maxi, node->val + leftMax + rightMax)`.
6. **Return Value:** Return the maximum single-line path that can be extended to the parent: `node->val + max(leftMax, rightMax)`.

**Time Complexity:** $O(N)$ since every node is visited exactly once.
**Space Complexity:** $O(H)$ for the recursive call stack.

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
public:
    int maxPathSum(TreeNode* root) {
        int maxi = INT_MIN;
        findMaxPath(root, maxi);
        return maxi;
    }
    
private:
    int findMaxPath(TreeNode* node, int& maxi) {
        if (node == nullptr) {
            return 0;
        }
        
        // Recursively get max path from left and right children.
        // If they are negative, we don't include them in our path (hence max with 0).
        int leftMax = max(0, findMaxPath(node->left, maxi));
        int rightMax = max(0, findMaxPath(node->right, maxi));
        
        // The maximum path forming an inverted U-shape through THIS node
        int currentArchSum = node->val + leftMax + rightMax;
        
        // Update the global maximum path sum found so far
        maxi = max(maxi, currentArchSum);
        
        // Return the maximum single continuous path down one branch
        // so the parent can connect to it.
        return node->val + max(leftMax, rightMax);
    }
};
```

## Dry Run
Tree: `[-10, 9, 20, null, null, 15, 7]`
- `findMax(-10)`
  - `findMax(9)`
    - left/right are null (returns 0).
    - `archSum` = 9 + 0 + 0 = 9. `maxi` = 9.
    - returns 9 + 0 = 9.
  - `leftMax` at -10 is 9.
  - `findMax(20)`
    - `findMax(15)` -> returns 15. `maxi` = max(9, 15) = 15.
    - `findMax(7)` -> returns 7. `maxi` = max(15, 7) = 15.
    - `archSum` at 20 = 20 + 15 + 7 = 42. `maxi` = max(15, 42) = 42.
    - returns 20 + max(15, 7) = 35.
  - `rightMax` at -10 is 35.
  - `archSum` at -10 = -10 + 9 + 35 = 34. `maxi` = max(42, 34) = 42.
  - returns -10 + max(9, 35) = 25.
Result: `maxi = 42`.

## Common Mistakes
- **Not handling negative paths:** If you don't do `max(0, ...)` for the children, you will forcefully include negative numbers into your path, lowering your maximum score.
- **Updating `maxi` with just the returned value:** You must update `maxi` using the sum of BOTH children + the node's value, because the highest path might span across both left and right subtrees of a node.

## Similar Problems
- Diameter of Binary Tree
- Path Sum
- Longest Univalue Path
