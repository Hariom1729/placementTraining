# Problem 2: Level Order Traversal

## Problem Statement
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

## Approach: BFS with Queue

Level order traversal is synonymous with Breadth-First Search (BFS). We use a queue to keep track of nodes at the current level.

1. If the root is `NULL`, return an empty list.
2. Initialize a `queue<TreeNode*> q` and push the `root` into it.
3. While the queue is not empty:
   - Determine the number of nodes at the current level (`size = q.size()`).
   - Create a temporary list to store the values of the current level.
   - Run a loop `size` times:
     - Pop the node from the front of the queue.
     - Add its value to the temporary list.
     - If it has a left child, push it to the queue.
     - If it has a right child, push it to the queue.
   - Add the temporary list to the final result.
4. Return the final result.

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == NULL) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int size = q.size(); // Number of nodes at the current level
            vector<int> currentLevel;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                currentLevel.push_back(node->val);
                
                if (node->left != NULL) q.push(node->left);
                if (node->right != NULL) q.push(node->right);
            }
            
            result.push_back(currentLevel);
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
    vector<vector<int>> res = sol.levelOrder(root);

    cout << "Level Order: \n";
    for(auto level : res) {
        for(int x : level) {
            cout << x << " ";
        }
        cout << "\n";
    }
    // Expected:
    // 3
    // 9 20
    // 15 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. Each node is pushed and popped from the queue exactly once.
- **Space Complexity:** `O(N)` to store the nodes in the queue (at most `N/2` nodes in the last level) and the output array.
