# Problem 26: Pascal's Triangle

## Problem Statement
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

## Input Format
- An integer `numRows`.

## Output Format
- A 2D array of integers representing the triangle.

## Constraints
- `1 <= numRows <= 30`

---

## Approach

This problem is a pure implementation of dynamic programming/combinatorics.
1. Create a `vector<vector<int>> res` to hold the final triangle.
2. Loop `i` from `0` to `numRows - 1`.
3. In each iteration, create a vector `row` of size `i + 1` filled with `1`s. (This automatically sets the boundaries to 1).
4. For the inner elements of the row (from `j = 1` to `i - 1`), calculate the value using the previous row in our result: `row[j] = res[i - 1][j - 1] + res[i - 1][j]`.
5. Push this new `row` to `res`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        
        for (int i = 0; i < numRows; i++) {
            // Create a row of size i + 1, all initialized to 1
            vector<int> row(i + 1, 1);
            
            // Calculate the internal values using the row above
            for (int j = 1; j < i; j++) {
                row[j] = res[i - 1][j - 1] + res[i - 1][j];
            }
            
            res.push_back(row);
        }
        
        return res;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> result = sol.generate(5);
    
    for (const auto& row : result) {
        for (int x : row) {
            cout << x << " ";
        }
        cout << endl;
    }
    /* Expected output:
       1
       1 1
       1 2 1
       1 3 3 1
       1 4 6 4 1
    */
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(numRows^2)`. The outer loop runs `numRows` times, and the inner loop runs up to `i` times. Sum of `1 + 2 + 3 + ... + N` is `O(N^2)`.
- **Space Complexity:** `O(numRows^2)` to store the result 2D array. Auxiliary space is `O(1)`.
