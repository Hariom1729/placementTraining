# 8. Least Common Multiple (LCM)

**Problem:** Find the LCM of two numbers `a` and `b`.

**Concept:** 
The LCM is easily derived from the GCD using the formula: $a \times b = \text{GCD}(a, b) \times \text{LCM}(a, b)$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b; // Divide first to prevent overflow
}

int main() {
    cout << "LCM of 15 and 20: " << lcm(15, 20) << "\n"; // 60
    return 0;
}
```
