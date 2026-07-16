# Permutation in String

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Microsoft, Amazon, Oracle

## Topic
Sliding Window / Hash Table / Strings

## Pattern
Fixed Size Window with HashMap/Array

## Problem Statement
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

## Constraints
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Input
- `s1` string.
- `s2` string.

## Output
- Return a boolean.

## Sample Test Cases

**Example 1:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Edge Cases
- `s1.length() > s2.length()` (Impossible to find permutation, return `false`).

## Intuition
A permutation of `s1` means a string that has the EXACT same length as `s1`, and the EXACT same character frequencies as `s1`. The order doesn't matter.

This is a textbook **Fixed Size Sliding Window** problem!
The size of our window is ALWAYS exactly `s1.length()`.
We just need to slide a window of size `s1.length()` across `s2`. At every step, we check if the character frequencies inside our window perfectly match the character frequencies of `s1`.

To do this efficiently:
1. Create a frequency array for `s1` (`count1`).
2. Create a frequency array for our current window in `s2` (`count2`).
3. Slide the window one character to the right:
   - Add the new character entering the window to `count2`.
   - Remove the old character leaving the window from `count2`.
   - Compare `count1` and `count2`. If they are exactly identical, we found a permutation!

Since the arrays are always exactly size 26 (lowercase English letters), comparing them takes $O(26) = O(1)$ time!

## Optimal Approach (Fixed Sliding Window)
**Detailed explanation:**
1. If `s1.length() > s2.length()`, return `false`.
2. Initialize two vectors of size 26 with zeros: `count1` and `count2`.
3. Populate `count1` and the first window of `count2` (first `s1.length()` characters).
4. If `count1 == count2`, return `true`.
5. Loop `i` from `s1.length()` to `s2.length() - 1`:
   - The new character entering the window is `s2[i]`. Add it to `count2`: `count2[s2[i] - 'a']++`.
   - The old character leaving the window is `s2[i - s1.length()]`. Remove it: `count2[s2[i - s1.length()] - 'a']--`.
   - If `count1 == count2`, return `true`.
6. Return `false`.

**Time Complexity:** $O(N)$ where $N$ is the length of `s2`. (Comparing arrays of size 26 takes $O(1)$).
**Space Complexity:** $O(1)$ constant space (two arrays of size 26).

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) {
            return false;
        }
        
        vector<int> count1(26, 0);
        vector<int> count2(26, 0);
        
        int windowSize = s1.length();
        
        // Initialize the frequency maps for s1 and the first window of s2
        for (int i = 0; i < windowSize; i++) {
            count1[s1[i] - 'a']++;
            count2[s2[i] - 'a']++;
        }
        
        // Check if the very first window is a match
        if (count1 == count2) {
            return true;
        }
        
        // Slide the window across s2
        for (int i = windowSize; i < s2.length(); i++) {
            // Add the new character entering the window
            count2[s2[i] - 'a']++;
            
            // Remove the character that is left behind
            count2[s2[i - windowSize] - 'a']--;
            
            // Check if the updated window is a match
            if (count1 == count2) {
                return true;
            }
        }
        
        return false;
    }
};
```

## Dry Run
`s1 = "ab", s2 = "eidbaooo"`
- `windowSize = 2`.
- `count1` has `{a:1, b:1}`.
- First window in `s2` ("ei"): `count2` has `{e:1, i:1}`. No match.
- Slide to `i = 2` ('d'):
  - Add 'd', remove 'e'. Window = "id". `count2` has `{i:1, d:1}`. No match.
- Slide to `i = 3` ('b'):
  - Add 'b', remove 'i'. Window = "db". `count2` has `{d:1, b:1}`. No match.
- Slide to `i = 4` ('a'):
  - Add 'a', remove 'd'. Window = "ba". `count2` has `{b:1, a:1}`.
  - `count1 == count2`. MATCH!
- Return `true`.

## Common Mistakes
- **Generating all permutations:** Generating all permutations of `s1` takes $O(K!)$ time. Even if you generated them, finding if any exist in `s2` would be overwhelmingly slow. Always rely on character counts when order doesn't matter!
- **Using Unordered Maps:** In C++, `unordered_map == unordered_map` is technically supported, but hashing and map lookups are slow. Because the problem explicitly says "lowercase English letters", an array of size 26 (`vector<int>`) is vastly faster and supports direct equality checking `count1 == count2` natively in C++.

## Similar Problems
- Find All Anagrams in a String (Exact same logic, just returns all starting indices instead of a boolean).
- Minimum Window Substring
