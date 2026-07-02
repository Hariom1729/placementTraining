# 🔥 Top 50 High-Probability TCS NQT Coding Questions (Part 2: Q11 - Q20)

## 11. Check if a Given Year is a Leap Year
**Concept:** A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.
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
    cout << (isLeapYear(2024) ? "Leap Year" : "Not a Leap Year") << endl;
    return 0;
}
```

## 12. Find the GCD and LCM of Two Numbers
**Concept:** The product of two numbers is equal to the product of their GCD and LCM.
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}

int main() {
    int a = 12, b = 15;
    cout << "GCD: " << gcd(a, b) << ", LCM: " << lcm(a, b) << endl;
    return 0;
}
```

## 13. Fibonacci Series up to N terms
**Concept:** Iterate and compute the next term as the sum of the previous two terms.
```cpp
#include <iostream>
using namespace std;

void printFibonacci(int n) {
    long long a = 0, b = 1, nextTerm;
    for (int i = 1; i <= n; ++i) {
        cout << a << " ";
        nextTerm = a + b;
        a = b;
        b = nextTerm;
    }
    cout << endl;
}

int main() {
    printFibonacci(10);
    return 0;
}
```

## 14. Check if a String is a Palindrome
**Concept:** Use two pointers, one at the start and one at the end, and compare characters.
```cpp
#include <iostream>
using namespace std;

bool isPalindrome(string str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        if (str[left] != str[right]) return false;
        left++;
        right--;
    }
    return true;
}

int main() {
    cout << (isPalindrome("radar") ? "Palindrome" : "Not Palindrome") << endl;
    return 0;
}
```

## 15. Remove All Duplicates from a String
**Concept:** Use a boolean array or hash set to keep track of visited characters.
```cpp
#include <iostream>
#include <vector>
using namespace std;

string removeDuplicates(string str) {
    vector<bool> visited(256, false);
    string result = "";
    for (char c : str) {
        if (!visited[c]) {
            result += c;
            visited[c] = true;
        }
    }
    return result;
}

int main() {
    cout << removeDuplicates("programming") << endl; // Output: progamin
    return 0;
}
```

## 16. Maximum Scalar Product of Two Vectors
**Concept:** To get the maximum scalar (dot) product, sort both arrays in ascending order and multiply their corresponding elements.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxScalarProduct(vector<int>& arr1, vector<int>& arr2) {
    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());
    
    int product = 0;
    for (int i = 0; i < arr1.size(); i++) {
        product += arr1[i] * arr2[i];
    }
    return product;
}

int main() {
    vector<int> arr1 = {1, 2, 6, 3, 7};
    vector<int> arr2 = {10, 7, 45, 21, 34};
    cout << "Max Scalar Product: " << maxScalarProduct(arr1, arr2) << endl;
    return 0;
}
```

## 17. Check if a Number is Prime
**Concept:** A prime number is only divisible by 1 and itself. Check divisibility up to the square root of the number.
```cpp
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    cout << (isPrime(29) ? "Prime" : "Not Prime") << endl;
    return 0;
}
```

## 18. Find the Factorial of a Number
**Concept:** Compute $N! = 1 \times 2 \times \dots \times N$. Use an iterative loop to avoid recursion overhead.
```cpp
#include <iostream>
using namespace std;

long long factorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    cout << "Factorial of 5: " << factorial(5) << endl; // Output: 120
    return 0;
}
```

## 19. Sum of Digits of a Number
**Concept:** Extract the last digit using `% 10` and reduce the number using `/ 10`.
```cpp
#include <iostream>
using namespace std;

int sumOfDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    cout << "Sum of digits of 1234: " << sumOfDigits(1234) << endl; // Output: 10
    return 0;
}
```

## 20. Check if a Number is an Armstrong Number
**Concept:** A number is an Armstrong number if the sum of its own digits each raised to the power of the number of digits equals the number itself.
```cpp
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

bool isArmstrong(int n) {
    int original = n, sum = 0;
    int digits = to_string(n).length();
    
    while (n > 0) {
        int d = n % 10;
        sum += pow(d, digits);
        n /= 10;
    }
    return sum == original;
}

int main() {
    cout << (isArmstrong(153) ? "Armstrong" : "Not Armstrong") << endl;
    return 0;
}
```
