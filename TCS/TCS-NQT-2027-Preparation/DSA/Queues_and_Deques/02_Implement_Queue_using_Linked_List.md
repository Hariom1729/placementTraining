# Problem 2: Implement Queue using Linked List

## Problem Statement
Implement a Queue using a singly linked list. Support the standard operations: `push(x)` to enqueue an element, `pop()` to dequeue an element, and `front()` to get the front element.
The queue size is dynamic.

## Input Format
- Series of queue operations.

## Output Format
- Results of the operations.

## Constraints
- `-10^5 <= x <= 10^5`

---

## Approach

A Linked List overcomes the size limitation of an array-based queue.
1. We maintain two pointers: `front` (points to the first node) and `rear` (points to the last node).
2. **Push (Enqueue):** Create a new node. If the queue is empty, both `front` and `rear` point to this new node. Otherwise, link the current `rear`'s `next` to the new node, and update `rear` to the new node.
3. **Pop (Dequeue):** If the queue is empty, do nothing or throw an error. Otherwise, store the `front` node temporarily, move `front` to `front->next`, and delete the stored node to free memory. If `front` becomes `NULL` (queue becomes empty), make `rear` `NULL` as well.
4. **Front:** Return `front->val`.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

struct QueueNode {
    int val;
    QueueNode* next;
    QueueNode(int x) : val(x), next(NULL) {}
};

class MyQueue {
private:
    QueueNode* front_ptr;
    QueueNode* rear_ptr;

public:
    MyQueue() {
        front_ptr = NULL;
        rear_ptr = NULL;
    }
    
    void push(int x) {
        QueueNode* newNode = new QueueNode(x);
        
        // If queue is empty, new node is both front and rear
        if (rear_ptr == NULL) {
            front_ptr = rear_ptr = newNode;
            return;
        }
        
        // Add the new node at the end of queue and change rear
        rear_ptr->next = newNode;
        rear_ptr = newNode;
    }
    
    int pop() {
        // If queue is empty, return -1
        if (front_ptr == NULL) return -1;
        
        // Store previous front and move front one node ahead
        QueueNode* temp = front_ptr;
        int popped_val = temp->val;
        
        front_ptr = front_ptr->next;
        
        // If front becomes NULL, then change rear also as NULL
        if (front_ptr == NULL) {
            rear_ptr = NULL;
        }
        
        delete temp; // Free memory
        return popped_val;
    }
    
    int front() {
        if (front_ptr == NULL) return -1;
        return front_ptr->val;
    }
    
    bool empty() {
        return front_ptr == NULL;
    }
};

int main() {
    MyQueue q;
    q.push(100);
    q.push(200);
    q.push(300);
    
    cout << "Front element is: " << q.front() << endl; // Expected: 100
    cout << "Popped element is: " << q.pop() << endl;   // Expected: 100
    cout << "Front element is: " << q.front() << endl; // Expected: 200
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations (`push`, `pop`, `front`, `empty`).
- **Space Complexity:** `O(N)` where `N` is the number of elements in the queue, dynamically allocated.
