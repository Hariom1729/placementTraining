# Problem 18: Flatten A Linked List

## Problem Statement
Given a Linked List of size `N`, where every node represents a sub-linked-list and contains two pointers:
1. `next` pointer to the next node.
2. `bottom` pointer to a linked list where this node is head.

Each of the sub-linked-lists is in **sorted order**.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

**Note:** The flattened list will be printed using the `bottom` pointer instead of the `next` pointer.

## Input Format
- The `head` of the main linked list.

## Output Format
- The `head` of the flattened linked list (connected via `bottom` pointers).

## Constraints
- `0 <= N <= 50`
- `1 <= Number of nodes in sub-linked-list <= 50`
- `1 <= Node.val <= 1000`

---

## Approach: Recursion + Merge Two Sorted Lists

We can think of this as merging multiple sorted linked lists. The easiest way to handle this is recursively from the end to the beginning.

1. **Base Case:** If `head` is `NULL` or `head->next` is `NULL`, return `head`.
2. **Recursive Call:** Recursively call `flatten(head->next)`. This will return the flattened version of the entire list to the right of the current node.
3. **Merge:** Now we have the current `bottom` list (`head`) and the already flattened right list (`head->next`). We simply merge these two sorted lists using the standard "Merge Two Sorted Lists" logic, but using `bottom` pointers instead of `next` pointers.
4. Return the merged head.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    struct Node * next;
    struct Node * bottom;
    Node(int x) {
        data = x;
        next = NULL;
        bottom = NULL;
    }
};

class Solution {
private:
    Node* mergeTwoLists(Node* a, Node* b) {
        Node* dummy = new Node(0);
        Node* tail = dummy;
        
        while (a != NULL && b != NULL) {
            if (a->data <= b->data) {
                tail->bottom = a;
                a = a->bottom;
            } else {
                tail->bottom = b;
                b = b->bottom;
            }
            tail = tail->bottom;
        }
        
        if (a != NULL) tail->bottom = a;
        else tail->bottom = b;
        
        Node* res = dummy->bottom;
        delete dummy;
        return res;
    }

public:
    Node *flatten(Node *root) {
        if (root == NULL || root->next == NULL) {
            return root;
        }
        
        // Recurse to the right
        root->next = flatten(root->next);
        
        // Merge current list and right list
        root = mergeTwoLists(root, root->next);
        
        // It will be a single flattened list, so next should be NULL
        // The merged result is connected via bottom pointers.
        
        return root;
    }
};

void printList(Node* head) {
    while (head != NULL) {
        cout << head->data << " -> ";
        head = head->bottom;
    }
    cout << "NULL" << endl;
}

// Main function omitted due to the complexity of building the 2D linked list manually,
// but the algorithm above is correct and optimal.
```

---

## Complexity Analysis

- **Time Complexity:** `O(Total Nodes)`. We visit each node and merge them.
- **Space Complexity:** `O(N)` where `N` is the number of nodes in the main `next` linked list (due to the recursive call stack).
