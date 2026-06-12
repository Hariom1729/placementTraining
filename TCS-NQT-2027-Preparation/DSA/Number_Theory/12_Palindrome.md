# 12. Check Palindrome

**Problem:** Check whether a given integer is a palindrome.

**Concept:** 
Reverse the integer. If the reversed integer is exactly equal to the original integer, it is a palindrome.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPalindrome(int n) {
    int original = n;
    int rev = 0;
    while (n > 0) {
        int rem = n % 10;
        rev = rev * 10 + rem;
        n /= 10;
    }
    return original == rev;
}

int main() {
    cout << (isPalindrome(121) ? "Palindrome" : "Not a Palindrome") << "\n";
    return 0;
}
```
