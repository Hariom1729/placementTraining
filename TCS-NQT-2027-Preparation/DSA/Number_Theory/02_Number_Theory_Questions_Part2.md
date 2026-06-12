# Number Theory & Mathematics - TCS NQT Preparation (Part 2)

Here are 15 more advanced Number Theory and Mathematical logic questions frequently asked in TCS NQT, complete with **C++** solutions.

---

## 1. Finding Trailing Zeroes in a Factorial
**Problem:** Find the number of trailing zeroes in $N!$.
**Concept:** A trailing zero is formed by a factor of 10, which is $2 \times 5$. In $N!$, there are always more 2s than 5s, so we just need to count the number of 5s.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int trailingZeroes(int n) {
    int count = 0;
    while (n > 0) {
        n /= 5;
        count += n;
    }
    return count;
}

int main() {
    cout << "Trailing zeroes in 100!: " << trailingZeroes(100) << "\n"; // 24
    return 0;
}
```

## 2. Check if a Number is a Power of Two
**Problem:** Given an integer `n`, return `true` if it is a power of two.
**Concept:** A power of two in binary has exactly one '1' bit (e.g., 8 is `1000`). If we do `n & (n - 1)`, it will be 0.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    if (n <= 0) return false;
    return (n & (n - 1)) == 0;
}

int main() {
    cout << (isPowerOfTwo(16) ? "True" : "False") << "\n";
    return 0;
}
```

## 3. Happy Number
**Problem:** A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle.
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

## 4. Digital Root (Add Digits)
**Problem:** Given an integer `num`, repeatedly add all its digits until the result has only one digit.
**Concept:** Mathematically, the digital root of a number is `num % 9`, except when the number is a multiple of 9, then the root is 9.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int addDigits(int num) {
    if (num == 0) return 0;
    if (num % 9 == 0) return 9;
    return num % 9;
}

int main() {
    cout << "Digital Root of 38: " << addDigits(38) << "\n"; // 3+8=11, 1+1=2
    return 0;
}
```

## 5. Ugly Number
**Problem:** An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

bool isUgly(int n) {
    if (n <= 0) return false;
    while (n % 2 == 0) n /= 2;
    while (n % 3 == 0) n /= 3;
    while (n % 5 == 0) n /= 5;
    return n == 1;
}

int main() {
    cout << (isUgly(6) ? "Ugly" : "Not Ugly") << "\n"; // 6 has prime factors 2 and 3
    return 0;
}
```

## 6. Numbers with Exactly 3 Divisors
**Problem:** Check if a number has exactly 3 divisors.
**Concept:** A number has exactly 3 divisors ONLY if it is the square of a prime number. (e.g., $9 = 3^2$, divisors: 1, 3, 9).
**C++ Solution:**
```cpp
#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0) return false;
    }
    return true;
}

bool hasExactly3Divisors(int n) {
    int root = sqrt(n);
    if(root * root == n && isPrime(root)) {
        return true;
    }
    return false;
}

int main() {
    cout << (hasExactly3Divisors(49) ? "True" : "False") << "\n";
    return 0;
}
```

## 7. Missing Number using Math
**Problem:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number missing from the array.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int expectedSum = n * (n + 1) / 2;
    int actualSum = 0;
    for(int num : nums) {
        actualSum += num;
    }
    return expectedSum - actualSum;
}

int main() {
    vector<int> nums = {3, 0, 1};
    cout << "Missing Number: " << missingNumber(nums) << "\n"; // 2
    return 0;
}
```

## 8. Excel Sheet Column Title
**Problem:** Given an integer column number, return its corresponding column title as it appears in an Excel sheet (e.g., 1 -> A, 28 -> AB).
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string convertToTitle(int columnNumber) {
    string result = "";
    while(columnNumber > 0) {
        columnNumber--; // Make it 0-indexed
        int remainder = columnNumber % 26;
        result += (char)('A' + remainder);
        columnNumber /= 26;
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    cout << convertToTitle(28) << "\n"; // "AB"
    return 0;
}
```

## 9. Sum of All Divisors from 1 to N
**Problem:** Given a number N, find the sum of all divisors of all numbers from 1 to N.
**Concept:** A number `i` will appear as a divisor in all its multiples up to N. The number of multiples is `N / i`.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

long long sumOfAllDivisors(int n) {
    long long totalSum = 0;
    for(int i = 1; i <= n; i++) {
        totalSum += (n / i) * i;
    }
    return totalSum;
}

int main() {
    cout << "Sum for N=4: " << sumOfAllDivisors(4) << "\n"; // 15
    return 0;
}
```

## 10. Water Jug Problem (Using GCD)
**Problem:** You are given two jugs with capacities `x` and `y` liters. There is an infinite amount of water supply. Determine whether it is possible to measure exactly `z` liters using these two jugs.
**Concept:** It is possible if $z$ is a multiple of $\text{GCD}(x, y)$ and $z \le x + y$.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool canMeasureWater(int x, int y, int z) {
    if (x + y < z) return false;
    if (x == z || y == z || x + y == z) return true;
    return z % gcd(x, y) == 0;
}

int main() {
    cout << (canMeasureWater(3, 5, 4) ? "True" : "False") << "\n";
    return 0;
}
```

## 11. Count Primes (Sieve of Eratosthenes)
**Problem:** Count the number of prime numbers strictly less than `n`.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int countPrimes(int n) {
    if (n <= 2) return 0;
    vector<bool> isPrime(n, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int p = 2; p * p < n; p++) {
        if (isPrime[p]) {
            for (int i = p * p; i < n; i += p) {
                isPrime[i] = false;
            }
        }
    }
    
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isPrime[i]) count++;
    }
    return count;
}

int main() {
    cout << "Primes < 10: " << countPrimes(10) << "\n"; // 4 (2, 3, 5, 7)
    return 0;
}
```

## 12. Check if Array Pairs are Divisible by k
**Problem:** Given an integer array `arr` of even length and an integer `k`. Divide the array into exactly `n / 2` pairs such that the sum of each pair is divisible by `k`.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

bool canArrange(vector<int>& arr, int k) {
    unordered_map<int, int> remainderCount;
    for(int num : arr) {
        int rem = ((num % k) + k) % k; // Handles negative numbers
        remainderCount[rem]++;
    }
    
    for(auto const& [rem, count] : remainderCount) {
        if(rem == 0) {
            if(count % 2 != 0) return false;
        } else {
            if(remainderCount[rem] != remainderCount[k - rem]) return false;
        }
    }
    return true;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 10, 6, 7, 8, 9};
    int k = 5;
    cout << (canArrange(arr, k) ? "True" : "False") << "\n";
    return 0;
}
```

## 13. Number of Steps to Reduce a Number to Zero
**Problem:** Given an integer `num`, return the number of steps to reduce it to zero. If the current number is even, divide it by 2. If it is odd, subtract 1 from it.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int numberOfSteps(int num) {
    int steps = 0;
    while(num > 0) {
        if(num % 2 == 0) {
            num /= 2;
        } else {
            num -= 1;
        }
        steps++;
    }
    return steps;
}

int main() {
    cout << "Steps for 14: " << numberOfSteps(14) << "\n"; // 6
    return 0;
}
```

## 14. Add Binary
**Problem:** Given two binary strings `a` and `b`, return their sum as a binary string.
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string addBinary(string a, string b) {
    string res = "";
    int i = a.length() - 1, j = b.length() - 1;
    int carry = 0;
    
    while(i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if(i >= 0) sum += a[i--] - '0';
        if(j >= 0) sum += b[j--] - '0';
        res += to_string(sum % 2);
        carry = sum / 2;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    cout << addBinary("1010", "1011") << "\n"; // "10101"
    return 0;
}
```

## 15. Kth Factor of n
**Problem:** Given two positive integers `n` and `k`. Return the `k`-th factor of `n`. If `n` has fewer than `k` factors, return -1.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int kthFactor(int n, int k) {
    for(int i = 1; i <= n; i++) {
        if(n % i == 0) {
            k--;
            if(k == 0) return i;
        }
    }
    return -1;
}

int main() {
    cout << "3rd factor of 12: " << kthFactor(12, 3) << "\n"; // Factors: 1, 2, 3, 4, 6, 12 -> 3
    return 0;
}
```
