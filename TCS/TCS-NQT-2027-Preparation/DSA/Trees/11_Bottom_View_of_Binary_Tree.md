# Problem 11: Bottom View of Binary Tree

## Problem Statement
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

## Constraints
- `1 <= N <= 10^5`
- `1 <= Node Data <= 10^5`

---

## Approach: BFS (Level Order) with Vertical Distance

The logic is almost identical to the Top View problem.
The only difference is that instead of only recording the *first* node we encounter at a specific Horizontal Distance (HD), we continuously **overwrite** the value in our map every time we encounter a new node at that HD.
Since we use Level Order Traversal (BFS), the last node we process at any given HD will be the lowest node in the tree at that HD (i.e., the one visible from the bottom).

1. Use a `queue<pair<TreeNode*, int>> q` to store the node and its HD.
2. Use a `map<int, int> mpp` to store the latest node's value encountered for each HD.
3. Start with `q.push({root, 0})`.
4. While queue is not empty:
   - Pop `{node, hd}`.
   - Overwrite the map entry: `mpp[hd] = node->data`.
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
    vector<int> bottomView(Node *root) {
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
            
            // Always overwrite to get the bottom-most node
            mpp[hd] = node->data;
            
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
    root->left->right->left = new Node(8);
    root->left->right->right = new Node(9);

    Solution sol;
    vector<int> res = sol.bottomView(root);
    
    cout << "Bottom View: ";
    for(int x : res) cout << x << " ";
    cout << endl;
    // Expected: 4 8 6 9 7 
    // (Note: at HD=0, both 1, 5, 6 are there. 6 is the last one encountered in BFS)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N)` because of the `map` insertions.
- **Space Complexity:** `O(N)` for the queue and the map.
