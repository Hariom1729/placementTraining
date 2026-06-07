# Problem 6: Minimum Platforms

## Problem Statement
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

## Constraints
- `1 <= n <= 50000`
- `0000 <= A[i] <= D[i] <= 2359`

---

## Approach: Greedy (Two Pointers / Sorting)

We don't need to match specific arrivals to specific departures. We just need to know how many trains are currently at the station at any given time.

1. Sort the `arrival` array.
2. Sort the `departure` array independently.
3. Use two pointers: `i` for traversing the `arrival` array (starting at `1`, since train 0 arrives at `0`) and `j` for traversing the `departure` array (starting at `0`).
4. Keep track of `platforms_needed = 1` (for the first train) and `max_platforms = 1`.
5. While `i < n` and `j < n`:
   - If `arrival[i] <= departure[j]`: A train arrives before or exactly when the other leaves. We need an extra platform. Increment `platforms_needed` and move `i++`.
   - If `arrival[i] > departure[j]`: A train leaves before the next one arrives. We free up a platform. Decrement `platforms_needed` and move `j++`.
   - Update `max_platforms = max(max_platforms, platforms_needed)`.
6. Return `max_platforms`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to find the minimum number of platforms required at the
    // railway station such that no train waits.
    int findPlatform(int arr[], int dep[], int n) {
        // Sort arrival and departure arrays
        sort(arr, arr + n);
        sort(dep, dep + n);
        
        int platforms_needed = 1;
        int max_platforms = 1;
        
        int i = 1; // Start from second train's arrival
        int j = 0; // Start from first train's departure
        
        while (i < n && j < n) {
            // If arrival is earlier than or equal to departure, we need a platform
            if (arr[i] <= dep[j]) {
                platforms_needed++;
                i++;
            } 
            // If departure is earlier, a platform becomes free
            else {
                platforms_needed--;
                j++;
            }
            
            // Keep track of the maximum platforms needed so far
            max_platforms = max(max_platforms, platforms_needed);
        }
        
        return max_platforms;
    }
};

int main() {
    Solution sol;
    int arr[] = {900, 940, 950, 1100, 1500, 1800};
    int dep[] = {910, 1200, 1120, 1130, 1900, 2000};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Minimum Platforms: " << sol.findPlatform(arr, dep, n) << endl; 
    // Expected: 3

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N)` due to the sorting of arrival and departure arrays. The two-pointer traversal takes `O(N)`.
- **Space Complexity:** `O(1)` if we sort the arrays in-place.
