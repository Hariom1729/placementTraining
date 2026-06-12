# 2. Print all Prime Numbers in a Range

**Problem:** Print all prime numbers between `L` and `R`.

**Concept:** 
For each number from `L` to `R`, check if it's prime. For large ranges, a Segmented Sieve is preferred, but for basic limits, checking `sqrt(N)` for each works.

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
    int L = 10, R = 30;
    for (int i = L; i <= R; i++) {
        if (isPrime(i)) {
            cout << i << " ";
        }
    }
    cout << "\n";
    return 0;
}
```
