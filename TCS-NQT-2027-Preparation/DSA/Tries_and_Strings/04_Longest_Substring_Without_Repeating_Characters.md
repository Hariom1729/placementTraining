# Problem 4: Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Approach: Sliding Window + Hash Map / Hash Set

We can use a sliding window approach with two pointers, `left` and `right`.
We expand the window by moving `right` and adding characters to a set.
If we encounter a character that is already in the set, it means we have a repeating character. We then shrink the window from the left by removing characters from the set and incrementing `left` until the duplicate is removed.

A more optimized approach uses a Hash Map (or an array) to store the **most recent index** of each character.
1. Create a `vector<int> charIndex(256, -1)` to store the last seen index of every ASCII character.
2. Maintain `left = 0` and `maxLength = 0`.
3. Iterate `right` from `0` to `n-1`:
   - If `s[right]` is already in the map AND its last seen index is `>= left`, it means we found a duplicate within our current window.
   - We jump the `left` pointer to `charIndex[s[right]] + 1`.
   - Update `charIndex[s[right]] = right`.
   - Update `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Array to store the last seen index of all 256 ASCII characters
        vector<int> charIndex(256, -1);
        
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // If the character is found and is within the current window
            if (charIndex[s[right]] != -1 && charIndex[s[right]] >= left) {
                // Move the left pointer to the right of the previous occurrence
                left = charIndex[s[right]] + 1;
            }
            
            // Update the last seen index of the character
            charIndex[s[right]] = right;
            
            // Update the maximum length
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};

int main() {
    Solution sol;
    string s1 = "abcabcbb";
    cout << "Length: " << sol.lengthOfLongestSubstring(s1) << endl; 
    // Expected: 3 ("abc")
    
    string s2 = "bbbbb";
    cout << "Length: " << sol.lengthOfLongestSubstring(s2) << endl; 
    // Expected: 1 ("b")
    
    string s3 = "pwwkew";
    cout << "Length: " << sol.lengthOfLongestSubstring(s3) << endl; 
    // Expected: 3 ("wke")

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. Both pointers only move forward.
- **Space Complexity:** `O(1)` or `O(M)` where `M` is the size of the character set (256).
