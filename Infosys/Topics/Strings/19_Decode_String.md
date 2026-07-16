# Decode String

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft, Bloomberg

## Topic
Strings / Stack

## Pattern
Two Stacks / Recursive Parsing

## Problem Statement
Given an encoded string, return its decoded string.
The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

## Constraints
- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.
- All the integers in `s` are in the range `[1, 300]`.

## Input
- `s` encoded string.

## Output
- Return the decoded string.

## Sample Test Cases

**Example 1:**
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2:**
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
Explanation: The nested structure requires decoding from the inside out: a2[c] -> acc -> 3[acc] -> accaccacc.
```

**Example 3:**
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Edge Cases
- Nested brackets (e.g., `2[2[b]]`). Handled elegantly by the stack.
- Multi-digit numbers (e.g., `100[a]`). Must parse the number sequentially.

## Intuition
Because brackets can be **nested**, we must process the string from the "inside out". This Last-In-First-Out behavior strongly suggests a **Stack**.
Since we are tracking two different things—the string we are currently building, and the multiplier `k` for that string—we can use **two stacks**:
1. `countStack`: To store the multipliers (numbers).
2. `stringStack`: To store the previously built strings before we entered a new bracket.

As we iterate through the string:
- If we see a **digit**, we build the number `k` (since it might be multi-digit like `12`).
- If we see a **`[`**, it means we are entering a new nested scope. We MUST save our current progress!
  - Push the current `k` to `countStack`.
  - Push the `currentString` to `stringStack`.
  - Reset `k = 0` and `currentString = ""`.
- If we see a **letter**, we just append it to `currentString`.
- If we see a **`]`**, it means the current scope is finished!
  - We pop the multiplier `k` from `countStack`.
  - We duplicate our `currentString` `k` times.
  - We pop the previous string from `stringStack` and append our newly duplicated string to it. This combined string becomes our new `currentString`!

## Brute Force Approach
N/A - Parsing algorithm is required.

## Optimal Approach (Two Stacks)
**Detailed explanation:**
1. Initialize `stack<int> counts`, `stack<string> strings`.
2. Initialize `string currentString = ""` and `int k = 0`.
3. Loop through each character `c` in `s`:
   - If `isdigit(c)`: `k = k * 10 + (c - '0')`.
   - Else if `c == '['`:
     - Push `k` to `counts`.
     - Push `currentString` to `strings`.
     - Reset `k = 0`, `currentString = ""`.
   - Else if `c == ']'`:
     - Pop `repeatTimes` from `counts`.
     - Pop `prevString` from `strings`.
     - Build `temp = ""`. Add `currentString` to `temp` `repeatTimes` times.
     - `currentString = prevString + temp`.
   - Else (letter):
     - `currentString += c`.
4. Return `currentString`.

**Time Complexity:** $O(\text{Output Length})$. We iterate through the string once, but we might duplicate strings many times. The time is proportional to the size of the final decoded string.
**Space Complexity:** $O(\text{Output Length})$ for the stacks and building strings.

## C++ Solution

```cpp
#include <string>
#include <stack>
#include <cctype>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<int> countStack;
        stack<string> stringStack;
        
        string currentString = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                // Build the multi-digit number
                k = k * 10 + (c - '0');
            } 
            else if (c == '[') {
                // Push current state to stacks and reset
                countStack.push(k);
                stringStack.push(currentString);
                
                k = 0;
                currentString = "";
            } 
            else if (c == ']') {
                // Decode the current scope
                int repeatTimes = countStack.top();
                countStack.pop();
                
                string prevString = stringStack.top();
                stringStack.pop();
                
                // Duplicate the current string 'repeatTimes' times
                string temp = "";
                for (int i = 0; i < repeatTimes; i++) {
                    temp += currentString;
                }
                
                // Append the duplicated string to the previous string
                currentString = prevString + temp;
            } 
            else {
                // It's a normal character
                currentString += c;
            }
        }
        
        return currentString;
    }
};
```

## Dry Run
`s = "3[a2[c]]"`
- `3`: `k = 3`.
- `[`: push `k(3)` to `counts`, push `""` to `strings`. Reset `k=0`, `curr=""`.
- `a`: `curr = "a"`.
- `2`: `k = 2`.
- `[`: push `k(2)` to `counts`, push `"a"` to `strings`. Reset `k=0`, `curr=""`.
- `c`: `curr = "c"`.
- `]`:
  - `repeat = counts.pop() -> 2`
  - `prev = strings.pop() -> "a"`
  - `temp = "c" + "c" = "cc"`
  - `curr = prev + temp = "a" + "cc" = "acc"`.
- `]`:
  - `repeat = counts.pop() -> 3`
  - `prev = strings.pop() -> ""`
  - `temp = "acc" * 3 = "accaccacc"`
  - `curr = "" + "accaccacc" = "accaccacc"`.
- Loop ends. Return `"accaccacc"`.

## Common Mistakes
- **Failing to handle multi-digit multipliers:** Assuming `k` is always a single digit (e.g., `k = c - '0'`) will crash on inputs like `100[leetcode]`. You must use `k = k * 10 + (c - '0')`.
- **String reference invalidation:** When duplicating `currentString`, if you do `currentString += currentString`, you double it every loop iteration (exponential growth!). You must append it to an empty `temp` string, or properly track sizes.

## Similar Problems
- Evaluate Reverse Polish Notation
- Basic Calculator
