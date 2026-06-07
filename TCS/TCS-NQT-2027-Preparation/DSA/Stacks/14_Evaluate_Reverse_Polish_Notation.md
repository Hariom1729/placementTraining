# Problem 14: Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation (Postfix Notation).
Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.
Division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid.

## Input Format
- An array of strings `tokens`.

## Output Format
- An integer representing the evaluated result.

## Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator or an integer in the range `[-200, 200]`.

---

## Approach

Postfix evaluation is a textbook stack problem.
1. Iterate through the `tokens`.
2. If the token is a number, push it onto the stack (convert string to integer using `stoi`).
3. If the token is an operator:
   - Pop the top two elements from the stack. Let the first popped be `num2` and the second popped be `num1`.
   - Perform the operation: `num1 [operator] num2`.
   - Push the result back onto the stack.
4. Finally, the stack will contain exactly one element, which is the answer.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st; // Use long long to prevent overflow during intermediate steps
        
        for (string token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                long long num2 = st.top(); st.pop();
                long long num1 = st.top(); st.pop();
                
                if (token == "+") st.push(num1 + num2);
                else if (token == "-") st.push(num1 - num2);
                else if (token == "*") st.push(num1 * num2);
                else if (token == "/") st.push(num1 / num2);
            } else {
                st.push(stoll(token));
            }
        }
        
        return st.top();
    }
};

int main() {
    Solution sol;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << "Result: " << sol.evalRPN(tokens) << endl; // Expected: 9 ((2+1)*3)
    
    vector<string> tokens2 = {"4", "13", "5", "/", "+"};
    cout << "Result: " << sol.evalRPN(tokens2) << endl; // Expected: 6 (4 + (13/5))
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of tokens.
- **Space Complexity:** `O(N)` for the stack.
