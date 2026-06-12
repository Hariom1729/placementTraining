# 32. Sum of All Divisors from 1 to N

**Problem:** Given a number N, find the sum of all divisors of all numbers from 1 to N.

**Concept:** 
A number `i` will appear as a divisor in all its multiples up to N. The number of multiples is `N / i`.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

long long sumOfAllDivisors(int n) {
    long long totalSum = 0;
    for(int i = 1; i <= n; i++) {
        totalSum += (n / i) * i;
    }
    return totalSum;
}

int main() {
    cout << "Sum for N=4: " << sumOfAllDivisors(4) << "\n"; // 15
    return 0;
}
```
