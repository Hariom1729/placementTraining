# Problem 9: Implement Stack using Queues

## Problem Statement
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

## Constraints
- You must use only standard operations of a queue (`push_back`, `peek/pop_front`, `size`, `empty`).
- `-9 <= x <= 9`
- `pop` and `top` will only be called on non-empty stacks.

---

## Approach: Single Queue (Optimal)

Although the problem says two queues, we can do it efficiently using just **one queue**.
The trick is to make the `push` operation expensive (`O(N)`) so that `pop` and `top` remain `O(1)`.

1. Initialize `queue<int> q`.
2. **Push(x):**
   - Push `x` to the back of the queue.
   - Let the previous size of the queue be `s`.
   - Pop `s` elements from the front of the queue and immediately push them back.
   - This effectively rotates the queue so that the newly inserted element `x` becomes the front of the queue (acting like the top of a stack).
3. **Pop():** Pop from the front.
4. **Top():** Return the front element.
5. **Empty():** Check if the queue is empty.

---

## C++ Solution

```cpp
#include <iostream>
#include <queue>
using namespace std;

class MyStack {
private:
    queue<int> q;

public:
    MyStack() {}
    
    void push(int x) {
        int s = q.size();
        q.push(x);
        
        // Rotate the previous elements to the back
        for (int i = 0; i < s; i++) {
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int topElement = q.front();
        q.pop();
        return topElement;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};

int main() {
    MyStack st;
    st.push(1);
    st.push(2);
    
    cout << "Top: " << st.top() << endl; // Expected: 2
    cout << "Pop: " << st.pop() << endl; // Expected: 2
    cout << "Empty? " << (st.empty() ? "Yes" : "No") << endl; // Expected: No
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** 
  - `push(x)`: `O(N)` where `N` is the current number of elements.
  - `pop()`, `top()`, `empty()`: `O(1)`.
- **Space Complexity:** `O(N)` for the queue.
