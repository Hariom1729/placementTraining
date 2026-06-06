# Problem 4: Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

## Input Format
- A single string `s`.

## Output Format
- An integer representing the length of the longest substring.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Approach: Sliding Window + Hashing

This is a classic problem for the **Sliding Window** technique.
1. We use two pointers, `left` and `right`, to represent the current window.
2. We use an `std::unordered_set<char>` to store the characters currently in the window.
3. We move `right` pointer to expand the window.
4. If `s[right]` is already in the set, we must shrink the window from the `left` by removing `s[left]` and incrementing `left`, until `s[right]` is no longer in the set.
5. If it's not in the set, we insert it, and calculate the maximum window size (`right - left + 1`).
6. We continue this until `right` reaches the end of the string.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLength = 0;
        unordered_set<char> charSet;
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            // If duplicate found, shrink window from the left
            while (charSet.count(s[right])) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add current character and update maxLength
            charSet.insert(s[right]);
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};

int main() {
    Solution sol;
    cout << sol.lengthOfLongestSubstring("abcabcbb") << endl; // Expected: 3
    cout << sol.lengthOfLongestSubstring("bbbbb") << endl;    // Expected: 1
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl;   // Expected: 3
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. Both `left` and `right` pointers traverse the string at most once.
- **Space Complexity:** `O(min(N, M))` where `M` is the size of the character set (e.g., 256).

---

## Interview Notes
- **C++ Optimization:** Instead of an `unordered_set`, you can use an integer array `vector<int> charIndex(256, -1)` to store the *most recent index* of each character. This allows you to jump the `left` pointer directly to `max(left, charIndex[s[right]] + 1)`, completely avoiding the inner `while` loop.
