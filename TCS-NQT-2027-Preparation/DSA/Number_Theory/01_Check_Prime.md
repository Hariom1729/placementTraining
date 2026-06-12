# 1. Check if a number is Prime

**Problem:** Check if a given number N is prime.

**Concept:** 
A prime number is only divisible by 1 and itself. We can check up to `sqrt(N)` because if `N = a * b`, one of the factors must be $\le \sqrt{N}$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n = 29;
    cout << (isPrime(n) ? "Prime" : "Not Prime") << "\n";
    return 0;
}
```
