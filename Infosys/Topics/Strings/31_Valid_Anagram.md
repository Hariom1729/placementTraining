# Valid Anagram

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Strings / Hash Table

## Pattern
Frequency Counting

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
- Strings have different lengths (impossible to be anagrams).
- Identical strings (they are anagrams of themselves).

## Intuition
If two strings are anagrams, they must have exactly the same characters with exactly the same frequencies.
The easiest (but slightly slower) way is to sort both strings. If they are anagrams, the sorted strings will be identical.
The optimal way is to count the frequency of each character. Since the problem guarantees lowercase English letters, we can use a simple integer array of size 26.
We can do this in a single pass! For every character in `s`, we INCREMENT the count. For every character in `t`, we DECREMENT the count.
If they are anagrams, every increment will be perfectly cancelled out by a decrement, leaving the entire array filled with `0`s at the end.

## Brute Force Approach
**Explanation:** Sort both strings and compare them `s == t`.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$ or $O(N)$ depending on sorting algorithm.

## Optimal Approach (Frequency Array)
**Detailed explanation:**
1. If `s.length() != t.length()`, return `false`.
2. Create an array `vector<int> count(26, 0)`.
3. Loop through the strings (since they are the same length, one loop from `0` to `n` works):
   - `count[s[i] - 'a']++`
   - `count[t[i] - 'a']--`
4. Loop through the `count` array.
   - If any value is not `0`, return `false`.
5. Return `true`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space (array of size 26).

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If lengths differ, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        vector<int> count(26, 0);
        
        // Increment for s, decrement for t
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        // Check if all counts are zero
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        
        return true;
    }
};
```

## Dry Run
`s = "rat", t = "car"`
- Lengths are equal (3).
- `i=0`: `s[0]='r'` -> `count['r']++` (1). `t[0]='c'` -> `count['c']--` (-1).
- `i=1`: `s[1]='a'` -> `count['a']++` (1). `t[1]='a'` -> `count['a']--` (0).
- `i=2`: `s[2]='t'` -> `count['t']++` (1). `t[2]='r'` -> `count['r']--` (0).
- Array check: `count['c']` is -1, `count['t']` is 1. Not all zero!
Result: `false`.

## Common Mistakes
- **Using an `unordered_map`:** While conceptually correct, an `unordered_map<char, int>` has significant hashing overhead and memory allocation costs. For lowercase letters, a flat array is mathematically faster and uses practically zero memory.

## Similar Problems
- Group Anagrams
- Find All Anagrams in a String
