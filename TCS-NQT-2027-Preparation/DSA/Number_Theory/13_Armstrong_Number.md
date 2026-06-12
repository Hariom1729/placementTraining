# 13. Armstrong Number

**Problem:** Check if a number is an Armstrong number. 

**Concept:** 
A number is an Armstrong number if the sum of its own digits each raised to the power of the number of digits equals the number itself (e.g., $153 = 1^3 + 5^3 + 3^3$).

**C++ Solution:**
```cpp
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

bool isArmstrong(int n) {
    int original = n;
    int sum = 0;
    int digits = to_string(n).length();
    
    while (n > 0) {
        int d = n % 10;
        sum += pow(d, digits);
        n /= 10;
    }
    return sum == original;
}

int main() {
    cout << (isArmstrong(153) ? "Armstrong" : "Not Armstrong") << "\n";
    return 0;
}
```
