# Programming: Recursion and Number Systems

## 1. Number to Words (Indian System)
**Problem:** Convert an integer (e.g., 1234) into words ("One Thousand Two Hundred Thirty Four").
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string belowTen[] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
string belowTwenty[] = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
string tens[] = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

string helper(int num) {
    if (num < 10) return belowTen[num];
    else if (num < 20) return belowTwenty[num - 10];
    else if (num < 100) return tens[num / 10] + (num % 10 != 0 ? " " + helper(num % 10) : "");
    else if (num < 1000) return belowTen[num / 100] + " Hundred" + (num % 100 != 0 ? " " + helper(num % 100) : "");
    else if (num < 100000) return helper(num / 1000) + " Thousand" + (num % 1000 != 0 ? " " + helper(num % 1000) : "");
    else if (num < 10000000) return helper(num / 100000) + " Lakh" + (num % 100000 != 0 ? " " + helper(num % 100000) : "");
    else return helper(num / 10000000) + " Crore" + (num % 10000000 != 0 ? " " + helper(num % 10000000) : "");
}

string convert(int num) {
    if (num == 0) return "Zero";
    return helper(num);
}

int main() {
    cout << convert(1234567) << "\n"; 
    // "Twelve Lakh Thirty Four Thousand Five Hundred Sixty Seven"
    return 0;
}
```

## 2. Subset Generation
**Problem:** Print all subsets of an array.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

void generateSubsets(vector<int>& arr, int index, vector<int>& current) {
    if (index == arr.size()) {
        cout << "[";
        for(int i=0; i<current.size(); i++) cout << current[i] << (i==current.size()-1 ? "" : ", ");
        cout << "]\n";
        return;
    }
    // Include
    current.push_back(arr[index]);
    generateSubsets(arr, index + 1, current);
    
    // Exclude
    current.pop_back();
    generateSubsets(arr, index + 1, current);
}

int main() {
    vector<int> arr = {1, 2, 3};
    vector<int> current;
    generateSubsets(arr, 0, current);
    return 0;
}
```

## 3. Decimal to Any Base Conversion
**Problem:** Convert a decimal number to base N (2 to 16).
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int number = 255;
    int base = 16;
    string result = "";
    
    while(number > 0) {
        int rem = number % base;
        if(rem < 10) {
            result += to_string(rem);
        } else {
            result += (char)('A' + (rem - 10));
        }
        number /= base;
    }
    reverse(result.begin(), result.end());
    cout << result << "\n"; // "FF"
    return 0;
}
```
