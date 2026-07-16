# Longest Palindromic Subsequence

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Google

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (Palindrome)

## Problem Statement
Given a string `s`, find the longest palindromic **subsequence**'s length in `s`.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of only lowercase English letters.

## Input
- `s` string.

## Output
- Return an integer length.

## Sample Test Cases

**Example 1:**
```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

**Example 2:**
```
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
```

## Edge Cases
- The string is already a palindrome.
- All characters are distinct (answer is 1).

## Intuition
This is a classic DP problem. However, there is a **massive brain-hack** to solve it without thinking about a new DP recurrence!
A palindrome reads the same forwards and backwards.
If we want to find the longest palindromic subsequence in `s`, that is MATHEMATICALLY EQUIVALENT to finding the **Longest Common Subsequence (LCS)** between `s` and the `reverse of s`!
If `s = "bbbab"`, its reverse is `r = "babbb"`.
The LCS of `"bbbab"` and `"babbb"` is `"bbbb"`, which has length 4!
Since we already know how to write the 2D DP for LCS, we can literally just reverse the string and copy-paste the LCS code!

*(Alternatively, you can write the standard 2D interval DP: `dp[i][j]` = max palindrome in `s[i...j]`. If `s[i] == s[j]`, `dp[i][j] = 2 + dp[i+1][j-1]`. Else `max(dp[i+1][j], dp[i][j-1])`. But the LCS trick is often easier to remember in an interview).*

## Brute Force Approach
**Explanation:** Generate all $2^N$ subsequences, check if they are palindromes, keep the max length.
**Time Complexity:** $O(2^N \times N)$
**Space Complexity:** $O(N)$

## Optimal Approach (LCS with Reversed String)
**Detailed explanation:**
1. Let `text1 = s`.
2. Let `text2 = s`, then `reverse(text2.begin(), text2.end())`.
3. Create `dp` table of size `(N+1) x (N+1)` initialized to 0.
4. Run standard LCS algorithm:
   - Loop `i` from 1 to $N$:
     - Loop `j` from 1 to $N$:
       - If `text1[i-1] == text2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`
       - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
5. Return `dp[N][N]`.

**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(N^2)$

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        string text1 = s;
        string text2 = s;
        reverse(text2.begin(), text2.end());
        
        int n = s.length();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        
        // Standard Longest Common Subsequence logic
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[n][n];
    }
};
```

## Dry Run
`s = "cbbd"` -> `t1 = "cbbd"`, `t2 = "dbbc"`.
- `i=1 ('c')`: Matches `t2[3] ('c')`.
- `i=2 ('b')`: Matches `t2[1] ('b')` and `t2[2] ('b')`.
- `i=3 ('b')`: Matches `t2[1] ('b')` and `t2[2] ('b')`.
- `i=4 ('d')`: Matches `t2[0] ('d')`.
- `dp` resolves the LCS to `"bb"`, length 2.

## Common Mistakes
- **Confusing Subsequence with Substring:** "Longest Palindromic Substring" requires contiguous characters (solved via Expand Around Center). "Subsequence" allows jumping over characters, making it a DP matching problem.

## Similar Problems
- Longest Common Subsequence
- Longest Palindromic Substring
