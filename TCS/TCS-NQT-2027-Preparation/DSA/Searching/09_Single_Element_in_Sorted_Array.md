# Problem 9: Single Element in a Sorted Array

## Problem Statement
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in `O(log n)` time and `O(1)` space.

## Input Format
- A sorted array of integers `nums`.

## Output Format
- An integer representing the single element.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

---

## Approach

Because the array is sorted and every element except one appears twice, the array size `n` will always be **odd**. The pairs follow an index pattern before and after the single element.

**Index Pattern Analysis:**
Suppose the array is: `[1, 1, 2, 3, 3, 4, 4]` (Single element is 2 at index 2).
- **Before the single element:** Pairs are at `(even, odd)` indices. E.g., `(0,1)`.
- **After the single element:** Pairs are at `(odd, even)` indices. E.g., `(3,4)`, `(5,6)`.

We can use Binary Search to find the point where this pattern breaks.
1. Handle edge cases: `n == 1`, or if the first/last element is the single element.
2. Shrink search space to `low = 1`, `high = n - 2`.
3. Find `mid`.
4. If `nums[mid]` is not equal to its left or right neighbor, `mid` is the answer.
5. If `mid` is **even**, and `nums[mid] == nums[mid + 1]`, we are in the left half (pattern intact). Move `low = mid + 1`.
6. If `mid` is **odd**, and `nums[mid] == nums[mid - 1]`, we are in the left half (pattern intact). Move `low = mid + 1`.
7. Otherwise, we are in the right half. Move `high = mid - 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        
        // Edge cases
        if (n == 1) return nums[0];
        if (nums[0] != nums[1]) return nums[0];
        if (nums[n - 1] != nums[n - 2]) return nums[n - 1];
        
        int low = 1, high = n - 2;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // If mid is the single element
            if (nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1]) {
                return nums[mid];
            }
            
            // Check if we are in the left half
            // Left half pattern: (even, odd) pairs
            if ((mid % 2 == 1 && nums[mid] == nums[mid - 1]) || 
                (mid % 2 == 0 && nums[mid] == nums[mid + 1])) {
                low = mid + 1; // Move right
            } else {
                high = mid - 1; // Move left
            }
        }
        
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1, 2, 3, 3, 4, 4, 8, 8};
    cout << "Single Element: " << sol.singleNonDuplicate(nums) << endl; // Expected: 2
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)`
- **Space Complexity:** `O(1)`
