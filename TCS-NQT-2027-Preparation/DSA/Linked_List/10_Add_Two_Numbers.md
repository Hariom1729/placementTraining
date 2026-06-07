# Problem 10: Add Two Numbers

## Problem Statement
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Input Format
- Two `ListNode*` pointers, `l1` and `l2`.

## Output Format
- A `ListNode*` pointing to the head of the sum linked list.

## Constraints
- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`

---

## Approach: Elementary Math with Dummy Node

Since the lists are already in reverse order, the heads represent the least significant digits (the "ones" place). We can simply add them together, keep track of the carry, and build a new list.

1. Create a `dummy` node to simplify the creation of the result list, and a `tail` pointer.
2. Initialize `carry = 0`.
3. Traverse both lists as long as `l1` is not `NULL` OR `l2` is not `NULL` OR `carry > 0`.
   - Calculate the sum of `l1->val`, `l2->val`, and `carry`.
   - The new digit is `sum % 10`.
   - The new carry is `sum / 10`.
   - Create a new node with the digit and attach it to `tail->next`.
   - Move `l1`, `l2`, and `tail` forward if possible.
4. Return `dummy->next`.

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        int carry = 0;
        
        while (l1 != NULL || l2 != NULL || carry > 0) {
            int sum = carry;
            
            if (l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            carry = sum / 10;
            tail->next = new ListNode(sum % 10);
            tail = tail->next;
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
    
    // Number 1: 342 (stored as 2 -> 4 -> 3)
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    
    // Number 2: 465 (stored as 5 -> 6 -> 4)
    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);
    
    cout << "List 1: "; printList(l1);
    cout << "List 2: "; printList(l2);
    
    ListNode* result = sol.addTwoNumbers(l1, l2);
    
    cout << "Sum List: "; printList(result); // Expected: 7 -> 0 -> 8 -> NULL (which is 807)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(max(N, M))` where `N` and `M` are the lengths of `l1` and `l2`. We iterate through both lists at the same time.
- **Space Complexity:** `O(max(N, M))` to store the new linked list.
