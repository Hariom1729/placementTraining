# 39. Count Odd Numbers in an Interval Range

**Problem:** Given two non-negative integers `low` and `high`. Return the count of odd numbers between `low` and `high` (inclusive).

**Concept:** 
The number of odds between 1 and `N` is `(N + 1) / 2`. So, we can compute `count(high) - count(low - 1)`.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int countOdds(int low, int high) {
    int countHigh = (high + 1) / 2;
    int countLow = low / 2;
    return countHigh - countLow;
}

int main() {
    cout << "Odds between 3 and 7: " << countOdds(3, 7) << "\n"; // 3
    return 0;
}
```
