# Problem 3: Longest Common Subsequence (LCS)

## Problem Statement
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

---

## Approach: 2D DP Tabulation

Let `dp[i][j]` be the length of the LCS of `text1[0...i-1]` and `text2[0...j-1]`.
We build a 2D matrix of size `(m+1) x (n+1)`.

- **Base Case:** If either string is empty, LCS is `0`. So, the first row and first column of `dp` are `0`.
- **Recursive Step:**
  - If characters match (`text1[i-1] == text2[j-1]`):
    - `dp[i][j] = 1 + dp[i-1][j-1]` (Include this character in the LCS).
  - If characters don't match:
    - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (Skip a character from either string and take the max).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        
        // DP table with dimensions (m+1) x (n+1) initialized to 0
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
};

int main() {
    Solution sol;
    string text1 = "abcde";
    string text2 = "ace";
    
    cout << "Length of LCS: " << sol.longestCommonSubsequence(text1, text2) << endl; 
    // Expected: 3 ("ace")
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(M * N)` where `M` and `N` are the lengths of the two strings.
- **Space Complexity:** `O(M * N)` for the 2D DP table. *(Can be optimized to `O(N)` since we only need the previous row).*
