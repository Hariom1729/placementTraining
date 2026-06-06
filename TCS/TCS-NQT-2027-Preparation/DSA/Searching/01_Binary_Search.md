# Problem 1: Binary Search

## Problem Statement
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## Input Format
- A sorted array of integers `nums`.
- An integer `target`.

## Output Format
- An integer representing the index of the `target`, or `-1` if not found.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

## Approach

Since the array is sorted, we can use the **Binary Search** algorithm to find the element in logarithmic time.
1. Initialize two pointers: `low = 0` and `high = n - 1`.
2. While `low <= high`:
   - Calculate `mid = low + (high - low) / 2`.
   - If `nums[mid] == target`, we found the element, return `mid`.
   - If `nums[mid] < target`, the target must be in the right half. Set `low = mid + 1`.
   - If `nums[mid] > target`, the target must be in the left half. Set `high = mid - 1`.
3. If the loop terminates without returning, the element is not in the array. Return `-1`.

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
            // Calculate mid safely to prevent integer overflow
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid; // Target found
            } else if (nums[mid] < target) {
                low = mid + 1; // Discard left half
            } else {
                high = mid - 1; // Discard right half
            }
        }
        
        return -1; // Target not found
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;
    
    cout << "Index of " << target << ": " << sol.search(nums, target) << endl; // Expected: 4
    
    int target2 = 2;
    cout << "Index of " << target2 << ": " << sol.search(nums, target2) << endl; // Expected: -1
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)` where `N` is the number of elements in `nums`. We divide the search space in half at every step.
- **Space Complexity:** `O(1)`. This is the iterative approach, so no extra stack space is used.
