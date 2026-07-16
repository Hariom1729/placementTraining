# Longest Substring Without Repeating Characters

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google, Bloomberg

## Topic
Strings / Hash Table

## Pattern
Sliding Window

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Input
- `s` string.

## Output
- Return an integer representing the maximum length.

## Sample Test Cases

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Edge Cases
- Empty string (`""`). Returns 0.
- String with all identical characters. Returns 1.
- String with all unique characters. Returns the string's length.

## Intuition
To find the longest substring, we can use the **Sliding Window** technique with two pointers: `left` and `right`.
The `right` pointer expands the window by moving forward and consuming characters.
If we encounter a character that is ALREADY in our window (a repeat), our current window is invalid.
To make it valid again, we must shrink the window from the left by moving the `left` pointer forward until the repeating character is removed!
We keep track of the characters currently in the window using an `unordered_set` or a boolean array (since ASCII characters are limited to 256).
At every valid step, we update `maxLength = max(maxLength, right - left + 1)`.

**Optimization:** Instead of just checking if a character is in the set and moving `left` one by one, we can store the **exact index** of every character in an `unordered_map` or an integer array. If we hit a duplicate, we can instantly jump `left` to `last_seen_index + 1`!

## Brute Force Approach
**Explanation:** Generate all possible substrings ( $O(N^2)$ pairs of indices), check if each has duplicate characters ($O(N)$), and return the max length.
**Time Complexity:** $O(N^3)$
**Space Complexity:** $O(\min(N, M))$ where $M$ is the character set size.

## Optimal Approach (Optimized Sliding Window)
**Detailed explanation:**
1. Initialize an array `vector<int> charIndex(256, -1)` to store the last seen index of each ASCII character. (Using an array of 256 integers is much faster than `unordered_map`).
2. Initialize `left = 0`, `maxLength = 0`.
3. Iterate `right` from 0 to `s.length() - 1`:
   - Let `currentChar = s[right]`.
   - If `charIndex[currentChar]` is NOT `-1`, it means we have seen this character before. 
   - However, we only care if we saw it **inside our current window**. If `charIndex[currentChar] >= left`, we must update `left` to `charIndex[currentChar] + 1` to instantly exclude the duplicate.
   - Update the last seen index: `charIndex[currentChar] = right`.
   - Calculate current window length: `right - left + 1`.
   - Update `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

**Time Complexity:** $O(N)$ because both `left` and `right` pointers only move forward, visiting each character at most once.
**Space Complexity:** $O(1)$ constant space because the array size is always 256 regardless of the input string length.

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Array to store the last index of each ASCII character
        vector<int> charIndex(256, -1);
        
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s[right];
            
            // If the character was seen before AND is inside the current window,
            // instantly jump the left pointer to avoid the duplicate
            if (charIndex[currentChar] >= left) {
                left = charIndex[currentChar] + 1;
            }
            
            // Update the last seen index for the current character
            charIndex[currentChar] = right;
            
            // Update the maximum length
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

## Dry Run
`s = "abcabcbb"`
- Init: `left = 0`, `maxLen = 0`, `charIndex` all `-1`.
- `right = 0` ('a'): `charIndex['a']` is -1. `charIndex['a'] = 0`. `maxLen = max(0, 1) = 1`.
- `right = 1` ('b'): `charIndex['b']` is -1. `charIndex['b'] = 1`. `maxLen = max(1, 2) = 2`.
- `right = 2` ('c'): `charIndex['c']` is -1. `charIndex['c'] = 2`. `maxLen = max(2, 3) = 3`.
- `right = 3` ('a'): `charIndex['a']` is 0. Since `0 >= left (0)`, `left = 0 + 1 = 1`. `charIndex['a'] = 3`. Window is "bca". `maxLen = max(3, 3) = 3`.
- `right = 4` ('b'): `charIndex['b']` is 1. Since `1 >= left (1)`, `left = 1 + 1 = 2`. `charIndex['b'] = 4`. Window is "cab". `maxLen = max(3, 3) = 3`.
- `right = 7` ('b'): `charIndex['b']` is 6. `6 >= left(5)`. `left = 7`. Window is "b". `maxLen = max(3, 1) = 3`.
Result: 3.

## Common Mistakes
- **Forgetting to check if the duplicate is inside the window:** If you just check `if (charIndex[currentChar] != -1)`, you might update `left` to an older index that is OUTSIDE your current window, moving the `left` pointer BACKWARDS and breaking the entire sliding window logic. You MUST check `charIndex[currentChar] >= left`.
- **Using sets and moving left one-by-one:** The `while(set.count(s[right])) { set.erase(s[left++]); }` method works and is valid $O(N)$, but the index jump method is strictly faster and shows a higher level of mastery to the interviewer.

## Similar Problems
- Longest Substring with At Most Two Distinct Characters
- Subarray Product Less Than K
- Minimum Window Substring
