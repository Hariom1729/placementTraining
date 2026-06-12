# 38. Kth Factor of N

**Problem:** Given two positive integers `n` and `k`. Return the `k`-th factor of `n`.

**Concept:** 
Iterate up to `n` (or `sqrt(n)` for optimization) and count factors until we hit the `k`-th one.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int kthFactor(int n, int k) {
    for(int i = 1; i <= n; i++) {
        if(n % i == 0) {
            k--;
            if(k == 0) return i;
        }
    }
    return -1;
}

int main() {
    cout << "3rd factor of 12: " << kthFactor(12, 3) << "\n"; // 3
    return 0;
}
```
