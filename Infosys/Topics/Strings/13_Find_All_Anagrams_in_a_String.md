# Find All Anagrams in a String

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Google, Microsoft

## Topic
Strings / Hash Table

## Pattern
Fixed-Size Sliding Window

## Problem Statement
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

## Input
- `s` string (haystack).
- `p` string (needle).

## Output
- Return a vector of integers representing indices.

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
- `s` is shorter than `p`. Return empty array.
- No anagrams found. Return empty array.

## Intuition
This combines checking for **Valid Anagrams** with a **Sliding Window**!
Since all anagrams of `p` must have the exact same length as `p`, our sliding window must be of a **fixed size** (`p.length()`).
We use two frequency arrays of size 26 (one for `p`, one for the current window in `s`).
1. We initialize both arrays for the first `p.length()` characters.
2. If they match, we add index 0 to our result.
3. Then, we "slide" the window across `s` one character at a time:
   - We **add** the new character on the right to our window frequency array.
   - We **remove** the old character on the left from our window frequency array.
   - We compare the two frequency arrays. If they match, we record the `left` index!

*Optimization:* Instead of doing a full 26-character array comparison at every step, we could track an exact `matchCount`. However, since checking 26 integers is insanely fast in C++, a direct `sCount == pCount` array comparison is optimal and much cleaner to implement.

## Brute Force Approach
**Explanation:** At every index `i`, extract a substring of length `p.length()`, sort it, and compare it to a sorted `p`.
**Time Complexity:** $O(N \times M \log M)$
**Space Complexity:** $O(M)$ for substring extraction.

## Optimal Approach (Fixed-Size Sliding Window)
**Detailed explanation:**
1. If `s.length() < p.length()`, return an empty vector.
2. Create `vector<int> pCount(26, 0)` and `vector<int> sCount(26, 0)`.
3. Populate `pCount` and the initial window for `sCount` (first `p.length()` chars).
4. Create `vector<int> ans`.
5. If `pCount == sCount`, push `0` to `ans`.
6. Loop from `i = p.length()` to `s.length() - 1`:
   - The character entering the window on the right is `s[i]`. Increment its count: `sCount[s[i] - 'a']++`.
   - The character leaving the window on the left is `s[i - p.length()]`. Decrement its count: `sCount[s[i - p.length()] - 'a']--`.
   - If `pCount == sCount`, the new window is an anagram! Push the left bound `i - p.length() + 1` to `ans`.
7. Return `ans`.

**Time Complexity:** $O(N)$ where $N$ is the length of `s`. We slide the window in one pass. Comparing 26-element arrays takes $O(1)$ constant time.
**Space Complexity:** $O(1)$ constant auxiliary space (two arrays of size 26).

## C++ Solution

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        int sLen = s.length();
        int pLen = p.length();
        
        // If s is shorter than p, it can't contain any anagrams of p
        if (sLen < pLen) {
            return ans;
        }
        
        // Frequency arrays for 'p' and the sliding window in 's'
        vector<int> pCount(26, 0);
        vector<int> sCount(26, 0);
        
        // Populate pCount and the first window of sCount
        for (int i = 0; i < pLen; i++) {
            pCount[p[i] - 'a']++;
            sCount[s[i] - 'a']++;
        }
        
        // Check if the first window is a match
        if (pCount == sCount) {
            ans.push_back(0);
        }
        
        // Slide the window across the rest of string 's'
        for (int i = pLen; i < sLen; i++) {
            // Add the new character on the right to the window
            sCount[s[i] - 'a']++;
            
            // Remove the old character on the left from the window
            sCount[s[i - pLen] - 'a']--;
            
            // Compare the frequency arrays
            if (pCount == sCount) {
                ans.push_back(i - pLen + 1); // The start index of the current window
            }
        }
        
        return ans;
    }
};
```

## Dry Run
`s = "cbaebabacd", p = "abc"`
- `pLen = 3`.
- `pCount = {a:1, b:1, c:1}`
- **Initial Window (Indices 0,1,2 - "cba"):**
  - `sCount = {a:1, b:1, c:1}`
  - `sCount == pCount` -> `ans.push_back(0)`.
- **Slide 1 (i=3, char 'e'):**
  - Entering: `s[3] = 'e'`. `sCount['e']++`.
  - Leaving: `s[0] = 'c'`. `sCount['c']--`.
  - Window is "bae". Not equal to pCount.
- **Slide 2 (i=4, char 'b'):**
  - Entering: `s[4] = 'b'`. `sCount['b']++`.
  - Leaving: `s[1] = 'b'`. `sCount['b']--`.
  - Window is "aeb". Not equal.
- ...
- **Slide 6 (i=8, char 'c'):**
  - Entering: `s[8] = 'c'`. `sCount['c']++`.
  - Leaving: `s[5] = 'b'`. `sCount['b']--`.
  - Window is "bac". `sCount == pCount`. `ans.push_back(8 - 3 + 1) = ans.push_back(6)`.
Result: `[0, 6]`.

## Common Mistakes
- **Using an expanding Sliding Window `(right - left)`:** This is not Minimum Window Substring! The window MUST be exactly `p.length()` at all times. The fixed-size `for` loop approach is massively simpler and less error-prone than trying to manage `left` and `right` pointers dynamically.
- **Trying to use Unordered Map:** Just like Valid Anagram, using `unordered_map` is incredibly slow compared to a flat `vector<int>(26)` array in C++. Comparing two vectors `vec1 == vec2` compiles down to ultra-fast memory checks, while comparing maps requires heavy iteration overhead.

## Similar Problems
- Valid Anagram
- Permutation in String (Exact same problem, but returns boolean instead of indices)
- Minimum Window Substring
