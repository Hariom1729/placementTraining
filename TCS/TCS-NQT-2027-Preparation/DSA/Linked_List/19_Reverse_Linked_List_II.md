# Problem 19: Reverse Linked List II (Within a Range)

## Problem Statement
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

## Input Format
- The `head` of a singly linked list.
- Integers `left` and `right`.

## Output Format
- The `head` of the modified linked list.

## Constraints
- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

---

## Approach: One Pass In-Place Reversal

1. Create a `dummy` node to handle the case where `left == 1` (reversing from the very head).
2. Use a `prev` pointer and advance it `left - 1` times. `prev` now points to the node exactly *before* the sub-list we want to reverse.
3. Let `curr = prev->next`. This `curr` node will eventually become the tail of the reversed sub-list.
4. Run a loop `right - left` times. In each iteration, we do a localized reversal:
   - Save `next_node = curr->next`.
   - Disconnect `curr` and point it to `next_node->next`.
   - Disconnect `next_node` and point it to the front of the reversed sub-list (`prev->next`).
   - Link `prev->next` to `next_node`.
   *(This effectively takes the node AFTER `curr` and moves it to the front of the reversed section).*
5. Return `dummy->next`.

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == NULL || left == right) return head;
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        
        // 1. Reach the node just before the 'left' position
        for (int i = 0; i < left - 1; i++) {
            prev = prev->next;
        }
        
        // 2. Start reversing
        ListNode* curr = prev->next;
        
        for (int i = 0; i < right - left; i++) {
            ListNode* next_node = curr->next;
            
            // Re-wiring
            curr->next = next_node->next;
            next_node->next = prev->next;
            prev->next = next_node;
        }
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
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
    
    // Create list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    cout << "Original: "; printList(head);
    
    // Reverse from position 2 to 4
    ListNode* reversedHead = sol.reverseBetween(head, 2, 4);
    
    cout << "Reversed 2 to 4: "; printList(reversedHead); // Expected: 1 -> 4 -> 3 -> 2 -> 5 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list at most once.
- **Space Complexity:** `O(1)`. Modifying pointers in place.
