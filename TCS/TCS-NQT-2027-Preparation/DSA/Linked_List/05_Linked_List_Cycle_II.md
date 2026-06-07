# Problem 5: Linked List Cycle II (Find Cycle Starting Node)

## Problem Statement
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
**Do not modify** the linked list.

## Input Format
- The `head` of a singly linked list.

## Output Format
- A reference to the `ListNode` where the cycle begins, or `NULL`.

## Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach: Extended Floyd's Cycle Algorithm

This builds upon detecting a cycle.
1. Use the standard `slow` and `fast` pointers to detect if a cycle exists.
2. If `fast == slow`, a cycle is detected.
3. The intersection point is **not necessarily** the start of the cycle. However, mathematically, the distance from the `head` to the start of the cycle is equal to the distance from the `intersection point` to the start of the cycle.
4. To find the start: 
   - Keep the `slow` pointer at the intersection point.
   - Reset the `fast` pointer back to the `head` of the list.
   - Move BOTH `slow` and `fast` by **one step** at a time.
   - The node where they meet next is exactly the starting node of the cycle.

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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        bool hasCycle = false;
        
        // Detect cycle
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        
        if (!hasCycle) return NULL;
        
        // Find starting node
        fast = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow;
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
    
    ListNode* start = sol.detectCycle(head);
    if (start) {
        cout << "Cycle starts at node with value: " << start->val << endl; // Expected: 2
    } else {
        cout << "No cycle detected." << endl;
    }
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Detecting the cycle takes `O(N)`. Finding the start takes another `O(N)`.
- **Space Complexity:** `O(1)`.
