# Valid Palindrome II

## Difficulty
Easy / Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Amazon, Microsoft

## Topic
Strings / Two Pointers / Greedy

## Pattern
Two Pointers with Deletion

## Problem Statement
Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Input
- `s` string.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "aba"
Output: true
```

**Example 2:**
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**
```
Input: s = "abc"
Output: false
```

## Edge Cases
- String is already a palindrome (requires 0 deletions, return `true`).
- Deleting the left mismatched character works, but deleting the right mismatched character doesn't (and vice versa).

## Intuition
We use the classic **Two Pointers** method for palindromes: `left = 0`, `right = s.length() - 1`.
We move them inwards as long as `s[left] == s[right]`.
But what happens when they DON'T match? `s[left] != s[right]`.
Since we are allowed exactly **ONE** deletion, we have a choice:
- Do we delete `s[left]` and see if the rest of the string is a palindrome? (The remaining string to check is `left + 1` to `right`).
- Or do we delete `s[right]` and see if the rest of the string is a palindrome? (The remaining string to check is `left` to `right - 1`).

Because we only have one deletion, whichever choice we make, the *remaining* substring MUST be a perfect palindrome with zero errors allowed.
So, we simply write a helper function `isPalindrome(s, left, right)` that strictly checks for a perfect palindrome.
When a mismatch occurs in our main loop, we return:
`isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)`.

## Brute Force Approach
**Explanation:** For every single index `i` in the string, create a new string with `s[i]` deleted. Check if that new string is a palindrome.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(N)$ for string copies. (Will TLE on $10^5$).

## Optimal Approach (Two Pointers with Divergence)
**Detailed explanation:**
1. Create a helper function `bool isStrictPalindrome(const string& s, int left, int right)`.
   - While `left < right`:
     - If `s[left] != s[right]`, return `false`.
     - `left++`, `right--`.
   - Return `true`.
2. In the main function `validPalindrome(string s)`:
   - Initialize `left = 0`, `right = s.length() - 1`.
   - While `left < right`:
     - If `s[left] == s[right]`, all is well. `left++`, `right--`.
     - If `s[left] != s[right]`, we hit our ONE allowed mismatch.
     - We must use our one deletion. We simulate deleting left OR right.
     - Return `isStrictPalindrome(s, left + 1, right) || isStrictPalindrome(s, left, right - 1)`.
   - If the while loop completes without mismatches, it was already a perfect palindrome. Return `true`.

**Time Complexity:** $O(N)$. We scan inwards. When we hit a mismatch, we scan the remaining substring at most twice. Total operations $\le 2N$.
**Space Complexity:** $O(1)$ constant extra space.

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            // Mismatch found
            if (s[left] != s[right]) {
                // Return true if either deleting the left character 
                // OR the right character results in a palindrome.
                return isStrictPalindrome(s, left + 1, right) || 
                       isStrictPalindrome(s, left, right - 1);
            }
            left++;
            right--;
        }
        
        return true;
    }
    
private:
    bool isStrictPalindrome(const string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
```

## Dry Run
`s = "abca"`
- `L=0 ('a'), R=3 ('a')`. Match! `L=1, R=2`.
- `L=1 ('b'), R=2 ('c')`. Mismatch!
- We hit the divergent path:
  - Option 1 (Delete L): `isStrict(s, 2, 2)` -> bounds are single char `'c'`. `L < R` is false. Returns `true`.
  - Option 2 (Delete R): `isStrict(s, 1, 1)` -> single char `'b'`. Returns `true`.
- Returns `true || true` -> `true`.

`s = "abxcba"`
- `L=0 ('a'), R=5 ('a')`. Match.
- `L=1 ('b'), R=4 ('b')`. Match.
- `L=2 ('x'), R=3 ('c')`. Mismatch!
- Option 1 (Delete x): `isStrict(s, 3, 3)`. `"c"` is palindrome. Returns `true`.
- Result: `true`.

## Common Mistakes
- **Trying to use a `deleted` boolean flag inside a single loop:** Many candidates try to write `if(s[left]!=s[right]){ if(deleted) return false; deleted=true; left++; }`. This approach FAILS because you are blindly choosing to delete `left`. What if deleting `right` was the correct choice? You must branch and check BOTH possibilities.

## Similar Problems
- Valid Palindrome
- Minimum Deletions to Make a String Palindrome
