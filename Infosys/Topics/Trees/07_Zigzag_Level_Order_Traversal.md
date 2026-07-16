# Binary Tree Zigzag Level Order Traversal

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees

## Pattern
Breadth First Search (BFS)

## Problem Statement
Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 2D array (vector of vectors) containing the zigzag traversal.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Example 2:**
```
Input: root = [1]
Output: [[1]]
```

**Example 3:**
```
Input: root = []
Output: []
```

## Edge Cases
- Empty tree.
- Tree with a single node.
- Skewed trees where switching direction might appear confusing but should follow the exact same level-based rules.

## Intuition
This is a direct extension of the standard Level Order Traversal (BFS). 
We can use a normal BFS to traverse level by level. The only difference is that on every *even* level (0-indexed), we append the values left-to-right. On every *odd* level, we append the values right-to-left.
We can achieve this by maintaining a boolean flag `leftToRight` that flips after every level is completed. 
Instead of modifying how we traverse or push children to the queue (which causes massive logical headaches), we just modify how we *insert* elements into the temporary level array.

## Brute Force Approach
N/A - Standard BFS with directional insertion is optimal.

## Optimal Approach
**Detailed explanation:**
1. If `root == nullptr`, return an empty result.
2. Initialize `queue<TreeNode*> q` and a boolean `leftToRight = true`.
3. Loop while the queue is not empty:
   - Get the `size` of the queue.
   - Create a vector `level(size)` of fixed size so we can index into it.
   - For `i = 0` to `size - 1`:
     - Pop `node` from the front of the queue.
     - If `leftToRight` is true, place the value at `level[i]` (left to right).
     - If `leftToRight` is false, place the value at `level[size - 1 - i]` (right to left).
     - Push the `left` and `right` children into the queue normally (order of pushing to queue NEVER changes).
   - Flip the flag: `leftToRight = !leftToRight`.
   - Add `level` to the final answer.

**Time Complexity:** $O(N)$ because every node is visited exactly once, and placing items in an array by index takes $O(1)$ time.
**Space Complexity:** $O(N)$ for the queue (at the lowest level it holds $N/2$ nodes).

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

#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        
        if (root == nullptr) {
            return ans;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int size = q.size();
            // Pre-allocate the vector with 'size' elements to allow index-based insertion
            vector<int> currentLevel(size);
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                // Determine the correct index to insert based on the zigzag direction
                int index = leftToRight ? i : (size - 1 - i);
                currentLevel[index] = node->val;
                
                // Push children to queue normally. NEVER change the queue pushing order!
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }
            
            // Flip the direction for the next level
            leftToRight = !leftToRight;
            ans.push_back(currentLevel);
        }
        
        return ans;
    }
};
```

## Dry Run
Tree: `[3, 9, 20, null, null, 15, 7]`
- Init: `q = [3]`, `leftToRight = true`
- **Level 1:**
  - `size = 1`. `currentLevel = [0]`.
  - `index = i = 0`. `currentLevel[0] = 3`.
  - Push 9, 20. `q = [9, 20]`.
  - `ans = [[3]]`. Flip flag `leftToRight = false`.
- **Level 2:**
  - `size = 2`. `currentLevel = [0, 0]`.
  - Loop 1 (pop 9): `index = 2 - 1 - 0 = 1`. `currentLevel[1] = 9`.
  - Loop 2 (pop 20): `index = 2 - 1 - 1 = 0`. `currentLevel[0] = 20`. Push 15, 7.
  - `ans = [[3], [20, 9]]`. Flip flag `leftToRight = true`.
- **Level 3:**
  - `size = 2`. `currentLevel = [0, 0]`.
  - Loop 1 (pop 15): `index = 0`. `currentLevel[0] = 15`.
  - Loop 2 (pop 7): `index = 1`. `currentLevel[1] = 7`.
  - `ans = [[3], [20, 9], [15, 7]]`.

## Common Mistakes
- **Trying to reverse the order of children pushed into the queue:** Some candidates try to push `right` then `left` depending on the level. This breaks down horribly because the nodes themselves will be popped in reverse order, requiring double-reversed logic. ALWAYS push children `left` then `right`. Handle the "reverse" only when storing the integers.
- **Using `vector::insert` or `std::reverse`:** While `std::reverse(level.begin(), level.end())` works, it takes an extra $O(K)$ time per level. The index-based insertion $O(1)$ shown in the optimal solution is much cleaner and faster.

## Similar Problems
- Binary Tree Level Order Traversal
- Binary Tree Right Side View
