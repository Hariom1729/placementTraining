# Reverse Linked List

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Frequency: Very High

---

## Problem Statement
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

---

## Optimal Approach (Iterative Pointers)
**Detailed explanation:**
We need three pointers: `prev`, `curr`, and `next_node`.
Initialize `prev = nullptr` and `curr = head`.
Iterate while `curr` is not null:
1. Save the next node: `next_node = curr->next`.
2. Reverse the link: `curr->next = prev`.
3. Move `prev` forward: `prev = curr`.
4. Move `curr` forward: `curr = next_node`.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

## C++ Solution
```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    
    while (curr != nullptr) {
        ListNode* next_node = curr->next; // Save next
        curr->next = prev;                // Reverse link
        prev = curr;                      // Advance prev
        curr = next_node;                 // Advance curr
    }
    
    return prev; // prev will be the new head
}
```
