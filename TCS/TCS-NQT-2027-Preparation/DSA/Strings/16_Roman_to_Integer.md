# Problem 16: Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
| :--- | :--- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

For example, `2` is written as `II` in Roman numeral. `12` is written as `XII`.

Given a roman numeral, convert it to an integer.

## Input Format
- A string `s` representing a valid roman numeral.

## Output Format
- An integer.

## Constraints
- `1 <= s.length <= 15`
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.

---

## Approach

1. Use an `unordered_map` to map each Roman character to its integer value.
2. Traverse the string from left to right.
3. For each character, check the value of the *next* character (if it exists).
4. **Subtraction Rule:** If the current character's value is *less* than the next character's value, it means this is a subtractive combination (like `IV`). We subtract the current character's value from the total sum.
5. **Addition Rule:** Otherwise, we add the current character's value to the total sum.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // Map to store Roman numerals and their integer values
        unordered_map<char, int> map = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        int result = 0;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            // Get value of current Roman numeral
            int currentValue = map[s[i]];
            
            // Check if there is a next numeral and if it's strictly greater
            if (i + 1 < n && currentValue < map[s[i + 1]]) {
                // Subtraction case
                result -= currentValue;
            } else {
                // Normal addition case
                result += currentValue;
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.romanToInt("III") << endl;     // Expected: 3
    cout << sol.romanToInt("LVIII") << endl;   // Expected: 58
    cout << sol.romanToInt("MCMXCIV") << endl; // Expected: 1994
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string `s`. The maximum length is 15, so this effectively runs in `O(1)` constant time.
- **Space Complexity:** `O(1)`. We use an unordered_map with exactly 7 key-value pairs, which takes a tiny, constant amount of memory.
