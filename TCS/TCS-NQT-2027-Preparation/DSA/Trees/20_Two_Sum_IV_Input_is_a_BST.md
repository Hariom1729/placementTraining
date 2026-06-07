# Problem 20: Two Sum IV - Input is a BST

## Problem Statement
Given the `root` of a Binary Search Tree and a target number `k`, return `true` if there exist two elements in the BST such that their sum is equal to the given target.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- `root` is guaranteed to be a valid binary search tree.
- `-10^5 <= k <= 10^5`

---

## Approach: Inorder Traversal + Two Pointers

A BST's inorder traversal gives a sorted array. Once we have a sorted array, we can use the classic Two Pointers approach to find if two numbers sum to `k`.

1. Perform an inorder traversal and store the node values in a vector `nums`.
2. Initialize two pointers: `left = 0` and `right = nums.size() - 1`.
3. While `left < right`:
   - Calculate `sum = nums[left] + nums[right]`.
   - If `sum == k`, return `true`.
   - If `sum < k`, we need a larger sum, so move `left++`.
   - If `sum > k`, we need a smaller sum, so move `right--`.
4. If the loop ends without finding a pair, return `false`.

*(Note: There is an advanced `O(H)` space approach using a BST Iterator, but the `O(N)` space approach is much easier to implement and perfectly acceptable in most interviews).*

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
    void inorder(TreeNode* root, vector<int>& nums) {
        if (root == NULL) return;
        inorder(root->left, nums);
        nums.push_back(root->val);
        inorder(root->right, nums);
    }

public:
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        
        int left = 0;
        int right = nums.size() - 1;
        
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == k) {
                return true;
            } else if (sum < k) {
                left++;
            } else {
                right--;
            }
        }
        
        return false;
    }
};

int main() {
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->right->right = new TreeNode(7);

    Solution sol;
    cout << "Target 9: " << (sol.findTarget(root, 9) ? "True" : "False") << endl; // Expected: True (4+5 or 3+6 or 2+7)
    cout << "Target 28: " << (sol.findTarget(root, 28) ? "True" : "False") << endl; // Expected: False

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` for the inorder traversal + `O(N)` for the two-pointer search. Overall `O(N)`.
- **Space Complexity:** `O(N)` to store the elements in the vector `nums`.
