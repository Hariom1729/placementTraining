# Find All Anagrams in a String

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Sliding Window / Hash Table / Strings

## Pattern
Fixed Size Window with HashMap/Array

## Problem Statement
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

## Input
- `s` string.
- `p` string.

## Output
- Return a vector of integers (the starting indices).

## Sample Test Cases

**Example 1:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Edge Cases
- `p.length() > s.length()` (Impossible to find anagrams, return empty array).

## Intuition
This problem is **identical** to *Permutation in String*.
An Anagram is just a Permutation. The definition is literally exactly the same: a string with the exact same length and exact same character counts.

The only difference is that instead of returning `true` upon finding the first match, we just push the starting index of the window into a result array, and keep sliding the window until the very end of the string!

1. Build a frequency array `countP` of size 26 for `p`.
2. Build a frequency array `countS` of size 26 for the first window in `s` (length of `p`).
3. If they match, push index `0`.
4. Slide the window one character at a time.
5. The start index of the new window will be `i - p.length() + 1`. If the updated arrays match, push this index to the result array.

## Optimal Approach (Fixed Sliding Window)
**Detailed explanation:**
1. If `s.length() < p.length()`, return `{}`.
2. `vector<int> result;`
3. `vector<int> countP(26, 0);`
4. `vector<int> countS(26, 0);`
5. `int windowSize = p.length();`
6. Populate `countP` and the first `windowSize` characters of `countS`.
7. If `countP == countS`, `result.push_back(0)`.
8. Loop `i` from `windowSize` to `s.length() - 1`:
   - Add new character: `countS[s[i] - 'a']++`.
   - Remove old character: `countS[s[i - windowSize] - 'a']--`.
   - Check match: if `countP == countS`:
     - The starting index of the current window is exactly `i - windowSize + 1`.
     - `result.push_back(i - windowSize + 1)`.
9. Return `result`.

**Time Complexity:** $O(N)$ where $N$ is the length of `s`.
**Space Complexity:** $O(1)$ constant auxiliary space.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        
        if (s.length() < p.length()) {
            return result;
        }
        
        vector<int> countP(26, 0);
        vector<int> countS(26, 0);
        int windowSize = p.length();
        
        // Initialize counts for p and the first window of s
        for (int i = 0; i < windowSize; i++) {
            countP[p[i] - 'a']++;
            countS[s[i] - 'a']++;
        }
        
        // Check if the very first window is an anagram
        if (countP == countS) {
            result.push_back(0);
        }
        
        // Slide the window across s
        for (int i = windowSize; i < s.length(); i++) {
            // Add the new character entering the window
            countS[s[i] - 'a']++;
            
            // Remove the character that is left behind
            countS[s[i - windowSize] - 'a']--;
            
            // Check if the updated window is an anagram
            if (countP == countS) {
                result.push_back(i - windowSize + 1);
            }
        }
        
        return result;
    }
};
```

## Dry Run
`s = "cbaebabacd", p = "abc"`
- `windowSize = 3`. `countP` = `{a:1, b:1, c:1}`.
- First window `s[0..2]` = `"cba"`. `countS` = `{a:1, b:1, c:1}`.
- Matches! Push `0`. Result = `[0]`.
- Slide `i=3` ('e'):
  - Add 'e', remove `s[3-3]` ('c').
  - `countS` = `{a:1, b:1, e:1}`. No match.
- Slide `i=4` ('b'):
  - Add 'b', remove `s[4-3]` ('b').
  - `countS` = `{a:1, b:1, e:1}`. No match.
- Slide `i=5` ('a'):
  - Add 'a', remove `s[5-3]` ('a').
  - `countS` = `{a:1, b:1, e:1}`. No match.
- Slide `i=6` ('b'):
  - Add 'b', remove `s[6-3]` ('e').
  - `countS` = `{a:1, b:2}`. No match.
- Slide `i=7` ('a'):
  - Add 'a', remove `s[7-3]` ('b').
  - `countS` = `{a:2, b:1}`. No match.
- Slide `i=8` ('c'):
  - Add 'c', remove `s[8-3]` ('a').
  - `countS` = `{a:1, b:1, c:1}`.
  - Matches! Starting index = `8 - 3 + 1 = 6`. Push `6`. Result = `[0, 6]`.
- Output `[0, 6]`.

## Common Mistakes
- **Off-by-one errors with the start index:** The character leaving the window is at `i - windowSize`. The character entering the window is at `i`. The first character OF the newly shifted window is therefore `i - windowSize + 1`.

## Similar Problems
- Permutation in String
- Group Anagrams
