# Two Sum IV - Input is a BST

## Difficulty
Easy / Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Trees / BST / Two Pointers

## Pattern
Inorder Traversal / Hashing / BST Iterator

## Problem Statement
Given the `root` of a Binary Search Tree and a target number `k`, return `true` if there exist two elements in the BST such that their sum is equal to the given target.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- `root` is guaranteed to be a valid binary search tree.
- `-10^5 <= k <= 10^5`

## Input
- `root` pointer of the Binary Search Tree.
- `k` target integer.

## Output
- Return a boolean.

## Sample Test Cases

**Example 1:**
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Explanation: 5 + 4 = 9, or 3 + 6 = 9.
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

## Edge Cases
- Tree has only one node (impossible to find TWO elements).
- Target sum requires the same node twice (not allowed, values must come from two distinct nodes).

## Intuition
We know two things:
1. Two Sum is usually solved using a Hash Set or Two Pointers on a sorted array.
2. The Inorder traversal of a BST gives us a perfectly sorted array!

**Approach 1 (Hashing during Traversal):**
Traverse the tree (any order works). Keep a Hash Set of visited values. For every node, check if `k - node->val` exists in the set. If it does, return `true`. This takes $O(N)$ time and $O(N)$ space.

**Approach 2 (Inorder + Two Pointers):**
Do an Inorder traversal to extract all elements into a sorted array. Then use the classic Two Pointer approach (`left = 0`, `right = n - 1`) on the array.
- If `arr[L] + arr[R] == k`, return `true`.
- If sum < k, `L++`.
- If sum > k, `R--`.
This also takes $O(N)$ time and $O(N)$ space, but is generally preferred by interviewers because it leverages the BST property (the first approach works on ANY binary tree and ignores the BST structure).

**Approach 3 (BST Iterator Two Pointers - Ultimate Optimal):**
Instead of storing the whole array, what if we just use two BST Iterators? One iterator goes forward (Left -> Root -> Right) giving us the smallest elements, and one goes backward (Right -> Root -> Left) giving us the largest elements. This simulates the Two Pointers without needing an $O(N)$ array! The space complexity drops to $O(H)$, which is $O(\log N)$ on average.

## Brute Force Approach
N/A - Converting to array is standard and efficient enough for most interviews.

## Optimal Approach (Inorder + Array)
**Detailed explanation:**
1. Create a `vector<int> nums`.
2. Perform standard recursive inorder traversal, pushing every node's value into `nums`.
3. Initialize `left = 0` and `right = nums.size() - 1`.
4. While `left < right`:
   - `int sum = nums[left] + nums[right];`
   - If `sum == k`, return `true`.
   - If `sum < k`, increment `left`.
   - If `sum > k`, decrement `right`.
5. Return `false`.

**Time Complexity:** $O(N)$ to traverse the tree and $O(N)$ to process the array. Total $O(N)$.
**Space Complexity:** $O(N)$ for the array.

## C++ Solution (Inorder + Array)

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

#include <vector>
using namespace std;

class Solution {
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
    
private:
    void inorder(TreeNode* node, vector<int>& nums) {
        if (node == nullptr) return;
        inorder(node->left, nums);
        nums.push_back(node->val);
        inorder(node->right, nums);
    }
};
```

## Advanced Optimal Approach (BST Iterators - O(H) Space)
```cpp
class BSTIterator {
    stack<TreeNode*> st;
    bool reverse; // true for backward iterator, false for forward
    
    void pushAll(TreeNode* node) {
        while (node != nullptr) {
            st.push(node);
            if (reverse) {
                node = node->right;
            } else {
                node = node->left;
            }
        }
    }
    
public:
    BSTIterator(TreeNode* root, bool isReverse) {
        reverse = isReverse;
        pushAll(root);
    }
    
    int next() {
        TreeNode* tmp = st.top();
        st.pop();
        if (reverse) {
            pushAll(tmp->left);
        } else {
            pushAll(tmp->right);
        }
        return tmp->val;
    }
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        
        BSTIterator l(root, false); // Forward iterator
        BSTIterator r(root, true);  // Backward iterator
        
        int i = l.next();
        int j = r.next();
        
        while (i < j) {
            if (i + j == k) return true;
            else if (i + j < k) i = l.next();
            else j = r.next();
        }
        return false;
    }
};
```

## Dry Run (Inorder + Array)
Tree: `[5, 3, 6, 2, 4, null, 7]`, `k = 9`
- `inorder` produces: `[2, 3, 4, 5, 6, 7]`
- `L = 0` (val 2), `R = 5` (val 7). `sum = 9`. `9 == 9`, returns `true`.

## Common Mistakes
- **Checking `k / 2` in the hashset method:** If you use a hashset, you must ensure you don't use the same node twice (e.g., tree has one node `3`, target is `6`. `6 - 3 = 3`, which is in the set, but it's the SAME node). The array/iterator two-pointer method mathematically prevents this because `left < right`.

## Similar Problems
- Two Sum
- Two Sum II - Input Array Is Sorted
- Binary Search Tree Iterator
