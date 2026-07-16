# Search a 2D Matrix

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Searching / Matrix

## Pattern
1D to 2D Binary Search Mapping

## Problem Statement
You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in $O(\log(m * n))$ time complexity.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Input
- `matrix` vector of vectors of integers.
- `target` integer.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## Edge Cases
- `1 x 1` matrix.
- Target is smaller than the very first element or larger than the very last element.

## Intuition
Because the properties state that every row is sorted AND the first element of a row is greater than the last element of the previous row, if we were to lay the entire matrix out flat, it would just be one giant perfectly sorted 1D array!
Since it's a perfectly sorted array and we need $O(\log(m * n))$ time, we just do a standard **Binary Search**!

The only tricky part is: how do we do a 1D binary search on a 2D matrix?
We imagine the matrix is a 1D array of size `m * n`.
The `left` pointer starts at `0`, and the `right` pointer starts at `(m * n) - 1`.
When we calculate `mid`, we need to map this 1D index back to 2D coordinates `(row, col)` so we can access `matrix[row][col]`.
- The row is: `mid / n` (because each row has `n` elements).
- The column is: `mid % n` (the remainder is the offset within that row).

That's it! Standard binary search from there.

## Brute Force Approach
**Explanation:** Nested loops iterating through every cell in the matrix.
**Time Complexity:** $O(M \times N)$
**Space Complexity:** $O(1)$

## Optimal Approach (Virtual 1D Binary Search)
**Detailed explanation:**
1. Let `m = matrix.size()` and `n = matrix[0].size()`.
2. Initialize `left = 0` and `right = m * n - 1`.
3. Loop while `left <= right`:
   - Calculate `mid = left + (right - left) / 2`.
   - Map `mid` to 2D coordinates: `row = mid / n`, `col = mid % n`.
   - Let `midValue = matrix[row][col]`.
   - If `midValue == target`, return `true`.
   - If `midValue < target`, set `left = mid + 1`.
   - If `midValue > target`, set `right = mid - 1`.
4. If loop terminates without finding the target, return `false`.

**Time Complexity:** $O(\log(M \times N))$ which is mathematically equivalent to $O(\log M + \log N)$.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Imagine the 2D matrix as a 1D array
        int left = 0;
        int right = m * n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // Convert 1D index back to 2D coordinates
            int row = mid / n;
            int col = mid % n;
            int midValue = matrix[row][col];
            
            if (midValue == target) {
                return true;
            } else if (midValue < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return false;
    }
};
```

## Dry Run
`matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3`
- `m = 3`, `n = 4`.
- `left = 0`, `right = 11`.
- `mid = 5`.
  - `row = 5 / 4 = 1`.
  - `col = 5 % 4 = 1`.
  - `matrix[1][1] = 11`.
- `11 > 3`. Target must be on the left. `right = mid - 1 = 4`.
- `left = 0`, `right = 4`.
- `mid = 2`.
  - `row = 2 / 4 = 0`.
  - `col = 2 % 4 = 2`.
  - `matrix[0][2] = 5`.
- `5 > 3`. Target must be on the left. `right = mid - 1 = 1`.
- `left = 0`, `right = 1`.
- `mid = 0`. `matrix[0][0] = 1`.
- `1 < 3`. Target must be on the right. `left = mid + 1 = 1`.
- `left = 1`, `right = 1`.
- `mid = 1`. `matrix[0][1] = 3`.
- `3 == 3`. Return `true`!

## Common Mistakes
- **Doing Binary Search on rows, then Binary Search on columns:** While this also takes $O(\log M + \log N)$ time, it is much more complex to code and very prone to off-by-one errors when determining which row to search in. The 1D mapping is vastly superior and less error-prone.

## Similar Problems
- Search a 2D Matrix II (The matrix is no longer fully sorted sequentially).
