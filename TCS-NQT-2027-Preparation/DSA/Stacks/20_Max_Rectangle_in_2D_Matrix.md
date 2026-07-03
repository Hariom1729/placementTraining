# Maximal Rectangle in a 2D Matrix

## Problem Statement
Given a `rows x cols` binary matrix filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

**Example:**
- **Input:** 
  matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
  ]
- **Output:** 6
- **Explanation:** The maximal rectangle spans across row 1 and 2, col 2 to 4 (area 2x3 = 6).

## Optimal Approach (Extension of Largest Rectangle in Histogram)
We can treat each row of the matrix as the base of a histogram. 
- For the first row, the histogram heights are just the values of the row.
- For subsequent rows, if the matrix element is '1', the height becomes `previous height + 1`. If it's '0', the height becomes `0`.
- We run the `Largest Rectangle in Histogram` algorithm on each row and keep track of the maximum area.

### C++ Code
```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

// Helper function: Largest Rectangle in Histogram
int largestRectangleArea(vector<int>& heights) {
    stack<int> s;
    int maxArea = 0;
    int n = heights.size();
    
    for (int i = 0; i <= n; i++) {
        while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
            int height = heights[s.top()];
            s.pop();
            int width;
            if (s.empty()) width = i;
            else width = i - s.top() - 1;
            maxArea = max(maxArea, width * height);
        }
        s.push(i);
    }
    return maxArea;
}

int maximalRectangle(vector<vector<char>>& matrix) {
    if (matrix.empty()) return 0;
    
    int maxArea = 0;
    vector<int> heights(matrix[0].size(), 0);
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[i][j] == '1') {
                heights[j]++;
            } else {
                heights[j] = 0; // reset
            }
        }
        // Calculate max area for the histogram at this row
        maxArea = max(maxArea, largestRectangleArea(heights));
    }
    
    return maxArea;
}

int main() {
    vector<vector<char>> matrix = {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','1','1','1'},
        {'1','0','0','1','0'}
    };
    cout << "Max Rectangle Area: " << maximalRectangle(matrix) << endl; // Output: 6
    return 0;
}
```

### Complexity
- **Time Complexity:** $O(R \times C)$, where $R$ is rows and $C$ is cols. We process each cell in the matrix to build histograms, and computing the max area for each row takes $O(C)$.
- **Space Complexity:** $O(C)$ to store the histogram heights for a row.
