# Problem 14: Add 1 to a number represented as linked list

## Problem Statement
A number `N` is represented in a Linked List such that each digit corresponds to a node in the linked list. You need to add 1 to it.
For example, `199` is represented as `1 -> 9 -> 9`. Adding 1 to it gives `200`, which should be represented as `2 -> 0 -> 0`.

## Input Format
- The `head` of a singly linked list.

## Output Format
- The `head` of the modified linked list.

## Constraints
- `1 <= N <= 10^4`
- `0 <= Node.val <= 9`

---

## Approach

Since we have to add 1 to the least significant digit (which is at the end of the list), it is much easier to do this from right to left. Since it's a singly linked list, we can reverse it first!

1. **Reverse the Linked List:** So `1 -> 9 -> 9` becomes `9 -> 9 -> 1`.
2. **Add 1:** Traverse the reversed list. Add 1 to the first node.
   - If `node->val` becomes 10, set `node->val = 0` and carry `1` to the next node.
   - Keep doing this as long as `carry == 1`.
   - If you reach the end of the list and `carry == 1` is still there, append a new node with value `1`.
3. **Reverse Again:** Reverse the list back to its original (but modified) orientation.

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
private:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        while (curr != NULL) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }

public:
    ListNode* addOne(ListNode *head) {
        // Step 1: Reverse the linked list
        head = reverseList(head);
        
        // Step 2: Add 1
        ListNode* curr = head;
        int carry = 1; // We want to add 1
        
        while (curr != NULL) {
            curr->val += carry;
            if (curr->val < 10) {
                carry = 0;
                break; // No more carry, we can stop
            } else {
                curr->val = 0;
                carry = 1;
            }
            
            // If it's the last node and we still have a carry, we need to add a new node
            if (curr->next == NULL && carry == 1) {
                curr->next = new ListNode(1);
                carry = 0;
                break;
            }
            
            curr = curr->next;
        }
        
        // Step 3: Reverse back
        return reverseList(head);
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
    
    // Create list: 1 -> 9 -> 9
    ListNode* head = new ListNode(1);
    head->next = new ListNode(9);
    head->next->next = new ListNode(9);
    
    cout << "Original: "; printList(head);
    
    ListNode* newHead = sol.addOne(head);
    
    cout << "After Adding 1: "; printList(newHead); // Expected: 2 -> 0 -> 0 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We reverse the list (`O(N)`), traverse to add 1 (`O(N)` in the worst case), and reverse it back (`O(N)`).
- **Space Complexity:** `O(1)`. Modifying links and values in place.
