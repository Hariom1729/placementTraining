# Valid Palindrome

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Apple, Microsoft

## Topic
Strings / Two Pointers

## Pattern
Two Pointers (Left & Right)

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Input
- `s` representing the string phrase.

## Output
- Return a boolean value.

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
- String with only spaces or special characters (should return `true`).
- String with numbers (numbers are valid alphanumeric characters and must be compared).
- String with mixed cases (must ignore case).

## Intuition
The naïve way is to build a brand new string containing only the valid lowercase alphanumeric characters, reverse it, and compare it with itself. However, creating a new string takes $O(N)$ extra memory.
The optimal way is to use **Two Pointers**. One pointer starts at the beginning (`left`) and one starts at the end (`right`). 
If the character at `left` is not alphanumeric, we just skip it by doing `left++`. 
If the character at `right` is not alphanumeric, we skip it by doing `right--`.
Once both point to valid characters, we convert them to lowercase and compare. If they don't match, it's not a palindrome. If they do match, we move both pointers inward and continue.

## Brute Force Approach
**Explanation:** Iterate over `s` and build a new string `filtered`. Use `isalnum()` to check if a char is valid, and `tolower()` to convert it. Then check if `filtered == reversed(filtered)`.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the new string.

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. Initialize `left = 0` and `right = s.length() - 1`.
2. While `left < right`:
   - While `left < right` and `!isalnum(s[left])`, increment `left`.
   - While `left < right` and `!isalnum(s[right])`, decrement `right`.
   - If `tolower(s[left]) != tolower(s[right])`, return `false`.
   - Increment `left`, decrement `right`.
3. If the loop completes without mismatches, return `true`.

**Time Complexity:** $O(N)$ because each character is visited at most once.
**Space Complexity:** $O(1)$ constant extra space.

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
            
            // Compare characters after converting to lowercase
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            
            // Move both pointers inward
            left++;
            right--;
        }
        
        return true;
    }
};
```

## Dry Run
`s = "A man, a plan"` (simplified) -> Indices: 0 to 12.
- `L=0` ('A', alnum). `R=12` ('n', alnum). `tolower('A') != tolower('n')` (`a != n`). Returns `false`.

Let's try a valid one: `s = "a.a"`
- `L=0` ('a'). `R=2` ('a'). `a == a`. `L=1, R=1`.
- `L < R` is false. Loop ends.
- Returns `true`.

## Common Mistakes
- **Forgetting the inner `left < right` check:** Inside the inner `while(!isalnum())` loop, you MUST include `left < right`. Otherwise, if the string has no alphanumeric characters (e.g., `"   "`), the pointers will go out of bounds and cause a Segmentation Fault.
- **Ignoring numbers:** Using `isalpha()` instead of `isalnum()`. The problem states numbers are valid! `"0P"` should return `false`, but if you use `isalpha()`, you skip the `0` and might get a wrong answer.

## Similar Problems
- Valid Palindrome II
- Palindrome Linked List
