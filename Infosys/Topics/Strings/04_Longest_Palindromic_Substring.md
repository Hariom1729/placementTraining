# Longest Palindromic Substring

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Bloomberg

## Topic
Strings / Dynamic Programming

## Pattern
Expand Around Center

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Input
- `s` string.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

## Edge Cases
- String with length 1. Returns the string itself.
- String with all identical characters (`"aaaa"`).

## Intuition
A palindrome reads the same forwards and backwards. This means it is perfectly symmetrical around its center!
If we iterate through every character in the string and treat it as the **center** of a potential palindrome, we can expand outwards to the left and right simultaneously. As long as `s[left] == s[right]`, we have a valid palindrome!
The only trick is that palindromes can have an **odd** length (center is one character, e.g., `"bab"`) OR an **even** length (center is between two characters, e.g., `"bb"`).
Therefore, for every character at index `i`, we must attempt to expand outwards assuming it is an odd palindrome (`center = i`), AND attempt to expand assuming it is an even palindrome (`center1 = i, center2 = i+1`).

*Note: There is an $O(N)$ algorithm called Manacher's Algorithm, but it is excessively complex for interviews. The $O(N^2)$ Expand Around Center approach is universally accepted and expected.*

## Brute Force Approach
**Explanation:** Generate all $O(N^2)$ substrings, and check if each is a palindrome taking $O(N)$ time.
**Time Complexity:** $O(N^3)$
**Space Complexity:** $O(1)$

## Optimal Approach (Expand Around Center)
**Detailed explanation:**
1. Maintain `start = 0` and `maxLength = 0` to track the longest palindrome found.
2. Create a helper function `expandAroundCenter(s, left, right)` that expands outwards while `left >= 0 && right < s.length() && s[left] == s[right]`, returning the length of the palindrome found: `right - left - 1`.
3. Iterate `i` from 0 to `s.length() - 1`:
   - Find max length assuming odd center: `len1 = expandAroundCenter(s, i, i)`.
   - Find max length assuming even center: `len2 = expandAroundCenter(s, i, i + 1)`.
   - Get the max of both: `len = max(len1, len2)`.
   - If `len > maxLength`, update `maxLength = len`. We also need to update the `start` index! 
   - `start = i - (len - 1) / 2`. (This math works flawlessly for both odd and even lengths).
4. Return `s.substr(start, maxLength)`.

**Time Complexity:** $O(N^2)$ because expanding from the center takes $O(N)$ time in the worst case, and we do it $2N - 1$ times.
**Space Complexity:** $O(1)$ since no extra space is needed beyond variables.

## C++ Solution

```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        
        int start = 0;
        int maxLength = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Check for odd length palindrome (center is at i)
            int len1 = expandAroundCenter(s, i, i);
            
            // Check for even length palindrome (center is between i and i+1)
            int len2 = expandAroundCenter(s, i, i + 1);
            
            int len = max(len1, len2);
            
            if (len > maxLength) {
                maxLength = len;
                // Mathematically derive the start index of the palindrome
                start = i - (len - 1) / 2;
            }
        }
        
        return s.substr(start, maxLength);
    }
    
private:
    int expandAroundCenter(const string& s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // When the while loop breaks, left and right have moved ONE step too far!
        // The actual length is (right - 1) - (left + 1) + 1 = right - left - 1.
        return right - left - 1;
    }
};
```

## Dry Run
`s = "babad"`
- `i = 0` ('b'):
  - `expand(0, 0)`: `left=-1, right=1`. Returns `1 - (-1) - 1 = 1`.
  - `expand(0, 1)`: 'b' != 'a'. Returns `1 - 0 - 1 = 0`.
  - `maxLen = 1`, `start = 0 - (1-1)/2 = 0`.
- `i = 1` ('a'):
  - `expand(1, 1)`: 'a' == 'a'. Next: 'b' == 'b' (`s[0]==s[2]`). Next: left=-1. Returns 3.
  - `expand(1, 2)`: 'a' != 'b'. Returns 0.
  - `len = 3`. `3 > maxLen (1)`.
  - `maxLen = 3`. `start = 1 - (3-1)/2 = 1 - 1 = 0`.
- `i = 2` ('b'):
  - `expand(2, 2)`: Finds "aba". Length 3. Not greater than `maxLen`.
Result: `s.substr(0, 3) = "bab"`.

## Common Mistakes
- **Miscalculating the returned length:** In the `while` loop, `left` is decremented and `right` is incremented. When the condition fails, they are one index PAST the valid palindrome bounds. The true bounds are `left + 1` to `right - 1`. Length is `(right - 1) - (left + 1) + 1 = right - left - 1`. Doing `right - left + 1` is a massive bug!
- **Not handling even lengths:** A lot of candidates only write `expandAroundCenter(i, i)` and completely fail test cases like `"cbbd"`.

## Similar Problems
- Palindromic Substrings (Count all palindromes)
- Longest Palindromic Subsequence (DP required)
