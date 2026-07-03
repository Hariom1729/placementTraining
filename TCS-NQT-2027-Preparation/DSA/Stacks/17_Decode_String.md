# Decode String

## Problem Statement
Given an encoded string, return its decoded string.
The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

**Example:**
- **Input:** s = "3[a]2[bc]"
- **Output:** "aaabcbc"
- **Explanation:** 'a' is repeated 3 times, 'bc' is repeated 2 times.

## Optimal Approach (Two Stacks)
Use one stack for numbers (repeat counts) and another stack for strings.
When encountering `[`, push the current number and current string to their respective stacks and reset them.
When encountering `]`, pop the repeat count, multiply the current string by it, and append it to the string popped from the string stack.

### C++ Code
```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

string decodeString(string s) {
    stack<int> numStack;
    stack<string> strStack;
    string currentString = "";
    int currentNum = 0;
    
    for (char c : s) {
        if (isdigit(c)) {
            currentNum = currentNum * 10 + (c - '0');
        } else if (isalpha(c)) {
            currentString += c;
        } else if (c == '[') {
            numStack.push(currentNum);
            strStack.push(currentString);
            currentNum = 0;
            currentString = "";
        } else if (c == ']') {
            int k = numStack.top(); numStack.pop();
            string decodedString = strStack.top(); strStack.pop();
            
            for (int i = 0; i < k; i++) {
                decodedString += currentString;
            }
            currentString = decodedString;
        }
    }
    return currentString;
}

int main() {
    cout << decodeString("3[a2[c]]") << endl; // Output: accaccacc
    return 0;
}
```

### Complexity
- **Time Complexity:** $O(N \times K)$, where $N$ is the length of the string and $K$ is the maximum repeat count.
- **Space Complexity:** $O(N)$ for the stacks.
