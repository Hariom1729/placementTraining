# Problem 7: Search in Rotated Sorted Array

## Problem Statement
There is an integer array `nums` sorted in ascending order (with **distinct** values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).
For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

## Input Format
- An array of integers `nums`.
- An integer `target`.

## Output Format
- An integer index or `-1`.

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

---

## Approach

In a rotated sorted array, if you pick any `mid` point, **at least one half of the array (either left or right) will always be strictly sorted**.
1. Find `mid`.
2. Check if `nums[mid] == target`.
3. **Check if the left half is sorted:** `nums[low] <= nums[mid]`
   - If it is sorted, check if the `target` lies within this left half: `nums[low] <= target && target <= nums[mid]`.
   - If yes, eliminate the right half: `high = mid - 1`.
   - If no, eliminate the left half: `low = mid + 1`.
4. **Otherwise, the right half must be sorted:**
   - Check if the `target` lies within this right half: `nums[mid] <= target && target <= nums[high]`.
   - If yes, eliminate the left half: `low = mid + 1`.
   - If no, eliminate the right half: `high = mid - 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) return mid;
            
            // Left half is sorted
            if (nums[low] <= nums[mid]) {
                if (target >= nums[low] && target < nums[mid]) {
                    high = mid - 1; // Target is in the left half
                } else {
                    low = mid + 1;  // Target is in the right half
                }
            } 
            // Right half is sorted
            else {
                if (target > nums[mid] && target <= nums[high]) {
                    low = mid + 1;  // Target is in the right half
                } else {
                    high = mid - 1; // Target is in the left half
                }
            }
        }
        
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    
    cout << "Index of " << target << ": " << sol.search(nums, target) << endl; // Expected: 4
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)`. We discard half the array at each step.
- **Space Complexity:** `O(1)`.
