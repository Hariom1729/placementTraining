# Problem 12: Sort List

## Problem Statement
Given the `head` of a linked list, return the list after sorting it in ascending order.
Can you sort the linked list in `O(n log n)` time and `O(1)` memory (i.e. constant space)?

## Input Format
- The `head` of a singly linked list.

## Output Format
- The `head` of the sorted linked list.

## Constraints
- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach: Merge Sort

Merge Sort is the ideal sorting algorithm for linked lists because it takes `O(N log N)` time and can be implemented without the `O(N)` auxiliary array that is required for arrays (though recursive call stack takes `O(log N)` space, it is often accepted as `O(1)` space in linked list context, or we can implement it iteratively).

1. **Base Case:** If the list is empty or has only one node, it's already sorted. Return it.
2. **Find Middle:** Use the slow/fast pointer approach to find the middle node.
   - *Crucial step:* Break the list into two separate lists by setting the `next` of the node *before* the middle to `NULL`.
3. **Recursively Sort:** Call `sortList` on the left half and the right half.
4. **Merge:** Merge the two sorted halves using the "Merge Two Sorted Lists" logic.

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
    // Helper function to find the middle and break the list
    ListNode* findMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next; // Notice fast starts at head->next to get the first middle in even length
        
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    // Helper function to merge two sorted lists
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        
        if (l1 != NULL) tail->next = l1;
        else tail->next = l2;
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }

public:
    ListNode* sortList(ListNode* head) {
        // Base case: 0 or 1 node
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        // 1. Find middle
        ListNode* mid = findMiddle(head);
        
        // 2. Break the list into two halves
        ListNode* rightHalf = mid->next;
        mid->next = NULL;
        ListNode* leftHalf = head;
        
        // 3. Recursively sort both halves
        leftHalf = sortList(leftHalf);
        rightHalf = sortList(rightHalf);
        
        // 4. Merge the sorted halves
        return merge(leftHalf, rightHalf);
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
    
    // Create list: 4 -> 2 -> 1 -> 3
    ListNode* head = new ListNode(4);
    head->next = new ListNode(2);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(3);
    
    cout << "Original List: "; printList(head);
    
    ListNode* sortedHead = sol.sortList(head);
    
    cout << "Sorted List: "; printList(sortedHead); // Expected: 1 -> 2 -> 3 -> 4 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N log N)`. Dividing takes `O(log N)` levels, and merging at each level takes `O(N)` time.
- **Space Complexity:** `O(log N)` due to the recursive call stack. (Can be reduced to strictly `O(1)` using iterative bottom-up merge sort).
