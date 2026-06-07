# Problem 8: Find Minimum in Rotated Sorted Array

## Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. 
Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the minimum element.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.

---

## Approach

Similar to searching in a rotated array, we use the property that one half is always sorted.
1. We initialize `ans = INT_MAX`.
2. Find `mid`.
3. If the **left half is sorted** (`nums[low] <= nums[mid]`):
   - The minimum element in this left half will always be `nums[low]`.
   - Update `ans = min(ans, nums[low])`.
   - Since we have recorded the minimum from the left half, we can discard it and search the right half: `low = mid + 1`.
4. If the **right half is sorted** (`nums[mid] <= nums[high]`):
   - The minimum element in this right half will always be `nums[mid]`.
   - Update `ans = min(ans, nums[mid])`.
   - Discard the right half and search the left half: `high = mid - 1`.

*Optimization:* If the entire array from `low` to `high` is already sorted (`nums[low] <= nums[high]`), the minimum is definitively `nums[low]`. We can update `ans` and break early.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        int ans = INT_MAX;
        
        while (low <= high) {
            // Optimization: If the search space is already sorted
            if (nums[low] <= nums[high]) {
                ans = min(ans, nums[low]);
                break;
            }
            
            int mid = low + (high - low) / 2;
            
            // Left half is sorted
            if (nums[low] <= nums[mid]) {
                ans = min(ans, nums[low]);
                low = mid + 1;
            } 
            // Right half is sorted
            else {
                ans = min(ans, nums[mid]);
                high = mid - 1;
            }
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {3, 4, 5, 1, 2};
    cout << "Minimum element: " << sol.findMin(nums) << endl; // Expected: 1
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)`. We discard half the search space at each step.
- **Space Complexity:** `O(1)`.
