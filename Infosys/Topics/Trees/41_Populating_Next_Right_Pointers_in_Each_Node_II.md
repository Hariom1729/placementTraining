# Populating Next Right Pointers in Each Node II

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Bloomberg

## Topic
Trees

## Pattern
Level Order Traversal / Linked List

## Problem Statement
Given a binary tree:
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
Unlike the previous version of this problem, **the given tree could be any binary tree (it is NOT perfectly balanced)**.

**Follow-up:** You may only use constant extra space.

## Constraints
- The number of nodes in the tree is in the range `[0, 6000]`.
- `-100 <= Node.val <= 100`

## Input
- `root` pointer of the Binary Tree.

## Output
- Return the `root` pointer after modifying the tree.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
```

**Example 2:**
```
Input: root = []
Output: []
```

## Edge Cases
- Skewed trees.
- Missing intermediate children (e.g., node 2 has a left child, but node 3 only has a right child).

## Intuition
If we use a Queue for Level Order Traversal, the solution is identical to Part 1 and very trivial, but it takes $O(N)$ space.
To achieve **$O(1)$ space**, we must use the `next` pointers we've already established in the *parent* level to traverse horizontally and hook up the *children* level.

Because the tree isn't perfectly balanced, a node might not have a left child, or a right child, or both!
To gracefully handle the gaps, we can treat the children level as a **singly linked list** that we are actively building.
For every level, we create a `dummyHead` node. We also maintain a `tail` pointer (initially pointing to `dummyHead`) that always points to the last hooked-up child in the current level.
As we traverse the parent level horizontally using `curr = curr->next`:
- If `curr->left` exists, we hook it up to our linked list: `tail->next = curr->left; tail = tail->next;`
- If `curr->right` exists, we hook it up: `tail->next = curr->right; tail = tail->next;`
When we finish traversing the parent level, the `dummyHead->next` will automatically point to the very first node of the newly formed children level! We just move our parent pointer down to `dummyHead->next` and repeat.

## Brute Force Approach (Queue)
**Explanation:** Standard BFS Level Order Traversal using a Queue. Connect popped nodes on the same level.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Optimal Approach (Dummy Node Level Linked List)
**Detailed explanation:**
1. If `root == nullptr`, return `nullptr`.
2. Use a pointer `curr = root` to track our traversal on the parent level.
3. While `curr != nullptr` (while there are still levels to process):
   - Create a `dummy` node for the *next* level: `Node dummy(0);`
   - Create a `tail` pointer: `Node* tail = &dummy;`
   - **Horizontal Traversal:** While `curr != nullptr`:
     - If `curr->left != nullptr`, link it: `tail->next = curr->left; tail = tail->next;`
     - If `curr->right != nullptr`, link it: `tail->next = curr->right; tail = tail->next;`
     - Move to the next parent: `curr = curr->next;`
   - **Move Down:** The current level is fully processed. The next level starts at `dummy.next`. So, `curr = dummy.next`.
4. Return `root`.

**Time Complexity:** $O(N)$ because we visit every node exactly once.
**Space Complexity:** $O(1)$ constant extra space.

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
        
        Node* curr = root; // Start at the root level
        
        while (curr != nullptr) {
            // Dummy node to serve as the anchor for the NEXT level
            Node dummy(0);
            Node* tail = &dummy;
            
            // Traverse the CURRENT level
            while (curr != nullptr) {
                if (curr->left != nullptr) {
                    tail->next = curr->left;
                    tail = tail->next; // Move tail forward
                }
                if (curr->right != nullptr) {
                    tail->next = curr->right;
                    tail = tail->next;
                }
                
                // Move horizontally to the next node in the current level
                curr = curr->next;
            }
            
            // Move DOWN to the next level. 
            // dummy.next points to the first node of the children level we just connected.
            curr = dummy.next;
        }
        
        return root;
    }
};
```

## Dry Run
Tree: `[1, 2, 3, 4, 5, null, 7]`
- **Level 1 (curr = 1):**
  - `dummy` created. `tail = &dummy`.
  - `1->left (2)` exists. `tail->next = 2`. `tail = 2`.
  - `1->right (3)` exists. `tail->next = 3`. `tail = 3`.
  - `curr = curr->next (null)`. Horizontal loop ends.
  - Level connected: `dummy -> 2 -> 3`.
  - `curr = dummy.next (2)`. (Moves down to level 2).
- **Level 2 (curr = 2):**
  - `dummy` created. `tail = &dummy`.
  - `2->left (4)` exists. `tail->next = 4`. `tail = 4`.
  - `2->right (5)` exists. `tail->next = 5`. `tail = 5`.
  - `curr = curr->next (3)`.
  - `curr = 3`.
  - `3->left` is null.
  - `3->right (7)` exists. `tail->next = 7`. `tail = 7`.
  - `curr = curr->next (null)`. Horizontal loop ends.
  - Level connected: `dummy -> 4 -> 5 -> 7`.
  - `curr = dummy.next (4)`. (Moves down to level 3).
- **Level 3 (curr = 4):**
  - All children are null. `dummy.next` remains null.
  - `curr = null`. Outer loop ends.
Result: Correctly populated!

## Common Mistakes
- **Trying to use `curr->left->next = curr->right` logic from Part 1:** That logic fails instantly if `curr->left` doesn't exist but `curr->right` does, because you try to dereference a null pointer. Furthermore, finding the "next" node for the right child requires a complicated while loop to scan across `curr->next` until you find a node with children. The dummy node approach is vastly simpler.

## Similar Problems
- Populating Next Right Pointers in Each Node
- Binary Tree Level Order Traversal
