# Trapping Rain Water

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Google, Apple, Microsoft

## Topic
Two Pointers / Arrays / DP

## Pattern
Opposite Ends (Collision) with Max Tracking

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Input
- `height` vector of integers.

## Output
- Return an integer (the total trapped water).

## Sample Test Cases

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Edge Cases
- `height.size() < 3` (impossible to trap water, returns `0`).
- Completely flat or strictly increasing/decreasing array (returns `0`).

## Intuition
How much water can a single index `i` hold?
It depends on the tallest building to its **left** and the tallest building to its **right**.
Water stored at `i` = `min(max_left, max_right) - height[i]`. (If this value is negative, it stores 0 water).

**Approach 1: Dynamic Programming (Prefix Arrays)**
We can precompute `max_left` for every index by sweeping left-to-right.
Then precompute `max_right` by sweeping right-to-left.
Finally, loop through and calculate the water.
Time: $O(N)$, Space: $O(N)$.

**Approach 2: Two Pointers (Optimal)**
We can optimize the space to $O(1)$ by using Two Pointers.
Instead of precomputing arrays, we use `left = 0` and `right = n - 1`, and maintain `leftMax` and `rightMax` variables.
At any point:
- If `height[left] < height[right]`: We are guaranteed that the water height at `left` is bounded by `leftMax` (because `right` is already taller, so the global `max_right` will be at least `height[right]`). So we can calculate the water at `left` immediately!
- If `height[left] >= height[right]`: We are guaranteed that the water height at `right` is bounded by `rightMax`. We can calculate the water at `right` immediately!

This elegant logic computes the exact same answer but uses no extra space!

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. If array size < 3, return 0.
2. `left = 0`, `right = n - 1`.
3. `leftMax = 0`, `rightMax = 0`.
4. `water = 0`.
5. Loop while `left < right`:
   - If `height[left] < height[right]`:
     - If `height[left] >= leftMax`: `leftMax = height[left]` (No water can be trapped here, just updated the wall height).
     - Else: `water += leftMax - height[left]` (Water is trapped!).
     - `left++`.
   - Else:
     - If `height[right] >= rightMax`: `rightMax = height[right]`.
     - Else: `water += rightMax - height[right]`.
     - `right--`.
6. Return `water`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 3) return 0;
        
        int left = 0;
        int right = height.size() - 1;
        
        int leftMax = 0;
        int rightMax = 0;
        int water = 0;
        
        while (left < right) {
            // Which side is lower? Process the lower side first
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left]; // Update max wall on the left
                } else {
                    water += leftMax - height[left]; // Trap water
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right]; // Update max wall on the right
                } else {
                    water += rightMax - height[right]; // Trap water
                }
                right--;
            }
        }
        
        return water;
    }
};
```

## Dry Run
`height = [4, 2, 0, 3, 2, 5]`
- `left = 0` (4), `right = 5` (5). `lMax=0, rMax=0, w=0`.
- `4 < 5`. `4 >= lMax (0)`. `lMax = 4`. `left = 1`.
- `left = 1` (2), `right = 5` (5).
- `2 < 5`. `2 < lMax (4)`. `water += 4 - 2 = 2`. `w = 2`. `left = 2`.
- `left = 2` (0), `right = 5` (5).
- `0 < 5`. `0 < lMax (4)`. `water += 4 - 0 = 4`. `w = 6`. `left = 3`.
- `left = 3` (3), `right = 5` (5).
- `3 < 5`. `3 < lMax (4)`. `water += 4 - 3 = 1`. `w = 7`. `left = 4`.
- `left = 4` (2), `right = 5` (5).
- `2 < 5`. `2 < lMax (4)`. `water += 4 - 2 = 2`. `w = 9`. `left = 5`.
- Loop breaks. Return `9`.

## Common Mistakes
- **Mixing up Container With Most Water and Trapping Rain Water:** Container calculates the area between TWO lines (Width * Height). Rain water calculates the water ABOVE a single block of land (Height - Block_Height). The algorithmic patterns are entirely different (Greedy vs Dynamic Max Tracking).

## Similar Problems
- Container With Most Water
- Trapping Rain Water II (3D version using Priority Queue)
