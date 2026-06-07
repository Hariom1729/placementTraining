# Problem 9: Binary Tree Right Side View

## Problem Statement
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Approach: DFS / Reverse Preorder (Root -> Right -> Left)

While we can use Level Order Traversal (BFS) and just take the last element of each level, DFS is usually cleaner and takes less space.

We can use a recursive function `dfs(node, current_level, result_list)`.
1. We visit nodes in a specific order: Root, then **Right**, then **Left**.
2. Because we visit the right child first, the *first* node we encounter at any new level `L` is guaranteed to be the rightmost node of that level.
3. We add a node's value to our `result_list` ONLY IF `current_level == result_list.size()`.
4. Then we recursively call `dfs` for `node->right` with `level + 1`, followed by `node->left` with `level + 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    void dfs(TreeNode* root, int level, vector<int>& res) {
        if (root == NULL) return;
        
        // If this is the first time we are visiting this level, add it to result
        if (level == res.size()) {
            res.push_back(root->val);
        }
        
        // Traverse Right first, then Left
        dfs(root->right, level + 1, res);
        dfs(root->left, level + 1, res);
    }

public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root, 0, res);
        return res;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(4);

    Solution sol;
    vector<int> res = sol.rightSideView(root);
    
    cout << "Right Side View: ";
    for(int x : res) cout << x << " ";
    cout << endl;
    // Expected: 1 3 4

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We visit each node exactly once.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the tree height.
