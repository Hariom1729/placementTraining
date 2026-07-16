# Roman to Integer

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Apple, Google

## Topic
Strings / Hash Table / Math

## Pattern
Left-to-Right Scan with Lookahead

## Problem Statement
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D` and `M`.
Given a roman numeral, convert it to an integer.

## Constraints
- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.

## Input
- `s` string.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Edge Cases
- Subtractive notation combinations: `IV (4)`, `IX (9)`, `XL (40)`, `XC (90)`, `CD (400)`, `CM (900)`.

## Intuition
Normally, Roman numerals are written largest to smallest from left to right (e.g., `VI` is `5 + 1 = 6`).
However, when a smaller numeral appears BEFORE a larger numeral, it means subtraction (e.g., `IV` is `5 - 1 = 4`).
This gives us an incredibly simple algorithm:
1. Map all characters to their integer values using a Hash Map (or switch statement).
2. Read the string from left to right.
3. Compare the current character's value to the NEXT character's value.
4. If `value(current) < value(next)`, we subtract `value(current)` from our total! (This handles `I` before `V`).
5. Else, we add `value(current)` to our total!

## Brute Force Approach
N/A - Parsing algorithm is $O(N)$ anyway.

## Optimal Approach (Hash Map + Lookahead)
**Detailed explanation:**
1. Create a function or unordered_map `roman` that maps `'I'`->1, `'V'`->5, `'X'`->10, etc.
2. Initialize `total = 0`.
3. Loop `i` from `0` to `s.length() - 1`:
   - If `i + 1 < s.length()` and `roman[s[i]] < roman[s[i+1]]`:
     - `total -= roman[s[i]]`
   - Else:
     - `total += roman[s[i]]`
4. Return `total`.

*Optimization:* Instead of `unordered_map`, using a switch statement or an array `vector<int> roman(256)` indexed by character is much faster in C++.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // Flat array for ultra-fast lookup (ASCII character indexing)
        vector<int> roman(256, 0);
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;
        
        int total = 0;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            // If the current value is less than the next value, subtract it
            if (i + 1 < n && roman[s[i]] < roman[s[i + 1]]) {
                total -= roman[s[i]];
            } 
            // Otherwise, add it
            else {
                total += roman[s[i]];
            }
        }
        
        return total;
    }
};
```

## Dry Run
`s = "MCMXCIV"`
- `i=0 ('M')`: `roman['M'] = 1000`. Next is `'C'` (100). `1000 >= 100`. Add 1000. `total = 1000`.
- `i=1 ('C')`: `roman['C'] = 100`. Next is `'M'` (1000). `100 < 1000`. Subtract 100. `total = 900`.
- `i=2 ('M')`: `roman['M'] = 1000`. Next is `'X'` (10). `1000 >= 10`. Add 1000. `total = 1900`.
- `i=3 ('X')`: `roman['X'] = 10`. Next is `'C'` (100). `10 < 100`. Subtract 10. `total = 1890`.
- `i=4 ('C')`: `roman['C'] = 100`. Next is `'I'` (1). `100 >= 1`. Add 100. `total = 1990`.
- `i=5 ('I')`: `roman['I'] = 1`. Next is `'V'` (5). `1 < 5`. Subtract 1. `total = 1989`.
- `i=6 ('V')`: `roman['V'] = 5`. No next element. Add 5. `total = 1994`.
Result: 1994.

## Common Mistakes
- **Checking exact subtractive pairs like `if (s[i]=='I' && s[i+1]=='V')`:** Writing 6 specific `if-else` branches works, but is extremely bloated and error-prone. The logic `roman[s[i]] < roman[s[i+1]]` perfectly covers every valid subtractive case dynamically.

## Similar Problems
- Integer to Roman
