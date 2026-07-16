# Palindromic Substrings

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Facebook, Bloomberg

## Topic
Strings / Dynamic Programming

## Pattern
Expand Around Center

## Problem Statement
Given a string `s`, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Input
- `s` string.

## Output
- Return an integer count.

## Sample Test Cases

**Example 1:**
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## Edge Cases
- All characters are identical (`"aaaa"`).
- All characters are distinct (`"abcdef"`). The answer will just be `s.length()`.

## Intuition
This problem is almost identical to **Longest Palindromic Substring**.
Instead of finding the *maximum* length, we just want to **count** every valid palindrome we find.
Every time we treat a character (or the space between two characters) as a center, we expand outwards.
Every time `s[left] == s[right]`, we have found a valid palindrome, so we simply increment our `count` by 1!
We must remember to check both **odd-length** palindromes (center is exactly at index `i`) and **even-length** palindromes (center is between index `i` and `i+1`).

## Brute Force Approach
**Explanation:** Generate all $O(N^2)$ substrings, and check if each is a palindrome taking $O(N)$ time. Add to total count.
**Time Complexity:** $O(N^3)$
**Space Complexity:** $O(1)$

## Optimal Approach (Expand Around Center)
**Detailed explanation:**
1. Initialize a global/member variable `count = 0` (or return it from helper).
2. Create a helper function `countPalindromesFromCenter(s, left, right)`.
   - Initialize `localCount = 0`.
   - While `left >= 0 && right < s.length() && s[left] == s[right]`:
     - We found a valid palindrome! `localCount++`.
     - Expand outwards: `left--`, `right++`.
   - Return `localCount`.
3. Iterate `i` from 0 to `s.length() - 1`:
   - Odd lengths (center at `i`): `totalCount += countPalindromesFromCenter(s, i, i)`.
   - Even lengths (center between `i` and `i+1`): `totalCount += countPalindromesFromCenter(s, i, i + 1)`.
4. Return `totalCount`.

**Time Complexity:** $O(N^2)$ because expanding from the center takes $O(N)$ time in the worst case, and we do it $2N$ times.
**Space Complexity:** $O(1)$ since no extra space is needed beyond variables.

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int totalCount = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Count odd-length palindromes (center is at character i)
            totalCount += countPalindromes(s, i, i);
            
            // Count even-length palindromes (center is between i and i+1)
            totalCount += countPalindromes(s, i, i + 1);
        }
        
        return totalCount;
    }
    
private:
    int countPalindromes(const string& s, int left, int right) {
        int count = 0;
        
        // Expand outwards as long as the boundaries match
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            count++; // We found a valid palindrome
            left--;
            right++;
        }
        
        return count;
    }
};
```

## Dry Run
`s = "aaa"`
- `i = 0`:
  - `count(0, 0)`: `"a"`. `L=-1`, `R=1`. Returns 1.
  - `count(0, 1)`: `"aa"`. `L=-1`, `R=2`. Returns 1.
  - Total = 2.
- `i = 1`:
  - `count(1, 1)`: `"a"`. `L=0`, `R=2` -> `"aaa"`. `L=-1`, `R=3`. Returns 2.
  - `count(1, 2)`: `"aa"`. `L=0`, `R=3`. Returns 1.
  - Total = 2 + 2 + 1 = 5.
- `i = 2`:
  - `count(2, 2)`: `"a"`. `L=1`, `R=3`. Returns 1.
  - `count(2, 3)`: Right is out of bounds immediately. Returns 0.
  - Total = 5 + 1 = 6.

Result: 6.

## Common Mistakes
- **Forgetting even length palindromes:** If you only expand from `(i, i)`, you will completely miss palindromes like `"abba"`. You must always check both `(i, i)` and `(i, i+1)`.

## Similar Problems
- Longest Palindromic Substring
- Longest Palindromic Subsequence
