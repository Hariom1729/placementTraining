# All Nodes Distance K in Binary Tree

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Microsoft

## Topic
Trees / Graphs

## Pattern
BFS / Parent Pointers (Tree to Graph)

## Problem Statement
Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.
You can return the answer in any order.

## Constraints
- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are unique.
- `target` is the value of one of the nodes in the tree.
- `0 <= k <= 1000`

## Input
- `root` pointer of the Binary Tree.
- `target` pointer to the target node.
- `k` integer distance.

## Output
- Return a 1D vector of integers.

## Sample Test Cases

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```

**Example 2:**
```
Input: root = [1], target = 1, k = 3
Output: []
```

## Edge Cases
- `k = 0`. Simply return `[target->val]`.
- Target is a leaf node, requiring us to only traverse upwards.
- Tree has fewer nodes than `k` depth. Return empty array.

## Intuition
In a standard Binary Tree, we can easily move *down* to children using `left` and `right` pointers. If we want nodes at distance `K` downwards, it's a simple DFS.
However, this problem requires finding nodes at distance `K` in ANY direction (including upwards through the parent, and then down the other branch).
To do this, we need to be able to move UP the tree.
If we convert the Tree into an undirected Graph by storing a map of **parent pointers**, we can easily traverse in all 3 directions: `Left`, `Right`, and `Up`!
Once we have the parent pointers, we start a standard BFS from the `target` node. We expand outwards radially level by level. After `k` levels of expansion, whatever nodes are currently in our BFS queue are exactly distance `k` away!

## Brute Force Approach
N/A - The Tree-to-Graph conversion is required to traverse upwards.

## Optimal Approach (BFS with Parent Map)
**Detailed explanation:**
1. **Build Parent Pointers:**
   - Create an `unordered_map<TreeNode*, TreeNode*> parentMap`.
   - Run a simple BFS or DFS starting from `root`. For every node, map its left child to it (`parentMap[node->left] = node`), and map its right child to it.
2. **Radial BFS from Target:**
   - Create a `queue<TreeNode*> q`. Push `target` into `q`.
   - Create an `unordered_set<TreeNode*> visited`. Insert `target` into `visited` (so we don't bounce back and forth between parent and child).
   - Maintain a `currentDistance = 0`.
3. **BFS Loop:**
   - While `!q.empty()`:
     - If `currentDistance == k`, we break the loop! The nodes currently inside the queue are exactly distance `k` away.
     - Get the current size of the queue `s`. Iterate `s` times (process level by level):
       - Pop `curr`.
       - If `curr->left` exists and is NOT in `visited`, push it to `q` and mark as visited.
       - If `curr->right` exists and is NOT in `visited`, push it to `q` and mark as visited.
       - If `curr` has a parent in `parentMap` and the parent is NOT in `visited`, push the parent to `q` and mark as visited.
     - Increment `currentDistance++`.
4. **Extract Result:**
   - Pop remaining elements from `q`, push their values into the answer vector, and return.

**Time Complexity:** $O(N)$ to build the parent map + $O(N)$ worst-case to do the BFS. Overall $O(N)$.
**Space Complexity:** $O(N)$ for the parent map, queue, and visited set.

## C++ Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
    void markParents(TreeNode* root, unordered_map<TreeNode*, TreeNode*>& parentMap) {
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            if (curr->left) {
                parentMap[curr->left] = curr;
                q.push(curr->left);
            }
            if (curr->right) {
                parentMap[curr->right] = curr;
                q.push(curr->right);
            }
        }
    }
    
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> ans;
        if (root == nullptr) return ans;
        
        // Map to store parent pointers
        unordered_map<TreeNode*, TreeNode*> parentMap;
        markParents(root, parentMap);
        
        // BFS to find all nodes at distance k
        queue<TreeNode*> q;
        unordered_set<TreeNode*> visited;
        
        q.push(target);
        visited.insert(target);
        int currentDistance = 0;
        
        while (!q.empty()) {
            if (currentDistance == k) {
                break; // Queue now contains nodes at distance K
            }
            
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* curr = q.front();
                q.pop();
                
                // Go Left
                if (curr->left != nullptr && visited.find(curr->left) == visited.end()) {
                    q.push(curr->left);
                    visited.insert(curr->left);
                }
                
                // Go Right
                if (curr->right != nullptr && visited.find(curr->right) == visited.end()) {
                    q.push(curr->right);
                    visited.insert(curr->right);
                }
                
                // Go Up (Parent)
                if (parentMap.find(curr) != parentMap.end() && visited.find(parentMap[curr]) == visited.end()) {
                    q.push(parentMap[curr]);
                    visited.insert(parentMap[curr]);
                }
            }
            currentDistance++;
        }
        
        // Extract the nodes remaining in the queue
        while (!q.empty()) {
            ans.push_back(q.front()->val);
            q.pop();
        }
        
        return ans;
    }
};
```

## Dry Run
Tree: `[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]`, Target `5`, k = `2`
- `markParents`: `map[5]=3, map[1]=3, map[6]=5, map[2]=5...`
- `q = [5]`. `dist = 0`.
- **Level 1 (dist=0):**
  - Pop 5. Push left(6), right(2), up(3).
  - `q = [6, 2, 3]`. `dist` becomes 1.
- **Level 2 (dist=1):**
  - Pop 6. Left/right null. Up(5) is visited.
  - Pop 2. Push left(7), right(4). Up(5) is visited.
  - Pop 3. Push right(1). Left(5) is visited. Up(null).
  - `q = [7, 4, 1]`. `dist` becomes 2.
- **Level 3 (dist=2):**
  - Loop condition `currentDistance == k` triggers! `2 == 2`. Break loop.
- Pop queue into answer. `ans = [7, 4, 1]`.

## Common Mistakes
- **Forgetting the `visited` set:** Since you are traversing an undirected graph, if you don't use a visited set, node A will push its parent B, and in the next step parent B will push node A, causing an infinite loop.
- **Processing queue elements one-by-one instead of level-by-level:** For BFS distance algorithms, you MUST process all nodes in the queue for the current depth before incrementing `currentDistance`. The `int size = q.size(); for(int i=0; i<size; i++)` loop is crucial.

## Similar Problems
- Amount of Time for Binary Tree to Be Infected
- Step-By-Step Directions From a Binary Tree Node to Another
