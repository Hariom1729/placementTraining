# 21. N-th Term of Mixed Series

**Problem:** Find the N-th term of the series: `1, 2, 1, 3, 2, 5, 3, 7...` (TCS Specific)

**Concept:** 
This is a mix of two series. Odd indices are Fibonacci numbers, and Even indices are Prime numbers. Separate them based on $N$.

**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

// (Implementation assumes separate functions for Nth Prime and Nth Fibonacci are available)
// This is a common TCS NQT pattern problem. The logic involves isolating the odd/even position.
// If n is odd: find (n/2 + 1)-th Fibonacci
// If n is even: find (n/2)-th Prime
```
