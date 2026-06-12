# 27. Happy Number

**Problem:** A happy number is defined by replacing the number by the sum of the squares of its digits repeatedly until it equals 1 or loops endlessly.

**Concept:** 
Use a HashSet to keep track of seen numbers. If we see a number we've already calculated, we are in an infinite loop, so it's not a happy number.

**C++ Solution:**
```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

int getNext(int n) {
    int totalSum = 0;
    while (n > 0) {
        int d = n % 10;
        n /= 10;
        totalSum += d * d;
    }
    return totalSum;
}

bool isHappy(int n) {
    unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        n = getNext(n);
    }
    return n == 1;
}

int main() {
    cout << (isHappy(19) ? "Happy" : "Not Happy") << "\n";
    return 0;
}
```
