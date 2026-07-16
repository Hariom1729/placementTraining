# String to Integer (atoi)

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Bloomberg, Apple

## Topic
Strings / Math

## Pattern
State Machine / Iterative Parsing

## Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:
1. **Whitespace:** Ignore any leading whitespace (`" "`).
2. **Signedness:** Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity is neither present.
3. **Conversion:** Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
4. **Rounding:** If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.

Return the integer as the final result.

## Constraints
- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

## Input
- `s` string.

## Output
- Return a 32-bit integer.

## Sample Test Cases

**Example 1:**
```
Input: s = "42"
Output: 42
```

**Example 2:**
```
Input: s = "   -042"
Output: -42
Explanation: Leading whitespace is ignored. Sign is '-'. Leading zeros are ignored.
```

**Example 3:**
```
Input: s = "1337c0d3"
Output: 1337
Explanation: Reading stops at 'c' because it is a non-digit.
```

**Example 4:**
```
Input: s = "0-1"
Output: 0
Explanation: Sign must be at the beginning. Reading stops at '-'.
```

**Example 5:**
```
Input: s = "words and 987"
Output: 0
Explanation: First non-whitespace character is 'w', which is a non-digit.
```

## Edge Cases
- Pure whitespace string `"   "`.
- Integer overflow: `"99999999999999999"`.
- Integer underflow: `"-9999999999999999"`.
- Multiple signs: `"+-12"` (Invalid, should return `0`).

## Intuition
This problem is an exercise in rigorous parsing and checking conditions in exact order.
We process the string character by character:
1. Skip all spaces using a `while` loop.
2. Check for an optional sign (`+` or `-`). Mark a `sign` variable.
3. Start parsing digits (`'0' <= c && c <= '9'`).
4. **The Overflow Check:** Before we multiply our current result by 10 and add the new digit, we MUST check if it will overflow the 32-bit integer limit `INT_MAX`.
   - If `result > INT_MAX / 10`, multiplying by 10 will definitely overflow.
   - If `result == INT_MAX / 10`, multiplying by 10 is fine, but adding a digit greater than `7` (since `INT_MAX` ends in 7: `2147483647`) will overflow!
   If overflow happens, we immediately return `INT_MAX` or `INT_MIN` depending on the sign.

## Brute Force Approach
N/A - This is purely an implementation problem.

## Optimal Approach (Sequential Parsing)
**Detailed explanation:**
1. Initialize `i = 0`, `sign = 1`, `result = 0`.
2. **Whitespace:** `while (i < n && s[i] == ' ') i++;`
3. **Sign:** If `i < n` and `s[i] == '+'` or `s[i] == '-'`:
   - Set `sign = (s[i] == '-') ? -1 : 1`.
   - `i++`.
4. **Digits:** While `i < n && isdigit(s[i])`:
   - int `digit = s[i] - '0'`.
   - **Check Overflow:**
     - `if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10))`:
       - Return `sign == 1 ? INT_MAX : INT_MIN`.
   - `result = result * 10 + digit`.
   - `i++`.
5. Return `result * sign`.

**Time Complexity:** $O(N)$ because we iterate through the string characters at most once.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
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
        
        // 2. Check for optional sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        
        // 3. Process digits and build the result
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';
            
            // 4. Check for overflow/underflow BEFORE multiplying by 10
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        return result * sign;
    }
};
```

## Dry Run
`s = "   -42"`
- `i = 0`: space, skip. `i=1`: space, skip. `i=2`: space, skip. `i=3`.
- `s[3] == '-'`: `sign = -1`, `i = 4`.
- `s[4] == '4'`: `digit = 4`. Overflow check passes. `result = 0 * 10 + 4 = 4`. `i = 5`.
- `s[5] == '2'`: `digit = 2`. Overflow check passes. `result = 4 * 10 + 2 = 42`. `i = 6`.
- `i=6 == n`. Loop ends.
- Return `42 * -1 = -42`.

Overflow check for `2147483648`:
- ... `result` reaches `214748364`. `digit = 8`.
- `result == INT_MAX / 10` is True. `digit > 7` is True (`8 > 7`).
- Overflow triggered! Returns `INT_MAX`.

## Common Mistakes
- **Multiplying by 10 then checking for overflow:** If you do `result = result * 10 + digit; if (result > INT_MAX)`, the overflow has *already occurred* in C++, causing Undefined Behavior and corrupted values! You MUST check mathematically if the next operation will overflow BEFORE doing it.
- **Using `long long` for result:** While using `long long result = 0;` and checking `if (result > INT_MAX)` works in many environments, some strict interviewers forbid it, stating "Assume the environment does not allow you to store 64-bit integers". The `INT_MAX / 10` approach is bulletproof and strictly adheres to 32-bit limits.

## Similar Problems
- Valid Number
- String to Integer (atoi) variants in C/C++ library (`stoi`).
