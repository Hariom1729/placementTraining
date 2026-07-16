# Word Break

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, ByteDance

## Topic
Strings / Dynamic Programming

## Pattern
Bottom-Up DP

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Constraints
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are unique.

## Input
- `s` string.
- `wordDict` vector of strings.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Edge Cases
- Entire string `s` matches a single word in the dictionary.
- No matching dictionary words at all.

## Intuition
This is the classic **Dynamic Programming** string problem!
If we want to know if `leetcode` can be broken, we can ask: "If I find `leet` in the dictionary, can the *rest of the string* (`code`) be broken?"
We are breaking a big problem into overlapping smaller subproblems.
Instead of Top-Down recursion (which works with memoization), let's use **Bottom-Up DP**.
Create a boolean array `dp` of size `s.length() + 1`, where `dp[i]` is `true` if the first `i` characters of the string can be successfully segmented.
- `dp[0] = true` (an empty string can always be segmented).
For every index `i` from 1 to `s.length()`:
  - We check every word in `wordDict`.
  - If the word's length `len <= i`:
  - We check if `dp[i - len]` is true (meaning the string *before* this word was successfully segmented!).
  - AND we check if the substring `s.substr(i - len, len)` perfectly matches the word!
  - If BOTH are true, then `dp[i] = true`, and we break out of the word loop (since one success is all we need for index `i`).

## Brute Force Approach
**Explanation:** Recursion. For every prefix that exists in the dictionary, recurse on the suffix. $O(2^N)$ possibilities.
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$

## Optimal Approach (1D Dynamic Programming)
**Detailed explanation:**
1. Create a `vector<bool> dp(s.length() + 1, false)`.
2. `dp[0] = true`.
3. Loop `i` from `1` to `s.length()`:
   - Loop over every `word` in `wordDict`:
     - `int len = word.length();`
     - If `i >= len`:
       - If `dp[i - len] == true` AND `s.substr(i - len, len) == word`:
         - `dp[i] = true`.
         - `break;` (We found a valid segmentation for index `i`, no need to check other words).
4. Return `dp[s.length()]`.

**Time Complexity:** $O(N \times M \times K)$ where $N$ is `s.length()`, $M$ is `wordDict.length()`, and $K$ is the average length of a word in the dictionary (due to substring comparison). Given constraints ($300 \times 1000 \times 20 = 6,000,000$ operations), it passes instantly.
**Space Complexity:** $O(N)$ for the DP array.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        // dp[i] is true if the substring s[0...i-1] can be segmented
        vector<bool> dp(n + 1, false);
        dp[0] = true; // Empty string is valid
        
        for (int i = 1; i <= n; i++) {
            // Check every word in the dictionary against the current index
            for (const string& word : wordDict) {
                int len = word.length();
                
                // If the word fits in the current prefix 
                // AND the string prior to this word was successfully segmented
                if (i >= len && dp[i - len]) {
                    // Check if the actual substring matches the word
                    if (s.substr(i - len, len) == word) {
                        dp[i] = true;
                        break; // Move to the next i since this prefix is already verified
                    }
                }
            }
        }
        
        return dp[n];
    }
};
```

## Dry Run
`s = "leetcode", dict = ["leet", "code"]`
- `dp = [T, F, F, F, F, F, F, F, F]`
- `i = 1 to 3`: `dp[1...3]` remain false because neither "leet" nor "code" fit or match.
- `i = 4`:
  - Word "leet": `len = 4`. `4 >= 4`. `dp[4 - 4]` is `dp[0]` which is TRUE.
  - Substring `s.substr(0, 4)` is "leet". Match!
  - `dp[4] = true`. Break inner loop.
- `i = 5 to 7`: remain false.
- `i = 8`:
  - Word "leet": `len = 4`. `dp[4]` is TRUE. Substring `substr(4, 4)` is "code". No match.
  - Word "code": `len = 4`. `dp[4]` is TRUE. Substring `substr(4, 4)` is "code". Match!
  - `dp[8] = true`. Break inner loop.
- Return `dp[8]` -> `true`.

## Common Mistakes
- **Checking if dictionary contains the entire prefix directly:** If you try `if (dict.count(s.substr(0, i)))`, you fail tests like `s="applepenapple"`. You MUST rely on `dp[i - len]` to chain segmentations together properly.
- **Using a nested loop `j` from `0` to `i`:** `for(i=1..N) { for(j=0..i) { if(dp[j] && dict.count(s.substr(j, i-j))) } }`. This works but converting the dictionary to an `unordered_set` and doing substring operations for every $i,j$ pair ($O(N^3)$) can be slower than just looping over the dictionary directly if the dictionary is small/medium.

## Similar Problems
- Word Break II (Requires backtracking to return all paths)
- Palindrome Partitioning
