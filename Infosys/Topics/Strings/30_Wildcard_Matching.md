# Wildcard Matching

## Difficulty
Hard

## Probability
★★☆☆☆

## Asked In
Infosys SP
Similar Companies: Google, Amazon

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (String Matching)

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `'?'` and `'*'` where:
- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

## Constraints
- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

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
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**
```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

## Edge Cases
- `p` is `"****"`, `s` is empty. The multiple stars can all match the empty sequence.
- Heavy use of consecutive `*` in the pattern (can cause TLE in recursion).

## Intuition
This is very similar to **Regular Expression Matching**, but the behavior of `*` is completely different.
Here, `*` is a true wildcard that can stand for ANY sequence of characters, totally independent of what character came before it.
Let `dp[i][j]` be `true` if `s[0...i-1]` matches `p[0...j-1]`.
When comparing `s[i-1]` and `p[j-1]`:
1. **If `p[j-1]` is a regular character or `'?'`: **
   - They match if `s[i-1] == p[j-1]` or `p[j-1] == '?'`.
   - `dp[i][j] = dp[i-1][j-1]`.
2. **If `p[j-1]` is `'*'`: **
   - It matches ANY sequence (0 or more characters).
   - **Match Zero characters:** The `*` acts as an empty string. `dp[i][j] = dp[i][j-1]` (we keep the `s` index the same, but move the pattern index back).
   - **Match One (or more) characters:** The `*` consumes the current character in `s`. `dp[i][j] = dp[i-1][j]` (we move the `s` index back, but KEEP the `*` active in the pattern!).
   - So `dp[i][j] = dp[i][j-1] || dp[i-1][j]`.

## Brute Force Approach
**Explanation:** Recursion. Whenever `*` is encountered, recursively test every possible length of substring it could match.
**Time Complexity:** $O(2^{N+M})$
**Space Complexity:** $O(N+M)$

## Optimal Approach (2D DP)
**Detailed explanation:**
1. Create `vector<vector<bool>> dp(M + 1, vector<bool>(N + 1, false))`.
2. `dp[0][0] = true` (empty string matches empty pattern).
3. Initialization for `dp[0][j]` (empty string vs pattern):
   - A pattern like `***` can match an empty string!
   - `for j=1 to N`: if `p[j-1] == '*'`, `dp[0][j] = dp[0][j-1]`. Else break.
4. Loop `i` from 1 to $M$:
   - Loop `j` from 1 to $N$:
     - If `p[j-1] == '?' || p[j-1] == s[i-1]`:
       - `dp[i][j] = dp[i-1][j-1]`
     - Else if `p[j-1] == '*'`:
       - `dp[i][j] = dp[i][j-1] || dp[i-1][j]`
5. Return `dp[M][N]`.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(M \times N)$ for the DP matrix. Can be optimized to $O(N)$ with 1D array swapping.

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
        
        // Base case: empty string and empty pattern match
        dp[0][0] = true;
        
        // Base case: empty string vs pattern with only '*'
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            } else {
                break; // If it's not a star, it can't match an empty string
            }
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                
                if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
                    // Exact match or '?' wildcard
                    dp[i][j] = dp[i - 1][j - 1];
                } 
                else if (p[j - 1] == '*') {
                    // '*' matches empty sequence (dp[i][j-1]) 
                    // OR '*' matches current character (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Dry Run
`s = "adceb", p = "*a*b"`
- `dp[0][0] = T`. `dp[0][1] (p="*") = T`.
- `i=1 ('a')`:
  - `j=1 ('*')`: `dp[1][1] = dp[1][0] || dp[0][1] = F || T = T`.
  - `j=2 ('a')`: Match. `dp[1][2] = dp[0][1] = T`.
- `i=2 ('d')`:
  - `j=3 ('*')`: `dp[2][3] = dp[2][2] || dp[1][3] = F || (wait, let's see)`.
  - Actually, since `p[2]='*'`, `dp[1][3] = dp[1][2] || dp[0][3] = T || F = T`.
  - So `dp[2][3] = dp[2][2] || dp[1][3] = F || T = T`. The second `*` consumes the `'d'`.
- `i=3 ('c'), i=4 ('e')`: The second `*` consumes both. `dp[3][3]=T, dp[4][3]=T`.
- `i=5 ('b')`:
  - `j=4 ('b')`: Match! `dp[5][4] = dp[4][3] = T`.
Result: `true`.

## Common Mistakes
- **Confusing Wildcard `*` with Regex `*`:** In Regex, `*` means "repeat previous". In Wildcard, `*` means "match ANYTHING". Their state transitions are different. Wildcard is simpler (`dp[i][j-1] || dp[i-1][j]`).

## Similar Problems
- Regular Expression Matching
