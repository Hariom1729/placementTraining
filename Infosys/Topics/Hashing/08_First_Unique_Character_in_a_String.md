# First Unique Character in a String

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Bloomberg, Microsoft, Apple

## Topic
Hashing / Strings

## Pattern
Frequency Array

## Problem Statement
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Input
- `s` string.

## Output
- Return an integer (the index).

## Sample Test Cases

**Example 1:**
```
Input: s = "leetcode"
Output: 0
Explanation: 'l' is the first character that only appears once.
```

**Example 2:**
```
Input: s = "loveleetcode"
Output: 2
Explanation: 'v' is the first unique character (at index 2).
```

**Example 3:**
```
Input: s = "aabb"
Output: -1
Explanation: All characters appear at least twice.
```

## Edge Cases
- All characters repeat. (Return `-1`).
- String length is 1. (Return `0`).

## Intuition
To know if a character is "unique", we must know how many times it appears in the *entire* string. This means we cannot find the answer on the fly; we MUST scan the string at least once to count the frequencies.
After we know the frequencies of all characters, we need to find the "first" unique one. How?
Simply scan the original string `s` a SECOND time from left to right! 
For each character `s[i]`, we check its frequency. The first one we hit that has a frequency of exactly `1` is our answer! Return its index `i`.

Because the string only contains lowercase English letters, a fixed array of size 26 is much faster than an `unordered_map`.

## Brute Force Approach
**Explanation:** For every character, scan the rest of the string to see if it appears again.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Optimal Approach (Frequency Array / 2-Pass)
**Detailed explanation:**
1. Create a `vector<int> count(26, 0)`.
2. First Pass: Loop `c` through `s`.
   - `count[c - 'a']++`.
3. Second Pass: Loop `i` from 0 to `s.length() - 1`.
   - If `count[s[i] - 'a'] == 1`:
     - `return i`.
4. If loop finishes without returning, `return -1`.

**Time Complexity:** $O(N)$ since we scan the string exactly twice.
**Space Complexity:** $O(1)$ because the frequency array is always size 26, independent of string length.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> count(26, 0);
        
        // Pass 1: Count the frequency of each character
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Pass 2: Find the first character with a frequency of 1
        for (int i = 0; i < s.length(); i++) {
            if (count[s[i] - 'a'] == 1) {
                return i;
            }
        }
        
        return -1; // No unique character found
    }
};
```

## Dry Run
`s = "loveleetcode"`
- Pass 1:
  `l:2, o:2, v:1, e:4, t:1, c:1, d:1`.
- Pass 2:
  - `i=0, s[0]='l'`: count is 2.
  - `i=1, s[1]='o'`: count is 2.
  - `i=2, s[2]='v'`: count is 1! We found it!
  - Return `2`.

## Common Mistakes
- **Iterating over the frequency array to find the answer:** If you iterate `for(int i=0; i<26; i++) { if(count[i]==1) ... }`, you will find the first alphabetically unique character (like 'a'), not the first unique character in the *order they appeared in the string*. You MUST iterate over the original string `s` in the second pass.

## Similar Problems
- Sort Characters By Frequency
- Find the Difference
