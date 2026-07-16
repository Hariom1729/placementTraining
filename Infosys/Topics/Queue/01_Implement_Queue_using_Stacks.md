# Implement Queue using Stacks

## Difficulty
Easy

## Asked In
Infosys SP
Frequency: Medium

---

## Problem Statement
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

---

## Optimal Approach (Amortized $O(1)$)
**Detailed explanation:**
We use two stacks: `s1` (for input) and `s2` (for output).
- **Push:** Always push to `s1`. (Time: $O(1)$)
- **Pop/Peek:** If `s2` is empty, pop everything from `s1` and push to `s2`. This reverses the order, placing the oldest element at the top of `s2`. Then pop/peek from `s2`. (Amortized Time: $O(1)$).

**Complexity:**
- **Time Complexity:** Amortized $O(1)$ for operations.
- **Space Complexity:** $O(N)$ for storing elements.

---

## C++ Solution
```cpp
#include <stack>
using namespace std;

class MyQueue {
    stack<int> s1, s2;
public:
    MyQueue() {}
    
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        peek(); // Ensure s2 has elements
        int val = s2.top();
        s2.pop();
        return val;
    }
    
    int peek() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
};
```
