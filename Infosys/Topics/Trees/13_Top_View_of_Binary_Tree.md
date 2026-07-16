# Top View of Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Samsung, OLA

## Topic
Trees

## Pattern
Coordinate Traversal / BFS / Map

## Problem Statement
Given below is a binary tree. The task is to print the top view of binary tree. 
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Return the values of the nodes in the top view from left to right.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 1D array of integers representing the top view.

## Sample Test Cases

**Example 1:**
```
Input: 
       1
    /    \
   2      3
  / \    / \
 4   5  6   7
Output: [4, 2, 1, 3, 7]
```

**Example 2:**
```
Input:
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
Output: [2, 1, 3, 6]
```

## Edge Cases
- Skewed trees. A completely right-skewed tree will have all nodes in its top view.
- Overlapping nodes. If two nodes are at the same vertical column, the one that is HIGHER up in the tree (closer to root) obscures the lower one.

## Intuition
This problem is a simplified version of the Vertical Order Traversal.
We assign horizontal coordinates (x-coordinates) to each node. The root is at `x = 0`. Moving left means `x - 1`, moving right means `x + 1`.
Because we are looking from the **top**, we only care about the **first node we encounter** for any given `x` coordinate!
If we traverse the tree level by level (using BFS), we are guaranteed to process nodes from top to bottom. Therefore, the very first time we see an `x` coordinate, that node is the topmost node for that column. We record it in a map and ignore any future nodes with the same `x` coordinate.

## Brute Force Approach
N/A - The BFS map approach is standard.

## Optimal Approach
**Detailed explanation:**
1. If `root == nullptr`, return an empty vector.
2. We use a `map<int, int> mpp` where the key is the horizontal column `x`, and the value is the node's value. We use a `map` (not `unordered_map`) because it keeps the columns sorted from left to right automatically.
3. We use a `queue<pair<TreeNode*, int>> q`. The pair holds the node and its `x` coordinate.
4. Push `{root, 0}` into the queue.
5. While the queue is not empty:
   - Pop `(node, x)`.
   - **Crucial step:** Check if `x` is already a key in the map. If it is NOT, insert it: `mpp[x] = node->val`. Since BFS guarantees top-to-bottom order, the first node seen at `x` is the topmost.
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
    vector<int> topView(TreeNode *root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        
        // Map to store the first node found at each horizontal distance
        // map automatically sorts the keys in ascending order (left to right)
        map<int, int> mpp; 
        
        // Queue to perform BFS. Stores {node, horizontal_distance}
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto it = q.front();
            q.pop();
            
            TreeNode* node = it.first;
            int hd = it.second;
            
            // If the horizontal distance is seen for the first time,
            // add it to the map. (Since it's BFS, this is the topmost node)
            if (mpp.find(hd) == mpp.end()) {
                mpp[hd] = node->val;
            }
            
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
- Pop 1 (hd=0). `mpp[0]` doesn't exist. `mpp[0] = 1`.
  - Push 2 (hd=-1), push 3 (hd=1).
- Pop 2 (hd=-1). `mpp[-1]` doesn't exist. `mpp[-1] = 2`.
  - Push 4 (hd=-2), push 5 (hd=0).
- Pop 3 (hd=1). `mpp[1]` doesn't exist. `mpp[1] = 3`.
  - Push 6 (hd=0), push 7 (hd=2).
- Pop 4 (hd=-2). `mpp[-2] = 4`.
- Pop 5 (hd=0). `mpp[0]` ALREADY EXISTS (value is 1). Ignored! (1 obscures 5 from the top).
- Pop 6 (hd=0). `mpp[0]` ALREADY EXISTS. Ignored!
- Pop 7 (hd=2). `mpp[2] = 7`.
Result from map: `[-2: 4, -1: 2, 0: 1, 1: 3, 2: 7]`.
Returns `[4, 2, 1, 3, 7]`.

## Common Mistakes
- **Using DFS (Recursion) instead of BFS:** If you use DFS, you cannot simply say "the first node I see at this `x` is the topmost", because DFS dives deep immediately. You would have to also track the `y` coordinate (depth) and overwrite map values if a newly discovered node at the same `x` has a smaller `y`. Using BFS completely eliminates the need to track `y` because BFS naturally explores smaller `y` first.

## Similar Problems
- Bottom View of Binary Tree
- Vertical Order Traversal
- Binary Tree Right Side View
