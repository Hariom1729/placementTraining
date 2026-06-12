# 20. Perfect Square Check

**Problem:** Check if a number is a perfect square.

**Concept:** 
A number $N$ is a perfect square if its square root is an integer. Check if $\lfloor\sqrt{N}\rfloor \times \lfloor\sqrt{N}\rfloor == N$.

**C++ Solution:**
```cpp
#include <iostream>
#include <cmath>
using namespace std;

bool isPerfectSquare(int n) {
    if (n < 0) return false;
    int root = round(sqrt(n));
    return root * root == n;
}

int main() {
    cout << (isPerfectSquare(16) ? "Perfect Square" : "Not Perfect Square") << "\n";
    return 0;
}
```
