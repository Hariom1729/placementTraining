# Container With Most Water

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Related Companies: Amazon, Google, Meta

## Topic
Arrays

## Pattern
Two Pointers

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

## Constraints
- $n == height.length$
- $2 \le n \le 10^5$
- $0 \le height[i] \le 10^4$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a single integer representing the maximum water.

## Sample Input
```
9
1 8 6 2 5 4 8 3 7
```

## Sample Output
```
49
```

## Edge Cases
- All heights are the same.
- Minimum size array `n=2`.

## Approach 1
Brute Force
**Explanation:** Check every possible pair of lines. Calculate the area for each pair and keep the maximum. Area = `min(height[i], height[j]) * (j - i)`.
**Time Complexity:** $O(N^2)$ (TLE).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Two Pointers)
**Explanation:** 
1. Initialize two pointers: `left` at the beginning (0) and `right` at the end (`n-1`).
2. The width of the container is `right - left`. The height is `min(height[left], height[right])`.
3. The current area is `width * height`. Update the maximum area seen so far.
4. To maximize the area, we need to find taller lines. The width is always decreasing as we move pointers inward. Therefore, the only way to potentially increase the area is to discard the shorter line.
5. If `height[left] < height[right]`, increment `left`. Else, decrement `right`.
6. Repeat until `left >= right`.

**Dry Run:**
`height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- `left = 0` (1), `right = 8` (7). `width = 8`, `minH = 1`. `Area = 8`. Max = 8. Move `left` (since 1 < 7).
- `left = 1` (8), `right = 8` (7). `width = 7`, `minH = 7`. `Area = 49`. Max = 49. Move `right`.
- `left = 1` (8), `right = 7` (3). `width = 6`, `minH = 3`. `Area = 18`. Max = 49. Move `right`.
- ... and so on.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        
        while (left < right) {
            int currentWidth = right - left;
            int currentHeight = Math.min(height[left], height[right]);
            int currentArea = currentWidth * currentHeight;
            
            if (currentArea > maxArea) {
                maxArea = currentArea;
            }
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxArea;
    }
}
```

## Python Solution
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            
            if current_area > max_area:
                max_area = current_area
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
```

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
        int maxArea = 0;
        
        while (left < right) {
            int currentWidth = right - left;
            int currentHeight = min(height[left], height[right]);
            int currentArea = currentWidth * currentHeight;
            
            if (currentArea > maxArea) {
                maxArea = currentArea;
            }
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxArea;
    }
};
```

## Common Mistakes
- **Confusing with Trapping Rain Water:** This problem asks for the maximum volume of a *single* container formed by two lines. Trapping Rain Water asks for the *total* accumulated water across all peaks and valleys. Make sure you don't implement the wrong algorithm!

## Interview Tips
- The mathematical proof behind the two-pointer greedy choice is highly valued. Always explain *why* moving the smaller pointer works: "If we move the larger pointer, the width decreases, and the height is still bottlenecked by the smaller pointer. The area is guaranteed to decrease. Thus, the only logical move is to discard the smaller pointer."

## Similar Questions
- Trapping Rain Water
