# 🔥 Top 50 High-Probability TCS NQT Coding Questions (Part 4: Q31 - Q40)

## 31. Print All Prime Numbers in a Given Range
**Concept:** Use a loop and a helper function to check if a number is prime. For a large range, Sieve of Eratosthenes is optimal.
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

void primesInRange(int L, int R) {
    for (int i = L; i <= R; i++) {
        if (isPrime(i)) cout << i << " ";
    }
    cout << endl;
}

int main() {
    primesInRange(10, 30);
    return 0;
}
```

## 32. Toggle All Characters in a String
**Concept:** Convert uppercase characters to lowercase, and lowercase to uppercase using ASCII operations or `<cctype>` functions.
```cpp
#include <iostream>
#include <string>
using namespace std;

string toggleChars(string str) {
    for (char &c : str) {
        if (islower(c)) c = toupper(c);
        else if (isupper(c)) c = tolower(c);
    }
    return str;
}

int main() {
    cout << toggleChars("HeLLo WoRLd") << endl; // Output: hEllO wOrlD
    return 0;
}
```

## 33. Remove Vowels from a String
**Concept:** Iterate through the string and append only the consonants to a new string.
```cpp
#include <iostream>
#include <string>
using namespace std;

string removeVowels(string str) {
    string result = "";
    for(char c : str) {
        char lower = tolower(c);
        if(lower != 'a' && lower != 'e' && lower != 'i' && lower != 'o' && lower != 'u') {
            result += c;
        }
    }
    return result;
}

int main() {
    cout << removeVowels("TCS NQT Preparation") << endl; // Output: TCS NQT Prprtn
    return 0;
}
```

## 34. Longest Palindrome in an Array of Strings
**Concept:** Check each string for palindrome properties, and keep track of the one with the maximum length.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isPalindrome(string str) {
    string rev = str;
    reverse(rev.begin(), rev.end());
    return rev == str;
}

string longestPalindromeStr(vector<string>& arr) {
    string longest = "";
    for(string s : arr) {
        if(isPalindrome(s) && s.length() > longest.length()) {
            longest = s;
        }
    }
    return longest;
}
```

## 35. Find the Equilibrium Index of an Array
**Concept:** An equilibrium index is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
```cpp
#include <iostream>
#include <vector>
using namespace std;

int equilibriumIndex(vector<int>& arr) {
    int totalSum = 0, leftSum = 0;
    for(int num : arr) totalSum += num;
    
    for(int i = 0; i < arr.size(); i++) {
        totalSum -= arr[i]; // totalSum is now right sum for index i
        if(leftSum == totalSum) return i;
        leftSum += arr[i];
    }
    return -1;
}

int main() {
    vector<int> arr = {-7, 1, 5, 2, -4, 3, 0};
    cout << "Equilibrium Index: " << equilibriumIndex(arr) << endl; // Output: 3
    return 0;
}
```

## 36. Left Rotate an Array by K Elements
**Concept:** Use the reversal algorithm: Reverse the first $K$ elements, reverse the remaining $N-K$ elements, then reverse the whole array.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void leftRotate(vector<int>& arr, int k) {
    int n = arr.size();
    k = k % n;
    reverse(arr.begin(), arr.begin() + k);
    reverse(arr.begin() + k, arr.end());
    reverse(arr.begin(), arr.end());
}
```

## 37. Right Rotate an Array by K Elements
**Concept:** Reverse the whole array, reverse the first $K$ elements, then reverse the remaining $N-K$ elements.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rightRotate(vector<int>& arr, int k) {
    int n = arr.size();
    k = k % n;
    reverse(arr.begin(), arr.end());
    reverse(arr.begin(), arr.begin() + k);
    reverse(arr.begin() + k, arr.end());
}
```

## 38. Convert Octal to Decimal
**Concept:** Extract digits from the right, multiply by increasing powers of 8, and add to the sum.
```cpp
#include <iostream>
#include <cmath>
using namespace std;

int octalToDecimal(int octal) {
    int decimal = 0, power = 0;
    while(octal > 0) {
        int lastDigit = octal % 10;
        decimal += lastDigit * pow(8, power);
        power++;
        octal /= 10;
    }
    return decimal;
}

int main() {
    cout << octalToDecimal(17) << endl; // Output: 15
    return 0;
}
```

## 39. Convert Binary to Decimal
**Concept:** Similar to Octal to Decimal, but multiply by powers of 2.
```cpp
#include <iostream>
#include <cmath>
using namespace std;

int binaryToDecimal(long long binary) {
    int decimal = 0, power = 0;
    while(binary > 0) {
        int lastDigit = binary % 10;
        decimal += lastDigit * pow(2, power);
        power++;
        binary /= 10;
    }
    return decimal;
}

int main() {
    cout << binaryToDecimal(1010) << endl; // Output: 10
    return 0;
}
```

## 40. Calculate Permutations (nPr) and Combinations (nCr)
**Concept:** Calculate using the factorial formulas: $nPr = \frac{n!}{(n-r)!}$ and $nCr = \frac{n!}{r!(n-r)!}$.
```cpp
#include <iostream>
using namespace std;

long long fact(int n) {
    long long f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    return f;
}

long long nPr(int n, int r) {
    return fact(n) / fact(n - r);
}

long long nCr(int n, int r) {
    return fact(n) / (fact(r) * fact(n - r));
}

int main() {
    cout << "5P2: " << nPr(5, 2) << ", 5C2: " << nCr(5, 2) << endl;
    return 0;
}
```
