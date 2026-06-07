# Problem 17: Copy List with Random Pointer

## Problem Statement
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list.

## Input Format
- The `head` of a linked list with random pointers.

## Output Format
- The `head` of the deep copied linked list.

## Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

---

## Approach: Interweaving Nodes (O(1) Space)

The naïve approach uses a Hash Map mapping `OldNode -> NewNode`, taking `O(N)` space. We can do it in `O(1)` extra space by interweaving the original and copied lists.

1. **Insert Copies:** Traverse the original list. For each node `curr`, create a `new_node` with the same value. Insert `new_node` directly *after* `curr`.
   - Original: `A -> B -> C`
   - Becomes: `A -> A' -> B -> B' -> C -> C'`
2. **Assign Random Pointers:** Traverse the interweaved list. If `curr->random` exists, then `curr->next->random` (which is `A' -> random`) should point to `curr->random->next` (which is `A's random's copy`).
3. **Separate Lists:** Traverse the list again to restore the original list and extract the copied list.
   - `copyHead = head->next`.
   - `curr->next = curr->next->next`.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        
        // Step 1: Interweave nodes
        Node* curr = head;
        while (curr != NULL) {
            Node* newNode = new Node(curr->val);
            newNode->next = curr->next;
            curr->next = newNode;
            curr = newNode->next;
        }
        
        // Step 2: Assign random pointers to the copies
        curr = head;
        while (curr != NULL) {
            if (curr->random != NULL) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }
        
        // Step 3: Separate the lists
        curr = head;
        Node* copyHead = head->next;
        Node* copyCurr = copyHead;
        
        while (curr != NULL) {
            curr->next = curr->next->next;
            if (copyCurr->next != NULL) {
                copyCurr->next = copyCurr->next->next;
            }
            
            curr = curr->next;
            copyCurr = copyCurr->next;
        }
        
        return copyHead;
    }
};

// Main function omitted due to the complexity of building a random pointer list manually,
// but the algorithm above is correct and optimal.
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list three times, which simplifies to `O(N)`.
- **Space Complexity:** `O(1)`. We don't use any auxiliary data structures (like maps). The space taken by the new copied list is not counted as auxiliary space.
