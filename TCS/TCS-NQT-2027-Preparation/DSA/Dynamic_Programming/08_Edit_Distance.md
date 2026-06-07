# Problem 8: Edit Distance

## Problem Statement
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.
You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

## Constraints
- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

---

## Approach: 2D DP (String Matching)

Let `dp[i][j]` be the minimum operations to convert `word1[0...i-1]` to `word2[0...j-1]`.
Create a `(m+1) x (n+1)` DP table.

- **Base Cases:**
  - `dp[i][0] = i`: Converting a string of length `i` to an empty string takes `i` deletions.
  - `dp[0][j] = j`: Converting an empty string to a string of length `j` takes `j` insertions.

- **Recursive Step:**
  - If `word1[i-1] == word2[j-1]`: Characters match, no operation needed.
    - `dp[i][j] = dp[i-1][j-1]`
  - If they don't match, we try all 3 operations and take the minimum:
    1. **Replace:** `dp[i-1][j-1] + 1`
    2. **Delete (from word1):** `dp[i-1][j] + 1`
    3. **Insert (into word1):** `dp[i][j-1] + 1`
    - `dp[i][j] = 1 + min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]})`

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
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i; // Delete all chars
        for (int j = 0; j <= n; j++) dp[0][j] = j; // Insert all chars
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]; // No cost
                } else {
                    dp[i][j] = 1 + min({
                        dp[i - 1][j - 1], // Replace
                        dp[i - 1][j],     // Delete
                        dp[i][j - 1]      // Insert
                    });
                }
            }
        }
        
        return dp[m][n];
    }
};

int main() {
    Solution sol;
    string word1 = "horse";
    string word2 = "ros";
    
    cout << "Min Operations: " << sol.minDistance(word1, word2) << endl; 
    // Expected: 3
    // 1. horse -> rorse (replace 'h' with 'r')
    // 2. rorse -> rose (delete 'r')
    // 3. rose -> ros (delete 'e')

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(M * N)`.
- **Space Complexity:** `O(M * N)` for the DP table. (Can be optimized to `O(N)`).
