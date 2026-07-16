# Minimum Window Substring

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Airbnb, Google, Facebook, Amazon

## Topic
Sliding Window / Hash Table / Strings

## Pattern
Variable Size Window with Dual Frequency Maps

## Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Input
- `s` string.
- `t` string.

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
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Edge Cases
- `s.length() < t.length()` (impossible, return `""`).
- `t` has duplicate characters (e.g., `t = "AAB"`. The window MUST contain at least two 'A's and one 'B').

## Intuition
This is the ultimate Sliding Window problem. We need to find the SHORTEST window that contains all required characters.
1. We need a way to know exactly what characters we need, and how many of them. A Hash Map (or frequency array) for `t` solves this. Let's call it `targetCount`.
2. We need to track what we currently have in our window. Let's call it `windowCount`.
3. We expand our window by moving `right` and adding `s[right]` to `windowCount`.
4. As soon as our window contains all the characters in `t` in the correct quantities, our window is **VALID**!
5. Because we want the MINIMUM window, once it's valid, we must try to **shrink** it from the left! We move `left++` and remove `s[left]` from `windowCount` until the window becomes invalid. We record the minimum size seen during this shrinking process.
6. Once invalid, we resume expanding `right` to find the next valid window.

To quickly check if the window is valid without looping through the entire hash map every time, we use a `have` counter and a `need` counter. `need` is the number of unique characters in `t`. `have` increases when `windowCount[char] == targetCount[char]`. When `have == need`, the window is valid!

## Optimal Approach (Sliding Window with Have/Need Pointers)
**Detailed explanation:**
1. If `t` is larger than `s`, return `""`.
2. Populate `targetCount` array (size 128 for ASCII) with the frequencies of `t`.
3. `need` is the number of unique characters in `t` (i.e. characters where `targetCount[c] > 0`).
4. Initialize `have = 0`. Initialize `windowCount` array (size 128) to 0.
5. Initialize `left = 0`, `minLen = INT_MAX`, `minLeft = 0`.
6. Loop `right` from `0` to `s.length() - 1`:
   - `c = s[right]`.
   - `windowCount[c]++`.
   - If `targetCount[c] > 0` AND `windowCount[c] == targetCount[c]`:
     - `have++`.
   - While `have == need`: (Window is valid!)
     - If `(right - left + 1) < minLen`:
       - `minLen = right - left + 1`.
       - `minLeft = left`.
     - Now shrink from left: `leftChar = s[left]`.
     - `windowCount[leftChar]--`.
     - If `targetCount[leftChar] > 0` AND `windowCount[leftChar] < targetCount[leftChar]`:
       - `have--`. (Window is now invalid!).
     - `left++`.
7. Return `minLen == INT_MAX ? "" : s.substr(minLeft, minLen)`.

**Time Complexity:** $O(S + T)$ where $S$ and $T$ are the lengths of the strings.
**Space Complexity:** $O(1)$ constant space (two arrays of size 128).

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
        
        vector<int> targetCount(128, 0);
        int need = 0;
        
        // Populate target map
        for (char c : t) {
            if (targetCount[c] == 0) need++;
            targetCount[c]++;
        }
        
        vector<int> windowCount(128, 0);
        int have = 0;
        
        int left = 0;
        int minLen = INT_MAX;
        int minLeft = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            windowCount[c]++;
            
            // If the character is part of target AND we just reached the exact required amount
            if (targetCount[c] > 0 && windowCount[c] == targetCount[c]) {
                have++;
            }
            
            // While the window is valid, try to shrink it
            while (have == need) {
                // Update minimum window
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                }
                
                // Remove the leftmost character
                char leftChar = s[left];
                windowCount[leftChar]--;
                
                // If removing it breaks the validity
                if (targetCount[leftChar] > 0 && windowCount[leftChar] < targetCount[leftChar]) {
                    have--;
                }
                
                left++;
            }
        }
        
        if (minLen == INT_MAX) return "";
        return s.substr(minLeft, minLen);
    }
};
```

## Dry Run
`s = "ADOBECODEBANC", t = "ABC"`
- `targetCount`: A=1, B=1, C=1. `need = 3`.
- Expand right:
  - `right=0 (A)`: `windowCount[A]=1`. `have=1`.
  - `right=1..4`: Adds D, O, B, E. `have=2` (when B is added).
  - `right=5 (C)`: `windowCount[C]=1`. `have=3`. VALID WINDOW!
- Window `[0..5]` ("ADOBEC"): `minLen = 6`.
  - Shrink left (A): `windowCount[A]=0`. `have=2`. Invalid! `left=1`.
- Expand right:
  - `right=6..9 (ODEB)`: Adds O, D, E, B. `have=2`.
  - `right=10 (A)`: `windowCount[A]=1`. `have=3`. VALID WINDOW!
- Window `[1..10]` ("DOBECODEBA"): `minLen` stays 6.
  - Shrink left until B is removed...
- Eventually `right=12 (C)`, `left=9 (B)`. Window: `[9..12]` ("BANC"). Length = 4. `minLen = 4`.
- Return `"BANC"`.

## Common Mistakes
- **Using a map instead of a vector for characters:** While `unordered_map<char, int>` works, it is significantly slower than an array `vector<int>(128, 0)` due to hashing overhead. For string sliding windows, always use an array.

## Similar Problems
- Substring with Concatenation of All Words
- Find All Anagrams in a String
