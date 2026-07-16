# Distinct Subsequences

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (String Matching)

## Problem Statement
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

## Constraints
- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Input
- `s` string (source).
- `t` string (target).

## Output
- Return an integer (number of distinct subsequences).

## Sample Test Cases

**Example 1:**
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```

**Example 2:**
```
Input: s = "babgbag", t = "bag"
Output: 5
```

## Edge Cases
- `s` is shorter than `t` (impossible, return 0).
- `t` is empty. (An empty string is a subsequence of any string exactly 1 time, by deleting everything).

## Intuition
This is another classic **2D DP** matching problem.
Let `dp[i][j]` be the number of ways to form the first `j` characters of `t` using the first `i` characters of `s`.

Base cases:
- Forming an empty `t` (`j=0`) from any prefix of `s` can always be done in exactly 1 way: delete all characters. `dp[i][0] = 1`.
- Forming a non-empty `t` from an empty `s` (`i=0`) is impossible: `dp[0][j] = 0`.

Transitions for `dp[i][j]`:
1. **If `s[i-1] != t[j-1]`:** The current character of `s` is useless. We MUST ignore it and rely entirely on the previous characters of `s` to form `t`.
   `dp[i][j] = dp[i-1][j]`
2. **If `s[i-1] == t[j-1]`:** We have a choice!
   - We can USE `s[i-1]` to match `t[j-1]`. If we do, we need to know how many ways we could form the rest of `t` (`j-1`) from the rest of `s` (`i-1`). (That's `dp[i-1][j-1]`).
   - OR, we can IGNORE `s[i-1]` and see if we can form all of `t` (`j`) using the rest of `s` (`i-1`), just like if they didn't match. (That's `dp[i-1][j]`).
   So the total ways is the sum of both choices:
   `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`

## Brute Force Approach
**Explanation:** Recursion. Explore all subsets of `s`.
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$

## Optimal Approach (2D DP Tabulation)
**Detailed explanation:**
1. Let $M = s.length(), N = t.length()$.
2. Create `vector<vector<unsigned int>> dp(M + 1, vector<unsigned int>(N + 1, 0))`. (Use `unsigned int` to prevent intermediate overflow before modulo/constraints, though constraints say answer fits in signed 32-bit).
3. Base cases: `dp[i][0] = 1` for all `i`.
4. Iterate `i` from 1 to $M$:
   - Iterate `j` from 1 to $N$:
     - If `s[i-1] == t[j-1]`:
       - `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`
     - Else:
       - `dp[i][j] = dp[i-1][j]`
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
    int numDistinct(string s, string t) {
        int m = s.length();
        int n = t.length();
        
        // Use unsigned int to prevent potential integer overflow during intermediate additions
        vector<vector<unsigned int>> dp(m + 1, vector<unsigned int>(n + 1, 0));
        
        // Base case: forming an empty string t from any prefix of s requires 1 way (deleting all)
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    // Two choices: use the current character of s, or ignore it
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // Must ignore the current character of s
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Dry Run
`s = "babgbag", t = "bag"`
- `i=1 ('b')`:
  - `j=1 ('b')`: Match! `dp[1][1] = dp[0][0] + dp[0][1] = 1 + 0 = 1`.
- `i=2 ('a')`:
  - `j=1 ('b')`: Mismatch. `dp[2][1] = dp[1][1] = 1`.
  - `j=2 ('a')`: Match! `dp[2][2] = dp[1][1] + dp[1][2] = 1 + 0 = 1`.
- `i=3 ('b')`:
  - `j=1 ('b')`: Match. `dp[3][1] = dp[2][0] + dp[2][1] = 1 + 1 = 2`.
  - `j=2 ('a')`: Mismatch. `dp[3][2] = dp[2][2] = 1`.
- `i=4 ('g')`:
  - `j=3 ('g')`: Match. `dp[4][3] = dp[3][2] + dp[3][3] = 1 + 0 = 1`.
- `i=5 ('b')`:
  - `j=1 ('b')`: Match. `dp[5][1] = dp[4][0] + dp[4][1] = 1 + 2 = 3`.
- `i=6 ('a')`:
  - `j=2 ('a')`: Match. `dp[6][2] = dp[5][1] + dp[5][2] = 3 + 1 = 4`.
- `i=7 ('g')`:
  - `j=3 ('g')`: Match. `dp[7][3] = dp[6][2] + dp[6][3] = 4 + 1 = 5`.
Result: 5.

## Common Mistakes
- **Unsigned Int Overflow Error:** Even though the problem says the final answer fits in a 32-bit signed integer, intermediate values in the DP table (where paths combine but eventually fail) can overflow a standard signed integer in C++. Always use `unsigned int` or `long long` for combinatorial DP tables to be safe.

## Similar Problems
- Edit Distance
- Longest Common Subsequence
