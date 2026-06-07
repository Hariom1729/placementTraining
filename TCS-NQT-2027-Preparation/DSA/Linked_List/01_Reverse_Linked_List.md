# Problem 1: Reverse Linked List

## Problem Statement
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Input Format
- The `head` of a singly linked list.

## Output Format
- The `head` of the reversed linked list.

## Constraints
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Approach: Iterative (In-place)

To reverse a linked list, we need to change the `next` pointer of each node to point to its previous node.
Since a node does not have a reference to its previous node, we must store its previous element beforehand.

1. Initialize three pointers: 
   - `prev = NULL`
   - `curr = head`
   - `next_node = NULL`
2. Iterate while `curr != NULL`:
   - Store the next node: `next_node = curr->next`.
   - Reverse the current node's pointer: `curr->next = prev`.
   - Move `prev` and `curr` one step forward: `prev = curr`, `curr = next_node`.
3. Return `prev` as the new head.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next_node = NULL;
        
        while (curr != NULL) {
            next_node = curr->next; // Store next
            curr->next = prev;      // Reverse pointer
            
            // Move forward
            prev = curr;
            curr = next_node;
        }
        
        return prev;
    }
};

void printList(ListNode* head) {
    while (head != NULL) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

int main() {
    Solution sol;
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    cout << "Original List: ";
    printList(head);
    
    ListNode* reversedHead = sol.reverseList(head);
    
    cout << "Reversed List: ";
    printList(reversedHead); // Expected: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes in the linked list. We traverse the list exactly once.
- **Space Complexity:** `O(1)`. The algorithm only uses a few pointers for the reversal process.
