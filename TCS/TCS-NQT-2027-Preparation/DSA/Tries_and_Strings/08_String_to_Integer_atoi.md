# Problem 8: String to Integer (atoi)

## Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.
The algorithm for `myAtoi(string s)` is as follows:
1. **Whitespace:** Ignore any leading whitespace (`" "`).
2. **Signedness:** Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
3. **Conversion:** Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. **Rounding:** If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.
Return the integer as the final result.

## Constraints
- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

---

## Approach: State Machine / Iterative Parsing

The problem is straightforward but requires careful handling of edge cases (overflows, leading spaces, signs).

1. Initialize index `i = 0`, `sign = 1`, `result = 0`.
2. Skip leading spaces.
3. Check for `+` or `-` sign. Update `sign` accordingly and increment `i`.
4. While `i < s.length()` and `s[i]` is a digit (`s[i] >= '0' && s[i] <= '9'`):
   - Check for overflow **BEFORE** multiplying `result` by 10.
   - If `result > INT_MAX / 10` OR `(result == INT_MAX / 10 && (s[i] - '0') > 7)`:
     - Return `INT_MAX` if `sign == 1`.
     - Return `INT_MIN` if `sign == -1`.
   - Update `result = result * 10 + (s[i] - '0')`.
   - Increment `i`.
5. Return `result * sign`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        int n = s.length();
        int sign = 1;
        int result = 0;
        
        // 1. Skip leading whitespaces
        while (i < n && s[i] == ' ') {
            i++;
        }
        
        // 2. Check for sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        
        // 3. Process digits
        while (i < n && s[i] >= '0' && s[i] <= '9') {
            int digit = s[i] - '0';
            
            // 4. Check for overflow
            // INT_MAX = 2147483647
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
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
    cout << "Result: " << sol.myAtoi("42") << endl;            // Expected: 42
    cout << "Result: " << sol.myAtoi("   -42") << endl;        // Expected: -42
    cout << "Result: " << sol.myAtoi("4193 with words") << endl; // Expected: 4193
    cout << "Result: " << sol.myAtoi("-91283472332") << endl;    // Expected: -2147483648 (INT_MIN)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string.
- **Space Complexity:** `O(1)` as we only use a few integer variables.
