# Problem 3: Merge Two Sorted Lists

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

## Input Format
- Two `ListNode*` pointers, `list1` and `list2`.

## Output Format
- A `ListNode*` pointing to the head of the merged list.

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Approach: Dummy Node + Two Pointers

A **dummy node** simplifies the code because we don't need to write special logic for initializing the `head` of the merged list.
1. Create a `dummy` node and a pointer `tail` pointing to `dummy`.
2. Traverse both lists using two pointers, `ptr1` (on `list1`) and `ptr2` (on `list2`), while neither is `NULL`.
3. Compare `ptr1->val` and `ptr2->val`.
   - If `ptr1->val <= ptr2->val`, link `tail->next` to `ptr1` and move `ptr1` forward.
   - Else, link `tail->next` to `ptr2` and move `ptr2` forward.
4. Move `tail` forward.
5. If either list is exhausted, simply attach the remaining portion of the other list to `tail->next`.
6. The merged list starts from `dummy->next`.

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-1); // Dummy node
        ListNode* tail = dummy;
        
        while (list1 != NULL && list2 != NULL) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }
        
        // Attach the remaining nodes
        if (list1 != NULL) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }
        
        ListNode* head = dummy->next;
        delete dummy; // Prevent memory leak
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
    
    ListNode* list1 = new ListNode(1);
    list1->next = new ListNode(2);
    list1->next->next = new ListNode(4);
    
    ListNode* list2 = new ListNode(1);
    list2->next = new ListNode(3);
    list2->next->next = new ListNode(4);
    
    ListNode* mergedHead = sol.mergeTwoLists(list1, list2);
    
    cout << "Merged List: ";
    printList(mergedHead); // Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N + M)` where `N` and `M` are the lengths of `list1` and `list2`. We iterate through both lists exactly once.
- **Space Complexity:** `O(1)`. We reuse the existing nodes, so no extra space is required except for a few pointers.
