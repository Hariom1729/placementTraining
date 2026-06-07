# Problem 7: Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

## Input Format
- An array of integers `heights`.

## Output Format
- An integer representing the maximum area.

## Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## Approach: Monotonic Stack (Optimal O(N))

To find the largest rectangle that includes bar `i`, we need to find the first bar to its left that is smaller, and the first bar to its right that is smaller. The area will be `heights[i] * (right_smaller_index - left_smaller_index - 1)`.

We can do this in one pass using a stack that stores indices in **increasing order of their heights**.

1. Create a `stack<int> st` to store indices.
2. Iterate `i` from `0` to `n`. (Go one extra step where `heights[n] = 0` to flush the stack).
3. If the stack is empty or the current bar is higher than the bar at `st.top()`, push the index `i` onto the stack.
4. If the current bar is shorter, it means we have found the **right smaller element** for the bar at `st.top()`.
   - `height = heights[st.top()]`
   - `st.pop()`
   - `width = i - st.top() - 1` (if stack is empty after pop, `width = i`)
   - `maxArea = max(maxArea, height * width)`
   - Repeat this until the top of the stack is smaller than the current bar.
5. Push the current index `i`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> st;
        int maxArea = 0;
        
        for (int i = 0; i <= n; i++) {
            // Treat the end of the array as height 0 to flush remaining elements
            int currHeight = (i == n) ? 0 : heights[i];
            
            while (!st.empty() && currHeight < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();
                
                int width;
                if (st.empty()) {
                    width = i;
                } else {
                    width = i - st.top() - 1;
                }
                
                maxArea = max(maxArea, height * width);
            }
            
            st.push(i);
        }
        
        return maxArea;
    }
};

int main() {
    Solution sol;
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    cout << "Largest Rectangle Area: " << sol.largestRectangleArea(heights) << endl; 
    // Expected: 10 (formed by bars 5 and 6)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Every element is pushed and popped exactly once.
- **Space Complexity:** `O(N)` for the stack.
