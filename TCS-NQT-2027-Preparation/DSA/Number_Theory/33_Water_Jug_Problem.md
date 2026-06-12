# 33. Water Jug Problem (GCD)

**Problem:** Determine whether it is possible to measure exactly `z` liters using two jugs with capacities `x` and `y`.

**Concept:** 
It is possible if $z$ is a multiple of $\text{GCD}(x, y)$ and $z \le x + y$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool canMeasureWater(int x, int y, int z) {
    if (x + y < z) return false;
    if (x == z || y == z || x + y == z) return true;
    return z % gcd(x, y) == 0;
}

int main() {
    cout << (canMeasureWater(3, 5, 4) ? "True" : "False") << "\n";
    return 0;
}
```
