# Programming: Matrix Problems

Matrices are heavily tested to check nested loop boundaries and bounds checking.

## 1. Rotate Matrix 90 Degrees In-Place
**Problem:** Rotate an N x N matrix by 90 degrees clockwise without using extra space.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> matrix = { {1,2,3}, {4,5,6}, {7,8,9} };
    int n = matrix.size();
    
    // Step 1: Transpose
    for(int i=0; i<n; i++) {
        for(int j=i; j<n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    // Step 2: Reverse each row
    for(int i=0; i<n; i++) {
        int left = 0, right = n-1;
        while(left < right) {
            swap(matrix[i][left], matrix[i][right]);
            left++; right--;
        }
    }
    
    // Output
    for(auto& row : matrix) {
        for(int val : row) cout << val << " ";
        cout << "\n";
    }
    return 0;
}
```

## 2. Print Matrix Diagonally
**Problem:** Given a 2D matrix, print all elements diagonally.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> mat = { {1,2,3}, {4,5,6}, {7,8,9} };
    int m = mat.size();
    int n = mat[0].size();
    
    // First half
    for (int row = 0; row < m; row++) {
        int i = row, j = 0;
        while (i >= 0 && j < n) {
            cout << mat[i][j] << " ";
            i--; j++;
        }
        cout << "\n";
    }
    // Second half
    for (int col = 1; col < n; col++) {
        int i = m - 1, j = col;
        while (i >= 0 && j < n) {
            cout << mat[i][j] << " ";
            i--; j++;
        }
        cout << "\n";
    }
    return 0;
}
```

## 3. Set Matrix Zeroes
**Problem:** If an element is 0, set its entire row and column to 0. Must be done in $O(1)$ extra space.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> matrix = { {1,1,1}, {1,0,1}, {1,1,1} };
    bool firstRowHasZero = false, firstColHasZero = false;
    int m = matrix.size();
    int n = matrix[0].size();
    
    for(int j=0; j<n; j++) {
        if(matrix[0][j] == 0) firstRowHasZero = true;
    }
    for(int i=0; i<m; i++) {
        if(matrix[i][0] == 0) firstColHasZero = true;
    }
    
    for(int i=1; i<m; i++) {
        for(int j=1; j<n; j++) {
            if(matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    for(int i=1; i<m; i++) {
        for(int j=1; j<n; j++) {
            if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
    if(firstRowHasZero) {
        for(int j=0; j<n; j++) matrix[0][j] = 0;
    }
    if(firstColHasZero) {
        for(int i=0; i<m; i++) matrix[i][0] = 0;
    }
    
    return 0;
}
```
