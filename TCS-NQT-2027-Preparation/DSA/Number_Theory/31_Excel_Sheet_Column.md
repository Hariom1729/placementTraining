# 31. Excel Sheet Column Title

**Problem:** Given an integer column number, return its corresponding column title as it appears in an Excel sheet (e.g., 1 -> A, 28 -> AB).

**Concept:** 
Subtract 1 to make it 0-indexed, find the remainder when divided by 26, convert to a character, and divide by 26.

**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string convertToTitle(int columnNumber) {
    string result = "";
    while(columnNumber > 0) {
        columnNumber--; 
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
