# 9. GCD of an Array

**Problem:** Find the GCD of an entire array of numbers.

**Concept:** 
Compute the GCD of the first two numbers. Take that result, and compute the GCD with the third number, and so on.

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int arrayGCD(vector<int>& arr) {
    int res = arr[0];
    for(int i = 1; i < arr.size(); i++) {
        res = gcd(res, arr[i]);
        if(res == 1) return 1; // Optimization
    }
    return res;
}

int main() {
    vector<int> arr = {12, 24, 36, 48};
    cout << "GCD of Array: " << arrayGCD(arr) << "\n";
    return 0;
}
```
