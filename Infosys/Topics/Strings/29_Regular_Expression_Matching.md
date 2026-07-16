# Regular Expression Matching

## Difficulty
Hard

## Probability
★★☆☆☆

## Asked In
Infosys SP
Similar Companies: Google, Amazon, Facebook, Apple

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (String Matching)

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

## Constraints
- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

## Input
- `s` string (input).
- `p` string (pattern).

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

## Edge Cases
- `p` is `"a*b*c*"`, and `s` is empty. The answer is `true` because `*` can mean ZERO matches!
- `.*` which acts as a universal wildcard matching anything.

## Intuition
This is a complex matching problem where decisions affect the future (e.g., does `a*` match 0, 1, 2, or 3 `'a'`s?). Dynamic Programming is required.
Let `dp[i][j]` be `true` if `s[0...i-1]` matches `p[0...j-1]`.
When comparing `s[i-1]` and `p[j-1]`:
1. **If `p[j-1]` is a regular character or `'.'`: **
   - They match if `s[i-1] == p[j-1]` or `p[j-1] == '.'`.
   - `dp[i][j] = dp[i-1][j-1] && match`.
2. **If `p[j-1]` is `'*'`: **
   - `'*'` relies on the PRECEDING character in the pattern, `p[j-2]`.
   - We have two choices:
     - **Match ZERO times:** We completely ignore the `Char + '*'` combination. We look back 2 steps in the pattern. `dp[i][j] = dp[i][j-2]`.
     - **Match ONE OR MORE times:** The `Char + '*'` combination is actively being used. This requires that `s[i-1]` actually MATCHES the preceding character `p[j-2]` (or `p[j-2] == '.'`). If it matches, we "consume" `s[i-1]` but KEEP the `Char + '*'` active in the pattern (so we look at `dp[i-1][j]`).

## Brute Force Approach
**Explanation:** Recursion with backtracking. Branch every time you see a `*`.
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$

## Optimal Approach (2D DP)
**Detailed explanation:**
1. Create `vector<vector<bool>> dp(M + 1, vector<bool>(N + 1, false))`.
2. `dp[0][0] = true` (empty string matches empty pattern).
3. Initialization for `dp[0][j]` (empty string vs pattern):
   - A pattern like `a*b*` can match an empty string!
   - `for j=2 to N`: if `p[j-1] == '*'`, `dp[0][j] = dp[0][j-2]`.
4. Loop `i` from 1 to $M$:
   - Loop `j` from 1 to $N$:
     - If `p[j-1] == '.' || p[j-1] == s[i-1]`:
       - `dp[i][j] = dp[i-1][j-1]`
     - Else if `p[j-1] == '*'`:
       - Match Zero: `dp[i][j] = dp[i][j-2]`
       - Match One/More: If `p[j-2] == '.' || p[j-2] == s[i-1]`:
         - `dp[i][j] = dp[i][j] || dp[i-1][j]`
5. Return `dp[M][N]`.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(M \times N)$

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Base case: empty string and empty pattern
        dp[0][0] = true;
        
        // Base case: empty string vs pattern like "a*b*c*"
        for (int j = 2; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                
                if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                    // Exact match or '.' wildcard
                    dp[i][j] = dp[i - 1][j - 1];
                } 
                else if (p[j - 1] == '*') {
                    // Match Zero times (ignore the X*)
                    dp[i][j] = dp[i][j - 2];
                    
                    // Match One or More times
                    char prevChar = p[j - 2];
                    if (prevChar == '.' || prevChar == s[i - 1]) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Dry Run
`s = "aab", p = "c*a*b"`
- `dp[0][0] = T`.
- Initialize `dp[0][j]`: `j=2 ('*')`, `dp[0][2] = dp[0][0] = T`. (`"c*"` matches empty).
- `i=1 ('a')`:
  - `j=1 ('c')`: Mismatch.
  - `j=2 ('*')`: Match Zero: `dp[1][2] = dp[1][0] = F`.
  - `j=3 ('a')`: Match. `dp[1][3] = dp[0][2] = T`. ( `"a"` matches `"c*a"`).
- `i=2 ('a')`:
  - `j=3 ('a')`: Match. `dp[2][3] = dp[1][2] = F`.
  - `j=4 ('*')`: Match Zero: `dp[2][4] = dp[2][2] = F`. Match One/More: prev is `'a'`, matches `s[1]`. `dp[2][4] = dp[2][4] || dp[1][4]`. Since `"c*a*"` matched `"a"`, `"c*a*"` can match `"aa"`. So `dp[2][4] = T`.
- `i=3 ('b')`:
  - `j=5 ('b')`: Match! `dp[3][5] = dp[2][4] = T`.
Result: `true`.

## Common Mistakes
- **Confusing `*` behavior:** In Regex, `*` means "Zero or more of the PRECEDING character". It is NOT a universal wildcard like it is in the terminal (that is `Wildcard Matching`). `a*` matches `""`, `"a"`, `"aa"`, etc.

## Similar Problems
- Wildcard Matching
