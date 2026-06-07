# Problem 6: Palindrome Linked List

## Problem Statement
Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

## Input Format
- The `head` of a singly linked list.

## Output Format
- A boolean representing whether the linked list is a palindrome.

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`.
- `0 <= Node.val <= 9`

---

## Approach: Find Middle, Reverse Half, Compare (O(1) Space)

A naive approach is to store the values in an array and use two pointers, but that takes `O(N)` space. To do it in `O(1)` space:

1. **Find the middle:** Use the Tortoise and Hare (slow and fast pointers) to find the middle of the linked list. 
2. **Reverse the second half:** Reverse the linked list starting from the `slow` pointer to the end.
3. **Compare:** Use two pointers, one at the `head` and one at the head of the reversed second half. Compare their values. If any mismatch is found, return `false`.
4. **Restore (Optional but good practice):** Reverse the second half back to its original state.
5. Return `true`.

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        while (curr != NULL) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }

public:
    bool isPalindrome(ListNode* head) {
        if (head == NULL || head->next == NULL) return true;
        
        // 1. Find the middle
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // 2. Reverse the second half
        ListNode* secondHalfHead = reverseList(slow);
        ListNode* copySecondHalf = secondHalfHead; // Save for restoring later
        
        // 3. Compare both halves
        ListNode* p1 = head;
        ListNode* p2 = secondHalfHead;
        bool isPalin = true;
        
        while (p2 != NULL) {
            if (p1->val != p2->val) {
                isPalin = false;
                break;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        
        // 4. Restore the list (optional)
        reverseList(copySecondHalf);
        
        return isPalin;
    }
};

int main() {
    Solution sol;
    
    // Create list: 1 -> 2 -> 2 -> 1
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(2);
    head->next->next->next = new ListNode(1);
    
    cout << "Is Palindrome? " << (sol.isPalindrome(head) ? "Yes" : "No") << endl; // Expected: Yes
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Finding the middle takes `O(N/2)`, reversing takes `O(N/2)`, comparing takes `O(N/2)`. Total is `O(N)`.
- **Space Complexity:** `O(1)`. Only pointers are used, no extra data structures.
