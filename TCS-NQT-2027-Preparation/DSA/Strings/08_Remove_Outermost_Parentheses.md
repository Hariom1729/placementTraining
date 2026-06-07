# Problem 8: Remove Outermost Parentheses

## Problem Statement
A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings.
Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings (cannot be split further).

Return `s` after removing the outermost parentheses of every primitive string in the primitive decomposition of `s`.

## Input Format
- A single string `s` representing a valid parentheses string.

## Output Format
- A string with the outermost parentheses removed.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.

---

## Approach

This is a classic problem that tests logic using a counter variable instead of explicitly needing a Stack.
1. Use an integer variable `openCount` to track the nesting depth of parentheses.
2. Initialize an empty `string result` to build the answer.
3. Iterate through the string `s`.
   - If the current character is `'('`:
     - If `openCount > 0`, it means this is NOT an outermost parenthesis. Append it to `result`.
     - Increment `openCount`.
   - If the current character is `')'`:
     - Decrement `openCount`.
     - If `openCount > 0`, it means this is NOT an outermost parenthesis. Append it to `result`.
4. Return the `result` string.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string removeOuterParentheses(string s) {
        string result = "";
        int openCount = 0;
        
        for (char c : s) {
            if (c == '(') {
                // If openCount is greater than 0, it's not the outermost '('
                if (openCount > 0) {
                    result += c;
                }
                openCount++;
            } else if (c == ')') {
                openCount--;
                // If openCount is greater than 0, it's not the outermost ')'
                if (openCount > 0) {
                    result += c;
                }
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.removeOuterParentheses("(()())(())") << endl;         // Expected: "()()()"
    cout << sol.removeOuterParentheses("(()())(())(()(()))") << endl; // Expected: "()()()()(())"
    cout << sol.removeOuterParentheses("()()") << endl;               // Expected: ""
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We iterate through the string exactly once. Appending to a `std::string` is an `O(1)` amortized operation in C++.
- **Space Complexity:** `O(N)` to store the resulting string. The auxiliary space is `O(1)` since we only use a single integer variable `openCount`.
