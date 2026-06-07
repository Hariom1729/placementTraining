# Problem 8: Delete Node in a Linked List

## Problem Statement
There is a singly-linked list `head` and we want to delete a node `node` in it.
You are given the node to be deleted `node`. You will **not be given access to the first node** of `head`.
All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.

## Input Format
- A reference to the `ListNode` to be deleted.

## Output Format
- Modify the list in-place. No return value.

## Constraints
- The number of the nodes in the given list is in the range `[2, 1000]`.
- `-1000 <= Node.val <= 1000`
- The value of each node in the list is unique.
- The `node` to be deleted is in the list and is not a tail node.

---

## Approach: Value Copy Trick

Since we don't have the `head` of the list, we cannot traverse from the beginning to find the node right before the one we need to delete. 
Therefore, we cannot do a traditional deletion (`prev->next = curr->next`).

Instead, we can copy the value of the **next** node into the current node, and then delete the **next** node.
1. Store the next node: `temp = node->next`.
2. Copy its value: `node->val = temp->val`.
3. Bypass the next node: `node->next = temp->next`.
4. Delete `temp` to free memory.

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
    void deleteNode(ListNode* node) {
        // Copy the value of the next node
        ListNode* temp = node->next;
        node->val = temp->val;
        
        // Link to the next of next
        node->next = temp->next;
        
        // Free the memory of the duplicated next node
        delete temp;
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
    
    // Create list: 4 -> 5 -> 1 -> 9
    ListNode* head = new ListNode(4);
    ListNode* node5 = new ListNode(5);
    ListNode* node1 = new ListNode(1);
    ListNode* node9 = new ListNode(9);
    
    head->next = node5;
    node5->next = node1;
    node1->next = node9;
    
    cout << "Original List: ";
    printList(head);
    
    // Delete node '5' (we only pass the pointer to node '5')
    sol.deleteNode(node5);
    
    cout << "After deleting 5: ";
    printList(head); // Expected: 4 -> 1 -> 9 -> NULL
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)`. We only perform a few constant time operations.
- **Space Complexity:** `O(1)`.
