# Problem 9: String to Integer (atoi)

## Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm is as follows:
1. **Read in and ignore any leading whitespace.**
2. **Check if the next character is `'-'` or `'+'`.** Read this character in if it is either. This determines if the final result is negative or positive respectively.
3. **Read in next the characters until the next non-digit character or the end of the input is reached.**
4. **Convert these digits into an integer**. If no digits were read, then the integer is `0`.
5. **If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer** so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.

## Input Format
- A single string `s`.

## Output Format
- An integer.

## Constraints
- `0 <= s.length <= 200`
- `s` consists of English letters, digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

---

## Approach

This problem is a pure implementation problem. You just need to follow the rules exactly as written, being very careful with integer overflow.
1. Trim leading whitespace. Handle empty string cases.
2. Track the sign. Check index 0 for `+` or `-`.
3. Iterate through the string. Stop when a non-digit is encountered (`!isdigit()`).
4. Build the number: `result = result * 10 + (c - '0')`.
5. Check for overflow *before* multiplying by 10 using `INT_MAX / 10`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <climits>
#include <cctype>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int n = s.length();
        int i = 0;
        int sign = 1;
        int result = 0;
        
        // 1. Ignore leading whitespaces
        while (i < n && s[i] == ' ') {
            i++;
        }
        
        if (i == n) return 0;
        
        // 2. Determine sign
        if (s[i] == '-' || s[i] == '+') {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        
        // 3. Convert digits and handle overflow
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';
            
            // Overflow check
            // If result > INT_MAX / 10, then result * 10 will surely overflow.
            // If result == INT_MAX / 10, then result * 10 + digit will overflow if digit > 7
            // (since INT_MAX is 2147483647).
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        return result * sign;
    }
};

int main() {
    Solution sol;
    cout << sol.myAtoi("42") << endl;              // Expected: 42
    cout << sol.myAtoi("   -42") << endl;          // Expected: -42
    cout << sol.myAtoi("4193 with words") << endl; // Expected: 4193
    cout << sol.myAtoi("words and 987") << endl;   // Expected: 0
    cout << sol.myAtoi("-91283472332") << endl;    // Expected: -2147483648
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We process each character at most once.
- **Space Complexity:** `O(1)`. We only use a few primitive variables.
