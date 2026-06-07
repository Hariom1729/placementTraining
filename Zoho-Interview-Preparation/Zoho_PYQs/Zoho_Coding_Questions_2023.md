# Zoho Coding Questions - 2023

## Round 2: Basic Programming

### 1. Remove Unbalanced Parentheses
**Problem:** Given an expression, remove the minimum number of parentheses to make it valid.
**Input:** `(a)b)c)d(e`
**Output:** `(a)bcd(e)` or `(a)bcde`
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

int main() {
    string s = "(a)b)c)d(e";
    stack<int> st;
    vector<bool> remove(s.length(), false);
    
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == '(') st.push(i);
        else if(s[i] == ')') {
            if(!st.empty()) st.pop();
            else remove[i] = true;
        }
    }
    while(!st.empty()) {
        remove[st.top()] = true;
        st.pop();
    }
    
    string res = "";
    for(int i = 0; i < s.length(); i++) {
        if(!remove[i]) res += s[i];
    }
    cout << res << "\n";
    return 0;
}
```

### 2. Form Largest Number
**Problem:** Given an array of numbers, arrange them to form the largest possible number.
**Input:** `[3, 30, 34, 5, 9]`
**Output:** `9534330`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string a, string b) {
    return a + b > b + a;
}

int main() {
    vector<int> arr = {3, 30, 34, 5, 9};
    vector<string> strArr;
    for(int i : arr) strArr.push_back(to_string(i));
    
    sort(strArr.begin(), strArr.end(), compare);
    
    string res = "";
    for(string s : strArr) res += s;
    
    if(res[0] == '0') cout << "0\n";
    else cout << res << "\n";
    return 0;
}
```

## Round 3: Advanced Logic

### 3. Print Matrix Diagonally Downwards
**Problem:** Given a 2D matrix, print it in a specific zigzag diagonal format.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> mat = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int r = mat.size(), c = mat[0].size();
    
    for(int k=0; k < r+c-1; k++) {
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                if(i+j == k) cout << mat[i][j] << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}
```

## Technical Interview Questions
1. Difference between `std::map` and `std::unordered_map` in C++?
2. What is normalization? Why do we normalize databases?
3. Explain the OSI Model. At which layer does a Router operate?
