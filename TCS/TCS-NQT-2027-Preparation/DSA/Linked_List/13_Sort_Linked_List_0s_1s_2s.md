# Problem 13: Sort Linked List of 0s, 1s, and 2s

## Problem Statement
Given a linked list of `N` nodes where nodes can contain values `0`, `1`, and `2` only. Sort the linked list.

## Input Format
- The `head` of a singly linked list.

## Output Format
- The `head` of the sorted linked list.

## Constraints
- `1 <= N <= 10^5`
- `0 <= Node.val <= 2`

---

## Approach: Data Replacement vs Link Modification

**Approach 1: Data Replacement (Easy but sometimes restricted)**
Traverse the list, count the number of 0s, 1s, and 2s. Traverse again and replace the node values.
*Interviewers often say "Do not modify the data, modify the links".*

**Approach 2: Modifying Links (Three Dummy Nodes)**
1. Create three dummy nodes: `zeroDummy`, `oneDummy`, `twoDummy`.
2. Maintain three tail pointers for these lists: `zero`, `one`, `two`.
3. Traverse the original list. If the current node's value is:
   - `0`: Append it to the `zero` list.
   - `1`: Append it to the `one` list.
   - `2`: Append it to the `two` list.
4. **Crucial Merge Step:**
   - Link the end of the `zero` list to the head of the `one` list (if it exists) or directly to the `two` list.
   - Link the end of the `one` list to the head of the `two` list.
   - Set the end of the `two` list to `NULL`.
5. The new head is `zeroDummy->next`.

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
    ListNode* sortList012(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        
        ListNode* zeroDummy = new ListNode(-1);
        ListNode* oneDummy = new ListNode(-1);
        ListNode* twoDummy = new ListNode(-1);
        
        ListNode* zero = zeroDummy;
        ListNode* one = oneDummy;
        ListNode* two = twoDummy;
        
        ListNode* curr = head;
        
        // Traverse and distribute nodes
        while (curr != NULL) {
            if (curr->val == 0) {
                zero->next = curr;
                zero = zero->next;
            } else if (curr->val == 1) {
                one->next = curr;
                one = one->next;
            } else {
                two->next = curr;
                two = two->next;
            }
            curr = curr->next;
        }
        
        // Connect the lists
        // If 'one' list is not empty, connect zero's end to one's start
        zero->next = (oneDummy->next != NULL) ? oneDummy->next : twoDummy->next;
        
        // Connect one's end to two's start
        one->next = twoDummy->next;
        
        // Crucial: Set two's end to NULL to terminate the list
        two->next = NULL;
        
        ListNode* newHead = zeroDummy->next;
        
        delete zeroDummy;
        delete oneDummy;
        delete twoDummy;
        
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
    
    // Create list: 1 -> 2 -> 0 -> 1 -> 2 -> 0
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(1);
    head->next->next->next->next = new ListNode(2);
    head->next->next->next->next->next = new ListNode(0);
    
    cout << "Original List: "; printList(head);
    
    ListNode* sortedHead = sol.sortList012(head);
    
    cout << "Sorted List: "; printList(sortedHead); // Expected: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We traverse the list exactly once.
- **Space Complexity:** `O(1)`. We reuse the existing nodes, just updating their `next` pointers.
