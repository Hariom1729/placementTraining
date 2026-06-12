# 7. Greatest Common Divisor (GCD)

**Problem:** Find the GCD of two numbers `a` and `b`.

**Concept:** 
Use the Euclidean Algorithm: `gcd(a, b) = gcd(b, a % b)`. Base case is when `b == 0`, returning `a`.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    cout << "GCD of 48 and 18: " << gcd(48, 18) << "\n"; // 6
    return 0;
}
```
