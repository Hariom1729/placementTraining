# Count and Say

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft

## Topic
Strings

## Pattern
Simulation / Recursive Sequence

## Problem Statement
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string `"3322251"`:
- Two 3's, three 2's, one 5, and one 1.
- `"23" + "32" + "15" + "11"`
- `"23321511"`

Given a positive integer `n`, return the $n^{th}$ term of the count-and-say sequence.

## Constraints
- `1 <= n <= 30`

## Input
- `n` integer.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: n = 1
Output: "1"
Explanation: This is the base case.
```

**Example 2:**
```
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

## Edge Cases
- `n = 1`. Directly returns `"1"`.

## Intuition
This is purely a **simulation** problem. 
Because `countAndSay(n)` strictly depends on `countAndSay(n-1)`, we must generate the sequence iteratively from $1$ up to $n$.
We start with `result = "1"`.
For step 2 to $n$, we take the current `result` and process it character by character to generate the *next* `result`.
To process the string:
We use a pointer `i = 0`. We count how many times the character `s[i]` repeats by iterating `j` until `s[j] != s[i]`.
The count is `j - i`. The character is `s[i]`.
We simply append `to_string(count) + s[i]` to our new string, and then update `i = j` to process the next distinct character group!

## Brute Force Approach
N/A - Simulation is the required approach.

## Optimal Approach (Iterative Simulation)
**Detailed explanation:**
1. If `n == 1`, return `"1"`.
2. Initialize `string result = "1"`.
3. Loop from `2` up to `n`:
   - Initialize `string nextResult = ""`.
   - `int i = 0`.
   - `while (i < result.length())`:
     - `int count = 1`.
     - `while (i + 1 < result.length() && result[i] == result[i + 1])`:
       - `i++`.
       - `count++`.
     - `nextResult += to_string(count) + result[i]`.
     - `i++`.
   - `result = nextResult`.
4. Return `result`.

**Time Complexity:** $O(\text{Length of Answer})$. The length of the string grows exponentially, but for $n=30$, the operations are perfectly within the 1-second limit.
**Space Complexity:** $O(\text{Length of Answer})$ to store the strings.

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        
        string result = "1";
        
        // Generate up to the nth term
        for (int step = 2; step <= n; step++) {
            string nextResult = "";
            int i = 0;
            
            while (i < result.length()) {
                int count = 1;
                
                // Count how many times the current character repeats
                while (i + 1 < result.length() && result[i] == result[i + 1]) {
                    count++;
                    i++;
                }
                
                // Append the count and the character
                nextResult += to_string(count) + result[i];
                
                // Move to the next completely different character
                i++;
            }
            
            result = nextResult;
        }
        
        return result;
    }
};
```

## Dry Run
`n = 4`
- `step = 2`:
  - `result = "1"`. `i = 0`.
  - While loop: `result[0] == result[1]`? (No, `1` out of bounds).
  - `nextResult` = `"1"` (count) + `"1"` (char) = `"11"`.
  - `result = "11"`.
- `step = 3`:
  - `result = "11"`. `i = 0`.
  - While loop: `result[0] == result[1]`? (Yes, `'1' == '1'`). `count = 2, i = 1`.
  - `nextResult` = `"2"` + `"1"` = `"21"`.
  - `result = "21"`.
- `step = 4`:
  - `result = "21"`.
  - `i = 0 ('2')`: count=1. `nextResult = "12"`. `i = 1`.
  - `i = 1 ('1')`: count=1. `nextResult = "12" + "11" = "1211"`.
  - `result = "1211"`.
- Returns `"1211"`.

## Common Mistakes
- **Recursion depth limit / memory overhead:** While you *can* write this recursively `string prev = countAndSay(n-1)`, the iterative loop avoids creating $N$ stack frames and makes it slightly more memory efficient. Both are acceptable.
- **Forgetting `to_string()`:** Writing `nextResult += count + result[i]` will treat `count` as an ASCII value and append weird characters (like `'\x01'`) instead of `"1"`. You must use `to_string(count)`.

## Similar Problems
- Encode and Decode Strings
- String Compression
