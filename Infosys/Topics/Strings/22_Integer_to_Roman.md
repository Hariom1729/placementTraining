# Integer to Roman

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Apple, Bloomberg

## Topic
Strings / Math

## Pattern
Greedy / Hash Table

## Problem Statement
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D` and `M`.
- `I = 1`, `V = 5`, `X = 10`, `L = 50`, `C = 100`, `D = 500`, `M = 1000`.

There are six instances where subtraction is used:
- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer `num`, convert it to a roman numeral.

## Constraints
- `1 <= num <= 3999`

## Input
- `num` integer.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
```

**Example 2:**
```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 3:**
```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Edge Cases
- Exact values like 4, 9, 40, 90, 400, 900.

## Intuition
Roman numerals are essentially a **Greedy** algorithm system. 
To represent a number, you always want to use the LARGEST possible symbol first.
For example, to represent 3000, you use `M` (1000) three times. You don't use `D` six times.
The only complication is the subtraction instances (4, 9, 40, 90, etc.).
We can completely eliminate this complication by simply **hardcoding** those 6 special instances into our list of available symbols!
Available symbols (sorted largest to smallest):
`1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"`.

With this complete list, the algorithm is trivial:
Loop through the list from largest to smallest. While our `num` is greater than or equal to the current symbol's value, we subtract the value from `num` and append the symbol to our answer string.

## Brute Force Approach
N/A - Hardcoding if-else statements for every decimal place is tedious. The array mapping is the standard solution.

## Optimal Approach (Greedy Array Mapping)
**Detailed explanation:**
1. Define an array of values `val = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}`.
2. Define a corresponding array of strings `sym = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}`.
3. Initialize an empty string `ans = ""`.
4. Iterate `i` from `0` to `12` (size of array):
   - `while (num >= val[i])`:
     - `num -= val[i]`
     - `ans += sym[i]`
5. Return `ans`.

**Time Complexity:** $O(1)$ because the loop runs at most 13 times, and the inner while loop runs at most 3 times per value (since numbers are up to 3999). Total operations are capped by a small constant.
**Space Complexity:** $O(1)$ constant space for the mapping arrays.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        // Define all Roman numerals and their values, including subtractive combinations
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        string roman = "";
        
        // Greedily subtract the largest possible value
        for (int i = 0; i < 13; i++) {
            while (num >= values[i]) {
                num -= values[i];
                roman += symbols[i];
            }
        }
        
        return roman;
    }
};
```

## Dry Run
`num = 1994`
- `i=0` (1000, "M"): `1994 >= 1000`. `num = 994`. `roman = "M"`.
- `i=1` (900, "CM"): `994 >= 900`. `num = 94`. `roman = "MCM"`.
- `i=2` to `i=4` (500, 400, 100): All skipped.
- `i=5` (90, "XC"): `94 >= 90`. `num = 4`. `roman = "MCMXC"`.
- `i=6` to `i=10`: All skipped.
- `i=11` (4, "IV"): `4 >= 4`. `num = 0`. `roman = "MCMXCIV"`.
- Loop finishes as `num` is 0.
- Result: `"MCMXCIV"`.

## Common Mistakes
- **Using an `unordered_map`:** Hash maps are unordered by definition! If you try to loop through an `unordered_map`, you won't get the values from largest to smallest. You MUST use a parallel array or a `vector<pair<int, string>>` to maintain the strict descending order.

## Similar Problems
- Roman to Integer
- Integer to English Words
