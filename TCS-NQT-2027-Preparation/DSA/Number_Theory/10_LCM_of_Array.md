# 10. LCM of an Array

**Problem:** Find the LCM of an entire array of numbers.

**Concept:** 
Keep a running LCM. The new LCM is the LCM of the running LCM and the next array element.

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

long long arrayLCM(vector<int>& arr) {
    long long res = arr[0];
    for(int i = 1; i < arr.size(); i++) {
        res = (res / gcd(res, arr[i])) * arr[i];
    }
    return res;
}

int main() {
    vector<int> arr = {2, 3, 4, 5};
    cout << "LCM of Array: " << arrayLCM(arr) << "\n"; // 60
    return 0;
}
```
