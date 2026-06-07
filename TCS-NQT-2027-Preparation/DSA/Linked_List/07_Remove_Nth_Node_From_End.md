# Problem 7: Remove Nth Node From End of List

## Problem Statement
Given the `head` of a linked list, remove the `n`th node from the end of the list and return its head.

## Input Format
- The `head` of a singly linked list.
- An integer `n`.

## Output Format
- The `head` of the modified linked list.

## Constraints
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Approach: Fast and Slow Pointers (One Pass)

A naive approach is to count the total nodes (`L`), then remove the `(L - n + 1)`th node. This requires two passes. We can do it in one pass using two pointers.

1. Create a `dummy` node pointing to `head`. This handles edge cases like removing the very first node.
2. Initialize two pointers, `fast` and `slow`, both pointing to `dummy`.
3. Move `fast` pointer `n` steps ahead.
4. Now, move both `fast` and `slow` one step at a time until `fast->next` becomes `NULL`.
5. Because `fast` had an `n`-step head start, when `fast` reaches the last node, `slow` will be exactly right before the node we need to remove.
6. Delete the target node by setting `slow->next = slow->next->next`.
7. Return `dummy->next`.

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode* slow = dummy;
        ListNode* fast = dummy;
        
        // Move fast pointer n steps ahead
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        
        // Move both until fast reaches the last node
        while (fast->next != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
        
        // slow is now pointing to the node BEFORE the one to be deleted
        ListNode* nodeToDelete = slow->next;
        slow->next = slow->next->next;
        delete nodeToDelete; // Free memory
        
        ListNode* newHead = dummy->next;
        delete dummy;
        return newHead;
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
    
    cout << "Original: ";
    printList(head);
    
    // Remove 2nd from end (which is 4)
    head = sol.removeNthFromEnd(head, 2);
    
    cout << "Modified: ";
    printList(head); // Expected: 1 -> 2 -> 3 -> 5 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list only once.
- **Space Complexity:** `O(1)`. We only use a few extra pointers.
