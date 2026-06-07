# Problem 2: Middle of the Linked List

## Problem Statement
Given the `head` of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the **second middle** node.

## Input Format
- The `head` of a singly linked list.

## Output Format
- A reference to the middle `ListNode`.

## Constraints
- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

---

## Approach: Tortoise and Hare (Slow and Fast Pointers)

Instead of counting all the nodes and then traversing half the distance, we can use two pointers moving at different speeds.
1. Initialize two pointers, `slow` and `fast`, both pointing to the `head`.
2. Move `slow` by **one step** and `fast` by **two steps** at a time.
3. When `fast` reaches the end of the list (`fast == NULL` or `fast->next == NULL`), `slow` will be exactly at the middle.
   - If the number of nodes is odd, `fast->next` will become `NULL`, and `slow` will be exactly on the middle node.
   - If the number of nodes is even, `fast` will become `NULL`, and `slow` will be on the second middle node (which satisfies the problem constraints).

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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        // Fast pointer moves twice as fast as the slow pointer
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
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
    
    // List 1: Odd length
    ListNode* head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);
    head1->next->next->next->next = new ListNode(5);
    
    cout << "Middle of odd list: " << sol.middleNode(head1)->val << endl; // Expected: 3
    
    // List 2: Even length
    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = new ListNode(3);
    head2->next->next->next = new ListNode(4);
    head2->next->next->next->next = new ListNode(5);
    head2->next->next->next->next->next = new ListNode(6);
    
    cout << "Middle of even list: " << sol.middleNode(head2)->val << endl; // Expected: 4
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of nodes. We traverse the list at most once (technically `N/2` times).
- **Space Complexity:** `O(1)`. Only two pointers are used.
