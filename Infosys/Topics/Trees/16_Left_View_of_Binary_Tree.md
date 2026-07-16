# Left View of Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Oyo, Paytm, Flipkart

## Topic
Trees

## Pattern
Preorder Traversal / BFS

## Problem Statement
Given the `root` of a binary tree, imagine yourself standing on the **left side** of it, return the values of the nodes you can see ordered from top to bottom.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the left side view.

## Sample Test Cases

**Example 1:**
```
Input: 
       1
    /    \
   2      3
    \      \
     4      5
      \
       6
Output: [1, 2, 4, 6]
```

**Example 2:**
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,2,5]
```

**Example 3:**
```
Input: root = []
Output: []
```

## Edge Cases
- Skewed trees: A completely right-skewed tree `1 -> null, 3` will have a left view of `[1, 3]`. The left view is NOT just the left boundary! If the left branch doesn't exist, you look "through" the empty space and see the right branch.

## Intuition
This is the exact symmetric twin of the **Right Side View** problem.
If we traverse the tree level-by-level (BFS), the left side view is the **very first node** at every level.
If we traverse the tree via DFS (Preorder: Root -> Left -> Right), the first node we encounter at any depth level will be the leftmost node of that level!

## Brute Force Approach
N/A. Both BFS and DFS are optimal $O(N)$ approaches.

## Optimal Approach (DFS)
**Detailed explanation:**
1. Create a `vector<int> ans` and a recursive function `recursion(TreeNode* root, int depth, vector<int>& ans)`.
2. **Base Case:** If `root == nullptr`, return.
3. If the current `depth` is equal to the size of `ans`, it means this is the *first* time we are visiting this depth level. Add `root->val` to `ans`.
4. **Recursive Step:**
   - Recursively visit the **left** child first: `recursion(root->left, depth + 1, ans)`.
   - Recursively visit the **right** child next: `recursion(root->right, depth + 1, ans)`.

By visiting the left child before the right child, we mathematically guarantee that the first time we reach depth `D`, it will be on the leftmost possible node.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(H)$ where $H$ is the height of the tree for the recursion stack.

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
    vector<int> leftSideView(TreeNode* root) {
        vector<int> ans;
        recursion(root, 0, ans);
        return ans;
    }
    
private:
    void recursion(TreeNode* root, int depth, vector<int>& ans) {
        if (root == nullptr) {
            return;
        }
        
        // If this is the first time we are visiting this depth level,
        // add the node's value. Because we visit left before right, 
        // the first node we hit at a depth will always be the leftmost one.
        if (depth == ans.size()) {
            ans.push_back(root->val);
        }
        
        // Visit Left first, then Right!
        recursion(root->left, depth + 1, ans);
        recursion(root->right, depth + 1, ans);
    }
};
```

## Dry Run
Tree: `[1, 2, 3, null, 5, null, 4]` (1 has children 2,3. 2 has right child 5. 3 has right child 4).
- `recursion(1, depth=0)`
  - `depth (0) == ans.size() (0)`. `ans = [1]`.
  - `recursion(2, depth=1)`
    - `depth (1) == ans.size() (1)`. `ans = [1, 2]`.
    - `recursion(2->left(null))` returns.
    - `recursion(5, depth=2)`
      - `depth (2) == ans.size() (2)`. `ans = [1, 2, 5]`.
      - right/left are null. returns.
  - `recursion(3, depth=1)`
    - `depth (1) != ans.size() (3)`. Ignored!
    - `recursion(3->left(null))` returns.
    - `recursion(4, depth=2)`
      - `depth (2) != ans.size() (3)`. Ignored!
Result: `[1, 2, 5]`.

## Common Mistakes
- **Assuming Left View == Left Boundary:** A node on the right side of the tree CAN be part of the left view if there are no nodes on the left side of the tree at that specific depth.

## Similar Problems
- Binary Tree Right Side View
- Top View of Binary Tree
- Bottom View of Binary Tree
