# Binary Tree Right Side View

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Trees

## Pattern
Reverse Preorder Traversal / BFS

## Problem Statement
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the right side view.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2:**
```
Input: root = [1,null,3]
Output: [1,3]
```

**Example 3:**
```
Input: root = []
Output: []
```

## Edge Cases
- Skewed trees: A completely left-skewed tree `1 -> 2 -> 3` will have a right view of `[1, 2, 3]`. The right view is NOT just the right boundary! If the right branch doesn't exist, you look "through" the empty space and see the left branch.

## Intuition
**BFS Intuition:**
If we traverse the tree level-by-level, the right side view simply consists of the **very last node** at every level. We can use a standard Level Order Traversal and just pick `level[size - 1]`.

**DFS Intuition (Optimal):**
We can achieve this elegantly with DFS. If we traverse the tree in a **Reverse Preorder** manner (Root -> Right -> Left), we guarantee that the first node we encounter at any depth level will be the rightmost node of that level!
We can use a vector `ans`. If `depth == ans.size()`, it means this is the first time we are visiting this depth level, so we append the node to `ans`.

## Brute Force Approach
N/A. Both BFS and DFS are $O(N)$ and optimal.

## Optimal Approach (DFS)
**Detailed explanation:**
1. Create a `vector<int> ans` and a recursive function `recursion(TreeNode* root, int depth, vector<int>& ans)`.
2. **Base Case:** If `root == nullptr`, return.
3. If the current `depth` is equal to the size of `ans`, it means we have reached a new depth level for the first time. Add `root->val` to `ans`.
   - *(e.g., At depth 0, `ans` size is 0. We add the root. Now `ans` size is 1. If we visit another node at depth 0, `0 != 1`, so we ignore it.)*
4. **Recursive Step:**
   - Recursively visit the **right** child first: `recursion(root->right, depth + 1, ans)`.
   - Recursively visit the **left** child next: `recursion(root->left, depth + 1, ans)`.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(H)$ where $H$ is the height of the tree, representing the recursion stack. (This is generally better space complexity than BFS which takes $O(N/2)$ queue space in the worst case).

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
    vector<int> rightSideView(TreeNode* root) {
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
        // add the node's value. Because we visit right before left, 
        // the first node we hit at a depth will always be the rightmost one.
        if (depth == ans.size()) {
            ans.push_back(root->val);
        }
        
        // Visit Right first, then Left!
        recursion(root->right, depth + 1, ans);
        recursion(root->left, depth + 1, ans);
    }
};
```

## Dry Run
Tree: `[1, 2, 3, null, 5, null, 4]` (1 has children 2,3. 2 has right child 5. 3 has right child 4).
- `recursion(1, depth=0)`
  - `depth (0) == ans.size() (0)`. `ans = [1]`.
  - `recursion(3, depth=1)`
    - `depth (1) == ans.size() (1)`. `ans = [1, 3]`.
    - `recursion(4, depth=2)`
      - `depth (2) == ans.size() (2)`. `ans = [1, 3, 4]`.
      - right is null, left is null. Returns.
    - `recursion(3->left(null))` returns.
  - `recursion(2, depth=1)`
    - `depth (1) != ans.size() (3)`. Ignored!
    - `recursion(5, depth=2)`
      - `depth (2) != ans.size() (3)`. Ignored!
    - `recursion(2->left(null))` returns.
Result: `[1, 3, 4]`.

## Common Mistakes
- **Assuming Right View == Right Boundary:** A node on the left side of the tree CAN be part of the right view if there are no nodes on the right side of the tree at that specific depth.
- **Visiting Left before Right in DFS:** If you visit left before right, you will generate the **Left Side View**.

## Similar Problems
- Binary Tree Left Side View
- Top View of Binary Tree
- Bottom View of Binary Tree

## Infosys Variations
- **Left Side View:** To solve Left View, simply swap the order of recursive calls to `recursion(root->left)` followed by `recursion(root->right)`.
