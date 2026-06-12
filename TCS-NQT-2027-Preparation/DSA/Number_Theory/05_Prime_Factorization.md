# 5. Prime Factorization

**Problem:** Find all the prime factors of a number.

**Concept:** 
Divide by 2 as much as possible. Then try dividing by all odd numbers from 3 up to `sqrt(N)`. If anything is left over, it's a prime factor itself.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

void primeFactors(int n) {
    while (n % 2 == 0) {
        cout << 2 << " ";
        n /= 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            cout << i << " ";
            n /= i;
        }
    }
    if (n > 2) {
        cout << n << " ";
    }
    cout << "\n";
}

int main() {
    primeFactors(315);
    return 0;
}
```
