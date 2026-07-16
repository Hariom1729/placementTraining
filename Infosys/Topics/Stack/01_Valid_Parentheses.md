# Valid Parentheses

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Year: 2021, 2023
Frequency: Very High

---

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Input Format
- A single string `s`.

---

## Optimal Approach (Using Stack)
**Detailed explanation:**
Iterate through the string.
- If we encounter an opening bracket `(`, `{`, or `[`, we push it onto the stack.
- If we encounter a closing bracket `)`, `}`, or `]`, we check the top of the stack.
  - If the stack is empty, it's invalid (no opening bracket for this closing bracket).
  - If the top of the stack is the corresponding opening bracket, we pop it.
  - If it is a different opening bracket, it's invalid.
- At the end, if the stack is completely empty, it's valid.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for the stack.

---

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
            if (st.empty()) return false;
            
            char top = st.top();
            if ((c == ')' && top == '(') ||
                (c == '}' && top == '{') ||
                (c == ']' && top == '[')) {
                st.pop();
            } else {
                return false; // Mismatched brackets
            }
        }
    }
    
    return st.empty();
}
```

---

## Common Mistakes
- **Not checking `st.empty()` at the end:** The string `"((("` will not trigger any mismatch logic, but it is invalid because brackets are left unclosed. You must return `st.empty()`.

---

## Pattern Recognition
**Identify this when:** You need to parse hierarchical or nested structures. Stacks are the fundamental DS for any LIFO (Last In, First Out) pairing problem.
