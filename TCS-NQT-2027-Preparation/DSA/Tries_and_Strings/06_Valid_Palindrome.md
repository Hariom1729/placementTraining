# Problem 6: Valid Palindrome

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Approach: Two Pointers

We can solve this optimally without creating a new string by using two pointers, one at the beginning (`left`) and one at the end (`right`) of the string.

1. Loop while `left < right`:
2. **Skip non-alphanumeric characters:** If `s[left]` is not alphanumeric, increment `left`.
3. If `s[right]` is not alphanumeric, decrement `right`.
4. **Compare:** If both are alphanumeric, convert both to lowercase and compare them.
   - If they are NOT equal, return `false`.
   - If they are equal, increment `left` and decrement `right`.
5. If the loop completes without returning `false`, the string is a palindrome. Return `true`.

*C++ provides `isalnum()` to check if a char is alphanumeric, and `tolower()` to convert to lowercase.*

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
            // Skip non-alphanumeric characters from left
            while (left < right && !isalnum(s[left])) {
                left++;
            }
            
            // Skip non-alphanumeric characters from right
            while (left < right && !isalnum(s[right])) {
                right--;
            }
            
            // Compare characters (convert to lowercase for case-insensitivity)
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    string s1 = "A man, a plan, a canal: Panama";
    cout << "Is Palindrome? " << (sol.isPalindrome(s1) ? "Yes" : "No") << endl; 
    // Expected: Yes ("amanaplanacanalpanama")
    
    string s2 = "race a car";
    cout << "Is Palindrome? " << (sol.isPalindrome(s2) ? "Yes" : "No") << endl; 
    // Expected: No ("raceacar")

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We traverse the string once.
- **Space Complexity:** `O(1)` as we only use two integer pointers and modify no extra space.
