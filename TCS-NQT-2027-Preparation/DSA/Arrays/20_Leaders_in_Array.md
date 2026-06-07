# Problem 20: Leaders in an Array

## Problem Statement
Given an array `arr` of `n` positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is strictly greater than all the elements to its right side. The rightmost element is always a leader.

## Input Format
- An array of integers `arr`.

## Output Format
- An array of integers containing all the leaders. The elements can be returned in the order they appear in the original array.

## Constraints
- `1 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^7`

---

## Approach

1. The brute force approach takes `O(N^2)` where for every element, we check all elements to its right.
2. The optimal approach is to traverse the array from **right to left**.
3. The rightmost element is always a leader. Add it to our `ans` array and mark it as the current `max_val`.
4. As we move left, if the current element is strictly greater than `max_val`, it means it's greater than everything to its right.
5. In this case, we add the current element to `ans` and update `max_val` to the current element.
6. Since we traversed from right to left, the leaders are gathered in reverse order. We must reverse the `ans` array before returning.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> leaders(vector<int>& arr) {
        vector<int> ans;
        if (arr.empty()) return ans;
        
        int n = arr.size();
        int max_val = arr[n - 1]; // Rightmost element is always a leader
        ans.push_back(max_val);
        
        // Traverse from right to left
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > max_val) {
                ans.push_back(arr[i]);
                max_val = arr[i]; // Update max
            }
        }
        
        // Reverse to maintain original order
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {16, 17, 4, 3, 5, 2};
    vector<int> res = sol.leaders(arr);
    
    cout << "Leaders: ";
    for (int x : res) {
        cout << x << " "; // Expected: 17 5 2
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements. We traverse the array once backwards and then reverse the output array which is at most `O(N)`.
- **Space Complexity:** `O(N)` in the worst case (if the array is strictly decreasing, every element is a leader). Otherwise `O(1)` auxiliary space.
