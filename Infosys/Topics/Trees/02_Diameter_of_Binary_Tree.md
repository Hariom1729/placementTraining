# Diameter of Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Microsoft

## Topic
Trees

## Pattern
DFS / Tree DP

## Problem Statement
Given the `root` of a binary tree, return the length of the **diameter** of the tree.
The diameter of a binary tree is the length of the **longest path** between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return an integer representing the maximum diameter.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**
```
Input: root = [1,2]
Output: 1
```

**Example 3:**
```
Input: root = [1]
Output: 0
```

## Edge Cases
- A single node tree. The diameter is 0 because there are 0 edges.
- A highly skewed tree (linked list). The diameter is just the depth - 1.
- The longest path might be completely contained within a subtree and NOT pass through the global root.

## Intuition
The diameter passing through a specific node is essentially the depth of its left subtree plus the depth of its right subtree. 
Since the longest path might not pass through the root of the tree, we need to calculate this `leftDepth + rightDepth` for *every single node* in the tree and keep track of the maximum value found.

## Brute Force Approach
**Explanation:** For every node in the tree, calculate the maximum depth of its left subtree and right subtree. The diameter passing through this node is `leftDepth + rightDepth`. Maintain a global maximum.
**Time Complexity:** $O(N^2)$ because for each of the $N$ nodes, we traverse its subtrees to find the depth, taking $O(N)$ time per node.
**Space Complexity:** $O(H)$ for the recursion stack.

## Optimal Approach
**Detailed explanation:**
Instead of calculating the depth from scratch for every node, we can calculate the depth AND the diameter simultaneously using a bottom-up DFS (Tree DP).
1. We define a recursive function `calculateDepth` that returns the depth of the tree.
2. We maintain a global or reference variable `maxi` to track the maximum diameter found so far.
3. For any node, we recursively find `leftDepth` and `rightDepth`.
4. The diameter passing through this current node is `leftDepth + rightDepth`. We update `maxi = max(maxi, leftDepth + rightDepth)`.
5. The function then returns the depth of the current subtree: `1 + max(leftDepth, rightDepth)` to its parent.

This way, we only traverse the tree exactly once!

**Time Complexity:** $O(N)$. We visit each node exactly once during the DFS.
**Space Complexity:** $O(H)$, where $H$ is the height of the tree. This is for the recursive call stack.

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
using namespace std;

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxi = 0;
        calculateDepth(root, maxi);
        return maxi;
    }
    
private:
    // Helper function that returns the depth, but updates maxi with the diameter
    int calculateDepth(TreeNode* node, int& maxi) {
        if (node == nullptr) {
            return 0; // Base case: Depth of null node is 0
        }
        
        // Get depths of left and right subtrees
        int leftDepth = calculateDepth(node->left, maxi);
        int rightDepth = calculateDepth(node->right, maxi);
        
        // The diameter passing through THIS node is leftDepth + rightDepth
        // Update the global maximum diameter found so far
        maxi = max(maxi, leftDepth + rightDepth);
        
        // Return the depth of the subtree rooted at this node
        return 1 + max(leftDepth, rightDepth);
    }
};
```

## Dry Run
Given Tree: `[1, 2, 3, 4, 5]`
- `calculateDepth(1)` -> calls `calc(2)` and `calc(3)`
  - `calc(2)` -> calls `calc(4)` and `calc(5)`
    - `calc(4)` returns 1. `maxi = max(0, 0+0) = 0`.
    - `calc(5)` returns 1. `maxi = max(0, 0+0) = 0`.
    - Back to `calc(2)`: `leftDepth=1`, `rightDepth=1`. 
      - `maxi = max(0, 1 + 1) = 2`.
      - Returns `1 + max(1, 1) = 2`.
  - `calc(3)` returns 1. `maxi` remains 2.
- Back to `calc(1)`: `leftDepth = 2` (from node 2), `rightDepth = 1` (from node 3).
  - `maxi = max(2, 2 + 1) = 3`.
  - Returns `1 + max(2, 1) = 3`.
Result: `maxi = 3`.

## Common Mistakes
- Assuming the longest path MUST pass through the root node. It doesn't. A deep left subtree and right subtree attached to a child node could form a longer path than anything passing through the global root.
- Returning the diameter from the recursive function instead of the depth. The recursive function *must* return the depth so the parent can calculate its own diameter. The diameter itself is tracked via a side-effect (a reference variable).

## Similar Problems
- Binary Tree Maximum Path Sum
- Longest Univalue Path

## Infosys Variations
- **Return the path itself:** Instead of returning just the length of the diameter, you might be asked to return the actual list of nodes that make up the diameter. This requires passing around path vectors, which makes the problem significantly harder.
