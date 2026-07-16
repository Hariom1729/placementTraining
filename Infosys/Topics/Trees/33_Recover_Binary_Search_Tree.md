# Recover Binary Search Tree

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Trees / BST

## Pattern
Inorder Traversal

## Problem Statement
You are given the `root` of a binary search tree (BST), where the values of **exactly two nodes** of the tree were swapped by mistake. Recover the tree without changing its structure.

## Constraints
- The number of nodes in the tree is in the range `[2, 1000]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Input
- `root` pointer of the Binary Search Tree.

## Output
- Modify the tree in-place. Do not return anything.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
```

**Example 2:**
```
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
```

## Edge Cases
- The swapped nodes are adjacent to each other in the Inorder traversal.
- The swapped nodes are far apart from each other in the Inorder traversal.

## Intuition
The core property of a BST is that its **Inorder Traversal is strictly increasing**.
If two nodes are swapped, the sorted order will be violated.
Let's look at an example array: `[1, 2, 3, 4, 5]`.
If we swap `2` and `5` (far apart), the array becomes: `[1, 5, 3, 4, 2]`.
Where are the violations?
1. `5 > 3` (First violation). The first swapped node is the **first element** (5).
2. `4 > 2` (Second violation). The second swapped node is the **second element** (2).

If we swap `2` and `3` (adjacent), the array becomes: `[1, 3, 2, 4, 5]`.
Where are the violations?
1. `3 > 2` (First and ONLY violation). The first swapped node is the **first element** (3), and the second swapped node is the **second element** (2).

**Strategy:**
We perform an Inorder traversal while keeping track of the `prev` node.
Whenever `prev->val > curr->val`, a violation has occurred!
- For the FIRST violation, we store `first = prev` and `middle = curr`. (In case they are adjacent, `middle` will be the answer).
- For the SECOND violation, we store `last = curr`.
After the traversal, if `last` is not null (they were far apart), we swap `first` and `last`.
If `last` is null (they were adjacent), we swap `first` and `middle`.

## Brute Force Approach
**Explanation:** Do a full Inorder traversal and store the nodes in an array. Sort the array's values. Do another Inorder traversal and overwrite every node's value with the sorted values.
**Time Complexity:** $O(N \log N)$ to sort.
**Space Complexity:** $O(N)$ for the array.

## Optimal Approach (Inorder Pointers)
**Detailed explanation:**
1. Initialize three pointers `first`, `middle`, and `last` to `nullptr`. Also maintain a `prev` pointer initialized to a dummy node with `LONG_MIN`.
2. Perform Inorder traversal `inorder(root)`.
3. In the processing step of the Inorder traversal:
   - Check if `prev != nullptr && prev->val > root->val`.
   - If it's the first time this happens (`first == nullptr`), assign `first = prev` and `middle = root`.
   - If it's the second time this happens (`first != nullptr`), assign `last = root`.
   - Update `prev = root`.
4. After traversal finishes, if `last != nullptr`, swap `first->val` and `last->val`.
5. Else (they were adjacent), swap `first->val` and `middle->val`.

**Time Complexity:** $O(N)$ because every node is visited exactly once.
**Space Complexity:** $O(H)$ for the recursive stack.

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

#include <algorithm>
using namespace std;

class Solution {
private:
    TreeNode* first;
    TreeNode* prev;
    TreeNode* middle;
    TreeNode* last;

    void inorder(TreeNode* root) {
        if (root == nullptr) return;

        // Go Left
        inorder(root->left);

        // Process Node
        if (prev != nullptr && root->val < prev->val) {
            // If this is the first violation
            if (first == nullptr) {
                first = prev;
                middle = root;
            } 
            // If this is the second violation
            else {
                last = root;
            }
        }
        
        // Mark this node as previous for the next iteration
        prev = root;

        // Go Right
        inorder(root->right);
    }

public:
    void recoverTree(TreeNode* root) {
        first = middle = last = nullptr;
        
        // Initialize prev to a dummy value (or just null and check for null)
        prev = new TreeNode(INT_MIN); // Note: using INT_MIN might fail if tree has INT_MIN. Best to use nullptr check.
        // Actually, just set prev = nullptr and handle in the traversal
        prev = nullptr;

        inorder(root);

        if (first && last) {
            swap(first->val, last->val); // Swapped nodes were not adjacent
        } else if (first && middle) {
            swap(first->val, middle->val); // Swapped nodes were adjacent
        }
    }
};
```

## Dry Run
Tree: `[3, 1, 4, null, null, 2]`
Inorder of this tree is: `1 -> 3 -> 2 -> 4`
- Node 1: `prev=null`. `prev=1`.
- Node 3: `3 > 1` (valid). `prev=3`.
- Node 2: `2 < 3` (VIOLATION 1).
  - `first` is null, so `first=3`, `middle=2`.
  - `prev=2`.
- Node 4: `4 > 2` (valid). `prev=4`.
Traversal ends.
`first=3`, `middle=2`, `last=null`.
We swap `first` and `middle` -> Swap 3 and 2.
Final inorder becomes `1 -> 2 -> 3 -> 4`, which is perfectly sorted!

## Common Mistakes
- **Failing to handle adjacent swaps:** Many people just look for the first element out of order and the last element out of order. If the elements are adjacent, there is only ONE point of violation, so `last` will remain null. You must track `middle` to handle this.
- **Using `INT_MIN` for `prev`:** LeetCode test cases include `INT_MIN`. If you initialize `prev = new TreeNode(INT_MIN)`, the comparison `root->val < prev->val` will fail if `root->val` is also `INT_MIN`. Initializing `prev = nullptr` is much safer.

## Similar Problems
- Validate Binary Search Tree
