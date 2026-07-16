# Edit Distance

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Google

## Topic
Strings / Dynamic Programming

## Pattern
2D DP (String Matching)

## Problem Statement
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
1. **Insert** a character
2. **Delete** a character
3. **Replace** a character

## Constraints
- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Input
- `word1` string.
- `word2` string.

## Output
- Return an integer (minimum number of operations).

## Sample Test Cases

**Example 1:**
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (delete 'r')
rose -> ros (delete 'e')
```

**Example 2:**
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Edge Cases
- One string is empty. Answer is the length of the other string (all insertions).
- Strings are identical. Answer is 0.

## Intuition
This is the textbook problem for **2D Dynamic Programming** (Levenshtein distance).
We can compare `word1` (length $M$) and `word2` (length $N$) character by character.
Let `dp[i][j]` be the minimum operations to convert the first `i` characters of `word1` into the first `j` characters of `word2`.
If we are looking at `word1[i-1]` and `word2[j-1]`, two things can happen:
1. **They Match:** The cost to convert them is exactly the same as the cost *before* adding these two characters! So, `dp[i][j] = dp[i-1][j-1]`.
2. **They Don't Match:** We MUST perform 1 operation. We take the minimum cost of our three choices and add 1:
   - **Replace:** We replace `word1[i-1]` with `word2[j-1]`. The remaining strings to convert are `i-1` and `j-1`. Cost = `dp[i-1][j-1] + 1`.
   - **Delete:** We delete `word1[i-1]`. The remaining string `1` is now `i-1`, but string `2` is still `j`. Cost = `dp[i-1][j] + 1`.
   - **Insert:** We insert `word2[j-1]` into `word1`. Now string `1` perfectly matches the `j`-th character of string `2`. So we move `j` back (since it's matched), but `i` stays the same. Cost = `dp[i][j-1] + 1`.

So if they don't match: `dp[i][j] = 1 + min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]})`.

## Brute Force Approach
**Explanation:** Recursion. At each mismatched character, recursively branch into 3 paths (Insert, Delete, Replace).
**Time Complexity:** $O(3^N)$
**Space Complexity:** $O(N)$

## Optimal Approach (2D DP Tabulation)
**Detailed explanation:**
1. Let $M = word1.length()$ and $N = word2.length()$.
2. Create a `vector<vector<int>> dp(M + 1, vector<int>(N + 1, 0))`.
3. **Base Cases:**
   - Converting an empty string to string 2 of length `j` requires `j` insertions: `dp[0][j] = j`.
   - Converting string 1 of length `i` to an empty string requires `i` deletions: `dp[i][0] = i`.
4. Loop `i` from 1 to $M$:
   - Loop `j` from 1 to $N$:
     - If `word1[i-1] == word2[j-1]`:
       - `dp[i][j] = dp[i-1][j-1]`.
     - Else:
       - `dp[i][j] = 1 + min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]})`.
5. Return `dp[M][N]`.

**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(M \times N)$ for the DP matrix. Can be optimized to $O(N)$ by only storing the previous row, but $O(M \times N)$ is perfectly standard and accepted.

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        
        // dp[i][j] represents the minimum operations to convert 
        // the first i characters of word1 to the first j characters of word2
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i; // Delete all characters
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j; // Insert all characters
        }
        
        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the characters match, no new operation is needed
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } 
                else {
                    // Mismatch: take the minimum of Insert, Delete, or Replace, and add 1
                    dp[i][j] = 1 + min({
                        dp[i][j - 1],    // Insert
                        dp[i - 1][j],    // Delete
                        dp[i - 1][j - 1] // Replace
                    });
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Dry Run
`w1 = "ab", w2 = "bc"`
DP Matrix initial:
`[0, 1, 2]`
`[1, 0, 0]`
`[2, 0, 0]`

- `i=1 ('a'), j=1 ('b')`: Mismatch. `1 + min(dp[0][0], dp[0][1], dp[1][0]) = 1 + min(0,1,1) = 1`. `dp[1][1] = 1`.
- `i=1 ('a'), j=2 ('c')`: Mismatch. `1 + min(dp[0][1], dp[0][2], dp[1][1]) = 1 + min(1,2,1) = 2`. `dp[1][2] = 2`.
- `i=2 ('b'), j=1 ('b')`: Match! `dp[2][1] = dp[1][0] = 1`.
- `i=2 ('b'), j=2 ('c')`: Mismatch. `1 + min(dp[1][1](Replace), dp[1][2](Delete), dp[2][1](Insert)) = 1 + min(1, 2, 1) = 2`. `dp[2][2] = 2`.
Result: 2. (Delete 'a', Insert 'c').

## Common Mistakes
- **Confusing indices:** `dp[i][j]` corresponds to `word1[i-1]` and `word2[j-1]`. If you check `word1[i]`, you will get out of bounds errors.

## Similar Problems
- Longest Common Subsequence
- Delete Operation for Two Strings
