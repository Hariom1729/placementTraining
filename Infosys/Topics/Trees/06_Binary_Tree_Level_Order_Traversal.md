# Binary Tree Level Order Traversal

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google

## Topic
Trees

## Pattern
Breadth First Search (BFS)

## Problem Statement
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 2D array (vector of vectors) containing the values at each level.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
- An empty tree (`nullptr`). Should return an empty 2D array `[]`.
- An asymmetric tree where some levels have missing nodes. The output should gracefully handle nulls without adding them to the array.

## Intuition
To traverse a tree level by level, we use Breadth-First Search (BFS).
BFS is perfectly suited for queues because a queue operates on a First-In-First-Out (FIFO) principle.
If we push the root into the queue, we can process it, and then push its children. Because of FIFO, all children of level 1 will be processed before any children of level 2.
To separate the nodes into distinct lists representing each level, we must record the `size` of the queue *before* we start popping nodes for the current level.

## Brute Force Approach
N/A - BFS is the standard and optimal way to accomplish this. (A DFS approach keeping track of depth is also possible but conceptually less direct for level order).

## Optimal Approach
**Detailed explanation:**
1. Handle the base case: if `root == nullptr`, return an empty result.
2. Initialize a queue `q` and push the `root`.
3. Initialize a 2D vector `ans`.
4. Run a loop `while (!q.empty())`:
   - Get the current number of nodes at this level: `int size = q.size()`.
   - Create a 1D vector `level` to hold the values for the current level.
   - Run a `for` loop exactly `size` times.
     - Inside the loop, pop the front node.
     - Add its value to `level`.
     - If its `left` child exists, push it into the queue.
     - If its `right` child exists, push it into the queue.
   - After the `for` loop finishes, the entire level has been processed. Add the `level` vector to `ans`.
5. Return `ans`.

**Time Complexity:** $O(N)$ where $N$ is the number of nodes. Every node is enqueued and dequeued exactly once.
**Space Complexity:** $O(N)$. In the worst case (a perfectly balanced tree), the lowest level will hold $N/2$ nodes. Thus, the maximum queue size is $O(N)$.

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        
        // Base case
        if (root == nullptr) {
            return ans;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            // Get the number of nodes at the current level
            int size = q.size();
            vector<int> currentLevel;
            
            // Process all nodes at this level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                currentLevel.push_back(node->val);
                
                // Add children to the queue for the NEXT level
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }
            
            // Add the processed level to the final answer
            ans.push_back(currentLevel);
        }
        
        return ans;
    }
};
```

## Dry Run
Tree: `[3, 9, 20, null, null, 15, 7]`
- Initial: `q = [3]`, `ans = []`
- **Level 1:**
  - `size = 1`. `currentLevel = []`.
  - Loop 1 time:
    - pop 3. `currentLevel = [3]`.
    - push 9, push 20. `q = [9, 20]`.
  - `ans = [[3]]`
- **Level 2:**
  - `size = 2`. `currentLevel = []`.
  - Loop 2 times:
    - pop 9. `currentLevel = [9]`. (left/right are null)
    - pop 20. `currentLevel = [9, 20]`.
    - push 15, push 7. `q = [15, 7]`.
  - `ans = [[3], [9, 20]]`
- **Level 3:**
  - `size = 2`. `currentLevel = []`.
  - Loop 2 times:
    - pop 15. `currentLevel = [15]`.
    - pop 7. `currentLevel = [15, 7]`.
  - `ans = [[3], [9, 20], [15, 7]]`
- Queue is empty. Return `ans`.

## Common Mistakes
- **Not capturing queue size BEFORE the loop:** If you use `for (int i = 0; i < q.size(); i++)`, the loop will run infinitely (or incorrectly) because you are adding children to the queue *inside* the loop, which changes `q.size()` dynamically! You MUST snapshot the size in a separate variable: `int size = q.size();`.

## Similar Problems
- Zigzag Level Order Traversal
- Binary Tree Right Side View
- Average of Levels in Binary Tree

## Infosys Variations
- Sometimes asked as a precursor to harder problems like "Left View" or "Right View" where you just take the first or last element of `currentLevel`.
