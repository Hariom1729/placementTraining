# Problem 6: Next Smaller Element

## Problem Statement
Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element `x` is the first smaller element on the right side of `x` in the array.
Elements for which no smaller element exist, consider the next smaller element as `-1`.

## Input Format
- An array of integers `arr`.

## Output Format
- An array of integers representing the next smaller element for each index.

## Constraints
- `1 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^9`

---

## Approach: Monotonic Increasing Stack

This is exactly the same logic as the "Next Greater Element", but instead of looking for larger elements, we look for smaller ones.
Thus, our stack should maintain an **increasing** order.

1. Traverse from right to left.
2. We maintain a stack.
3. For the current element `arr[i]`:
   - While the stack is not empty and the top of the stack is **greater than or equal to** `arr[i]`, we `pop` it. (Because larger elements cannot be the "next smaller" element).
   - If the stack becomes empty, answer for `i` is `-1`.
   - If the stack is not empty, the top element is strictly smaller. Answer for `i` is `st.top()`.
4. Push `arr[i]` onto the stack.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextSmallerElement(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n, -1);
        stack<int> st;
        
        for (int i = n - 1; i >= 0; i--) {
            // Pop elements that are greater than or equal to current
            while (!st.empty() && st.top() >= arr[i]) {
                st.pop();
            }
            
            // If stack is not empty, top is the next smaller element
            if (!st.empty()) {
                result[i] = st.top();
            }
            
            // Push current element
            st.push(arr[i]);
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {4, 8, 5, 2, 25};
    vector<int> result = sol.nextSmallerElement(arr);
    
    cout << "Input:  ";
    for(int x : arr) cout << x << " ";
    cout << "\nResult: ";
    for(int x : result) cout << x << " ";
    cout << "\n";
    // Expected: 2 5 2 -1 -1
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each element is pushed and popped at most once.
- **Space Complexity:** `O(N)` for the stack.
