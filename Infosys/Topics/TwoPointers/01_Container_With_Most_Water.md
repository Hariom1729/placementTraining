# Container With Most Water

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2022
Frequency: High

---

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

---

## Input Format
- First line: `N`
- Second line: `N` space-separated integers representing the `height` array.

---

## Output Format
- Return a single integer representing the maximum water area.

---

## Constraints
- $2 \le n \le 10^5$
- $0 \le height[i] \le 10^4$

---

## Examples

### Example 1
**Input:** 
```
9
1 8 6 2 5 4 8 3 7
```
**Output:** 
```
49
```
**Explanation:** The lines at index 1 (height 8) and index 8 (height 7) form a container of width 7. The height is min(8,7) = 7. Area = 7 * 7 = 49.

---

## Brute Force Approach
Calculate the area for every possible pair of lines using two nested loops.
`Area = (j - i) * min(height[i], height[j])`

**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$.

---

## Optimal Approach (Two Pointers)
**Detailed explanation:**
Set two pointers, `left` at the beginning and `right` at the end of the array.
Calculate the area formed between the lines at `left` and `right`.
To maximize the area, we need to keep the taller line and move the pointer pointing to the shorter line inward.
Why? Because moving the taller line inward could only possibly *decrease* the height (since height is bounded by the shorter line) while definitely decreasing the width, resulting in a strictly smaller area.

**Dry Run:**
`height = [1,8,6,2,5,4,8,3,7]`
- `L=0(1)`, `R=8(7)`. Area = `min(1,7) * 8 = 8`. Max = 8.
- Move L (since 1 < 7).
- `L=1(8)`, `R=8(7)`. Area = `min(8,7) * 7 = 49`. Max = 49.
- Move R (since 7 < 8).
- `L=1(8)`, `R=7(3)`. Area = `min(8,3) * 6 = 18`. Max = 49.
- ...

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int max_area = 0;
    
    while (left < right) {
        // Calculate current area
        int current_width = right - left;
        int current_height = min(height[left], height[right]);
        int area = current_width * current_height;
        
        max_area = max(max_area, area);
        
        // Move the shorter line inward
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return max_area;
}
```

---

## Pattern Recognition
**Identify this when:** You need to find a pair of elements at different ends of an array that maximize a certain metric bounded by the minimum of the two elements. The **Two Pointers** greedy logic perfectly applies here.
