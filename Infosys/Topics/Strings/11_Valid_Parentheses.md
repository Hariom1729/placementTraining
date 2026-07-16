# Valid Parentheses

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Google, Facebook, Bloomberg

## Topic
Strings / Stack

## Pattern
Stack Matching

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Input
- `s` string.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([)]"
Output: false
Explanation: The square bracket is closed before the inner parenthesis is closed.
```

## Edge Cases
- String with an odd length (can never be valid, return false immediately).
- String starting with a closing bracket `")"`.
- String ending with an opening bracket `"("`.
- All opening brackets `"(((("`.

## Intuition
This is the quintessential **Stack** problem.
When we see an **open** bracket, we expect it to be closed *later*. Because brackets can be nested `{[()]}`, the MOST RECENTLY opened bracket must be the FIRST one to be closed. This Last-In-First-Out (LIFO) behavior perfectly matches a Stack!

Every time we see an open bracket `(`, `{`, `[`, we push it onto the stack.
Every time we see a close bracket `)`, `}`, `]`, we check the top of the stack:
- If the stack is empty, it means there is no matching open bracket! (Invalid).
- If the top of the stack is the *correct* matching open bracket, great! We pop it off.
- If it's a different type of open bracket (e.g. we see `]` but the top is `(`), the order is wrong! (Invalid).

At the end of the string, if the stack is fully empty, all brackets were perfectly matched. If there are still open brackets left inside, they were never closed (Invalid).

## Brute Force Approach
**Explanation:** Continually use `string::find` and `string::replace` to remove all instances of `"()"`, `"[]"`, and `"{}"` until the string stops shrinking. If it's empty, return true.
**Time Complexity:** $O(N^2 / 2)$ (String shifting takes $O(N)$ and we do it $N/2$ times).
**Space Complexity:** $O(N)$ for string modifications.

## Optimal Approach (Stack)
**Detailed explanation:**
1. Check if `s.length() % 2 != 0`. If odd, return `false`.
2. Initialize `stack<char> st`.
3. Iterate through each character `c` in `s`:
   - If `c == '(' || c == '{' || c == '['`: 
     - Push to stack: `st.push(c)`.
   - Else (it's a closing bracket):
     - If stack is empty, return `false` (Nothing to match with).
     - Let `top = st.top()`.
     - Check for a match: 
       - `c == ')' && top == '('`
       - `c == '}' && top == '{'`
       - `c == ']' && top == '['`
     - If it matches, `st.pop()`.
     - If it doesn't match, return `false`.
4. After the loop, return `st.empty()`.

**Time Complexity:** $O(N)$ because we iterate through the string exactly once, and stack `push`/`pop` operations take $O(1)$.
**Space Complexity:** $O(N)$ worst-case for the stack (e.g. all open brackets `((((((( `).

## C++ Solution

```cpp
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // If string length is odd, it's impossible to have balanced pairs
        if (s.length() % 2 != 0) {
            return false;
        }
        
        stack<char> st;
        
        for (char c : s) {
            // Push open brackets onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // Handle closing brackets
            else {
                // If stack is empty, there is no corresponding open bracket
                if (st.empty()) {
                    return false;
                }
                
                char top = st.top();
                
                // Check if the current closing bracket matches the top opening bracket
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false; // Mismatched types (e.g., '(]')
                }
            }
        }
        
        // If the stack is empty, all brackets were matched.
        // If it's not empty, there are unclosed brackets (e.g., '((()').
        return st.empty();
    }
};
```

## Dry Run
`s = "([)]"`
- `c = '('`: push `(`. Stack: `['(']`
- `c = '['`: push `[`. Stack: `['(', '[']`
- `c = ')'`: Stack is not empty. Top is `[`.
  - Is `)` a match for `[`? No.
  - Returns `false`.

`s = "()[]{}"`
- `c = '('`: push `(`. Stack: `['(']`
- `c = ')'`: Top is `(`. Matches! Pop. Stack: `[]`
- `c = '['`: push `[`. Stack: `['[']`
- `c = ']'`: Top is `[`. Matches! Pop. Stack: `[]`
- `c = '{'`: push `{`. Stack: `['{']`
- `c = '}'`: Top is `{`. Matches! Pop. Stack: `[]`
- Loop ends. Stack is empty. Return `true`.

## Common Mistakes
- **Returning `true` simply when the loop finishes:** You MUST return `st.empty()`. If the input is `"("`, the loop finishes without error, but the bracket was never closed!
- **Not checking if the stack is empty before calling `st.top()`:** If the input is `")"`, calling `st.top()` on an empty stack triggers a **Segmentation Fault** (Undefined Behavior in C++). Always check `st.empty()` first.

## Similar Problems
- Generate Parentheses
- Minimum Remove to Make Valid Parentheses
- Valid Parenthesis String
