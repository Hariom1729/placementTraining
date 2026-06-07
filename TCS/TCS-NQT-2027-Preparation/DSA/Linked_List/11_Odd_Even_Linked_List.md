# Problem 11: Odd Even Linked List

## Problem Statement
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(N)` time complexity.

## Input Format
- The `head` of a singly linked list.

## Output Format
- The `head` of the modified linked list.

## Constraints
- The number of nodes in the linked list is in the range `[0, 10^4]`.
- `-10^6 <= Node.val <= 10^6`

---

## Approach: Two Pointers (Odd and Even)

1. If the list is empty or has only one node, return the `head`.
2. Initialize two pointers: `odd` pointing to `head`, and `even` pointing to `head->next`.
3. Keep a separate pointer `evenHead` pointing to `head->next` so we can attach the even list to the end of the odd list later.
4. Iterate while `even != NULL && even->next != NULL`:
   - Connect the current odd node to the next odd node: `odd->next = odd->next->next`.
   - Move the `odd` pointer forward: `odd = odd->next`.
   - Connect the current even node to the next even node: `even->next = even->next->next`.
   - Move the `even` pointer forward: `even = even->next`.
5. After the loop, the odd list is complete. Connect the end of the odd list to the head of the even list: `odd->next = evenHead`.
6. Return `head`.

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
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even; // Save the head of the even list
        
        while (even != NULL && even->next != NULL) {
            odd->next = odd->next->next;
            odd = odd->next;
            
            even->next = even->next->next;
            even = even->next;
        }
        
        // Attach even list to the end of odd list
        odd->next = evenHead;
        
        return head;
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
    
    cout << "Original List: "; printList(head);
    
    ListNode* result = sol.oddEvenList(head);
    
    cout << "Odd Even List: "; printList(result); // Expected: 1 -> 3 -> 5 -> 2 -> 4 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list exactly once.
- **Space Complexity:** `O(1)`. We only manipulate pointers.
