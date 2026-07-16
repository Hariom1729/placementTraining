# Diagonal Traversal of Binary Tree

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft

## Topic
Trees

## Pattern
Coordinate Traversal / Queue

## Problem Statement
Given a Binary Tree, print the diagonal traversal of the binary tree.
Consider lines of slope -1 passing between nodes. Given a Binary Tree, print all diagonal elements in a binary tree belonging to same line.
If there are multiple diagonals, print them one by one starting from the topmost diagonal to the bottommost diagonal. For nodes falling in the same diagonal, print them from left to right.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the diagonal traversal.

## Sample Test Cases

**Example 1:**
```
Input:
            8
         /     \
        3      10
      /   \      \
     1     6     14
         /   \   /
        4     7 13
Output: [8, 10, 14, 3, 6, 7, 13, 1, 4]
Explanation:
Diagonal 1: 8, 10, 14
Diagonal 2: 3, 6, 7, 13
Diagonal 3: 1, 4
```

## Edge Cases
- Skewed trees (either completely left or completely right).
- Single node trees.

## Intuition
When we move from a node to its **right child**, both the node and its right child lie on the *same* diagonal.
When we move from a node to its **left child**, the left child starts a *new* diagonal (specifically, the next diagonal below).
This logic is best handled iteratively using a Queue. We start at the root and print all nodes going strictly to the right. While we do this, any left children we encounter are pushed into a queue. These left children form the starting points of the *subsequent* diagonals!

## Brute Force Approach
**Explanation:** Assign a "diagonal distance" (DD) to each node using recursion. `DD(root) = 0`. `DD(left) = DD(parent) + 1`. `DD(right) = DD(parent)`. Store in a map `map<int, vector<int>>` and print.
**Time Complexity:** $O(N \log N)$ due to map insertions.
**Space Complexity:** $O(N)$

## Optimal Approach
**Detailed explanation:**
Instead of a map, we can use a pure iterative Queue approach to achieve $O(N)$ time.
1. Create a `queue<TreeNode*> q`.
2. Push the `root` into the queue.
3. While the queue is not empty:
   - Create a pointer `curr = q.front()` and `q.pop()`.
   - While `curr != nullptr`:
     - Add `curr->val` to the answer array.
     - If `curr->left` exists, **push it to the queue**. (This left child belongs to the *next* diagonal).
     - Move strictly to the right: `curr = curr->right`. (Since this belongs to the *current* diagonal).
4. The queue ensures that we process all components of Diagonal 1 before we process the left-children that form Diagonal 2.

**Time Complexity:** $O(N)$ because every node is pushed to the queue once and processed in the inner `while` loop once.
**Space Complexity:** $O(N)$ for the queue (which stores the left children).

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
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> diagonal(TreeNode *root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            // Traverse down the right slope, adding all nodes to the current diagonal
            while (curr != nullptr) {
                ans.push_back(curr->val);
                
                // If a left child exists, it starts a new diagonal on the next level.
                // Queue it up for later.
                if (curr->left != nullptr) {
                    q.push(curr->left);
                }
                
                // Move down the current diagonal
                curr = curr->right;
            }
        }
        
        return ans;
    }
};
```

## Dry Run
Tree:
```
    8
  /   \
 3    10
```
- Queue: `[8]`
- Pop 8. `curr = 8`.
  - Loop: `curr=8`. Add 8 to ans. Left child 3 pushed to `q=[3]`. `curr = curr->right(10)`.
  - Loop: `curr=10`. Add 10 to ans. Left null. `curr = curr->right(null)`.
  - Loop breaks. `ans = [8, 10]`.
- Pop 3. `curr = 3`.
  - Loop: `curr=3`. Add 3 to ans. Left null. `curr = curr->right(null)`.
  - Loop breaks. `ans = [8, 10, 3]`.
- Queue empty.
Result: `[8, 10, 3]`.

## Common Mistakes
- **Confusing Diagonal Traversal with Level Order or Vertical Order:** Remember the golden rule for diagonals: Right child = same diagonal. Left child = next diagonal.
- **Using Recursion without a Map:** Standard DFS cannot process diagonals in the correct printing order without using a `map<int, vector<int>>` to group them, which makes it $O(N \log N)$. The iterative queue approach is superior.

## Similar Problems
- Vertical Order Traversal of a Binary Tree
- Binary Tree Level Order Traversal
