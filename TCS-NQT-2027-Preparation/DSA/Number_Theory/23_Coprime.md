# 23. Coprime Numbers

**Problem:** Find if two numbers are Coprime.

**Concept:** 
Two numbers are coprime if their Greatest Common Divisor (GCD) is exactly 1.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool isCoprime(int a, int b) {
    return gcd(a, b) == 1;
}

int main() {
    cout << (isCoprime(14, 15) ? "Coprime" : "Not Coprime") << "\n"; // True
    return 0;
}
```
