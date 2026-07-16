# Kth Smallest Element in a BST

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Uber, Oracle

## Topic
Trees / BST

## Pattern
Inorder Traversal

## Problem Statement
Given the `root` of a binary search tree, and an integer `k`, return the $k^{th}$ smallest value (1-indexed) of all the values of the nodes in the tree.

## Constraints
- The number of nodes in the tree is $N$, where $1 \le k \le N \le 10^4$.
- $0 \le Node.val \le 10^4$

## Input
- `root` pointer of the Binary Search Tree.
- `k` integer representing the position to find.

## Output
- Return the integer value of the $k^{th}$ smallest node.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Edge Cases
- $k = 1$ (Find the minimum element).
- $k = N$ (Find the maximum element).

## Intuition
The most important property of a Binary Search Tree is that an **Inorder Traversal (Left -> Root -> Right)** visits the nodes in strictly **ascending order**.
Therefore, if we perform an inorder traversal, the $1^{st}$ node we process is the $1^{st}$ smallest, the $2^{nd}$ node is the $2^{nd}$ smallest, and so on.
We can simply maintain a counter. Every time we process a node (after returning from the left child), we decrement `k`. When `k` hits 0, the current node is our answer! We can immediately stop the traversal.

## Brute Force Approach
**Explanation:** Perform a full Inorder traversal and store all node values in an array `vector<int> arr`. Since the array will be sorted naturally, just return `arr[k-1]`.
**Time Complexity:** $O(N)$ since we visit every node.
**Space Complexity:** $O(N)$ for the array and recursion stack.

## Optimal Approach (Early Stopping DFS)
**Detailed explanation:**
1. Create a global or reference variable for `ans` and pass `k` by reference.
2. Define a recursive function `inorder(TreeNode* root, int& k, int& ans)`.
3. **Base Case:** If `root == nullptr`, return.
4. **Recursive Step:**
   - Traverse left: `inorder(root->left, k, ans)`.
   - **Process Node:** Decrement `k`. If `k == 0`, store `ans = root->val` and return immediately.
   - Traverse right: If `k > 0`, `inorder(root->right, k, ans)`.
5. Returning early when `k == 0` prevents us from traversing the rest of the tree once we find the answer.

**Time Complexity:** $O(H + k)$ where $H$ is the height of the tree. We first go down to the leftmost node $O(H)$, and then we process $k$ nodes. This is strictly better than $O(N)$ if $k \ll N$.
**Space Complexity:** $O(H)$ for the recursion stack.

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
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int ans = -1;
        inorder(root, k, ans);
        return ans;
    }
    
private:
    void inorder(TreeNode* root, int& k, int& ans) {
        if (root == nullptr) return;
        
        // Traverse Left
        inorder(root->left, k, ans);
        
        // Process Current Node
        k--;
        if (k == 0) {
            ans = root->val;
            return; // We found the answer, start unwinding the stack
        }
        
        // Traverse Right (only if we haven't found the answer yet)
        if (k > 0) {
            inorder(root->right, k, ans);
        }
    }
};
```

## Morris Traversal ($O(1)$ Space approach)
If the interviewer demands $O(1)$ auxiliary space, use Morris Inorder Traversal.
```cpp
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int ans = -1;
        TreeNode* curr = root;
        
        while (curr != nullptr) {
            if (curr->left == nullptr) {
                // Process Node
                k--;
                if (k == 0) ans = curr->val;
                curr = curr->right;
            } else {
                TreeNode* prev = curr->left;
                while (prev->right != nullptr && prev->right != curr) {
                    prev = prev->right;
                }
                
                if (prev->right == nullptr) {
                    prev->right = curr; // Create thread
                    curr = curr->left;
                } else {
                    prev->right = nullptr; // Cut thread
                    // Process Node
                    k--;
                    if (k == 0) ans = curr->val;
                    curr = curr->right;
                }
            }
        }
        return ans;
    }
};
```

## Dry Run
Tree: `[5, 3, 6, 2, 4, null, null, 1]`, `k = 3`
- `inorder(5)`
  - `inorder(3)`
    - `inorder(2)`
      - `inorder(1)`
        - left null.
        - process 1: `k` becomes 2.
        - right null.
      - process 2: `k` becomes 1.
      - right null.
    - process 3: `k` becomes 0! `ans = 3`. Return immediately.
- Result: 3.

## Common Mistakes
- **Sorting the tree manually:** Some students put the nodes in a priority queue or vector and call `sort()`. This is highly inefficient $O(N \log N)$ and completely ignores the inherent sorted nature of a BST.
- **Not stopping early:** If you don't wrap the right traversal in an `if (k > 0)` condition, your code will visit every single node in the tree even if $k=1$.

## Similar Problems
- Kth Largest Element in an Array
- Validate Binary Search Tree
