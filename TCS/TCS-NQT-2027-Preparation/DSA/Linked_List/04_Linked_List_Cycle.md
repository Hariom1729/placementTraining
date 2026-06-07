# Problem 4: Linked List Cycle

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Input Format
- The `head` of a singly linked list.

## Output Format
- A boolean representing whether a cycle exists.

## Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach: Floyd's Cycle-Finding Algorithm (Tortoise & Hare)

If we have two runners running on a circular track, a faster runner will eventually lap (catch up to) the slower runner.

1. Initialize two pointers, `slow` and `fast`, both pointing to the `head`.
2. Traverse the list:
   - Move `slow` by one step: `slow = slow->next`.
   - Move `fast` by two steps: `fast = fast->next->next`.
3. If there is a cycle, `fast` and `slow` will eventually point to the same node (`fast == slow`).
4. If `fast` reaches the end of the list (`fast == NULL` or `fast->next == NULL`), there is no cycle.

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
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                return true; // Cycle detected
            }
        }
        
        return false;
    }
};

int main() {
    Solution sol;
    
    // Create list: 3 -> 2 -> 0 -> -4 -> (points back to 2)
    ListNode* head = new ListNode(3);
    ListNode* node2 = new ListNode(2);
    ListNode* node0 = new ListNode(0);
    ListNode* node4 = new ListNode(-4);
    
    head->next = node2;
    node2->next = node0;
    node0->next = node4;
    node4->next = node2; // Creates the cycle
    
    cout << "Has cycle? " << (sol.hasCycle(head) ? "Yes" : "No") << endl; // Expected: Yes
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. If there is no cycle, `fast` reaches the end in `N/2` steps. If there is a cycle, the maximum number of steps `slow` takes before being caught is `N`.
- **Space Complexity:** `O(1)`. Only two pointers are used.
