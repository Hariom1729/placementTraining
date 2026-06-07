# Problem 5: Daily Temperatures

## Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature.
If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Input Format
- An array of integers `temperatures`.

## Output Format
- An array of integers representing the number of days to wait.

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## Approach: Monotonic Stack (Storing Indices)

This is a direct application of the "Next Greater Element" problem. However, instead of returning the *value* of the next greater element, we need to return the *difference in indices* (the number of days).
Therefore, our stack must store the **indices**, not the values.

1. Create a `stack<int> st` to store the indices of the days.
2. Initialize an `answer` array of the same size with `0`s.
3. Traverse the array from left to right (or right to left, both work). Let's do right to left.
4. For the current index `i`:
   - While the stack is not empty and the temperature at the top index `temperatures[st.top()]` is **less than or equal to** `temperatures[i]`, we `pop` it.
   - If the stack is not empty, the next warmer day is at `st.top()`. The number of days to wait is `st.top() - i`.
   - Push the current index `i` onto the stack.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> st; // Stores indices
        
        for (int i = n - 1; i >= 0; i--) {
            // Pop indices where the temperature is not warmer
            while (!st.empty() && temperatures[st.top()] <= temperatures[i]) {
                st.pop();
            }
            
            // If stack is not empty, we found a warmer day
            if (!st.empty()) {
                answer[i] = st.top() - i;
            }
            
            // Push current index
            st.push(i);
        }
        
        return answer;
    }
};

int main() {
    Solution sol;
    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
    vector<int> result = sol.dailyTemperatures(temperatures);
    
    cout << "Temperatures: ";
    for(int x : temperatures) cout << x << " ";
    cout << "\nDays to wait: ";
    for(int x : result) cout << x << " ";
    cout << "\n";
    // Expected: 1 1 4 2 1 1 0 0
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each index is pushed onto the stack exactly once and popped at most once.
- **Space Complexity:** `O(N)` for the stack.
