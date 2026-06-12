# 4. Find All Factors of a Number

**Problem:** Print all divisors (factors) of `N`.

**Concept:** 
Iterate up to `sqrt(N)`. If `i` is a divisor, then `N/i` is also a divisor. This finds all divisors in $O(\sqrt{N})$ time.

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void printFactors(int n) {
    vector<int> factors;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            factors.push_back(i);
            if (n / i != i) {
                factors.push_back(n / i);
            }
        }
    }
    sort(factors.begin(), factors.end());
    for(int f : factors) cout << f << " ";
    cout << "\n";
}

int main() {
    printFactors(36);
    return 0;
}
```
