# 29. Numbers with Exactly 3 Divisors

**Problem:** Check if a number has exactly 3 divisors.

**Concept:** 
A number has exactly 3 divisors ONLY if it is the square of a prime number. (e.g., $9 = 3^2$, divisors: 1, 3, 9).

**C++ Solution:**
```cpp
#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0) return false;
    }
    return true;
}

bool hasExactly3Divisors(int n) {
    int root = sqrt(n);
    if(root * root == n && isPrime(root)) {
        return true;
    }
    return false;
}

int main() {
    cout << (hasExactly3Divisors(49) ? "True" : "False") << "\n"; // True
    return 0;
}
```
