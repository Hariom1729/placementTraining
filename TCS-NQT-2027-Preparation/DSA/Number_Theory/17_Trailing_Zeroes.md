# 17. Trailing Zeroes in N!

**Problem:** Find the number of trailing zeroes in $N!$.

**Concept:** 
Count the number of 5s in the prime factorization of $N!$, which is $\lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \lfloor N/125 \rfloor \dots$

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int trailingZeroes(int n) {
    int count = 0;
    while (n > 0) {
        n /= 5;
        count += n;
    }
    return count;
}

int main() {
    cout << "Trailing zeroes in 100!: " << trailingZeroes(100) << "\n"; // 24
    return 0;
}
```
