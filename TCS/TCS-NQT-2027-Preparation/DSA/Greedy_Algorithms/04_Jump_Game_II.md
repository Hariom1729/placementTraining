# Problem 4: Jump Game II

## Problem Statement
You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.
Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:
- `0 <= j <= nums[i]`
- `i + j < n`
Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

---

## Approach: Greedy (Implicit BFS)

Unlike Jump Game I, we need the *minimum* number of jumps. This is equivalent to finding the shortest path in an unweighted graph, which suggests BFS. However, building a graph and running BFS is too slow.
We can optimize it using a Greedy approach that essentially mimics BFS.

We maintain a "window" of indices that we can reach with the current number of jumps.
1. `jumps = 0`, `current_end = 0`, `farthest = 0`.
2. Iterate `i` from `0` to `n - 2` (we don't need to jump from the last index).
3. At each index, update the `farthest` we can reach: `farthest = max(farthest, i + nums[i])`.
4. If we reach the `current_end` of our window (`i == current_end`), we MUST make a jump to continue. So, we increment `jumps` and update `current_end` to `farthest`.
5. Return `jumps`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        
        int jumps = 0;
        int current_end = 0;
        int farthest = 0;
        
        for (int i = 0; i < n - 1; i++) {
            // Update the farthest index we can reach from current position
            farthest = max(farthest, i + nums[i]);
            
            // If we have reached the end of the current jump range,
            // we MUST jump.
            if (i == current_end) {
                jumps++;
                current_end = farthest;
                
                // Optimization: if we can already reach the end, stop
                if (current_end >= n - 1) {
                    break;
                }
            }
        }
        
        return jumps;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 3, 1, 1, 4};
    
    cout << "Minimum Jumps: " << sol.jump(nums) << endl; 
    // Expected: 2 (Jump 1 step from index 0 to 1, then 3 steps to the last index)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the size of the array. We iterate through the array once.
- **Space Complexity:** `O(1)` since we only use a few integer variables.
