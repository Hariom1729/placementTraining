# 24. Leap Year Check

**Problem:** Check if a given year is a leap year.

**Concept:** 
A year is a leap year if it is perfectly divisible by 400. Or, if it is divisible by 4 but NOT divisible by 100.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isLeapYear(int year) {
    if (year % 400 == 0) return true;
    if (year % 100 == 0) return false;
    if (year % 4 == 0) return true;
    return false;
}

int main() {
    cout << (isLeapYear(2024) ? "Leap Year" : "Not a Leap Year") << "\n";
    return 0;
}
```
