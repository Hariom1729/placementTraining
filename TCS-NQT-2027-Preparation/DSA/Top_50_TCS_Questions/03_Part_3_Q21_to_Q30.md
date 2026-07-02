# 🔥 Top 50 High-Probability TCS NQT Coding Questions (Part 3: Q21 - Q30)

## 21. Replace All 0s with 1s in a Given Integer
**Concept:** Convert the integer to a string, replace characters, and convert back to integer.
```cpp
#include <iostream>
#include <string>
using namespace std;

int replaceZeros(int n) {
    string str = to_string(n);
    for (char &c : str) {
        if (c == '0') c = '1';
    }
    return stoi(str);
}

int main() {
    cout << replaceZeros(102030) << endl; // Output: 112131
    return 0;
}
```

## 22. Count Vowels, Consonants, Spaces in a String
**Concept:** Iterate over each character and check using `isalpha()`, `isspace()`, and a custom vowel check.
```cpp
#include <iostream>
#include <cctype>
using namespace std;

void countCharacters(string str) {
    int vowels = 0, consonants = 0, spaces = 0;
    for (char c : str) {
        c = tolower(c);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels++;
        } else if (isalpha(c)) {
            consonants++;
        } else if (isspace(c)) {
            spaces++;
        }
    }
    cout << "Vowels: " << vowels << ", Consonants: " << consonants << ", Spaces: " << spaces << endl;
}

int main() {
    countCharacters("Hello World 123");
    return 0;
}
```

## 23. Find the Non-Repeating Elements in an Array
**Concept:** Use a hash map to count the frequencies. Elements with a frequency of 1 are non-repeating.
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void nonRepeating(vector<int>& arr) {
    unordered_map<int, int> freq;
    for (int num : arr) freq[num]++;
    
    for (int num : arr) {
        if (freq[num] == 1) {
            cout << num << " ";
        }
    }
    cout << endl;
}

int main() {
    vector<int> arr = {1, 2, -1, 1, 3, 1};
    nonRepeating(arr); // Output: 2 -1 3
    return 0;
}
```

## 24. Sort First Half in Ascending, Second Half in Descending Order
**Concept:** Find the midpoint. Sort the first half ascending, and sort the second half descending using a custom comparator.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void customSort(vector<int>& arr) {
    int n = arr.size();
    sort(arr.begin(), arr.begin() + n/2);
    sort(arr.begin() + n/2, arr.end(), greater<int>());
}

int main() {
    vector<int> arr = {5, 4, 6, 2, 1, 3, 8, -1};
    customSort(arr);
    for (int num : arr) cout << num << " "; 
    // Output: 2 4 5 6 8 3 1 -1 (assuming n/2 = 4)
    return 0;
}
```

## 25. Find the Frequency of Elements in an Array
**Concept:** Traverse the array and keep a count in a Hash Map. Very standard TCS question.
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void countFrequency(vector<int>& arr) {
    unordered_map<int, int> freq;
    for(int num : arr) freq[num]++;
    
    for(auto it : freq) {
        cout << it.first << " occurs " << it.second << " times\n";
    }
}
```

## 26. Count Even and Odd Elements in an Array
**Concept:** Simple traversal using the modulo `% 2` operator.
```cpp
#include <iostream>
#include <vector>
using namespace std;

void countEvenOdd(vector<int>& arr) {
    int even = 0, odd = 0;
    for(int num : arr) {
        if (num % 2 == 0) even++;
        else odd++;
    }
    cout << "Even: " << even << ", Odd: " << odd << endl;
}
```

## 27. Matrix Multiplication
**Concept:** To multiply two matrices of sizes $M \times N$ and $N \times P$, use three nested loops. Time complexity $O(M \times N \times P)$.
```cpp
#include <iostream>
#include <vector>
using namespace std;

void multiplyMatrices(vector<vector<int>>& A, vector<vector<int>>& B) {
    int m = A.size(), n = A[0].size(), p = B[0].size();
    vector<vector<int>> C(m, vector<int>(p, 0));
    
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) {
            for(int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) cout << C[i][j] << " ";
        cout << endl;
    }
}
```

## 28. Find the Transpose of a Matrix
**Concept:** Swap `matrix[i][j]` with `matrix[j][i]` for all $j > i$.
```cpp
#include <iostream>
#include <vector>
using namespace std;

void transpose(vector<vector<int>>& matrix) {
    int n = matrix.size();
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
}
```

## 29. Calculate the Area of a Circle
**Concept:** A basic geometry problem. The formula is $\pi \times r^2$.
```cpp
#include <iostream>
#define PI 3.1415926535
using namespace std;

double circleArea(double radius) {
    return PI * radius * radius;
}

int main() {
    cout << "Area of circle with radius 5: " << circleArea(5) << endl;
    return 0;
}
```

## 30. Find the Roots of a Quadratic Equation
**Concept:** For $ax^2 + bx + c = 0$, the roots are calculated using the determinant $D = b^2 - 4ac$.
```cpp
#include <iostream>
#include <cmath>
using namespace std;

void findRoots(int a, int b, int c) {
    if (a == 0) return;
    
    double d = b * b - 4 * a * c;
    double sqrt_val = sqrt(abs(d));
    
    if (d > 0) {
        cout << "Roots are real and different \n";
        cout << (double)(-b + sqrt_val) / (2 * a) << "\n"
             << (double)(-b - sqrt_val) / (2 * a) << "\n";
    }
    else if (d == 0) {
        cout << "Roots are real and same \n";
        cout << -(double)b / (2 * a) << "\n";
    }
    else {
        cout << "Roots are complex \n";
        cout << -(double)b / (2 * a) << " + i" << sqrt_val / (2 * a) << "\n"
             << -(double)b / (2 * a) << " - i" << sqrt_val / (2 * a) << "\n";
    }
}
```
