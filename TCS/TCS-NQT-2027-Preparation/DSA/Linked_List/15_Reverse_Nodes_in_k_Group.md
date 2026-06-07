# Problem 15: Reverse Nodes in k-Group

## Problem Statement
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.
`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Input Format
- The `head` of a singly linked list.
- An integer `k`.

## Output Format
- The `head` of the modified linked list.

## Constraints
- The number of nodes in the list is in the range `[1, 5000]`.
- `0 <= Node.val <= 1000`
- `1 <= k <= 5000`

---

## Approach

This is a hard problem that combines finding lengths and reversing linked lists.
1. Find the total length of the linked list.
2. Create a `dummy` node pointing to `head` (essential for connecting groups).
3. We need pointers `prevGroupEnd`, `curr`, and `nextGroupStart`.
4. Run a loop `length / k` times. In each iteration, we reverse a group of size `k`.
   - The standard reverse logic applies, but we must carefully hook up the `prevGroupEnd` to the new head of the reversed group, and the tail of the reversed group to the remaining list.
5. Nodes remaining at the end (if `< k`) are left untouched.

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == NULL || k == 1) return head;
        
        // 1. Calculate length
        int length = 0;
        ListNode* temp = head;
        while (temp != NULL) {
            length++;
            temp = temp->next;
        }
        
        // 2. Setup Dummy Node
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode* prevGroupEnd = dummy;
        ListNode* curr = dummy;
        ListNode* next_node = dummy;
        
        // 3. Reverse k nodes at a time
        while (length >= k) {
            curr = prevGroupEnd->next;
            next_node = curr->next;
            
            // Reverse k-1 links
            for (int i = 1; i < k; i++) {
                curr->next = next_node->next;
                next_node->next = prevGroupEnd->next;
                prevGroupEnd->next = next_node;
                next_node = curr->next;
            }
            
            prevGroupEnd = curr;
            length -= k;
        }
        
        ListNode* res = dummy->next;
        delete dummy;
        return res;
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
    
    ListNode* newHead = sol.reverseKGroup(head, 2);
    
    cout << "Reversed in groups of 2: "; printList(newHead); // Expected: 2 -> 1 -> 4 -> 3 -> 5 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Finding length takes `O(N)`. Reversing takes `O(N)`.
- **Space Complexity:** `O(1)`. All in-place.
