# Problem 1: Implement Queue using Array

## Problem Statement
Implement a Queue using an array. Support the standard operations: `push(x)` to enqueue an element, `pop()` to dequeue an element, and `front()` to get the front element.
Assume a maximum queue size.

## Input Format
- Series of queue operations.

## Output Format
- Results of the operations.

## Constraints
- `1 <= Max Size <= 10^5`
- `1 <= x <= 10^5`

---

## Approach

A queue has two ends: `front` (where elements are removed) and `rear` (where elements are added).
1. We maintain an array `arr` of a fixed size, and two pointers: `front_idx = 0` and `rear_idx = 0`.
2. **Push:** Add the element at `arr[rear_idx]` and increment `rear_idx`.
3. **Pop:** Return the element at `arr[front_idx]` and increment `front_idx`.
4. **Empty:** The queue is empty if `front_idx == rear_idx`.

*(Note: A simple array implementation wastes space because `front_idx` keeps moving forward. A Circular Queue is a better practical implementation, which we will cover later).*

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

class MyQueue {
private:
    int* arr;
    int front_idx;
    int rear_idx;
    int maxSize;

public:
    MyQueue(int size = 100000) {
        maxSize = size;
        arr = new int[maxSize];
        front_idx = 0;
        rear_idx = 0;
    }
    
    ~MyQueue() {
        delete[] arr;
    }
    
    void push(int x) {
        if (rear_idx == maxSize) {
            cout << "Queue Overflow" << endl;
            return;
        }
        arr[rear_idx++] = x;
    }
    
    int pop() {
        if (front_idx == rear_idx) {
            cout << "Queue Underflow" << endl;
            return -1; // Or throw exception
        }
        return arr[front_idx++];
    }
    
    int front() {
        if (front_idx == rear_idx) {
            return -1; // Queue is empty
        }
        return arr[front_idx];
    }
    
    bool empty() {
        return front_idx == rear_idx;
    }
};

int main() {
    MyQueue q;
    q.push(10);
    q.push(20);
    q.push(30);
    
    cout << "Front element is: " << q.front() << endl; // Expected: 10
    cout << "Popped element is: " << q.pop() << endl;   // Expected: 10
    cout << "Front element is: " << q.front() << endl; // Expected: 20
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations (`push`, `pop`, `front`, `empty`).
- **Space Complexity:** `O(N)` where `N` is the maximum capacity of the queue.
