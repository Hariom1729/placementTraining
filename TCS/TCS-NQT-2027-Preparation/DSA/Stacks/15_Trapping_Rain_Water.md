# Problem 15: Trapping Rain Water

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Input Format
- An array of integers `height`.

## Output Format
- An integer representing total water trapped.

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## Approach

While this can be solved using Two Pointers or Prefix/Suffix max arrays, it can also be elegantly solved using a **Monotonic Stack**.

1. Use a stack to store the **indices** of the bars.
2. Iterate `i` through the array.
3. While the stack is not empty and the current height `height[i]` is greater than the height of the bar at the top of the stack:
   - This means we have found a "bowl" or depression that can hold water.
   - The `bottom` of the bowl is `height[st.top()]`. `st.pop()`.
   - If the stack becomes empty, there is no left boundary for this bowl, so break.
   - The left boundary is now at the new top of the stack.
   - The `distance` across the bowl is `i - st.top() - 1`.
   - The `bounded_height` is `min(height[i], height[st.top()]) - bottom`.
   - Add `distance * bounded_height` to the total water.
4. Push `i` to the stack.

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
    int trap(vector<int>& height) {
        int totalWater = 0;
        stack<int> st;
        
        for (int i = 0; i < height.size(); i++) {
            while (!st.empty() && height[i] > height[st.top()]) {
                int bottom = height[st.top()];
                st.pop();
                
                // If there's no left boundary, we can't trap water
                if (st.empty()) {
                    break;
                }
                
                int leftBoundaryIdx = st.top();
                int distance = i - leftBoundaryIdx - 1;
                int boundedHeight = min(height[i], height[leftBoundaryIdx]) - bottom;
                
                totalWater += distance * boundedHeight;
            }
            st.push(i);
        }
        
        return totalWater;
    }
};

int main() {
    Solution sol;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << "Trapped Water: " << sol.trap(height) << endl; // Expected: 6
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each index is pushed and popped exactly once.
- **Space Complexity:** `O(N)` for the stack.
