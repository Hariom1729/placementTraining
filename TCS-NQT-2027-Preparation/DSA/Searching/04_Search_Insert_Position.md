# Problem 4: Search Insert Position

## Problem Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Input Format
- A sorted array of distinct integers `nums`.
- An integer `target`.

## Output Format
- An integer representing the insertion index.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`

---

## Approach

If you analyze the problem statement carefully, "the index where it would be if it were inserted in order" is the exact definition of the **Lower Bound**.
The lower bound gives the first index where `arr[index] >= target`. 
- If `arr[index] == target`, it returns the index (target found).
- If `arr[index] > target`, it returns the index where the target *should* be inserted to maintain sorted order.
- If target is greater than all elements, lower bound returns `N` (size of array), which is the correct insertion index at the end.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int ans = nums.size();
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] >= target) {
                ans = mid;      // Potential insertion index
                high = mid - 1; // Try to find a smaller index on the left
            } else {
                low = mid + 1;  // Target must go to the right
            }
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 3, 5, 6};
    
    cout << "Insert 5 at: " << sol.searchInsert(nums, 5) << endl; // Expected: 2 (Found)
    cout << "Insert 2 at: " << sol.searchInsert(nums, 2) << endl; // Expected: 1 (Inserted between 1 and 3)
    cout << "Insert 7 at: " << sol.searchInsert(nums, 7) << endl; // Expected: 4 (Inserted at end)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)`
- **Space Complexity:** `O(1)`
