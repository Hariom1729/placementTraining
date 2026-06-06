# Problem 24: Spiral Traversal of Matrix

## Problem Statement
Given an `m x n` `matrix`, return all elements of the matrix in spiral order.

## Input Format
- A 2D array of integers `matrix`.

## Output Format
- A 1D array of integers containing the elements in spiral order.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

---

## Approach

We use 4 pointers/boundaries to keep track of the traversal.
1. Define 4 variables: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
2. Set up a `while` loop that runs as long as `top <= bottom && left <= right`.
3. Inside the loop, do the following 4 traversals in order:
   - **Left to Right:** Traverse from `left` to `right` along the `top` row. Then increment `top`.
   - **Top to Bottom:** Traverse from `top` to `bottom` along the `right` column. Then decrement `right`.
   - **Right to Left:** *Check if `top <= bottom` first.* Traverse from `right` to `left` along the `bottom` row. Then decrement `bottom`.
   - **Bottom to Top:** *Check if `left <= right` first.* Traverse from `bottom` to `top` along the `left` column. Then increment `left`.
4. Return the result vector.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if(matrix.empty()) return ans;
        
        int n = matrix.size();
        int m = matrix[0].size();
        int top = 0, left = 0, bottom = n - 1, right = m - 1;

        while (top <= bottom && left <= right) {
            // Traversal 1: Left to Right
            for (int i = left; i <= right; i++) ans.push_back(matrix[top][i]);
            top++;
            
            // Traversal 2: Top to Bottom
            for (int i = top; i <= bottom; i++) ans.push_back(matrix[i][right]);
            right--;
            
            // Traversal 3: Right to Left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) ans.push_back(matrix[bottom][i]);
                bottom--;
            }
            
            // Traversal 4: Bottom to Top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) ans.push_back(matrix[i][left]);
                left++;
            }
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    vector<int> res = sol.spiralOrder(matrix);
    cout << "Spiral Order: ";
    for (int x : res) cout << x << " "; // Expected: 1 2 3 6 9 8 7 4 5
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M)` where `N` and `M` are the rows and columns. We visit every element exactly once.
- **Space Complexity:** `O(N * M)` for the output array. Auxiliary space is `O(1)`.
