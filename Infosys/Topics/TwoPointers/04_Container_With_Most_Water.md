# Container With Most Water

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Two Pointers / Arrays / Greedy

## Pattern
Opposite Ends (Collision)

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

*Notice that you may not slant the container.*

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Input
- `height` vector of integers.

## Output
- Return an integer (the maximum area).

## Sample Test Cases

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are drawn at indices. The maximum area is formed by the line at index 1 (height 8) and index 8 (height 7). 
Width = 8 - 1 = 7. 
Height = min(8, 7) = 7. 
Area = 7 * 7 = 49.
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
```

## Edge Cases
- All lines are the same height.
- Very large widths but tiny heights (and vice versa).
- Large $N$ requires $O(N)$ solution (brute force $O(N^2)$ will TLE).

## Intuition
The area of water is determined by `Width * Height`.
- `Width` = distance between the two lines (`right - left`).
- `Height` = the shorter of the two lines (water spills over the shorter line, so `min(height[left], height[right])`).

We want to MAXIMIZE this area. 
If we start with the widest possible container, we place `left` at the beginning and `right` at the end of the array.
The width is strictly decreasing as we move the pointers inwards. So the only way to possibly get a LARGER area is to find a LARGER HEIGHT!

If `height[left] < height[right]`, the area is limited by `height[left]`. Moving `right` inwards would ONLY decrease the width, and the height can never exceed the bottleneck of `height[left]`. The area is mathematically guaranteed to decrease or stay the same.
Therefore, the ONLY logical move is to throw away the shorter line and move `left` inwards, hoping to find a much taller line to compensate for the lost width!

**Greedy Rule:** Always move the pointer that points to the **shorter** line.

## Optimal Approach (Two Pointers)
**Detailed explanation:**
1. Initialize `left = 0`, `right = height.size() - 1`.
2. Initialize `maxArea = 0`.
3. Loop while `left < right`:
   - Calculate width: `w = right - left`.
   - Calculate bottleneck height: `h = min(height[left], height[right])`.
   - Calculate area: `area = w * h`.
   - Update `maxArea = max(maxArea, area)`.
   - If `height[left] < height[right]`, move `left++` to search for a taller line.
   - Else, move `right--` to search for a taller line.
4. Return `maxArea`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;
        
        while (left < right) {
            // The height of the water is limited by the shorter line
            int current_height = min(height[left], height[right]);
            int width = right - left;
            int current_area = current_height * width;
            
            // Update max_area if we found a larger container
            max_area = max(max_area, current_area);
            
            // Move the pointer of the shorter line inwards
            // because moving the taller line can never increase the area
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return max_area;
    }
};
```

## Dry Run
`height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- `left = 0` (h=1), `right = 8` (h=7).
  - `w = 8`, `h = min(1, 7) = 1`. `area = 8`.
  - `max_area = 8`.
  - `height[left] < height[right]` (1 < 7). Move `left++`.
- `left = 1` (h=8), `right = 8` (h=7).
  - `w = 7`, `h = min(8, 7) = 7`. `area = 49`.
  - `max_area = 49`.
  - `height[left] > height[right]` (8 > 7). Move `right--`.
- `left = 1` (h=8), `right = 7` (h=3).
  - `w = 6`, `h = min(8, 3) = 3`. `area = 18`.
  - `max_area = 49`.
  - `height[left] > height[right]` (8 > 3). Move `right--`.
- ... Process continues ...
- Returns `49`.

## Common Mistakes
- **Moving both pointers when heights are equal:** If `height[left] == height[right]`, it does not matter which pointer you move. Moving either one is mathematically sound. You do not need complex nested while loops to skip equal heights.

## Similar Problems
- Trapping Rain Water (Very different algorithmic pattern despite the similar water theme)
