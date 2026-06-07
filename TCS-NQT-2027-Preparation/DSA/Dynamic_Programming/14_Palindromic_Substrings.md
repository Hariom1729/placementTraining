# Problem 14: Palindromic Substrings

## Problem Statement
Given a string `s`, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

---

## Approach 1: Expand Around Center (Optimal Space)
While this is in the DP section, the Expand Around Center approach is generally preferred because it runs in `O(N^2)` time and `O(1)` space, whereas 2D DP takes `O(N^2)` space.
Every palindrome has a center. A center can be a single character (for odd length palindromes) or between two characters (for even length palindromes). There are `2N - 1` such centers. We can expand outward from each center and count the palindromes.

## Approach 2: 2D DP (Tabulation)
Let `dp[i][j]` be `true` if the substring `s[i...j]` is a palindrome.
- Single characters (`i == j`) are always palindromes: `dp[i][i] = true`.
- Two characters (`j == i + 1`) are palindromes if `s[i] == s[j]`.
- Length > 2: `s[i...j]` is a palindrome if `s[i] == s[j]` AND the inner substring `s[i+1...j-1]` is a palindrome (`dp[i+1][j-1] == true`).

Here, we will provide the DP approach for conceptual consistency, but note that the expansion method is practically better for space.

---

## C++ Solution (2D DP)

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        int count = 0;
        
        // dp[i][j] is true if s[i...j] is a palindrome
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        // 1. All substrings of length 1 are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // 2. Check substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // 3. Check substrings of length 3 or more
        // L is the length of the substring
        for (int L = 3; L <= n; L++) {
            for (int i = 0; i < n - L + 1; i++) {
                int j = i + L - 1; // Ending index
                
                // Characters match AND inner substring is a palindrome
                if (s[i] == s[j] && dp[i + 1][j - 1] == true) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    string s = "abc";
    cout << "Palindromic Substrings in 'abc': " << sol.countSubstrings(s) << endl; 
    // Expected: 3 ("a", "b", "c")
    
    string s2 = "aaa";
    cout << "Palindromic Substrings in 'aaa': " << sol.countSubstrings(s2) << endl; 
    // Expected: 6 ("a", "a", "a", "aa", "aa", "aaa")

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` where `N` is the length of the string.
- **Space Complexity:** `O(N^2)` for the DP table. (Expand around center approach uses `O(1)` space).
