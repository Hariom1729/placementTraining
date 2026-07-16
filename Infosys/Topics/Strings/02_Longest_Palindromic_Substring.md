# Longest Palindromic Substring

## Difficulty
Medium / Hard

## Asked In
Infosys SP
Infosys DSE
Year: 2020, 2022, 2023
Frequency: Very High

---

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

---

## Input Format
- A single string `s`.

---

## Output Format
- Return the longest substring that reads the same forwards and backwards.

---

## Constraints
- $1 \le s.length \le 1000$
- `s` consists of only digits and English letters.

---

## Examples

### Example 1
**Input:** 
```
"babad"
```
**Output:** 
```
"bab"
```
**Explanation:** "aba" is also a valid answer.

### Example 2
**Input:** 
```
"cbbd"
```
**Output:** 
```
"bb"
```

---

## Brute Force Approach
Generate all possible substrings of `s` (there are $O(N^2)$ substrings). For each substring, check if it is a palindrome (takes $O(N)$ time). Keep track of the maximum length.

**Time Complexity:** $O(N^3)$
**Space Complexity:** $O(1)$

---

## Better Approach (Dynamic Programming)
Create a 2D boolean DP array where `dp[i][j]` is true if the substring from index `i` to `j` is a palindrome.
`dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`.

**Complexity:** 
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(N^2)$ for the DP table. (Will give Memory Limit Exceeded for large strings).

---

## Optimal Approach (Expand Around Center)
**Detailed explanation:**
A palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only $2N - 1$ such centers.
Why $2N - 1$? Because a palindrome can have an odd length (center is a single character, like 'a' in "bab") or an even length (center is between two characters, like between 'b' and 'b' in "abba").

For every center, expand to the left and right as long as the characters match. Keep track of the maximum length found.

**Dry Run:**
`s = "babad"`
- `i = 0` ('b'): Expand odd center (left=0, right=0) -> "b". Length 1.
- `i = 1` ('a'): Expand odd center (left=1, right=1) -> "aba". Length 3.
- `i = 1` ('a'): Expand even center (left=1, right=2) -> 'a' != 'b'.
- ...
- Max length is 3 ("aba" or "bab").

**Complexity:**
- **Time Complexity:** $O(N^2)$ since expanding takes $O(N)$ and we do it $2N$ times.
- **Space Complexity:** $O(1)$ constant space.

---

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Helper to expand around center
int expandAroundCenter(string s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    // Length is (right - left - 1) because the loop breaks when characters don't match
    return right - left - 1;
}

string longestPalindrome(string s) {
    if (s.empty()) return "";
    
    int start = 0, end = 0;
    
    for (int i = 0; i < s.length(); i++) {
        // Odd length palindrome
        int len1 = expandAroundCenter(s, i, i);
        // Even length palindrome
        int len2 = expandAroundCenter(s, i, i + 1);
        
        int len = max(len1, len2);
        
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    
    return s.substr(start, end - start + 1);
}

int main() {
    cout << longestPalindrome("babad") << endl; // Output: "bab" or "aba"
    return 0;
}
```

---

## Common Mistakes
- **Forgetting Even Lengths:** Assuming centers are only at the characters themselves. Palindromes like `abba` have a center *between* the characters `b` and `b`.
- **Substring Indexing Math:** The math to calculate `start` and `end` from the returned `len` can be tricky: `start = i - (len - 1) / 2`. Test it on paper before coding.

---

## Similar Questions
- Palindromic Substrings (Count them)
- Longest Palindromic Subsequence

---

## Interview Tips
- Mention Manacher's Algorithm ($O(N)$ time) just to show off, but explicitly state that **Expand Around Center** is the expected standard for coding rounds due to the complexity of Manacher's logic.

---

## Pattern Recognition
**Identify this when:** Finding longest / counting substrings that possess symmetry. **Expand Around Center** is the standard approach for contiguous symmetrical subarrays/strings.
