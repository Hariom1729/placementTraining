# 6. Count Total Divisors

**Problem:** Count the exact number of divisors for a number `N`.

**Concept:** 
A number can be prime factored as $N = p_1^{a} \cdot p_2^{b} \dots$. The total divisors equals $(a+1) \cdot (b+1) \dots$. We can either use this formula or simply count them in $O(\sqrt{N})$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int countDivisors(int n) {
    int count = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            count++;
            if (n / i != i) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    cout << "Total Divisors of 36: " << countDivisors(36) << "\n";
    return 0;
}
```
