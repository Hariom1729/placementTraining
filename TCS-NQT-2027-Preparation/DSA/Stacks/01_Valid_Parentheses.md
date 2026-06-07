# Problem 1: Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Input Format
- A string `s`.

## Output Format
- A boolean representing whether the string is valid.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only.

---

## Approach

This is the most classic stack problem.
1. Create a `stack<char>`.
2. Iterate through each character `c` in the string `s`.
3. If `c` is an opening bracket (`(`, `{`, `[`), push it onto the stack.
4. If `c` is a closing bracket (`)`, `}`, `]`):
   - If the stack is empty, there is no corresponding opening bracket. Return `false`.
   - Pop the top character from the stack.
   - If the popped character does not match the type of the closing bracket (e.g., popped `(` but current is `}`), return `false`.
5. After the loop, if the stack is not empty, it means there are unmatched opening brackets left. Return `false`. Otherwise, return `true`.

---

## C++ Solution

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        
        for (char c : s) {
            // Push opening brackets
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // Handle closing brackets
            else {
                if (st.empty()) return false;
                
                char top = st.top();
                st.pop();
                
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        
        // If stack is empty, all brackets were matched
        return st.empty();
    }
};

int main() {
    Solution sol;
    
    cout << "is \"()[]{}\" valid? " << (sol.isValid("()[]{}") ? "True" : "False") << endl; // Expected: True
    cout << "is \"(]\" valid? " << (sol.isValid("(]") ? "True" : "False") << endl; // Expected: False
    cout << "is \"([)]\" valid? " << (sol.isValid("([)]") ? "True" : "False") << endl; // Expected: False
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We process each character exactly once.
- **Space Complexity:** `O(N)` in the worst case (e.g., `((((((( `), all characters are pushed onto the stack.
