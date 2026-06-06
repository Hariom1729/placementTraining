# Problem 5: Longest Palindromic Substring

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

## Input Format
- A single string `s`.

## Output Format
- The string representing the longest palindromic substring.

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

---

## Approach: Expand Around Center

While Dynamic Programming is an option, the **Expand Around Center** approach is more space-efficient and widely accepted.
1. A palindrome mirrors around its center.
2. A center can be a single character (for odd-length palindromes like "aba") or between two characters (for even-length palindromes like "abba").
3. Therefore, for a string of length `N`, there are `2N - 1` possible centers.
4. We iterate through every possible center and expand outwards to the left and right as long as the characters match.
5. We keep track of the maximum length found and its starting/ending indices.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Check for odd length palindrome
            int len1 = expandAroundCenter(s, i, i);
            
            // Check for even length palindrome
            int len2 = expandAroundCenter(s, i, i + 1);
            
            int len = max(len1, len2);
            
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        
        return s.substr(start, end - start + 1);
    }
    
private:
    int expandAroundCenter(const string& s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // The length is (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1;
    }
};

int main() {
    Solution sol;
    cout << sol.longestPalindrome("babad") << endl; // Expected: "bab" or "aba"
    cout << sol.longestPalindrome("cbbd") << endl;  // Expected: "bb"
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N^2)` where `N` is the length of the string. Expanding around the center takes `O(N)` time, and we do this from `2N - 1` centers.
- **Space Complexity:** `O(1)`. We only use constant extra space for variables `start`, `end`, `left`, and `right`. The `substr` operation at the end creates the return string, taking `O(N)` space, but auxiliary space is `O(1)`.

---

## Interview Notes
- **Manacher's Algorithm:** Mentioning Manacher's Algorithm, which solves this problem in `O(N)` time, is a huge plus in TCS Prime interviews. However, you are rarely expected to implement it perfectly.
