# Problem 3: Implement Upper Bound

## Problem Statement
Given a sorted array of `N` integers and an integer `X`, find the upper bound of `X`.
The upper bound of `X` is the first index in the array where the value is **strictly greater than `X`**.
If no such element exists, the upper bound is the size of the array `N`.

## Input Format
- A sorted array of integers `arr`.
- An integer `x`.

## Output Format
- An integer representing the index of the upper bound.

## Constraints
- `1 <= N <= 10^5`
- `0 <= arr[i] <= 10^9`
- `arr` is sorted in non-decreasing order.

---

## Approach

This is exactly similar to Lower Bound, but with one crucial difference in the condition.
1. Initialize `low = 0`, `high = N - 1`, and `ans = N`.
2. While `low <= high`:
   - Calculate `mid = low + (high - low) / 2`.
   - If `arr[mid] > X` (strictly greater!), this is a potential answer. Save `ans = mid`. Since we want the first such element, move left: `high = mid - 1`.
   - If `arr[mid] <= X`, the required element must be on the right. Set `low = mid + 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::upper_bound
using namespace std;

class Solution {
public:
    int findUpperBound(vector<int>& arr, int x) {
        int low = 0;
        int high = arr.size() - 1;
        int ans = arr.size(); // Default answer
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Potential answer found (STRICTLY GREATER)
            if (arr[mid] > x) {
                ans = mid;
                high = mid - 1; // Look on the left for a smaller index
            } 
            // Required element is on the right
            else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
    
    // Alternative: Using C++ STL
    int findUpperBoundSTL(vector<int>& arr, int x) {
        auto it = upper_bound(arr.begin(), arr.end(), x);
        return distance(arr.begin(), it);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 2, 8, 10, 10, 12, 19};
    int x = 10;
    cout << "Upper bound index of " << x << ": " << sol.findUpperBound(arr, x) << endl; // Expected: 5 (element 12)
    
    int y = 5;
    cout << "Upper bound index of " << y << ": " << sol.findUpperBound(arr, y) << endl; // Expected: 2 (element 8)
    
    int z = 20;
    cout << "Upper bound index of " << z << ": " << sol.findUpperBound(arr, z) << endl; // Expected: 7 (N)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)` where `N` is the length of the array.
- **Space Complexity:** `O(1)`.
