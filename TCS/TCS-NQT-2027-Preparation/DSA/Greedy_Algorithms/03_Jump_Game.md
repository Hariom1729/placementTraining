# Problem 3: Jump Game

## Problem Statement
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return `true` if you can reach the last index, or `false` otherwise.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

---

## Approach: Greedy (Maximum Reach)

We can maintain the maximum reachable index (`maxReach`) as we iterate through the array.
If we ever reach an index `i` that is GREATER than our `maxReach`, it means we are stuck and cannot reach this point, so we return `false`.

1. Initialize `maxReach = 0`.
2. Iterate `i` from `0` to `n-1`:
   - If `i > maxReach`: return `false` (we can't even reach index `i`).
   - Update `maxReach = max(maxReach, i + nums[i])`.
   - If `maxReach >= n - 1`, we can reach the end, so return `true`.
3. If loop finishes, return `true`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxReach = 0;
        
        for (int i = 0; i < n; i++) {
            // If the current index is beyond the maximum reachable index
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable index
            maxReach = max(maxReach, i + nums[i]);
            
            // Early exit if we can already reach the end
            if (maxReach >= n - 1) {
                return true;
            }
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {2, 3, 1, 1, 4};
    cout << "Can Jump? " << (sol.canJump(nums1) ? "Yes" : "No") << endl; 
    // Expected: Yes (Jump 1 step from idx 0 to 1, then 3 steps to the last index)
    
    vector<int> nums2 = {3, 2, 1, 0, 4};
    cout << "Can Jump? " << (sol.canJump(nums2) ? "Yes" : "No") << endl; 
    // Expected: No (You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` since we iterate through the array exactly once.
- **Space Complexity:** `O(1)` as we only use a single integer variable.
