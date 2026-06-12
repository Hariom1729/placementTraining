# 35. Check if Array Pairs are Divisible by K

**Problem:** Divide an array into exactly `n/2` pairs such that the sum of each pair is divisible by `k`.

**Concept:** 
Count the frequencies of remainders. Ensure `remainderCount[rem] == remainderCount[k - rem]`. Handle `rem = 0` separately (must be even).

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

bool canArrange(vector<int>& arr, int k) {
    unordered_map<int, int> remCount;
    for(int num : arr) {
        int rem = ((num % k) + k) % k; 
        remCount[rem]++;
    }
    
    for(auto const& [rem, count] : remCount) {
        if(rem == 0) {
            if(count % 2 != 0) return false;
        } else {
            if(remCount[rem] != remCount[k - rem]) return false;
        }
    }
    return true;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 10, 6, 7, 8, 9};
    cout << (canArrange(arr, 5) ? "True" : "False") << "\n";
    return 0;
}
```
