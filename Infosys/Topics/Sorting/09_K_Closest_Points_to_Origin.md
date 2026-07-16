# K Closest Points to Origin

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Sorting / Heap / Math

## Pattern
Custom Sorting / Max-Heap

## Problem Statement
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.
The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).
You may return the answer in **any order**. The answer is guaranteed to be unique (except for the order that it is in).

## Constraints
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Input
- `points` vector of vectors (2D array).
- `k` integer.

## Output
- Return a 2D vector containing `k` points.

## Sample Test Cases

**Example 1:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points, so we return [[-2,2]].
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## Edge Cases
- Points equidistant from the origin (order doesn't matter per problem statement).
- `k` equals `points.length` (return all points).

## Intuition
We need to find the `k` "smallest" elements based on a custom metric (Euclidean distance).
First, we can avoid calculating the expensive `sqrt()` because if $A^2 < B^2$, then $A < B$. We can just compare $(x^2 + y^2)$!

**Approach 1: Custom Sort.**
Sort the entire array using a custom lambda function that compares the squared distances. Then return the first `k` elements.
Time: $O(N \log N)$. Space: $O(1)$.

**Approach 2: Max-Heap (Priority Queue).**
When we want the `k` *smallest* elements, we maintain a **Max-Heap** of size `k`!
Why a Max-Heap? Because as we iterate through the array, if the heap exceeds size `k`, we pop the top element (which is the *largest* distance). By continuously throwing away the largest distances, we are left with the `k` smallest distances in the heap!
Time: $O(N \log K)$. Space: $O(K)$.

Let's implement the **Custom Sort** as it is often faster in reality due to caching, and extremely clean to write in C++.

## Optimal Approach (Custom Sort / Partial Sort)
**Detailed explanation:**
1. Use `std::sort` (or `std::partial_sort` for better performance) on the `points` array.
2. The comparator lambda should be: 
   `[](const vector<int>& a, const vector<int>& b) { return (a[0]*a[0] + a[1]*a[1]) < (b[0]*b[0] + b[1]*b[1]); }`
3. After sorting, simply return the sub-vector from `0` to `k`. `return vector<vector<int>>(points.begin(), points.begin() + k);`

**Time Complexity:** $O(N \log N)$ (or $O(N \log K)$ with `partial_sort`).
**Space Complexity:** $O(1)$ in-place sorting.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Custom sort based on squared Euclidean distance from origin
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            int distA = a[0] * a[0] + a[1] * a[1];
            int distB = b[0] * b[0] + b[1] * b[1];
            // We want ascending order, so return true if A is smaller than B
            return distA < distB;
        });
        
        // Return the first k elements
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};
```

*(Bonus note: If you want to impress an interviewer, use `nth_element` in C++ instead of `sort`. It uses Quickselect internally and guarantees average $O(N)$ time! Just change `sort(...)` to `nth_element(points.begin(), points.begin() + k, points.end(), lambda);`)*

## Dry Run
`points = [[3,3], [5,-1], [-2,4]], k = 2`
- Distances:
  - `[3,3]`: $3^2 + 3^2 = 18$
  - `[5,-1]`: $5^2 + (-1)^2 = 26$
  - `[-2,4]`: $(-2)^2 + 4^2 = 20$
- Sorted array based on distances: `[[3,3], [-2,4], [5,-1]]`
- We return the first 2 elements: `[[3,3], [-2,4]]`.

## Common Mistakes
- **Computing `sqrt`:** Using `#include <cmath>` and `sqrt()` introduces floating-point precision issues and drastically slows down the algorithm. Stick to integer squares!
- **Using Min-Heap instead of Max-Heap:** If you use a Min-Heap for finding "smallest" elements, you must push ALL $N$ elements into the heap and then pop $K$ times. This is $O(N \log N)$. A Max-Heap allows you to bound the size to $K$, yielding $O(N \log K)$.

## Similar Problems
- Kth Largest Element in an Array
- Top K Frequent Elements
