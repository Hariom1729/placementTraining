# Zigzag Conversion

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Strings

## Pattern
Simulation / Index Mapping

## Problem Statement
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`
Write the code that will take a string and make this conversion given a number of rows.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

## Input
- `s` string.
- `numRows` integer.

## Output
- Return the converted string.

## Sample Test Cases

**Example 1:**
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**
```
Input: s = "A", numRows = 1
Output: "A"
```

## Edge Cases
- `numRows == 1` or `numRows >= s.length()`. The zigzag pattern never turns. Return `s` directly.

## Intuition
Instead of mathematically calculating the exact index jumps for each row (which is highly complicated and error-prone), we can simply **simulate** the writing process!
We can create an array of strings, where each string represents a single row.
We iterate through the input string `s` character by character, and place the character in the correct row string.
To do this, we maintain a `currRow` index, and a `direction` flag (going DOWN or going UP).
- We start at row 0, going DOWN.
- When we hit the bottom row (`numRows - 1`), we change direction to UP.
- When we hit the top row (`0`), we change direction to DOWN.
After we process the entire string, we simply concatenate all the row strings together!

## Brute Force Approach
N/A - This is an implementation simulation.

## Optimal Approach (Row Simulation)
**Detailed explanation:**
1. If `numRows == 1` or `numRows >= s.length()`, return `s`.
2. Create `vector<string> rows(min(numRows, (int)s.length()))`.
3. Initialize `currRow = 0` and `goingDown = false`.
4. Iterate through `s`:
   - Append the character to `rows[currRow]`.
   - If `currRow == 0` or `currRow == numRows - 1`, flip the direction: `goingDown = !goingDown`.
   - Update `currRow`: If `goingDown` is true, `currRow++`. Else `currRow--`.
5. Combine all rows: `string ans = ""; for(string row : rows) ans += row;`.
6. Return `ans`.

**Time Complexity:** $O(N)$ where $N$ is the length of `s`. We visit each character exactly once.
**Space Complexity:** $O(N)$ to store the rows.

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        // Edge cases where zigzag doesn't change the string
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        
        // Array to hold the string for each row
        vector<string> rows(min(numRows, int(s.length())));
        
        int currRow = 0;
        bool goingDown = false;
        
        // Traverse the string
        for (char c : s) {
            rows[currRow] += c;
            
            // Flip direction if we hit the top or bottom row
            if (currRow == 0 || currRow == numRows - 1) {
                goingDown = !goingDown;
            }
            
            // Move to the next row
            currRow += goingDown ? 1 : -1;
        }
        
        // Concatenate all rows
        string result = "";
        for (const string& row : rows) {
            result += row;
        }
        
        return result;
    }
};
```

## Dry Run
`s = "PAYPAL", numRows = 3`
- `rows = ["", "", ""]`
- `currRow = 0, goingDown = false`.
- `'P'`: `rows[0] = "P"`. `currRow == 0` -> `goingDown = true`. `currRow = 1`.
- `'A'`: `rows[1] = "A"`. `currRow` is 1. `currRow = 2`.
- `'Y'`: `rows[2] = "Y"`. `currRow == 2` -> `goingDown = false`. `currRow = 1`.
- `'P'`: `rows[1] = "AP"`. `currRow` is 1. `currRow = 0`.
- `'A'`: `rows[0] = "PA"`. `currRow == 0` -> `goingDown = true`. `currRow = 1`.
- `'L'`: `rows[1] = "APL"`. `currRow = 2`.
- Result: `rows[0] + rows[1] + rows[2]` = `"PA" + "APL" + "Y"` = `"PAAPLY"`.

## Common Mistakes
- **Complicated Mathematical Jumps:** Trying to solve this using math formulas (like jumping `2 * numRows - 2` characters) is technically $O(1)$ space, but takes 3x longer to write, is intensely difficult to debug, and is completely unnecessary for an interview unless specifically asked for $O(1)$ space. The simulation method is universally preferred for its elegance.

## Similar Problems
- Text Justification
- Spiral Matrix
