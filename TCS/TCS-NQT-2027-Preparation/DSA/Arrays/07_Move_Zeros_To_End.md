# Problem 7: Move all Zeros to the End

## Problem Statement
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

## Input Format
- An array of integers `nums`.

## Output Format
- The array `nums` modified in-place.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Approach

This is a classic problem for the **Two Pointers** pattern.
1. Use a pointer `j` to keep track of the next position where a non-zero element should be placed. Initialize `j = 0`.
2. Iterate through the array with pointer `i`.
3. If `nums[i]` is not equal to `0`:
   - Swap `nums[i]` and `nums[j]`.
   - Increment `j`.
4. If `nums[i]` is `0`, just continue to the next element (only `i` increments).

This approach naturally shifts all non-zero elements to the front, pushing the zeros to the back.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0; // Pointer for non-zero elements
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                // Swap non-zero element to the j-th position
                swap(nums[i], nums[j]);
                j++;
            }
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {0, 1, 0, 3, 12};
    sol.moveZeroes(nums);
    
    cout << "Array after moving zeros: ";
    for (int x : nums) {
        cout << x << " "; // Expected: 1 3 12 0 0
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We perform a single pass through the array.
- **Space Complexity:** `O(1)`. The operations are done in-place.
