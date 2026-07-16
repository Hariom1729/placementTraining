# Longest Common Subsequence

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Google, ByteDance

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (String Matching)

## Problem Statement
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, `"ace"` is a subsequence of `"abcde"`.
A common subsequence of two strings is a subsequence that is common to both strings.

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Input
- `text1` string.
- `text2` string.

## Output
- Return an integer length.

## Sample Test Cases

**Example 1:**
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2:**
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3:**
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Edge Cases
- One string is much longer than the other.
- Strings have no characters in common.

## Intuition
This is the foundational **2D DP** problem for strings.
We want to compare `text1` (length $M$) and `text2` (length $N$).
Let `dp[i][j]` be the length of the Longest Common Subsequence (LCS) for the first `i` characters of `text1` and the first `j` characters of `text2`.

If we are looking at `text1[i-1]` and `text2[j-1]`:
1. **If they match:** This character is part of our LCS! The total length is `1` PLUS the LCS length of the strings *before* we included these characters.
   `dp[i][j] = 1 + dp[i-1][j-1]`
2. **If they don't match:** We can't include both. We must drop either `text1[i-1]` or `text2[j-1]` and see which option gives us a longer subsequence.
   `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

We just build this table from the bottom up!

## Brute Force Approach
**Explanation:** Generate all $2^N$ subsequences of `text1` and check if they exist in `text2`.
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$

## Optimal Approach (2D DP Tabulation)
**Detailed explanation:**
1. Let $M = text1.length(), N = text2.length()$.
2. Create a `vector<vector<int>> dp(M + 1, vector<int>(N + 1, 0))`.
3. Base cases: `dp[0][j] = 0` and `dp[i][0] = 0` (handled by initialization).
4. Iterate `i` from 1 to $M$:
   - Iterate `j` from 1 to $N$:
     - If `text1[i-1] == text2[j-1]`:
       - `dp[i][j] = 1 + dp[i-1][j-1]`
     - Else:
       - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
5. Return `dp[M][N]`.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(M \times N)$ for the DP table. (Can be optimized to $O(min(M, N))$ by only storing the previous row).

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        
        // dp[i][j] stores the length of LCS of text1[0...i-1] and text2[0...j-1]
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    // Match found, add 1 to the previous diagonal value
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    // No match, take the max of excluding current char of text1 or text2
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Dry Run
`text1 = "abcde", text2 = "ace"`
- `i=1 ('a'), j=1 ('a')`: Match. `dp[1][1] = 1 + dp[0][0] = 1`.
- `i=1 ('a'), j=2 ('c')`: No match. `max(dp[0][2], dp[1][1]) = max(0, 1) = 1`.
- `i=1 ('a'), j=3 ('e')`: No match. `max(dp[0][3], dp[1][2]) = max(0, 1) = 1`.
- `i=2 ('b'), j=1 ('a')`: No match. `dp[2][1] = 1`.
- `i=2 ('b'), j=2 ('c')`: No match. `dp[2][2] = max(dp[1][2], dp[2][1]) = 1`.
- ...
- `i=3 ('c'), j=2 ('c')`: Match. `dp[3][2] = 1 + dp[2][1] = 1 + 1 = 2`.
- ...
- `i=5 ('e'), j=3 ('e')`: Match. `dp[5][3] = 1 + dp[4][2] = 1 + 2 = 3`.
Result: 3.

## Common Mistakes
- **Iterating using 0-indexed strings directly into DP:** `dp[i][j]` needs to map to `string[i-1][j-1]` to allow `dp[0]` to represent empty strings. Forgetting the `- 1` offset causes out-of-bounds errors.

## Similar Problems
- Edit Distance
- Longest Palindromic Subsequence
- Delete Operation for Two Strings
