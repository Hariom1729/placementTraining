# Vertical Order Traversal of a Binary Tree

## Difficulty
Hard

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Bloomberg

## Topic
Trees

## Pattern
Coordinate Traversal / BFS / Map

## Problem Statement
Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return a 2D array of integers representing the vertical order traversal.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
```

**Example 2:**
```
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: 4
Column -1: 2
Column 0: 1, 5, 6 (5 and 6 are at the same position (2, 0). 5 comes before 6 because 5 < 6).
Column 1: 3
Column 2: 7
```

## Edge Cases
- Nodes overlapping at the exact same `(row, col)` coordinate must be sorted by value!
- Completely unbalanced trees extending entirely to the left or right.

## Intuition
We need to assign a 2D coordinate `(x, y)` to every node, where `x` is the horizontal column and `y` is the vertical row.
When we move left, `x - 1`. When we move right, `x + 1`. When we move down, `y + 1`.
Because we need to output the columns from left to right, and rows from top to bottom, and sort by value if there's a tie, we need a data structure that automatically sorts its keys.
A `map` in C++ is perfectly suited for this. We can use a map of maps to multisets: `map<int, map<int, multiset<int>>> nodes`.
- The first key is `x` (column).
- The second key is `y` (row).
- The value is a `multiset` of node values (multiset because there can be duplicate values at the same exact coordinate, and they need to be sorted).

We can populate this structure using Level Order Traversal (BFS) to guarantee top-to-bottom processing visually, although DFS also works since the data structure sorts everything anyway.

## Brute Force Approach
N/A - The map approach is required to properly group and sort the coordinate data.

## Optimal Approach
**Detailed explanation:**
1. Create a `map<int, map<int, multiset<int>>> nodes;`
2. Perform a BFS using a `queue<pair<TreeNode*, pair<int, int>>> q;`
3. Push the root into the queue with coordinates `(0, 0)`.
4. While the queue is not empty:
   - Pop `(node, (x, y))`.
   - Insert the node's value into our map: `nodes[x][y].insert(node->val);`
   - If `node->left` exists, push it to queue with `(x - 1, y + 1)`.
   - If `node->right` exists, push it to queue with `(x + 1, y + 1)`.
5. After the BFS finishes, the `nodes` map is completely populated and perfectly sorted by `x` (columns), then by `y` (rows), and the multisets are sorted by value.
6. Iterate over the `nodes` map. For each column `x`, create a temporary vector. Iterate over its rows `y`, and push all elements from the multiset into the temporary vector. Add the vector to the final answer.

**Time Complexity:** $O(N \log N)$ where $N$ is the number of nodes. The `map` insertions and `multiset` insertions take logarithmic time.
**Space Complexity:** $O(N)$ to store the nodes in the map and the queue.

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
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;
        
        // Map structure: x -> (y -> sorted node values)
        map<int, map<int, multiset<int>>> nodes;
        
        // Queue stores: {node, {x, y}}
        queue<pair<TreeNode*, pair<int, int>>> q;
        q.push({root, {0, 0}});
        
        // Standard BFS
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            
            TreeNode* curr = p.first;
            int x = p.second.first;  // Column
            int y = p.second.second; // Row
            
            // Insert into our map
            nodes[x][y].insert(curr->val);
            
            if (curr->left != nullptr) {
                q.push({curr->left, {x - 1, y + 1}});
            }
            if (curr->right != nullptr) {
                q.push({curr->right, {x + 1, y + 1}});
            }
        }
        
        // Traverse the map to build the final answer
        for (auto p : nodes) {
            vector<int> col;
            for (auto q : p.second) {
                // Insert all elements from the multiset into the column vector
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            ans.push_back(col);
        }
        
        return ans;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, 6, 7]`
- Queue initialized with `{1, {0, 0}}`
- Pop 1. `nodes[0][0]` gets 1.
  - Push 2 `{ -1, 1 }`
  - Push 3 `{ 1, 1 }`
- Pop 2. `nodes[-1][1]` gets 2.
  - Push 4 `{ -2, 2 }`
  - Push 5 `{ 0, 2 }`
- Pop 3. `nodes[1][1]` gets 3.
  - Push 6 `{ 0, 2 }`
  - Push 7 `{ 2, 2 }`
- Pop 4. `nodes[-2][2]` gets 4.
- Pop 5. `nodes[0][2]` gets 5.
- Pop 6. `nodes[0][2]` gets 6. Note: `nodes[0][2]` is a multiset, so it automatically sorts {5, 6}.
- Pop 7. `nodes[2][2]` gets 7.
Build Answer:
- x = -2: `nodes[-2][2]` -> `[4]`
- x = -1: `nodes[-1][1]` -> `[2]`
- x = 0: `nodes[0][0]` -> 1, `nodes[0][2]` -> 5, 6 -> `[1, 5, 6]`
- x = 1: `nodes[1][1]` -> `[3]`
- x = 2: `nodes[2][2]` -> `[7]`
Result: `[[4], [2], [1, 5, 6], [3], [7]]`

## Common Mistakes
- **Forgetting that nodes at the exact same (row, col) must be sorted by value:** If you use a `vector` instead of a `multiset` in your map, and you encounter two nodes at `(0, 2)` like 6 and 5, your vector will keep them as `[6, 5]`, which will cause a test failure. The multiset automatically sorts them to `[5, 6]`.

## Similar Problems
- Binary Tree Level Order Traversal
- Top View of Binary Tree
- Bottom View of Binary Tree
