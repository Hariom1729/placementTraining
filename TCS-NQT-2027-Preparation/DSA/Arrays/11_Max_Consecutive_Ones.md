# Problem 11: Maximum Consecutive Ones

## Problem Statement
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

## Input Format
- An array of integers `nums` where `nums[i]` is either `0` or `1`.

## Output Format
- An integer representing the max consecutive ones.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach

1. Maintain two variables: `max_cnt` (to track the maximum consecutive ones found so far) and `cnt` (to track the current sequence of ones).
2. Iterate through the array.
3. If the current element is `1`:
   - Increment `cnt`.
   - Update `max_cnt` with `max(max_cnt, cnt)`.
4. If the current element is `0`:
   - Reset `cnt` to `0`.
5. Return `max_cnt`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_cnt = 0;
        int cnt = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                cnt++;
                max_cnt = max(max_cnt, cnt);
            } else {
                cnt = 0;
            }
        }
        
        return max_cnt;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 1, 0, 1, 1, 1};
    cout << "Max Consecutive Ones: " << sol.findMaxConsecutiveOnes(nums) << endl; // Expected: 3
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We iterate through the array once.
- **Space Complexity:** `O(1)`. We use only two integer variables.
