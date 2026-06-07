# Problem 13: Word Break

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Constraints
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are unique.

---

## Approach: 1D DP

Let `dp[i]` be a boolean indicating whether the substring `s[0...i-1]` (of length `i`) can be segmented into dictionary words.
We initialize `dp[0] = true` (an empty string can always be segmented).

To compute `dp[i]`, we check all possible split points `j` from `0` to `i-1`.
If `s[0...j-1]` can be segmented (which means `dp[j] == true`) AND the remaining substring `s[j...i-1]` is in the dictionary, then `s[0...i-1]` can be segmented (so `dp[i] = true`).

1. Put all words in an `unordered_set` for `O(1)` lookup.
2. Initialize `dp` array of size `s.length() + 1` with `false`.
3. `dp[0] = true`.
4. Loop `i` from `1` to `s.length()`.
5. Inner loop `j` from `0` to `i-1`.
   - If `dp[j]` is true and `s.substr(j, i - j)` is in the set, set `dp[i] = true` and `break` (no need to check other splits for `i`).
6. Return `dp[s.length()]`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        int n = s.length();
        
        // dp[i] is true if s[0...i-1] can be segmented
        vector<bool> dp(n + 1, false);
        dp[0] = true; 
        
        for (int i = 1; i <= n; i++) {
            // Check all split points j before i
            for (int j = 0; j < i; j++) {
                // If prefix is valid AND suffix is in dictionary
                if (dp[j] && wordSet.find(s.substr(j, i - j)) != wordSet.end()) {
                    dp[i] = true;
                    break; // Found a valid segmentation, move to next i
                }
            }
        }
        
        return dp[n];
    }
};

int main() {
    Solution sol;
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code"};
    
    cout << "Can be segmented? " << (sol.wordBreak(s, wordDict) ? "Yes" : "No") << endl; 
    // Expected: Yes
    
    string s2 = "catsandog";
    vector<string> wordDict2 = {"cats", "dog", "sand", "and", "cat"};
    cout << "Can be segmented? " << (sol.wordBreak(s2, wordDict2) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^3)` where `N` is the length of the string `s`. The two nested loops take `O(N^2)`, and `s.substr()` takes `O(N)`.
- **Space Complexity:** `O(N)` for the DP array + `O(W)` for the set where `W` is total characters in dictionary.
