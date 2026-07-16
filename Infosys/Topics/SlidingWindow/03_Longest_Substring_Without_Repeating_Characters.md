# Longest Substring Without Repeating Characters

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google, Apple

## Topic
Sliding Window / Hash Table / Strings

## Pattern
Variable Size Window with HashSet/HashMap

## Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Input
- `s` string.

## Output
- Return an integer.

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
- Empty string (returns `0`).
- String with all identical characters (returns `1`).
- String with no repeating characters at all (returns `s.length()`).

## Intuition
This is the quintessential **Sliding Window** problem.
We want to find the longest contiguous sequence (substring) that satisfies a condition (no duplicates).

We can maintain a window `[left, right]`. We also need a way to quickly check if a character is already inside our window. An `unordered_set` (or a boolean array of size 256 for ASCII) is perfect for this!

- We expand the window by moving `right` forward and attempting to add `s[right]` to our set.
- If `s[right]` is NOT in the set, great! We add it, the window remains valid, and we update our `maxLength`.
- If `s[right]` IS already in the set, our window is now invalid! We must shrink the window from the left until the duplicate character is removed.
  - To do this, we repeatedly remove `s[left]` from the set and increment `left`, until `s[right]` is no longer in the set.
  - Then we can finally add `s[right]` and continue expanding.

## Optimal Approach (Sliding Window with Hash Set)
**Detailed explanation:**
1. Initialize `left = 0`, `maxLength = 0`.
2. Create an `unordered_set<char> windowChars` (Alternatively, `vector<bool> seen(256, false)` is much faster for ASCII).
3. Loop `right` from `0` to `s.length() - 1`:
   - While `s[right]` is already in `windowChars`:
     - Remove `s[left]` from `windowChars`.
     - `left++`.
   - Now `s[right]` is guaranteed to not be in the set.
   - Insert `s[right]` into `windowChars`.
   - Update `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

**Time Complexity:** $O(N)$ because both `left` and `right` pointers traverse the string at most once.
**Space Complexity:** $O(\min(N, M))$ where $M$ is the size of the charset (e.g., 256). Essentially $O(1)$ space.

## C++ Solution

```cpp
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int maxLength = 0;
        unordered_set<char> windowChars;
        
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s[right];
            
            // If the character is already in the window, shrink from the left
            // until the duplicate character is removed
            while (windowChars.find(currentChar) != windowChars.end()) {
                windowChars.erase(s[left]);
                left++;
            }
            
            // Add the new character to the window
            windowChars.insert(currentChar);
            
            // Update the maximum length found so far
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};

/*
// Ultra-fast ASCII array solution (Preferred for competitive programming)
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<bool> seen(256, false);
        int left = 0, maxLength = 0;
        for (int right = 0; right < s.length(); right++) {
            while (seen[s[right]]) {
                seen[s[left]] = false;
                left++;
            }
            seen[s[right]] = true;
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
*/
```

## Dry Run
`s = "abcabcbb"`
- `right = 0` ('a'). Set = `{'a'}`. Length = 1.
- `right = 1` ('b'). Set = `{'a', 'b'}`. Length = 2.
- `right = 2` ('c'). Set = `{'a', 'b', 'c'}`. Length = 3. `max = 3`.
- `right = 3` ('a'). 'a' is already in set!
  - Shrink: remove `s[left]` ('a'), `left++ -> 1`.
  - Now 'a' is not in set. Add 'a'. Set = `{'b', 'c', 'a'}`. Window: `[1, 3] = "bca"`. Length = 3.
- `right = 4` ('b'). 'b' is in set!
  - Shrink: remove `s[left]` ('b'), `left++ -> 2`.
  - Add 'b'. Set = `{'c', 'a', 'b'}`. Window: `[2, 4] = "cab"`. Length = 3.
- `right = 5` ('c'). 'c' is in set!
  - Shrink: remove `s[left]` ('c'), `left++ -> 3`.
  - Add 'c'. Set = `{'a', 'b', 'c'}`. Window: `[3, 5] = "abc"`. Length = 3.
- `right = 6` ('b'). 'b' is in set!
  - Shrink: remove 'a', `left=4`.
  - Still in set! Shrink: remove 'b', `left=5`.
  - Add 'b'. Set = `{'c', 'b'}`. Window: `[5, 6] = "cb"`. Length = 2.
- Output: 3.

## Common Mistakes
- **Clearing the whole set:** When a duplicate is found, some candidates do `set.clear()` and `left = right`. This is completely wrong, because a valid substring might start immediately AFTER the first occurrence of the duplicate! You must shrink element by element.

## Similar Problems
- Longest Repeating Character Replacement
- Subarrays with K Different Integers
