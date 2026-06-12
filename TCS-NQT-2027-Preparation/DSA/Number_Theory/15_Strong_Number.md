# 15. Strong Number

**Problem:** Check if a number is a Strong Number.

**Concept:** 
A Strong number is a special number whose sum of the factorial of its digits is equal to the original number. (e.g., $145 = 1! + 4! + 5!$).

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int factorial(int n) {
    if(n == 0 || n == 1) return 1;
    int f = 1;
    for(int i = 2; i <= n; i++) f *= i;
    return f;
}

bool isStrong(int n) {
    int original = n;
    int sum = 0;
    while(n > 0) {
        sum += factorial(n % 10);
        n /= 10;
    }
    return sum == original;
}

int main() {
    cout << (isStrong(145) ? "Strong" : "Not Strong") << "\n";
    return 0;
}
```
