# Linked Lists

## 1. Theory & Core Concepts

A Linked List is a linear data structure where elements are not stored at contiguous memory locations. Instead, the elements are linked using pointers. They are frequently tested in TCS Digital and Prime interviews.

### Types of Linked Lists
1. **Singly Linked List:** Each node contains data and a pointer to the next node.
2. **Doubly Linked List:** Each node contains data, a pointer to the next node, and a pointer to the previous node.
3. **Circular Linked List:** The last node points back to the first node instead of `NULL`.

### Node Structure in C++
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

### Key Techniques for Linked List Problems
1. **Two Pointers (Slow & Fast / Tortoise & Hare):** Extremely useful for finding the middle of the list, detecting cycles, or finding the start of a cycle.
2. **Dummy Node:** A pseudo-head node used to simplify edge cases, especially when the head of the list might change or be removed (e.g., merging lists, removing elements).
3. **In-place Reversal:** Modifying the `next` pointers to reverse the list without using extra space.

---

## 2. Common TCS Interview Problems
*   `01_Reverse_Linked_List.md`
*   `02_Middle_of_Linked_List.md`
*   `03_Merge_Two_Sorted_Lists.md`
*   `04_Linked_List_Cycle.md`
*   `05_Linked_List_Cycle_II.md`
*   *(... and 10+ more high-frequency problems)*
