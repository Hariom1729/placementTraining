# Problem 10: Aggressive Cows

## Problem Statement
You are given an array `stalls` of size `N`, where `stalls[i]` denotes the coordinate of a stall. You are also given an integer `k` which denotes the number of aggressive cows.
You are tasked with assigning stalls to all `k` cows such that the minimum distance between any two of them is the maximum possible.
Return the maximum possible minimum distance.

## Input Format
- An array of integers `stalls`.
- An integer `k`.

## Output Format
- An integer representing the maximum possible minimum distance.

## Constraints
- `2 <= N <= 10^5`
- `0 <= stalls[i] <= 10^9`
- `2 <= k <= N`

---

## Approach: Binary Search on Answer

This is a hallmark **TCS Prime** problem. We need to find the *maximum* possible *minimum* distance.

1. **Sort the array:** We need to place cows sequentially to maximize distance.
2. **Define the Search Space:** The minimum possible distance is `1`. The maximum possible distance is `stalls[N-1] - stalls[0]`. We will perform binary search on this distance range `[low, high]`.
3. **Helper Function `canPlaceCows(dist)`:** For a given distance `dist`, can we place all `k` cows?
   - Place the first cow at `stalls[0]`.
   - Iterate through `stalls`. If `stalls[i] - last_cow_position >= dist`, place the next cow and update `last_cow_position`.
   - If we successfully place `k` cows, return `true`. Otherwise, `false`.
4. **Binary Search Logic:**
   - Find `mid` distance.
   - If `canPlaceCows(mid)` is true, it means `mid` is a valid answer. However, we want the *maximum* possible distance, so we save `ans = mid` and search the right half (`low = mid + 1`) for a larger valid distance.
   - If `canPlaceCows(mid)` is false, `mid` is too large. Search the left half (`high = mid - 1`).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    bool canPlaceCows(vector<int>& stalls, int k, int dist) {
        int cowsPlaced = 1;
        int lastPos = stalls[0];
        
        for (int i = 1; i < stalls.size(); i++) {
            if (stalls[i] - lastPos >= dist) {
                cowsPlaced++;
                lastPos = stalls[i];
            }
            if (cowsPlaced == k) return true;
        }
        return false;
    }

public:
    int aggressiveCows(vector<int>& stalls, int k) {
        sort(stalls.begin(), stalls.end());
        int n = stalls.size();
        
        int low = 1;
        int high = stalls[n - 1] - stalls[0];
        int ans = 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canPlaceCows(stalls, k, mid)) {
                ans = mid; // Potential answer
                low = mid + 1; // Try to find a larger minimum distance
            } else {
                high = mid - 1; // The distance is too large
            }
        }
        
        return ans; // 'high' also stores the correct answer at the end
    }
};

int main() {
    Solution sol;
    vector<int> stalls = {0, 3, 4, 7, 10, 9};
    int k = 4;
    // Sorted: 0, 3, 4, 7, 9, 10
    cout << "Max possible min distance: " << sol.aggressiveCows(stalls, k) << endl; // Expected: 3
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N log N) + O(N * log(MAX_DIST))`. Sorting takes `O(N log N)`. The binary search runs `log(MAX_DIST)` times, and the helper function takes `O(N)` time.
- **Space Complexity:** `O(1)` auxiliary space.
