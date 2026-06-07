# Problem 9: Longest Palindromic Substring

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

---

## Approach: Expand Around Center

While Dynamic Programming can solve this in `O(N^2)` time and `O(N^2)` space, the "Expand Around Center" approach solves it in `O(N^2)` time but only `O(1)` space, making it vastly superior for interviews.

A palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center. There are `2N - 1` such centers.
Why `2N - 1` and not `N`? Because the center of a palindrome can be in between two letters (for even-length palindromes).
For example, in "abba", the center is between the two 'b's.

1. Create a helper function `expandAroundCenter(s, left, right)` that expands outwards as long as `s[left] == s[right]` and returns the length of the palindrome.
2. Iterate `i` from `0` to `s.length() - 1`:
   - Find the length of the longest odd palindrome centered at `i`: `len1 = expandAroundCenter(s, i, i)`.
   - Find the length of the longest even palindrome centered between `i` and `i+1`: `len2 = expandAroundCenter(s, i, i + 1)`.
   - Let `len = max(len1, len2)`.
   - If `len > end - start`, update `start` and `end` indices of the longest palindrome found so far.
3. Return `s.substr(start, end - start + 1)`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
private:
    int expandAroundCenter(string s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // Return length of the palindrome
        // Note: left and right have moved one step past the valid palindrome bounds
        return right - left - 1;
    }

public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        
        int start = 0;
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Check for odd length palindrome (center is character at i)
            int len1 = expandAroundCenter(s, i, i);
            
            // Check for even length palindrome (center is between i and i+1)
            int len2 = expandAroundCenter(s, i, i + 1);
            
            int len = max(len1, len2);
            
            if (len > maxLen) {
                maxLen = len;
                // Calculate starting index based on center 'i' and length 'len'
                start = i - (len - 1) / 2;
            }
        }
        
        return s.substr(start, maxLen);
    }
};

int main() {
    Solution sol;
    cout << "Longest Palindrome: " << sol.longestPalindrome("babad") << endl; 
    // Expected: "bab" or "aba"
    
    cout << "Longest Palindrome: " << sol.longestPalindrome("cbbd") << endl; 
    // Expected: "bb"

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)`. Since expanding a palindrome around its center could take `O(N)` time, the overall complexity is `O(N^2)`.
- **Space Complexity:** `O(1)`. No extra space is used except for storing indices.
