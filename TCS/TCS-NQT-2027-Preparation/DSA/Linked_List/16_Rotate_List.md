# Problem 16: Rotate List

## Problem Statement
Given the `head` of a linked list, rotate the list to the right by `k` places.

## Input Format
- The `head` of a singly linked list.
- An integer `k`.

## Output Format
- The `head` of the rotated linked list.

## Constraints
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

---

## Approach: Make Circular and Break

Since `k` can be very large (`2 * 10^9`), we must use modulo arithmetic. If `k == length`, the list remains unchanged. So the effective rotations are `k % length`.

1. Find the `length` of the list and point a `tail` pointer to the last node.
2. If `head == NULL`, `head->next == NULL`, or `k == 0`, return `head`.
3. Compute `effective_k = k % length`. If `effective_k == 0`, return `head`.
4. Make the list circular by connecting the old tail to the old head: `tail->next = head`.
5. We need to find the *new tail*, which is at the `(length - effective_k)`-th node.
6. Traverse to the `(length - effective_k)`-th node. Let this be `newTail`.
7. The `newHead` will be `newTail->next`.
8. Break the circle: `newTail->next = NULL`.
9. Return `newHead`.

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL || head->next == NULL || k == 0) return head;
        
        // 1. Find length and the last node
        int length = 1;
        ListNode* tail = head;
        while (tail->next != NULL) {
            length++;
            tail = tail->next;
        }
        
        // 2. Compute effective rotations
        int effective_k = k % length;
        if (effective_k == 0) return head;
        
        // 3. Make circular
        tail->next = head;
        
        // 4. Find new tail (length - k th node)
        ListNode* newTail = head;
        for (int i = 1; i < length - effective_k; i++) {
            newTail = newTail->next;
        }
        
        // 5. Break circle and set new head
        ListNode* newHead = newTail->next;
        newTail->next = NULL;
        
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
    
    cout << "Original List: "; printList(head);
    
    ListNode* rotatedHead = sol.rotateRight(head, 2);
    
    cout << "Rotated List: "; printList(rotatedHead); // Expected: 4 -> 5 -> 1 -> 2 -> 3 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list once to find the length, and then a partial traversal to find the new tail.
- **Space Complexity:** `O(1)`. Only pointers are manipulated.
