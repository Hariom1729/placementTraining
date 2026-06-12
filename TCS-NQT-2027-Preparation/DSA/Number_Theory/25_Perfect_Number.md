# 25. Perfect Number

**Problem:** Check if a number is a Perfect Number.

**Concept:** 
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself). Example: $6 = 1 + 2 + 3$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPerfectNumber(int n) {
    if (n <= 1) return false;
    int sum = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (n / i != i) {
                sum += n / i;
            }
        }
    }
    return sum == n;
}

int main() {
    cout << (isPerfectNumber(28) ? "Perfect Number" : "Not Perfect Number") << "\n";
    return 0;
}
```
