# Stacks

## 1. Theory & Core Concepts

A Stack is a linear data structure that follows a particular order in which operations are performed. The order is **LIFO (Last In First Out)** or **FILO (First In Last Out)**.

Imagine a stack of plates in a cafeteria: you can only take the top plate, and if you want to add a plate, you place it on the top.

### Key Operations in C++ STL (`std::stack`)
```cpp
#include <stack>
stack<int> st;

st.push(10); // Adds 10 to the top
st.top();    // Returns the top element (10), does not remove it. O(1) time.
st.pop();    // Removes the top element. Returns nothing. O(1) time.
st.empty();  // Returns true if stack is empty, false otherwise.
st.size();   // Returns the number of elements.
```

### Common Interview Patterns
1. **Parentheses Matching:** Checking for balanced brackets.
2. **Monotonic Stack:** A stack whose elements are monotonically increasing or decreasing. This is extremely important for finding the "Next Greater Element", "Next Smaller Element", or calculating areas in histograms.
3. **Tracking Minimum/Maximum:** Maintaining a secondary stack to track the min/max value at any given point in `O(1)` time.
4. **String Reversal / Evaluation:** Evaluating Postfix/Prefix expressions or simplifying file paths.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Valid_Parentheses.md`
*   `02_Min_Stack.md`
*   `03_Next_Greater_Element.md`
*   `04_Next_Greater_Element_II.md`
*   `05_Daily_Temperatures.md`
*   *(... and 10+ more)*
