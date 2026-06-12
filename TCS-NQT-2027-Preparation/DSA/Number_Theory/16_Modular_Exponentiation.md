# 16. Modular Exponentiation

**Problem:** Compute $(A^B) \pmod M$ efficiently.

**Concept:** 
Use exponentiation by squaring to compute it in $O(\log B)$ time.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

long long modularExponentiation(long long base, long long exp, long long mod) {
    long long res = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        exp = exp >> 1;
        base = (base * base) % mod;
    }
    return res;
}

int main() {
    cout << "2^10 % 1000: " << modularExponentiation(2, 10, 1000) << "\n"; // 24
    return 0;
}
```
