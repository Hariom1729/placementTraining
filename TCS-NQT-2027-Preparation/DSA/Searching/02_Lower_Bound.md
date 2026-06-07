# Problem 2: Implement Lower Bound

## Problem Statement
Given a sorted array of `N` integers and an integer `X`, find the lower bound of `X`.
The lower bound of `X` is the first index in the array where the value is **greater than or equal to `X`**.
If all elements are smaller than `X`, the lower bound is the size of the array `N`.

## Input Format
- A sorted array of integers `arr`.
- An integer `x`.

## Output Format
- An integer representing the index of the lower bound.

## Constraints
- `1 <= N <= 10^5`
- `0 <= arr[i] <= 10^9`
- `arr` is sorted in non-decreasing order.

---

## Approach

This is a classic variation of Binary Search.
1. Initialize `low = 0`, `high = N - 1`, and an `ans = N` (default if all elements are smaller).
2. While `low <= high`:
   - Calculate `mid = low + (high - low) / 2`.
   - If `arr[mid] >= X`, this `mid` is a potential answer. Save `ans = mid`. Since we want the *first* such element (smallest index), we discard the right half to look for an even smaller index on the left: `high = mid - 1`.
   - If `arr[mid] < X`, the required element must be strictly on the right. Set `low = mid + 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::lower_bound
using namespace std;

class Solution {
public:
    int findLowerBound(vector<int>& arr, int x) {
        int low = 0;
        int high = arr.size() - 1;
        int ans = arr.size(); // Default answer
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Potential answer found
            if (arr[mid] >= x) {
                ans = mid; // Save the index
                high = mid - 1; // Look for a smaller index on the left
            } 
            // Required element is on the right
            else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
    
    // Alternative: Using C++ STL
    int findLowerBoundSTL(vector<int>& arr, int x) {
        auto it = lower_bound(arr.begin(), arr.end(), x);
        return distance(arr.begin(), it);
    }
};

int main() {
    Solution sol;
    vector<int> arr = {1, 2, 8, 10, 11, 12, 19};
    int x = 10;
    cout << "Lower bound index of " << x << ": " << sol.findLowerBound(arr, x) << endl; // Expected: 3
    
    int y = 5;
    cout << "Lower bound index of " << y << ": " << sol.findLowerBound(arr, y) << endl; // Expected: 2 (element 8)
    
    int z = 20;
    cout << "Lower bound index of " << z << ": " << sol.findLowerBound(arr, z) << endl; // Expected: 7 (N)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)` where `N` is the length of the array.
- **Space Complexity:** `O(1)`.

---

## Interview Notes
- `lower_bound` is one of the most critical concepts for solving hard binary search problems (like "Binary Search on Answer"). Understanding this manual logic is extremely important.
