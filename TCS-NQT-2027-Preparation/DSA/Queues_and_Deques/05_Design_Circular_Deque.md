# Problem 5: Design Circular Deque

## Problem Statement
Design your implementation of the circular double-ended queue (deque).
Implement the `MyCircularDeque` class:
- `MyCircularDeque(int k)` Initializes the deque with a maximum size of `k`.
- `boolean insertFront()` Adds an item at the front. Returns true if successful.
- `boolean insertLast()` Adds an item at the rear. Returns true if successful.
- `boolean deleteFront()` Deletes an item from the front. Returns true if successful.
- `boolean deleteLast()` Deletes an item from the rear. Returns true if successful.
- `int getFront()` Returns the front item. If empty, return `-1`.
- `int getRear()` Returns the last item. If empty, return `-1`.
- `boolean isEmpty()` Returns true if the deque is empty.
- `boolean isFull()` Returns true if the deque is full.

## Constraints
- `1 <= k <= 1000`
- `0 <= value <= 1000`

---

## Approach

This builds upon the Circular Queue, but allows insertion and deletion from *both* ends.
1. Use an array `arr` of size `k`.
2. Initialize `front = 0`, `rear = k - 1`, `size = 0`.
3. **insertLast:** Like normal enqueue. `rear = (rear + 1) % k`. `arr[rear] = value`.
4. **deleteFront:** Like normal dequeue. `front = (front + 1) % k`.
5. **insertFront:** We must move `front` backward. To handle negative numbers with modulo, `front = (front - 1 + k) % k`. `arr[front] = value`.
6. **deleteLast:** We must move `rear` backward. `rear = (rear - 1 + k) % k`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MyCircularDeque {
private:
    vector<int> arr;
    int front;
    int rear;
    int size;
    int capacity;

public:
    MyCircularDeque(int k) {
        capacity = k;
        arr.resize(k);
        front = 0;
        rear = k - 1; // Start rear at k-1 so that the first insertLast puts it at index 0
        size = 0;
    }
    
    bool insertFront(int value) {
        if (isFull()) return false;
        
        front = (front - 1 + capacity) % capacity;
        arr[front] = value;
        size++;
        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) return false;
        
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        size++;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) return false;
        
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) return false;
        
        rear = (rear - 1 + capacity) % capacity;
        size--;
        return true;
    }
    
    int getFront() {
        if (isEmpty()) return -1;
        return arr[front];
    }
    
    int getRear() {
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
    MyCircularDeque myCircularDeque(3);
    cout << myCircularDeque.insertLast(1) << " ";   // return True
    cout << myCircularDeque.insertLast(2) << " ";   // return True
    cout << myCircularDeque.insertFront(3) << " ";  // return True
    cout << myCircularDeque.insertFront(4) << " ";  // return False (full)
    cout << myCircularDeque.getRear() << " ";       // return 2
    cout << myCircularDeque.isFull() << " ";        // return True
    cout << myCircularDeque.deleteLast() << " ";    // return True
    cout << myCircularDeque.insertFront(4) << " ";  // return True
    cout << myCircularDeque.getFront() << "\n";     // return 4
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations.
- **Space Complexity:** `O(K)` to store the circular deque of size `K`.
