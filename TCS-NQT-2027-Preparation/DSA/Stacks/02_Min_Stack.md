# Problem 2: Min Stack

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.

---

## Approach

If we only use one stack, calling `getMin()` would require traversing the entire stack (`O(N)` time).
To achieve `O(1)` time, we can use a **secondary stack** to keep track of the minimums.

Let's call the main stack `s` and the minimum tracking stack `min_s`.
1. **Push(val):** 
   - Push `val` to `s`.
   - If `min_s` is empty or `val` is **less than or equal to** `min_s.top()`, push `val` to `min_s`.
2. **Pop():**
   - If `s.top()` is equal to `min_s.top()`, it means we are removing the current minimum. We must pop it from `min_s` as well.
   - Pop from `s`.
3. **Top():** Return `s.top()`.
4. **getMin():** Return `min_s.top()`.

*(Alternatively, you can store `pair<int, int>` in a single stack where `first` is the value and `second` is the current minimum up to that point).*

---

## C++ Solution

```cpp
#include <iostream>
#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> s;
    stack<int> min_s;

public:
    MinStack() {
    }
    
    void push(int val) {
        s.push(val);
        // Push to min stack if it's empty or the new value is a new minimum
        if (min_s.empty() || val <= min_s.top()) {
            min_s.push(val);
        }
    }
    
    void pop() {
        // If the element being removed is the current minimum, remove it from min stack too
        if (s.top() == min_s.top()) {
            min_s.pop();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min_s.top();
    }
};

int main() {
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    
    cout << "Minimum: " << minStack.getMin() << endl; // Expected: -3
    
    minStack.pop();
    
    cout << "Top: " << minStack.top() << endl;       // Expected: 0
    cout << "Minimum: " << minStack.getMin() << endl; // Expected: -2
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(1)` for all operations.
- **Space Complexity:** `O(N)` to maintain the secondary stack.
