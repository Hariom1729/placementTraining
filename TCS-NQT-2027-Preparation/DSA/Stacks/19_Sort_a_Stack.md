# Sort a Stack

## Problem Statement
Given a stack, sort it such that the top of the stack has the greatest element. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).

**Example:**
- **Input:** `[34, 3, 31, 98, 92, 23]` (where 23 is top)
- **Output:** `[3, 23, 31, 34, 92, 98]` (where 98 is top)

## Optimal Approach (Using Temporary Stack)
Create a temporary stack. While the original stack is not empty, pop the top element. While the temporary stack is not empty and its top is greater than the popped element, pop from the temporary stack and push back to the original stack. Push the popped element to the temporary stack.

### C++ Code
```cpp
#include <iostream>
#include <stack>
using namespace std;

void sortStack(stack<int>& input) {
    stack<int> tmpStack;
    
    while (!input.empty()) {
        int temp = input.top();
        input.pop();
        
        while (!tmpStack.empty() && tmpStack.top() > temp) {
            input.push(tmpStack.top());
            tmpStack.pop();
        }
        
        tmpStack.push(temp);
    }
    
    // tmpStack is now sorted with smallest at bottom. Transfer back.
    while(!tmpStack.empty()) {
        input.push(tmpStack.top());
        tmpStack.pop();
    }
}

int main() {
    stack<int> input;
    input.push(34); input.push(3); input.push(31);
    input.push(98); input.push(92); input.push(23);
    
    sortStack(input);
    
    while(!input.empty()) {
        cout << input.top() << " ";
        input.pop();
    }
    // Output: 98 92 34 31 23 3
    return 0;
}
```

### Complexity
- **Time Complexity:** $O(N^2)$ in the worst case (when the stack is sorted in reverse order).
- **Space Complexity:** $O(N)$ for the temporary stack.
