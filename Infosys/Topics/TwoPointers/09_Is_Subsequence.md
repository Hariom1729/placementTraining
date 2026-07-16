# Is Subsequence

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google

## Topic
Two Pointers / Strings / Greedy

## Pattern
Two Pointers for Subsequence

## Problem Statement
Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Constraints
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

## Input
- `s` string.
- `t` string.

## Output
- Return a boolean.

## Sample Test Cases

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: 'a', 'b', and 'c' appear in order in 't'.
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: 'x' does not appear in 't'.
```

## Edge Cases
- `s` is an empty string (always returns `true`).
- `t` is empty but `s` is not (returns `false`).
- `s.length() > t.length()` (returns `false`).

## Intuition
To check if `s` is a subsequence of `t`, we can just scan `t` from left to right.
We use a pointer for `s` and a pointer for `t`.
- We look at the first character of `s`. Does it appear in `t`?
- Yes! We move our `s` pointer to the next character we need to find.
- No? We just move our `t` pointer to check the next character in `t`.

Since a subsequence relies on **relative order**, this greedy matching (taking the very first match we see in `t` and moving forward) is mathematically perfectly sound. There is no benefit to skipping a match to look for a later one.

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. Initialize two pointers: `i = 0` (for string `s`) and `j = 0` (for string `t`).
2. Loop while `i < s.length()` AND `j < t.length()`:
   - If the characters match (`s[i] == t[j]`), it means we found the current character of `s` inside `t`. We can move on to the next character in `s` by incrementing `i`.
   - Regardless of whether they match or not, we ALWAYS increment `j` to scan the next character in `t`.
3. After the loop, if we successfully found all characters of `s`, then `i` will have reached `s.length()`.
4. Return `i == s.length()`.

**Time Complexity:** $O(N)$ where $N$ is the length of `t`.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0; // Pointer for s
        int j = 0; // Pointer for t
        
        // Traverse both strings
        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                // Character found, look for the next character in s
                i++;
            }
            // Always move forward in t
            j++;
        }
        
        // If we found all characters of s, i will equal s.length()
        return i == s.length();
    }
};
```

## Dry Run
`s = "abc", t = "ahbgdc"`
- `i = 0` ('a'), `j = 0` ('a'). Match! `i++`, `j++`.
- `i = 1` ('b'), `j = 1` ('h'). No match. `j++`.
- `i = 1` ('b'), `j = 2` ('b'). Match! `i++`, `j++`.
- `i = 2` ('c'), `j = 3` ('g'). No match. `j++`.
- `i = 2` ('c'), `j = 4` ('d'). No match. `j++`.
- `i = 2` ('c'), `j = 5` ('c'). Match! `i++`, `j++`.
- Loop breaks because `i == 3` (reaches `s.length()`).
- Return `3 == 3` -> `true`.

## Common Mistakes
- **Checking substrings instead of subsequences:** Make sure you don't reset `j` to 0 or try to match adjacent characters. A subsequence allows any number of characters to exist between matches in `t`.

## Similar Problems
- Longest Common Subsequence (DP version)
- String Compression
