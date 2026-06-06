# Problem 2: Valid Palindrome

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Input Format
- A single string `s`.

## Output Format
- A boolean value: `true` or `false`.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Approach

This problem uses the **Two Pointers** pattern.
1. Place `left` pointer at index `0` and `right` pointer at index `s.length() - 1`.
2. Move the `left` pointer forward if the current character is not alphanumeric using `isalnum()`.
3. Move the `right` pointer backward if the current character is not alphanumeric.
4. If both `left` and `right` point to alphanumeric characters, compare them (ignoring case using `tolower()`).
   - If they are different, return `false`.
   - If they are the same, move both pointers inward (`left++`, `right--`).
5. Repeat until `left >= right`. If the loop finishes without returning `false`, the string is a valid palindrome.

---

## C++ Solution

```cpp
#include <iostream>
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
            if (!isalnum(s[left])) {
                left++;
            } 
            // Skip non-alphanumeric characters from the right
            else if (!isalnum(s[right])) {
                right--;
            } 
            // Compare the characters (ignoring case)
            else {
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    cout << (sol.isPalindrome("A man, a plan, a canal: Panama") ? "true" : "false") << endl; // Expected: true
    cout << (sol.isPalindrome("race a car") ? "true" : "false") << endl; // Expected: false
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. In the worst-case, we traverse the entire string exactly once.
- **Space Complexity:** `O(1)`. We only use pointers. No extra strings or arrays are created.

---

## Interview Notes
- `isalnum` and `tolower` from `<cctype>` are your best friends for string manipulation problems involving character checking in C++.
