# Problem 11: Design Front Middle Back Queue

## Problem Statement
Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBackQueue` class:
- `FrontMiddleBackQueue()` Initializes the queue.
- `void pushFront(int val)` Adds `val` to the front of the queue.
- `void pushMiddle(int val)` Adds `val` to the middle of the queue.
- `void pushBack(int val)` Adds `val` to the back of the queue.
- `int popFront()` Removes the front element of the queue and returns it. If the queue is empty, return `-1`.
- `int popMiddle()` Removes the middle element of the queue and returns it. If the queue is empty, return `-1`.
- `int popBack()` Removes the back element of the queue and returns it. If the queue is empty, return `-1`.

Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:
- Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
- Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.

## Constraints
- `1 <= val <= 10^9`
- At most `1000` calls will be made.

---

## Approach: Two Deques

To achieve `O(1)` time complexity for all operations, we can use two deques (`front_dq` and `back_dq`).
We maintain the invariant that `front_dq.size() == back_dq.size()` OR `front_dq.size() == back_dq.size() - 1`.
In other words, `back_dq` can have at most one more element than `front_dq`. The "middle" element will be at the back of `front_dq` or front of `back_dq` depending on sizes.

1. **Balance Function:** A helper function to ensure the sizes stay balanced. If `front_dq` becomes larger than `back_dq`, move the back of `front` to the front of `back`. If `back_dq` becomes more than 1 element larger than `front_dq`, move the front of `back` to the back of `front`.
2. **PushFront:** Push to the front of `front_dq`, then balance.
3. **PushBack:** Push to the back of `back_dq`, then balance.
4. **PushMiddle:** 
   - If `front_dq.size() < back_dq.size()`, push to the back of `front_dq`.
   - Else, push to the front of `back_dq`.
   - Balance.
5. **PopFront:** Pop from `front_dq`. If `front_dq` is empty, pop from `back_dq` (this only happens if total size is 1). Balance.
6. **PopBack:** Pop from `back_dq`. Balance.
7. **PopMiddle:** 
   - If `front_dq.size() == back_dq.size()`, pop from the back of `front_dq`.
   - Else (meaning `back_dq` is larger), pop from the front of `back_dq`.
   - Balance.

---

## C++ Solution

```cpp
#include <iostream>
#include <deque>
using namespace std;

class FrontMiddleBackQueue {
private:
    deque<int> front_dq;
    deque<int> back_dq;
    
    void balance() {
        if (front_dq.size() > back_dq.size()) {
            back_dq.push_front(front_dq.back());
            front_dq.pop_back();
        } else if (back_dq.size() > front_dq.size() + 1) {
            front_dq.push_back(back_dq.front());
            back_dq.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        front_dq.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (front_dq.size() < back_dq.size()) {
            front_dq.push_back(val);
        } else {
            back_dq.push_front(val);
        }
        balance();
    }
    
    void pushBack(int val) {
        back_dq.push_back(val);
        balance();
    }
    
    int popFront() {
        if (back_dq.empty()) return -1;
        int val;
        if (front_dq.empty()) {
            val = back_dq.front();
            back_dq.pop_front();
        } else {
            val = front_dq.front();
            front_dq.pop_front();
        }
        balance();
        return val;
    }
    
    int popMiddle() {
        if (back_dq.empty()) return -1;
        int val;
        if (front_dq.size() == back_dq.size()) {
            val = front_dq.back();
            front_dq.pop_back();
        } else {
            val = back_dq.front();
            back_dq.pop_front();
        }
        balance();
        return val;
    }
    
    int popBack() {
        if (back_dq.empty()) return -1;
        int val = back_dq.back();
        back_dq.pop_back();
        balance();
        return val;
    }
};

// Main omitted for brevity
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations.
- **Space Complexity:** `O(N)` for storing elements.
