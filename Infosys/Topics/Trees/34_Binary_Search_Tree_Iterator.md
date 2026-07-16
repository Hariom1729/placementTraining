# Binary Search Tree Iterator

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, LinkedIn

## Topic
Trees / BST

## Pattern
Stack / Iterative DFS

## Problem Statement
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):
- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

**Follow up:** Could you implement `next()` and `hasNext()` to run in average `O(1)` time and use `O(h)` memory, where `h` is the height of the tree?

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `0 <= Node.val <= 10^6`
- At most `10^5` calls will be made to `hasNext`, and `next`.

## Input / Output
- Design a class.

## Sample Test Cases

**Example 1:**
```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
```

## Edge Cases
- Skewed Trees.
- A tree with only one node.

## Intuition
The easiest way is to do a full Inorder traversal in the constructor, store it in an array, and just use an index pointer. But this takes $O(N)$ space. The follow-up demands $O(H)$ space.

To achieve $O(H)$ space, we must partially execute an iterative Inorder traversal.
In an iterative Inorder traversal, we go as far left as possible, pushing nodes onto a Stack. The stack size will never exceed $O(H)$.
When `next()` is called, the top of the stack is the smallest element! We pop it and return it. But before we return, if this popped node has a right child, we must explore it by going one step right, and then as far left as possible again (pushing those onto the stack).

## Brute Force Approach
**Explanation:** Constructor does full recursive inorder traversal and stores into a `vector<int>`. `next()` returns `vec[i++]`. `hasNext()` returns `i < vec.size()`.
**Time Complexity:** $O(N)$ for constructor, $O(1)$ for `next()`/`hasNext()`.
**Space Complexity:** $O(N)$ for the array.

## Optimal Approach (Custom Stack Iteration)
**Detailed explanation:**
1. Initialize a `stack<TreeNode*> st`.
2. Create a helper function `pushAll(TreeNode* node)` that pushes `node` and continuously moves to `node->left`, pushing all left children onto the stack until it hits `nullptr`.
3. **Constructor:** Call `pushAll(root)`. The stack now holds the path to the absolute smallest element.
4. **hasNext():** Simply return `!st.empty()`.
5. **next():**
   - Pop the top node from the stack (this is the current smallest). Let's call it `tmp`.
   - Before returning `tmp->val`, we must process its right subtree. Call `pushAll(tmp->right)`. This ensures the stack is primed for the *next* call to `next()`.
   - Return `tmp->val`.

**Time Complexity:**
- `hasNext()`: $O(1)$.
- `next()`: $O(1)$ on average. Although `pushAll` contains a while loop, every node is pushed and popped exactly once over the entire lifecycle of the iterator. Thus, $N$ operations over $N$ calls = $O(1)$ amortized time.
**Space Complexity:** $O(H)$ because the stack only ever holds the left-path of nodes, which is strictly bounded by the height of the tree.

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

#include <stack>
using namespace std;

class BSTIterator {
private:
    stack<TreeNode*> st;
    
    // Helper function to push all left children
    void pushAll(TreeNode* node) {
        while (node != nullptr) {
            st.push(node);
            node = node->left;
        }
    }
    
public:
    BSTIterator(TreeNode* root) {
        pushAll(root);
    }
    
    int next() {
        // The top of the stack is the next smallest element
        TreeNode* tmp = st.top();
        st.pop();
        
        // Before returning, if there is a right subtree, 
        // we must push all of its left children onto the stack.
        pushAll(tmp->right);
        
        return tmp->val;
    }
    
    bool hasNext() {
        return !st.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```

## Dry Run
Tree: `[7, 3, 15, null, null, 9, 20]`
- `Constructor(7)`:
  - `pushAll(7)` pushes 7, then goes left to 3 and pushes 3. Left is null. Stack: `[7, 3] (top is 3)`.
- `next()`:
  - `tmp = 3`. Pop stack. Stack: `[7]`.
  - `pushAll(3->right)`. `3->right` is null. Nothing pushed.
  - returns `3`.
- `next()`:
  - `tmp = 7`. Pop stack. Stack: `[]`.
  - `pushAll(7->right (15))`. Pushes 15. Goes left to 9, pushes 9. Stack: `[15, 9]`.
  - returns `7`.
- `hasNext()`:
  - Stack is not empty (`[15, 9]`). Returns `true`.

## Common Mistakes
- **Pushing right children incorrectly:** Some candidates try to push both left and right children into the stack. This completely breaks the Inorder flow. You ONLY push left children, and you only explore the right child exactly when you are popping its parent!

## Similar Problems
- Binary Tree Inorder Traversal
- Flatten 2D Vector
- Two Sum IV - Input is a BST (Uses a forward and backward iterator)
