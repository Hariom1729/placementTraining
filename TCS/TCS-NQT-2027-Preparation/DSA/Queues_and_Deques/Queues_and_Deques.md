# Queues & Deques

## 1. Theory & Core Concepts

A **Queue** is a linear data structure that follows the **FIFO (First In First Out)** principle. The first element inserted is the first one to be removed.
Think of a queue of people waiting for a bus: the first person in line gets on the bus first.

A **Deque (Double-Ended Queue)** is a generalized version of a queue where elements can be inserted and removed from **both ends** (front and rear).

### Key Operations in C++ STL (`std::queue` and `std::deque`)
```cpp
#include <queue>
#include <deque>

// Queue
queue<int> q;
q.push(10); // Enqueue at the rear
q.front();  // Returns the front element
q.back();   // Returns the rear element
q.pop();    // Dequeue from the front. Returns nothing.
q.empty();  // Returns true if empty
q.size();   // Returns the number of elements

// Deque
deque<int> dq;
dq.push_back(10);  // Insert at rear
dq.push_front(20); // Insert at front
dq.front();        // Access front element
dq.back();         // Access rear element
dq.pop_front();    // Remove from front
dq.pop_back();     // Remove from rear
```

### Common Interview Patterns
1. **Simulation:** Simulating real-world queues (e.g., ticket counters, task scheduling).
2. **Breadth-First Search (BFS):** Queues are the fundamental data structure used for BFS in Trees and Graphs (Level Order Traversal, Shortest Path in unweighted graphs).
3. **Sliding Window:** Deques are extremely useful for sliding window problems, especially finding the Maximum/Minimum in a window of size `K`.
4. **Implementation:** Designing a Queue or Deque from scratch using Arrays or Linked Lists, or implementing them using Stacks.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Implement_Queue_using_Array.md`
*   `02_Implement_Queue_using_Linked_List.md`
*   `03_First_Non_Repeating_Character.md`
*   `04_Design_Circular_Queue.md`
*   `05_Design_Circular_Deque.md`
*   *(... and 10+ more)*
