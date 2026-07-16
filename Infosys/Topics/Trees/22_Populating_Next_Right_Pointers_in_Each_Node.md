# Populating Next Right Pointers in Each Node

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys DSE
Similar Companies: Microsoft, Amazon, Bloomberg

## Topic
Trees

## Pattern
Level Order Traversal / BFS

## Problem Statement
You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
Initially, all next pointers are set to `NULL`.

## Constraints
- The number of nodes in the tree is in the range `[0, 2^12 - 1]`.
- `-1000 <= Node.val <= 1000`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return the `root` pointer after modifying the tree.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree, your function should populate each next pointer to point to its next right node. The '#' signifies the end of each level.
```

**Example 2:**
```
Input: root = []
Output: []
```

## Edge Cases
- Empty tree.

## Intuition
**Standard BFS ($O(N)$ space):**
Since we need to connect nodes on the same level, we can use a standard Level Order Traversal with a Queue. For each level, we pop nodes one by one and set `node->next` to `queue.front()` (unless it's the last node of the level).

**Optimal Approach ($O(1)$ space):**
The problem asks if we can do this using constant extra space. Since the tree is perfectly balanced, we already have "next" pointers established at the parent level!
If we are at a `node`:
1. Its left child's next pointer should point to its right child: `node->left->next = node->right;`.
2. Its right child's next pointer should point to the left child of `node->next`: `if (node->next != nullptr) node->right->next = node->next->left;`.

We can traverse the tree level by level using the `next` pointers we just created, completely avoiding the need for a queue.

## Brute Force Approach (Queue)
**Explanation:** Standard BFS. Run a loop `for (int i = 0; i < size; i++)`. Pop the node. If `i < size - 1`, set `node->next = q.front()`. Push children.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Optimal Approach (O(1) Space)
**Detailed explanation:**
1. If `root == nullptr`, return `nullptr`.
2. Create a pointer `levelStart = root`. This keeps track of the leftmost node of the current level we are processing.
3. While `levelStart->left != nullptr` (i.e., we are not at the leaf level):
   - Create a traversal pointer `curr = levelStart`.
   - While `curr != nullptr` (traverse across the current level using `next` pointers):
     - Connect the left child to the right child: `curr->left->next = curr->right;`.
     - Connect the right child to the adjacent subtree's left child (if `curr->next` exists): 
       `if (curr->next != nullptr) curr->right->next = curr->next->left;`.
     - Move to the next node in the same level: `curr = curr->next;`.
   - Once we finish this level, move down to the next level: `levelStart = levelStart->left;`.
4. Return `root`.

**Time Complexity:** $O(N)$ as we visit every node exactly once.
**Space Complexity:** $O(1)$ constant extra space. (Note: The recursion stack of an implicit DFS approach would take $O(\log N)$ space, which technically isn't $O(1)$, so the iterative pointer approach is mathematically superior).

## C++ Solution

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // Start with the root node.
        Node* levelStart = root;
        
        // While there is a level below the current one to process.
        while (levelStart->left != nullptr) {
            
            // Traverse the current level to establish connections for the level BELOW.
            Node* curr = levelStart;
            
            while (curr != nullptr) {
                // Connection 1: Connect left child to right child
                curr->left->next = curr->right;
                
                // Connection 2: Connect right child to the next node's left child
                if (curr->next != nullptr) {
                    curr->right->next = curr->next->left;
                }
                
                // Move along the current level using the previously established 'next' pointers
                curr = curr->next;
            }
            
            // Move down to the next level
            levelStart = levelStart->left;
        }
        
        return root;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, 6, 7]`
- `levelStart = 1`. `curr = 1`.
  - `curr->left(2)->next = curr->right(3)`. (2 -> 3).
  - `curr->next` is null.
  - `curr = curr->next` (null). Loop ends.
- `levelStart = levelStart->left (2)`.
- `curr = 2`.
  - `curr->left(4)->next = curr->right(5)`. (4 -> 5).
  - `curr->next` is 3 (established above!).
  - `curr->right(5)->next = curr->next->left(6)`. (5 -> 6).
  - `curr = curr->next (3)`.
- `curr = 3`.
  - `curr->left(6)->next = curr->right(7)`. (6 -> 7).
  - `curr->next` is null.
  - `curr = null`. Loop ends.
- `levelStart = 4`. `4->left` is null. Outer loop ends.
Connections established: 2->3, 4->5, 5->6, 6->7. Perfect!

## Common Mistakes
- **Trying to connect `curr->right` without checking if `curr->next` exists:** `curr->next->left` will cause a segfault if `curr->next` is null (which is true for the rightmost node of every level).

## Similar Problems
- Populating Next Right Pointers in Each Node II (Tree is not perfectly balanced)
- Binary Tree Right Side View
