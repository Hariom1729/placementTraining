# Bottom View of Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Oyo, Paytm

## Topic
Trees

## Pattern
Coordinate Traversal / BFS / Map

## Problem Statement
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the bottom view.

## Sample Test Cases

**Example 1:**
```
Input: 
       1
    /    \
   2      3
  / \    / \
 4   5  6   7
Output: [4, 2, 6, 3, 7]
Explanation: For hd = 0, node 5 and 6 are at the same depth. The rule states to pick the later one in level traversal, which is 6.
```

**Example 2:**
```
Input:
        20
      /    \
    8       22
  /   \      \
 5      3      25
      /   \
    10    14
Output: [5, 10, 4, 14, 25]
```

## Edge Cases
- Skewed trees.
- Overlapping nodes at the exact same coordinate. Since BFS processes left-to-right, overwriting the map continuously guarantees the right-most node at the bottom level is kept.

## Intuition
This is the exact counterpart to the **Top View** problem.
In Top View, we only wanted the *first* node encountered at any horizontal distance `x`.
In Bottom View, we want the *last* node encountered at any horizontal distance `x` (because looking from the bottom, deeper nodes obscure shallower ones).
Using BFS, as we go level by level, we simply **overwrite** the map entry for `x` every time we encounter a node at `x`. By the time BFS finishes, the map will naturally hold the deepest nodes for every `x` column.

## Brute Force Approach
N/A - The BFS map approach is the standard optimal way.

## Optimal Approach
**Detailed explanation:**
1. If `root == nullptr`, return an empty vector.
2. We use a `map<int, int> mpp` where the key is the horizontal column `x`, and the value is the node's value.
3. We use a `queue<pair<TreeNode*, int>> q`. The pair holds the node and its `x` coordinate.
4. Push `{root, 0}` into the queue.
5. While the queue is not empty:
   - Pop `(node, x)`.
   - **Crucial step:** Unconditionally insert/overwrite the map: `mpp[x] = node->val`. Since BFS guarantees top-to-bottom, left-to-right order, overwriting ensures that the deepest (and right-most among ties) node remains in the map.
   - Push `node->left` with `x - 1` if it exists.
   - Push `node->right` with `x + 1` if it exists.
6. Iterate through the map and append the values to an answer vector.

**Time Complexity:** $O(N \log N)$ where $N$ is the number of nodes (due to map insertions).
**Space Complexity:** $O(N)$ to store the nodes in the queue and map.

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
#include <map>
using namespace std;

class Solution {
public:
    vector<int> bottomView(TreeNode *root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        
        // Map to store the last node found at each horizontal distance
        map<int, int> mpp; 
        
        // Queue to perform BFS. Stores {node, horizontal_distance}
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto it = q.front();
            q.pop();
            
            TreeNode* node = it.first;
            int hd = it.second;
            
            // Unconditionally overwrite the map.
            // This ensures the deepest node overwrites shallower ones.
            mpp[hd] = node->val;
            
            // Traverse left and right children
            if (node->left != nullptr) {
                q.push({node->left, hd - 1});
            }
            if (node->right != nullptr) {
                q.push({node->right, hd + 1});
            }
        }
        
        // Extract values from the map
        for (auto it : mpp) {
            ans.push_back(it.second);
        }
        
        return ans;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, 6, 7]`
- Queue: `{1, 0}`
- Pop 1 (hd=0). `mpp[0] = 1`.
  - Push 2 (hd=-1), push 3 (hd=1).
- Pop 2 (hd=-1). `mpp[-1] = 2`.
  - Push 4 (hd=-2), push 5 (hd=0).
- Pop 3 (hd=1). `mpp[1] = 3`.
  - Push 6 (hd=0), push 7 (hd=2).
- Pop 4 (hd=-2). `mpp[-2] = 4`.
- Pop 5 (hd=0). `mpp[0] = 5`. (Overwrites 1!)
- Pop 6 (hd=0). `mpp[0] = 6`. (Overwrites 5! Resolves the tie).
- Pop 7 (hd=2). `mpp[2] = 7`.
Result from map: `[-2: 4, -1: 2, 0: 6, 1: 3, 2: 7]`.
Returns `[4, 2, 6, 3, 7]`.

## Common Mistakes
- **Using DFS (Recursion):** Just like in Top View, using DFS for Bottom View is significantly harder because you have to explicitly track the depth (`y` coordinate). If you see a node at `x=0, y=2`, you only overwrite it if the new node is at `y >= 2`. BFS completely eliminates this logic.

## Similar Problems
- Top View of Binary Tree
- Vertical Order Traversal
