# Problem 12: Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

---

## Approach: BFS with a Toggle Flag

This is a variation of the standard Level Order Traversal.
1. We use a queue to perform standard BFS level by level.
2. We maintain a boolean flag `leftToRight` (initially `true`).
3. For each level, we find its size and create a temporary array `row` of that size.
4. If `leftToRight` is true, we insert nodes at index `i` (from `0` to `size - 1`).
5. If `leftToRight` is false, we insert nodes at index `size - 1 - i` (reverse order).
6. Push left and right children to the queue normally.
7. After processing the level, toggle `leftToRight = !leftToRight`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == NULL) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> row(size);
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                // Find position to fill node's value
                int index = (leftToRight) ? i : (size - 1 - i);
                row[index] = node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            // After this level
            leftToRight = !leftToRight;
            result.push_back(row);
        }
        
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution sol;
    vector<vector<int>> res = sol.zigzagLevelOrder(root);
    
    cout << "Zigzag Level Order: \n";
    for(auto level : res) {
        for(int x : level) cout << x << " ";
        cout << "\n";
    }
    // Expected:
    // 3
    // 20 9
    // 15 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We visit each node exactly once.
- **Space Complexity:** `O(N)` for the queue and storing the output.
