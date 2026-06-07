# Problem 9: Intersection of Two Linked Lists

## Problem Statement
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
**Note:** The linked lists must retain their original structure after the function returns.

## Input Format
- Two `ListNode*` pointers, `headA` and `headB`.

## Output Format
- A reference to the intersection `ListNode`, or `NULL`.

## Constraints
- The number of nodes of `listA` is in the `[0, 3 * 10^4]`.
- The number of nodes of `listB` is in the `[0, 3 * 10^4]`.

---

## Approach: Two Pointers (Distance Equalization)

If the lists intersect, the part of the lists *after* the intersection is identical. However, the lengths of the lists *before* the intersection might be different.
If pointer `A` travels through `listA` and then `listB`, and pointer `B` travels through `listB` and then `listA`, they will both travel exactly the same total distance `(lengthA + lengthB)`. Therefore, they will meet at the intersection point!

1. Initialize two pointers `p1 = headA` and `p2 = headB`.
2. While `p1 != p2`:
   - If `p1` reaches the end (`NULL`), redirect it to `headB`. Otherwise, move it forward.
   - If `p2` reaches the end (`NULL`), redirect it to `headA`. Otherwise, move it forward.
3. They will eventually meet at the intersection node. If there is no intersection, they will both become `NULL` at the exact same time, breaking the loop and returning `NULL`.

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL) return NULL;
        
        ListNode* p1 = headA;
        ListNode* p2 = headB;
        
        while (p1 != p2) {
            // If p1 reaches the end, point it to headB. Else move it forward.
            p1 = (p1 == NULL) ? headB : p1->next;
            
            // If p2 reaches the end, point it to headA. Else move it forward.
            p2 = (p2 == NULL) ? headA : p2->next;
        }
        
        // p1 will be the intersection node, or NULL if there is no intersection
        return p1;
    }
};

int main() {
    Solution sol;
    
    // Create common part: 8 -> 4 -> 5
    ListNode* intersect = new ListNode(8);
    intersect->next = new ListNode(4);
    intersect->next->next = new ListNode(5);
    
    // Create list A: 4 -> 1 -> 8 -> 4 -> 5
    ListNode* headA = new ListNode(4);
    headA->next = new ListNode(1);
    headA->next->next = intersect;
    
    // Create list B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    ListNode* headB = new ListNode(5);
    headB->next = new ListNode(6);
    headB->next->next = new ListNode(1);
    headB->next->next->next = intersect;
    
    ListNode* result = sol.getIntersectionNode(headA, headB);
    
    if (result) {
        cout << "Intersected at node with value: " << result->val << endl; // Expected: 8
    } else {
        cout << "No intersection." << endl;
    }
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N + M)` where `N` and `M` are the lengths of the two lists. In the worst case, each pointer traverses both lists.
- **Space Complexity:** `O(1)`. No extra space is used.
