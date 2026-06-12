# 3. Sieve of Eratosthenes

**Problem:** Find all prime numbers strictly less than `N` efficiently.

**Concept:** 
Create a boolean array. Start from the first prime (2), and mark all its multiples as `false` (not prime). Move to the next `true` index and repeat.

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

void sieve(int n) {
    vector<bool> prime(n + 1, true);
    prime[0] = prime[1] = false;
    
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }
    
    for (int p = 2; p <= n; p++) {
        if (prime[p]) cout << p << " ";
    }
    cout << "\n";
}

int main() {
    sieve(30);
    return 0;
}
```
