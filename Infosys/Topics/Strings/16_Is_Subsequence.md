# Is Subsequence

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google, Bloomberg

## Topic
Strings / Two Pointers

## Pattern
Two Pointers

## Problem Statement
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Constraints
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

## Input
- `s` string (subsequence candidate).
- `t` string (original string).

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Edge Cases
- `s` is an empty string (always a valid subsequence, return `true`).
- `s` is longer than `t` (impossible, return `false`).
- `s == t` (return `true`).

## Intuition
Because a subsequence must maintain the **relative order** of characters, we can simply scan through the original string `t` from left to right, looking for the characters of `s` in order!
We use two pointers: `i` for string `s`, and `j` for string `t`.
We iterate `j` through `t`. If the current character `t[j]` matches the character we are looking for `s[i]`, we have found a piece of our subsequence! So we increment `i` to look for the next character.
If `t[j]` doesn't match `s[i]`, we simply ignore it and move `j` to the next character in `t`.
If our pointer `i` ever reaches the end of `s` (`i == s.length()`), it means we found EVERY character of `s` inside `t` in the correct order! Return `true`.

## Brute Force Approach
**Explanation:** Generate all $2^N$ possible subsequences of `t` and check if any of them perfectly match `s`.
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$ for recursion.

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. Initialize two pointers: `i = 0` (for `s`) and `j = 0` (for `t`).
2. If `s.length() == 0`, return `true`.
3. If `s.length() > t.length()`, return `false`.
4. Loop while `i < s.length()` and `j < t.length()`:
   - If `s[i] == t[j]`, we found a match. Increment `i`.
   - Regardless of a match, increment `j` to continue scanning `t`.
5. After the loop, if `i == s.length()`, it means all characters of `s` were found. Return `true`. Otherwise, return `false`.

**Time Complexity:** $O(N)$ where $N$ is the length of `t`. We iterate through `t` at most once.
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
        
        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                i++; // Move pointer in s only on a match
            }
            j++; // Always move pointer in t
        }
        
        // If i reached the end of s, all characters were found in order
        return i == s.length();
    }
};
```

## Dry Run
`s = "abc"`, `t = "ahbgdc"`
- `i=0, j=0`: `s[0]=='a'`, `t[0]=='a'`. Match! `i=1, j=1`.
- `i=1, j=1`: `s[1]=='b'`, `t[1]=='h'`. No match. `j=2`.
- `i=1, j=2`: `s[1]=='b'`, `t[2]=='b'`. Match! `i=2, j=3`.
- `i=2, j=3`: `s[2]=='c'`, `t[3]=='g'`. No match. `j=4`.
- `i=2, j=4`: `s[2]=='c'`, `t[4]=='d'`. No match. `j=5`.
- `i=2, j=5`: `s[2]=='c'`, `t[5]=='c'`. Match! `i=3, j=6`.
- Loop condition `j < 6` fails. Loop ends.
- Return `i == s.length()` -> `3 == 3` -> `true`.

## Common Mistakes
- **Using a nested loop or `find()`:** Trying to repeatedly call `t.find(s[i], last_index)` works, but is less efficient and more prone to index-out-of-bounds errors than the incredibly simple two-pointer approach.

## Similar Problems
- Number of Matching Subsequences
- Shortest Way to Form String
