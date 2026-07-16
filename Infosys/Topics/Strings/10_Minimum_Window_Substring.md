# Minimum Window Substring

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Uber

## Topic
Strings / Hash Table

## Pattern
Sliding Window

## Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.
The testcases will be generated such that the answer is unique.

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Input
- `s` string (haystack).
- `t` string (needle components).

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
```

## Edge Cases
- `s` is shorter than `t` (Impossible, return `""`).
- `t` has duplicates (e.g. `t="aa"`, the window must contain at least two `a`s).

## Intuition
This is the ultimate **Sliding Window** problem.
We need to track the frequencies of characters required by `t`. 
1. Use an array `map` to store the frequencies of all characters in `t`. We also need a counter `required` which is the length of `t`.
2. Expand the window by moving `right`. For every character `s[right]`:
   - If this character is one we need (`map[s[right]] > 0`), we decrement `required`.
   - Decrement the map frequency: `map[s[right]]--`. (It can go negative! Negative means we have *more* of this character than we need, which is totally fine).
3. When `required == 0`, our window contains ALL characters of `t`! This is a valid window.
4. Now, we try to SHRINK the window from the `left` to make it as small as possible.
   - We record the length. If it's smaller than our `minLen`, we save it!
   - We increment `map[s[left]]++` because we are throwing this character out of our window.
   - If `map[s[left]]` becomes `> 0`, it means we just threw away a character we ACTUALLY NEEDED. So `required` goes up by 1 (`required++`). The window is now invalid, and the inner loop stops.
5. Move `right` to find the missing character again.

## Brute Force Approach
**Explanation:** For every possible starting index `i`, loop `j` to the end. Check if the substring `i...j` contains all characters of `t`.
**Time Complexity:** $O(N^3)$ or $O(N^2)$ with optimization.
**Space Complexity:** $O(M)$ for frequency map.

## Optimal Approach (Sliding Window with Frequency Map)
**Detailed explanation:**
1. Check if `s.length() < t.length()`. Return `""`.
2. Create `vector<int> map(128, 0)`.
3. Fill the map with frequencies from `t`: `for(char c : t) map[c]++;`.
4. Initialize `left = 0`, `right = 0`, `required = t.length()`.
5. Initialize `minLen = INT_MAX` and `startIndex = 0`.
6. `while (right < s.length())`:
   - If `map[s[right]] > 0`, it means this character is needed. Decrease `required`.
   - ALWAYS decrease `map[s[right]]`.
   - `right++`.
   - `while (required == 0)` (Window is valid!):
     - Update `minLen` and `startIndex` if `right - left < minLen`.
     - Now we throw away `s[left]`. Increase `map[s[left]]`.
     - If `map[s[left]] > 0`, it means we just lost a needed character! Increase `required`.
     - `left++`.
7. If `minLen == INT_MAX`, return `""`. Else return `s.substr(startIndex, minLen)`.

**Time Complexity:** $O(N + M)$ because both `left` and `right` traverse the string `s` at most once.
**Space Complexity:** $O(1)$ constant space because the array is strictly size 128 (ASCII characters).

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) return "";
        
        // 128 is enough for all ASCII characters
        vector<int> map(128, 0);
        for (char c : t) {
            map[c]++;
        }
        
        int left = 0;
        int right = 0;
        int required = t.length();
        
        int minLen = INT_MAX;
        int startIndex = 0;
        
        while (right < s.length()) {
            // Expand window
            if (map[s[right]] > 0) {
                required--;
            }
            map[s[right]]--; // Can become negative if we have surplus
            right++;
            
            // When window is valid, try to shrink it
            while (required == 0) {
                // Record the new minimum window
                if (right - left < minLen) {
                    minLen = right - left;
                    startIndex = left;
                }
                
                // Shrink window from the left
                map[s[left]]++;
                if (map[s[left]] > 0) {
                    required++; // We removed a needed character
                }
                left++;
            }
        }
        
        return minLen == INT_MAX ? "" : s.substr(startIndex, minLen);
    }
};
```

## Dry Run
`s = "ADOBECODEBANC", t = "ABC"`
`map['A']=1, map['B']=1, map['C']=1`. `req = 3`.
- `R=0 ('A')`: `map['A']>0`, `req=2`. `map['A']=0`. `R=1`.
- `R=1, 2 ('D', 'O')`: map goes negative. `req=2`. `R=3`.
- `R=3 ('B')`: `map['B']>0`, `req=1`. `map['B']=0`. `R=4`.
- `R=4, 5 ('E', 'C')`: map goes negative for E. For C, `req=0`. `map['C']=0`. `R=6`.
- `req == 0`! Window is `ADOBEC`. Length 6. `minLen = 6`.
  - Throw left `A`. `map['A']++` becomes 1. `map['A'] > 0` so `req = 1`. `L=1`.
- Need 1 character ('A'). `R` continues to 10 ('A').
- `R=10 ('A')`: `req=0`. Window valid again: `DOBECODEBA`.
  - Shrink left until we throw away B.
  - New window `CODEBA` length 6.
  - Throw C. `req=1`.
- `R` hits C at end. `BANC` becomes window length 4. `minLen = 4`.
Result: `"BANC"`.

## Common Mistakes
- **Confusing pointer indexing for `substr()`:** Notice that `right++` happens BEFORE the while loop. This means the length of the window is exactly `right - left`. If you don't do `right++` early, length is `right - left + 1`. Both work, but stick strictly to one logic format to avoid off-by-one errors.
- **Using `unordered_map` for frequency:** Checking map sizes in C++ is highly inefficient. Always use a 128 integer array for ASCII window problems.

## Similar Problems
- Substring with Concatenation of All Words
- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
