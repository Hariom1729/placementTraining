# 22. Calculate Combinations (nCr)

**Problem:** Calculate ${}^nC_r$.

**Concept:** 
${}^nC_r = \frac{n!}{r!(n-r)!}$. To avoid overflow, compute it iteratively. Also, use the property ${}^nC_r = {}^nC_{n-r}$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

long long nCr(int n, int r) {
    long long res = 1;
    if (r > n - r) r = n - r;
    for (int i = 0; i < r; ++i) {
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}

int main() {
    cout << "5C2: " << nCr(5, 2) << "\n"; // 10
    return 0;
}
```
