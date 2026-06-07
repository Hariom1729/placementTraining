# Problem 6: Same Tree

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Constraints
- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

---

## Approach: Recursive DFS

We can solve this by traversing both trees simultaneously.
- **Base Cases:**
  1. If both `p` and `q` are `NULL`, they are identical (return `true`).
  2. If only one of them is `NULL` (and the other is not), they are not identical (return `false`).
  3. If `p->val != q->val`, they are not identical (return `false`).
- **Recursive Step:** If the current nodes match, recursively check if their left subtrees are identical AND their right subtrees are identical.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // If both are NULL, they are identical
        if (p == NULL && q == NULL) {
            return true;
        }
        
        // If only one is NULL, they are not identical
        if (p == NULL || q == NULL) {
            return false;
        }
        
        // If values do not match, they are not identical
        if (p->val != q->val) {
            return false;
        }
        
        // Check left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

int main() {
    TreeNode* p = new TreeNode(1);
    p->left = new TreeNode(2);
    p->right = new TreeNode(3);

    TreeNode* q = new TreeNode(1);
    q->left = new TreeNode(2);
    q->right = new TreeNode(3);

    Solution sol;
    cout << "Are the trees same? " << (sol.isSameTree(p, q) ? "Yes" : "No") << endl; 
    // Expected: Yes

    q->right->val = 4;
    cout << "Are the trees same after modification? " << (sol.isSameTree(p, q) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the minimum number of nodes in both trees. We visit nodes until a mismatch is found or all nodes are visited.
- **Space Complexity:** `O(H)` for the recursive call stack, where `H` is the height of the smaller tree.
