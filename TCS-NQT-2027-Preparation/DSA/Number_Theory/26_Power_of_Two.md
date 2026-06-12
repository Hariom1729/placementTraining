# 26. Power of Two

**Problem:** Given an integer `n`, return `true` if it is a power of two.

**Concept:** 
A power of two in binary has exactly one '1' bit (e.g., 8 is `1000`). If we do `n & (n - 1)`, it flips the lowest set bit. If it was a power of two, the result will be 0.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    if (n <= 0) return false;
    return (n & (n - 1)) == 0;
}

int main() {
    cout << (isPowerOfTwo(16) ? "True" : "False") << "\n"; // True
    return 0;
}
```
