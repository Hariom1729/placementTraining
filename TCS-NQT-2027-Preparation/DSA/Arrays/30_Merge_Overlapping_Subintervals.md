# Problem 30: Merge Overlapping Subintervals

## Problem Statement
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Input Format
- A 2D array `intervals`.

## Output Format
- A 2D array of merged intervals.

## Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

---

## Approach

1. **Sort the intervals:** We must sort the intervals based on their starting times. This guarantees that any overlapping intervals will be adjacent to each other.
2. Initialize an empty result vector.
3. Maintain a `newInterval` representing the current interval we are trying to merge. Set it initially to `intervals[0]`.
4. Iterate through the `intervals`. For every `interval`:
   - If it overlaps with `newInterval` (i.e., `interval[0] <= newInterval[1]`):
     - Merge them by updating the end time: `newInterval[1] = max(newInterval[1], interval[1])`.
   - If it doesn't overlap:
     - The `newInterval` cannot be expanded further. Push it to the `result` vector.
     - Set `newInterval = interval` to start building a new one.
5. After the loop, don't forget to push the very last `newInterval` into the `result`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return intervals;
        }

        // Sort based on the starting times
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;
        vector<int> newInterval = intervals[0];

        for (auto interval : intervals) {
            // Overlapping condition
            if (interval[0] <= newInterval[1]) {
                newInterval[1] = max(newInterval[1], interval[1]);
            } else {
                // Not overlapping, push the completed interval
                result.push_back(newInterval);
                newInterval = interval;
            }
        }
        
        // Push the last constructed interval
        result.push_back(newInterval);

        return result;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> res = sol.merge(intervals);
    
    for (auto& interval : res) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }
    // Expected output: [1, 6] [8, 10] [15, 18]
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N log N)`. Sorting the array takes `O(N log N)` time. The linear traversal takes `O(N)`. Overall time is bounded by the sort.
- **Space Complexity:** `O(N)` to store the resulting array. Sorting might take `O(log N)` auxiliary space internally.
