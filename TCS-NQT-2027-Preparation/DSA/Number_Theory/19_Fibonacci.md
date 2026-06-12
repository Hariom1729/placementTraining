# 19. N-th Fibonacci Number

**Problem:** Find the N-th Fibonacci number.

**Concept:** 
$F(n) = F(n-1) + F(n-2)$. We can use an iterative $O(N)$ approach instead of the slower $O(2^N)$ recursion.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

long long fibonacci(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    cout << "10th Fibonacci: " << fibonacci(10) << "\n"; // 55
    return 0;
}
```
