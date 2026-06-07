# Problem 10: Implement Queue using Stacks

## Problem Statement
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

## Constraints
- You must use only standard operations of a stack (`push`, `top`, `pop`, `size`, `empty`).
- `1 <= x <= 9`
- `pop` and `peek` will only be called on non-empty queues.

---

## Approach: Amortized O(1) Pop/Peek

We use two stacks: `input` and `output`.
The basic idea is that a stack reverses order. If we push elements into a stack and then pop them into another stack, the order gets reversed twice, bringing it back to the original order (FIFO).

1. **Push(x):** Simply push `x` to the `input` stack. (Time Complexity: `O(1)`)
2. **Pop() / Peek():** 
   - If the `output` stack is empty, we pop all elements from the `input` stack and push them into the `output` stack. This reverses their order.
   - Now, the top of the `output` stack is the oldest element (the front of the queue).
   - Return (and remove, if `pop`) the top of the `output` stack.
   - Amortized Time Complexity: `O(1)` (because each element is moved between stacks at most once).

---

## C++ Solution

```cpp
#include <iostream>
#include <stack>
using namespace std;

class MyQueue {
private:
    stack<int> input;
    stack<int> output;

public:
    MyQueue() {}
    
    void push(int x) {
        input.push(x);
    }
    
    int pop() {
        peek(); // Ensure output stack has elements
        int frontElement = output.top();
        output.pop();
        return frontElement;
    }
    
    int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }
    
    bool empty() {
        return input.empty() && output.empty();
    }
};

int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    
    cout << "Peek: " << q.peek() << endl; // Expected: 1
    cout << "Pop: " << q.pop() << endl;   // Expected: 1
    cout << "Empty? " << (q.empty() ? "Yes" : "No") << endl; // Expected: No
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** 
  - `push(x)`: `O(1)`.
  - `pop()`, `peek()`: Amortized `O(1)`. Worst case `O(N)` when `output` is empty.
- **Space Complexity:** `O(N)` to store the elements across two stacks.
