# Valid Anagram

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Google, Bloomberg

## Topic
Strings / Hashing

## Pattern
Frequency Array

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Input
- `s` string.
- `t` string.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**
```
Input: s = "rat", t = "car"
Output: false
```

## Edge Cases
- Strings of different lengths (can never be anagrams, return `false` immediately).
- Strings of length 1.

## Intuition
An anagram simply means both strings have the exact same characters with the exact same frequencies.
If we sort both strings, they should become identical. This takes $O(N \log N)$ time.
Can we do it in $O(N)$ time? Yes, using Hashing!
Since the strings only contain lowercase English letters, we don't even need a complex Hash Map (`unordered_map`). We can just use a fixed-size array of 26 integers.
We iterate through the first string and increment the count for each character.
Then we iterate through the second string and decrement the count for each character.
Finally, if the array contains all zeros, they are anagrams!

## Brute Force Approach
**Explanation:** Sort both strings. If `s == t`, they are anagrams.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$ or $O(N)$ depending on the sorting algorithm used.

## Optimal Approach (Frequency Array)
**Detailed explanation:**
1. Check if `s.length() != t.length()`. If so, return `false`.
2. Create an array or vector `count` of size 26, initialized to 0.
3. Loop through both strings simultaneously (since they have the same length):
   - `count[s[i] - 'a']++`
   - `count[t[i] - 'a']--`
4. Loop through the `count` array. If any value is not `0`, return `false`.
5. Return `true`.

**Time Complexity:** $O(N)$ where $N$ is the length of the strings.
**Space Complexity:** $O(1)$ because the frequency array size is always 26, which is constant.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If lengths differ, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Use an array to store character frequencies
        vector<int> count(26, 0);
        
        // Increment for string s, decrement for string t
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        // Check if all frequencies are 0
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
};
```

## Dry Run
`s = "rat"`, `t = "car"`
- Lengths are equal (3).
- `i = 0`: `s[0] = 'r'`, `count['r']++`. `t[0] = 'c'`, `count['c']--`.
- `i = 1`: `s[1] = 'a'`, `count['a']++`. `t[1] = 'a'`, `count['a']--`.
- `i = 2`: `s[2] = 't'`, `count['t']++`. `t[2] = 'r'`, `count['r']--`.
- Final `count` array:
  - `count['a'] = 0` (1 - 1)
  - `count['c'] = -1`
  - `count['r'] = 0` (1 - 1)
  - `count['t'] = 1`
- Loop sees `count['c'] == -1 != 0`. Returns `false`.

## Common Mistakes
- **Using `unordered_map` instead of a fixed array:** While `unordered_map` works, it is much slower due to hashing overhead and dynamic memory allocation. Always use a 26-size array when dealing strictly with lowercase English letters.

## Similar Problems
- Group Anagrams
- Find All Anagrams in a String
