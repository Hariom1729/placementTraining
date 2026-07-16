# Step-By-Step Directions From a Binary Tree Node to Another

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft

## Topic
Trees

## Pattern
Lowest Common Ancestor / DFS String Building

## Problem Statement
You are given the `root` of a binary tree with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node, and a different integer `destValue` representing the value of the destination node.
Find the shortest path starting from node `startValue` to node `destValue`, and return the step-by-step directions of such path as a string.
- `'L'` means to go from a node to its left child node.
- `'R'` means to go from a node to its right child node.
- `'U'` means to go from a node to its parent node.

## Constraints
- The number of nodes in the tree is $n$.
- $2 \le n \le 10^5$
- $1 \le Node.val \le n$
- All the values in the tree are unique.
- $1 \le startValue, destValue \le n$
- $startValue \neq destValue$

## Input
- `root` pointer of the Binary Tree.
- `startValue` integer.
- `destValue` integer.

## Output
- Return a string of directions (e.g., `"UURL"`).

## Sample Test Cases

**Example 1:**
```
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
```

**Example 2:**
```
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
```

## Edge Cases
- Start node is an ancestor of the Destination node (Path only contains 'L' and 'R').
- Destination node is an ancestor of the Start node (Path only contains 'U').

## Intuition
The shortest path between ANY two nodes in a tree ALWAYS passes through their **Lowest Common Ancestor (LCA)**.
The path consists of two distinct parts:
1. Going UP from the `startValue` to the `LCA`. (This portion of the path will consist entirely of `'U'`s).
2. Going DOWN from the `LCA` to the `destValue`. (This portion will consist of `'L'`s and `'R'`s).

Instead of finding the LCA explicitly, which takes an extra tree traversal, we can do something much smarter:
1. Find the path string from the **Root** to `startValue`. (e.g., `"LLR"`)
2. Find the path string from the **Root** to `destValue`. (e.g., `"LLLL"`)
3. Notice that both paths might share a common prefix! The common prefix `"LL"` represents the path from the Root to their LCA.
4. We can safely delete the common prefix from both strings!
   - `startPath` becomes `"R"`.
   - `destPath` becomes `"LL"`.
5. Since we need to travel UP from the start node to the LCA, every character in `startPath` simply turns into a `'U'`. `"R" -> "U"`.
6. The `destPath` remains unchanged because it represents the downward path from the LCA.
7. We just concatenate them: `"U"` + `"LL"` = `"ULL"`. Done!

## Brute Force Approach
**Explanation:** Find the LCA using the standard LCA algorithm. Then run DFS from LCA to `startValue` (convert all path letters to 'U'), and run DFS from LCA to `destValue`. Concatenate.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Optimal Approach (Root Paths & Prefix Pruning)
**Detailed explanation:**
1. Create a helper boolean DFS function `findPath(TreeNode* node, int target, string& path)` that finds the path from the given node to a target value.
   - If `node->val == target`, return `true`.
   - Add 'L' to path. Recurse left. If it returns true, we found it. If false, pop the 'L' (backtrack).
   - Add 'R' to path. Recurse right. If true, we found it. If false, pop the 'R' (backtrack).
   - Return false if not found in either subtree.
2. Call `findPath(root, startValue, startPath)`.
3. Call `findPath(root, destValue, destPath)`.
4. Find the length of the common prefix between `startPath` and `destPath` by iterating with a pointer `i = 0` while `startPath[i] == destPath[i]`.
5. The remaining length of the start path is `startPath.length() - i`. These all become `'U'`. Create a string of `U`s of this length.
6. The remaining length of the dest path is `destPath.substr(i)`.
7. Return `string(startPath.length() - i, 'U') + destPath.substr(i)`.

**Time Complexity:** $O(N)$ to find the paths. String manipulations take $O(N)$. Overall $O(N)$.
**Space Complexity:** $O(N)$ for the recursion stack and path strings.

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

#include <string>
#include <algorithm>
using namespace std;

class Solution {
    bool findPath(TreeNode* node, int target, string& path) {
        if (node == nullptr) return false;
        
        if (node->val == target) return true;
        
        // Try Left
        path.push_back('L');
        if (findPath(node->left, target, path)) return true;
        path.pop_back(); // Backtrack
        
        // Try Right
        path.push_back('R');
        if (findPath(node->right, target, path)) return true;
        path.pop_back(); // Backtrack
        
        return false;
    }
    
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string startPath = "";
        string destPath = "";
        
        // Find paths from root to both nodes
        findPath(root, startValue, startPath);
        findPath(root, destValue, destPath);
        
        // Find the common prefix length
        int i = 0;
        int minLength = min(startPath.length(), destPath.length());
        while (i < minLength && startPath[i] == destPath[i]) {
            i++;
        }
        
        // Convert the remaining startPath characters to 'U'
        string uPath(startPath.length() - i, 'U');
        
        // Extract the remaining destPath characters
        string downPath = destPath.substr(i);
        
        // Combine them
        return uPath + downPath;
    }
};
```

## Dry Run
Tree: `[5, 1, 2, 3, null, 6, 4]`, Start `3`, Dest `6`
- `findPath(5, 3)` -> Root 5 goes left to 1, then left to 3. `startPath = "LL"`.
- `findPath(5, 6)` -> Root 5 goes right to 2, then left to 6. `destPath = "RL"`.
- `startPath = "LL"`, `destPath = "RL"`.
- Common prefix loop: `startPath[0] ('L') != destPath[0] ('R')`. The loop breaks instantly! `i = 0`.
- This means the LCA is the root itself (5).
- Convert `startPath` remainder length (2 - 0 = 2) to 'U's -> `"UU"`.
- Combine with `destPath` remainder (`"RL"`).
- Return `"UURL"`. Correct!

## Common Mistakes
- **Failing to backtrack in string building:** If you don't `path.pop_back()` when a recursive call returns `false`, your string will accumulate garbage paths (e.g., `"LRLRR"`) representing failed explorations, leading to completely wrong answers.
- **Using String Concatenation instead of push_back:** If you pass `path + "L"` by value to the recursive function, it avoids the need to backtrack, but it triggers massive memory allocations $O(N^2)$ causing Time Limit Exceeded (TLE) on strictly timed platforms. `push_back` and `pop_back` with references is highly optimized $O(1)$.

## Similar Problems
- Lowest Common Ancestor of a Binary Tree
- All Nodes Distance K in Binary Tree
