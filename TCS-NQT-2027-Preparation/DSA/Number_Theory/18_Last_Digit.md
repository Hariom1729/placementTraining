# 18. Last digit of A^B

**Problem:** Find the last digit of $A^B$.

**Concept:** 
Last digits repeat in cycles of 4. Find `A % 10` and `B % 4` (if `B % 4 == 0`, use 4), and compute $(A \% 10)^{(B \% 4)} \pmod{10}$.

**C++ Solution:**
```cpp
#include <iostream>
#include <cmath>
using namespace std;

int lastDigit(int a, int b) {
    if (b == 0) return 1;
    a = a % 10;
    int exp = b % 4;
    if (exp == 0) exp = 4;
    
    int result = pow(a, exp);
    return result % 10;
}

int main() {
    cout << "Last digit of 2^10: " << lastDigit(2, 10) << "\n"; // 4
    return 0;
}
```
