# 14. Add Digits to Single Digit

**Problem:** Repeatedly sum the digits of a number until it becomes a single digit.

**Concept:** 
This is mathematically known as the digital root. The answer is simply `n % 9`, except when the number is a multiple of 9 (then it's 9) and 0 (then it's 0).

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int addDigits(int n) {
    if (n == 0) return 0;
    if (n % 9 == 0) return 9;
    return n % 9;
}

int main() {
    cout << "Single digit sum of 38: " << addDigits(38) << "\n"; // 2
    return 0;
}
```
