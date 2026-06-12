# 28. Ugly Number

**Problem:** An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

**Concept:** 
Repeatedly divide the number by 2, 3, and 5 as long as it is divisible. If the resulting number is 1, then it's an ugly number.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isUgly(int n) {
    if (n <= 0) return false;
    while (n % 2 == 0) n /= 2;
    while (n % 3 == 0) n /= 3;
    while (n % 5 == 0) n /= 5;
    return n == 1;
}

int main() {
    cout << (isUgly(6) ? "Ugly" : "Not Ugly") << "\n"; 
    return 0;
}
```
