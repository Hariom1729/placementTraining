# 36. Number of Steps to Reduce to Zero

**Problem:** Given `num`, return the number of steps to reduce it to zero. If even, divide by 2. If odd, subtract 1.

**Concept:** 
Simply simulate the process. Alternatively, count the number of 1s and the total bits in its binary representation.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int numberOfSteps(int num) {
    int steps = 0;
    while(num > 0) {
        if(num % 2 == 0) num /= 2;
        else num -= 1;
        steps++;
    }
    return steps;
}

int main() {
    cout << "Steps for 14: " << numberOfSteps(14) << "\n"; // 6
    return 0;
}
```
