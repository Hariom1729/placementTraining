# Binary Tree Paths

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Trees

## Pattern
DFS / Backtracking

## Problem Statement
Given the `root` of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a vector of strings representing the paths.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Example 2:**
```
Input: root = [1]
Output: ["1"]
```

## Edge Cases
- Tree has only one node. The output should not contain any `"->"`.

## Intuition
This is a classic DFS string building problem. We need to explore every possible path from the root down to the leaves.
As we travel down the tree, we append the current node's value to our path string.
If we reach a leaf node (both children are null), we have completed a full path! We can add this path to our answer list.
If we are not at a leaf node, we append `"->"` and recursively call the function for the left and right children.

## Brute Force Approach
N/A - Standard DFS is optimal.

## Optimal Approach (DFS with String Copy)
**Detailed explanation:**
1. Create a `vector<string> ans`.
2. Create a recursive function `dfs(TreeNode* root, string path, vector<string>& ans)`. Note that `path` is passed **by value** (a copy is made), so changes in one branch don't affect the other branch.
3. **Base Case 1:** If `root == nullptr`, return.
4. Append `to_string(root->val)` to the `path`.
5. **Base Case 2 (Leaf Check):** If `root->left == nullptr && root->right == nullptr`, it means we are at a leaf. Add `path` to `ans` and return.
6. **Recursive Step:** If it's not a leaf, append `"->"` to the path, then recurse left and right.
   - `dfs(root->left, path + "->", ans)`
   - `dfs(root->right, path + "->", ans)`

*Note on optimization:* Passing strings by value creates a lot of copies, which is fine for small trees ($N=100$) and leads to very clean code. For massive trees, passing a single string by reference and explicitly backtracking (popping characters) would be faster, but significantly more complex to code due to varying lengths of `to_string()`.

**Time Complexity:** $O(N)$ where $N$ is the number of nodes. We visit each node once. The string copying adds overhead, so technically it's $O(N \times L)$ where $L$ is the string length.
**Space Complexity:** $O(H)$ for the recursion stack, plus the space for the output array.

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
#include <string>
using namespace std;

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        if (root == nullptr) return ans;
        
        dfs(root, "", ans);
        
        return ans;
    }
    
private:
    void dfs(TreeNode* root, string path, vector<string>& ans) {
        // Base case
        if (root == nullptr) {
            return;
        }
        
        // Append current node to the path
        path += to_string(root->val);
        
        // If it's a leaf node, add the completed path to our answer array
        if (root->left == nullptr && root->right == nullptr) {
            ans.push_back(path);
            return;
        }
        
        // If it's not a leaf, append the arrow and recurse
        path += "->";
        dfs(root->left, path, ans);
        dfs(root->right, path, ans);
    }
};
```

## Dry Run
Tree: `[1, 2, 3, null, 5]`
- `dfs(1, "", ans)`
  - `path = "1"`. Not a leaf. `path = "1->"`.
  - `dfs(2, "1->", ans)`
    - `path = "1->2"`. Not a leaf. `path = "1->2->"`.
    - `dfs(null)` -> returns.
    - `dfs(5, "1->2->", ans)`
      - `path = "1->2->5"`. Is a leaf! `ans.push_back("1->2->5")`. Returns.
  - `dfs(3, "1->", ans)`
    - `path = "1->3"`. Is a leaf! `ans.push_back("1->3")`. Returns.
Result: `["1->2->5", "1->3"]`.

## Common Mistakes
- **Checking for null at the top and adding to `ans` there:** If you do `if (root == nullptr) ans.push_back(path);`, you will add duplicate paths for leaves (because a leaf will trigger the null condition twice: once for left, once for right). Always check `if (left == null && right == null)` to detect leaves safely.

## Similar Problems
- Path Sum
- Sum Root to Leaf Numbers
