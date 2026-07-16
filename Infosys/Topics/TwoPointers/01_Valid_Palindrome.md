# Valid Palindrome

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Microsoft, Amazon

## Topic
Two Pointers / Strings

## Pattern
Opposite Ends (Collision)

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Input
- `s` string.

## Output
- Return a boolean.

## Sample Test Cases

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Edge Cases
- String with only punctuation and spaces (returns `true`).
- String with mixed cases and numbers.

## Intuition
The naive approach is to build a new string that only contains the alphanumeric characters, reverse it, and check if it's equal to the original cleaned string. This requires $O(N)$ extra space.

To optimize space to $O(1)$, we use **Two Pointers**.
We place a `left` pointer at the beginning of the string and a `right` pointer at the end.
We move them towards each other. If either pointer lands on a non-alphanumeric character (spaces, punctuation), we simply skip it!
Once both pointers are on alphanumeric characters, we convert them to lowercase and compare them.
If they don't match, it's not a palindrome.
If they do match, we move both pointers inwards.

## Optimal Approach (Two Pointers In-Place)
**Detailed explanation:**
1. Initialize `left = 0`, `right = s.length() - 1`.
2. Loop while `left < right`:
   - Use `isalnum()` to check if the characters are alphanumeric.
   - While `left < right` and `s[left]` is NOT alphanumeric, `left++`.
   - While `left < right` and `s[right]` is NOT alphanumeric, `right--`.
   - Convert both to lowercase using `tolower()`.
   - If `tolower(s[left]) != tolower(s[right])`, return `false`.
   - `left++`, `right--`.
3. If the loop completes, return `true`.

**Time Complexity:** $O(N)$ since each character is visited exactly once.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            // Skip non-alphanumeric characters from the left
            while (left < right && !isalnum(s[left])) {
                left++;
            }
            // Skip non-alphanumeric characters from the right
            while (left < right && !isalnum(s[right])) {
                right--;
            }
            
            // Compare the characters after converting to lowercase
            if (tolower(s[left]) != tolower(s[right])) {
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
`s = "A man, a plan, a canal: Panama"`
- `left = 0` ('A'), `right = 29` ('a'). Both alnum. `tolower('A') == tolower('a')`. Match! `left=1`, `right=28`.
- `left = 1` (' '). Not alnum. `left++` -> 2. `right = 28` ('m').
- `left = 2` ('m'). `right = 28` ('m'). Match!
- `right = 27` ('a')...
- ... skips spaces and commas ...
- Eventually `left >= right`, returns `true`.

## Common Mistakes
- **Forgetting `left < right` in inner loops:** When skipping non-alphanumeric characters, if the string is `"    "`, the `left` pointer will keep incrementing until it goes out of bounds if you don't explicitly check `left < right` inside the inner `while` loops!

## Similar Problems
- Valid Palindrome II (Can delete at most one character)
