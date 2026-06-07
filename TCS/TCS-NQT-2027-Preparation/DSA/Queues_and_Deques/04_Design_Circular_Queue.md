# Problem 4: Design Circular Queue

## Problem Statement
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

Implement the `MyCircularQueue` class:
- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.
- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return true if the operation is successful.
- `boolean deQueue()` Deletes an element from the circular queue. Return true if the operation is successful.
- `boolean isEmpty()` Checks whether the circular queue is empty or not.
- `boolean isFull()` Checks whether the circular queue is full or not.

## Constraints
- `1 <= k <= 1000`
- `0 <= value <= 1000`

---

## Approach

A regular array-based queue wastes space because the `front` pointer moves forward during dequeues, leaving empty spaces at the beginning of the array. A Circular Queue solves this using the modulo operator `%`.

1. Use an array `arr` of size `k`.
2. Maintain `front`, `rear`, and `size`. Initialize `front = 0`, `rear = -1`, `size = 0`.
3. **enQueue:** If `size == k`, it's full. Otherwise, move `rear` circularly: `rear = (rear + 1) % k`. Insert the value at `arr[rear]` and increment `size`.
4. **deQueue:** If `size == 0`, it's empty. Otherwise, move `front` circularly: `front = (front + 1) % k` and decrement `size`.
5. **Front:** Return `arr[front]`.
6. **Rear:** Return `arr[rear]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MyCircularQueue {
private:
    vector<int> arr;
    int front;
    int rear;
    int size;
    int capacity;

public:
    MyCircularQueue(int k) {
        capacity = k;
        arr.resize(k);
        front = 0;
        rear = -1;
        size = 0;
    }
    
    bool enQueue(int value) {
        if (isFull()) return false;
        
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return arr[front];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return arr[rear];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == capacity;
    }
};

int main() {
    MyCircularQueue myCircularQueue(3);
    cout << myCircularQueue.enQueue(1) << " "; // return True
    cout << myCircularQueue.enQueue(2) << " "; // return True
    cout << myCircularQueue.enQueue(3) << " "; // return True
    cout << myCircularQueue.enQueue(4) << " "; // return False (queue is full)
    cout << myCircularQueue.Rear() << " ";     // return 3
    cout << myCircularQueue.isFull() << " ";   // return True
    cout << myCircularQueue.deQueue() << " ";  // return True
    cout << myCircularQueue.enQueue(4) << " "; // return True
    cout << myCircularQueue.Rear() << "\n";     // return 4
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations.
- **Space Complexity:** `O(K)` to store the circular queue of size `K`.
