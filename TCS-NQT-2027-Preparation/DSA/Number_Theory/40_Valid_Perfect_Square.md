# 40. Valid Perfect Square without sqrt()

**Problem:** Check if `N` is a perfect square without using built-in `sqrt()`.

**Concept:** 
Use Binary Search from 1 to `N/2`.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPerfectSquare(int num) {
    if (num < 2) return true;
    long left = 2, right = num / 2;
    
    while(left <= right) {
        long mid = left + (right - left) / 2;
        long square = mid * mid;
        if(square == num) return true;
        if(square > num) right = mid - 1;
        else left = mid + 1;
    }
    return false;
}

int main() {
    cout << (isPerfectSquare(16) ? "Perfect Square" : "Not a Perfect Square") << "\n";
    return 0;
}
```
