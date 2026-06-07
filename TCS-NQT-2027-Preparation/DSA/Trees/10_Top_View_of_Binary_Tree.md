# Problem 10: Top View of Binary Tree

## Problem Statement
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

## Constraints
- `1 <= N <= 10^5`
- `1 <= Node Data <= 10^5`

---

## Approach: BFS (Level Order) with Vertical Distance

To solve problems related to vertical lines (Top View, Bottom View, Vertical Order Traversal), we assign a "Horizontal Distance" (HD) to each node.
- The root has `HD = 0`.
- The left child has `HD = parent's HD - 1`.
- The right child has `HD = parent's HD + 1`.

The Top View is simply the **first node** we encounter for each unique HD. We *must* use BFS (Level Order) instead of DFS to ensure we record the highest node at each HD.

1. Use a `queue<pair<TreeNode*, int>> q` to store the node and its HD.
2. Use a `map<int, int> mpp` to store the first node's value encountered for each HD. A `map` automatically sorts the keys (HDs) from smallest (leftmost) to largest (rightmost).
3. Start with `q.push({root, 0})`.
4. While queue is not empty:
   - Pop `{node, hd}`.
   - If `hd` is not present in `mpp`, insert it: `mpp[hd] = node->val`.
   - Push left child with `hd - 1`.
   - Push right child with `hd + 1`.
5. Iterate over the `map` and collect the values.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int x) : data(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> topView(Node *root) {
        vector<int> ans;
        if (root == NULL) return ans;
        
        map<int, int> mpp; // map<Horizontal Distance, Node Value>
        queue<pair<Node*, int>> q; // queue<Node, Horizontal Distance>
        
        q.push({root, 0});
        
        while (!q.empty()) {
            auto it = q.front();
            q.pop();
            
            Node* node = it.first;
            int hd = it.second;
            
            // If this horizontal distance is seen for the first time, add it to map
            if (mpp.find(hd) == mpp.end()) {
                mpp[hd] = node->data;
            }
            
            if (node->left != NULL) {
                q.push({node->left, hd - 1});
            }
            if (node->right != NULL) {
                q.push({node->right, hd + 1});
            }
        }
        
        for (auto it : mpp) {
            ans.push_back(it.second);
        }
        
        return ans;
    }
};

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    Solution sol;
    vector<int> res = sol.topView(root);
    
    cout << "Top View: ";
    for(int x : res) cout << x << " ";
    cout << endl;
    // Expected: 4 2 1 3 7

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N)` because inserting into a `map` takes `O(\log N)` time. If we use an `unordered_map` and maintain min/max HD, we can achieve `O(N)`. However, `map` is standard and `N` is usually small enough.
- **Space Complexity:** `O(N)` for the queue and the map.
