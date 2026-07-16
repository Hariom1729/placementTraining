# Trapping Rain Water

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Google, Amazon, Goldman Sachs

## Topic
Arrays

## Pattern
Two Pointers / Prefix Arrays

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Constraints
- $n == height.length$
- $1 \le n \le 2 \times 10^4$
- $0 \le height[i] \le 10^5$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers representing heights.

## Output Format
- Return the total units of water trapped.

## Sample Input
```
12
0 1 0 2 1 0 1 3 2 1 2 1
```

## Sample Output
```
6
```

## Edge Cases
- Flat terrain (`[0, 0, 0]`) traps 0 water.
- Increasing or strictly decreasing heights trap 0 water.

## Approach 1
Brute Force
**Explanation:** For every index `i`, finding the max height to its left and max height to its right. The water trapped above `i` is `min(max_left, max_right) - height[i]`.
**Time Complexity:** $O(N^2)$ (TLE)
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Prefix and Suffix Max Arrays)
**Explanation:** Precompute the `max_left` for every index in an array, and `max_right` in another array. Then loop through the heights calculating `min(left_max[i], right_max[i]) - height[i]`.
**Complexity:** $O(N)$ time, $O(N)$ space.

## Approach 3
Optimal Approach (Two Pointers)
**Explanation:** 
Instead of taking $O(N)$ extra space, we can maintain `left_max` and `right_max` variables while shrinking the array using two pointers (`left` and `right`).
Since water is determined by the *minimum* of the two highest walls, we only care about the smaller wall.
- If `height[left] <= height[right]`, the water bound for `left` is absolutely determined by `left_max` (because `right_max` is guaranteed to be at least `height[right]`, which is $\ge$ `height[left]`). We add `left_max - height[left]` to water, then `left++`.
- Conversely, if `height[right] < height[left]`, we do the same from the right side.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int left_max = 0, right_max = 0;
        int water = 0;
        
        while (left < right) {
            if (height[left] <= height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else {
                    water += left_max - height[left];
                }
                left++;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    water += right_max - height[right];
                }
                right--;
            }
        }
        
        return water;
    }
}
```

## Python Solution
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int left_max = 0;
        int right_max = 0;
        int water = 0;
        
        while (left < right) {
            if (height[left] <= height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else {
                    water += left_max - height[left];
                }
                left++;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    water += right_max - height[right];
                }
                right--;
            }
        }
        
        return water;
    }
};
```

## Common Mistakes
- **Handling equal heights:** The `<` vs `<=` condition on `height[left] <= height[right]` is critical to ensure one of the pointers moves.

## Interview Tips
- This is a very common hard question. The $O(N)$ space prefix max solution is usually perfectly acceptable to pass an interview, but deriving the Two Pointers $O(1)$ space solution shows mastery.

## Similar Questions
- Container With Most Water
- Trapping Rain Water II (3D version)
