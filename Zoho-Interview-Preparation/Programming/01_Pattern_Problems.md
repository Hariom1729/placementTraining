# Programming: Pattern Problems

Zoho is famous for its intricate pattern printing questions in Round 2. They test your ability to use nested loops and mathematical logic.

## 1. Cross String Pattern
**Problem:** Print the given string in a cross pattern. If the string is "PROGRAM", print it as an X shape.
**Input:** `PROGRAM`
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    string str = "PROGRAM";
    int n = str.length();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j || i + j == n - 1) {
                cout << str[j];
            } else {
                cout << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}
```

## 2. Spiral Number Pattern
**Problem:** Print numbers from 1 to $N^2$ in a spiral format.
**Input:** `N = 4`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    int n = 4;
    vector<vector<int>> matrix(n, vector<int>(n));
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    int num = 1;

    while (top <= bottom && left <= right) {
        for (int i = left; i <= right; i++) matrix[top][i] = num++;
        top++;
        for (int i = top; i <= bottom; i++) matrix[i][right] = num++;
        right--;
        if (top <= bottom) {
            for (int i = right; i >= left; i--) matrix[bottom][i] = num++;
            bottom--;
        }
        if (left <= right) {
            for (int i = bottom; i >= top; i--) matrix[i][left] = num++;
            left++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << setw(3) << matrix[i][j];
        }
        cout << "\n";
    }
    return 0;
}
```

## 3. Diamond Number Pattern
**Problem:** Print a diamond pattern of numbers based on $N$.
**Input:** `N = 3`
**Output:**
```text
  1
 212
32123
 212
  1
```
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 3;
    // Upper Half
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n-i; j++) cout << " ";
        for(int j=i; j>=1; j--) cout << j;
        for(int j=2; j<=i; j++) cout << j;
        cout << "\n";
    }
    // Lower Half
    for(int i=n-1; i>=1; i--) {
        for(int j=1; j<=n-i; j++) cout << " ";
        for(int j=i; j>=1; j--) cout << j;
        for(int j=2; j<=i; j++) cout << j;
        cout << "\n";
    }
    return 0;
}
```

## 4. Pascal's Triangle
**Problem:** Print the first N rows of Pascal's triangle.
**C++ Solution:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) cout << " ";
        int val = 1;
        for (int j = 0; j <= i; j++) {
            cout << val << " ";
            val = val * (i - j) / (j + 1);
        }
        cout << "\n";
    }
    return 0;
}
```

*(Remaining 10-15 pattern problems include: Hollow Square, Z-Pattern, Butterfly Pattern, Right Triangle Number Increment, Floyd's Triangle, etc. The approach fundamentally remains mapping $i$ and $j$ to mathematical equations.)*
