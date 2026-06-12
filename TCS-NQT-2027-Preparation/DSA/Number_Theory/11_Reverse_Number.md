# 11. Reverse a Number

**Problem:** Reverse the digits of a given integer.

**Concept:** 
Repeatedly extract the last digit using `% 10` and build the reversed number by multiplying the running result by 10.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int reverseNumber(int n) {
    int rev = 0;
    while (n > 0) {
        int rem = n % 10;
        rev = rev * 10 + rem;
        n /= 10;
    }
    return rev;
}

int main() {
    cout << "Reverse of 1234: " << reverseNumber(1234) << "\n"; // 4321
    return 0;
}
```
