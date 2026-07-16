# Non-overlapping Intervals

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Facebook, Amazon, Google

## Topic
Arrays

## Pattern
Intervals / Greedy

## Problem Statement
Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## Constraints
- $1 \le intervals.length \le 10^5$
- $intervals[i].length == 2$
- $-5 \times 10^4 \le start_i < end_i \le 5 \times 10^4$

## Input Format
- First line: `N`
- Next `N` lines: Two space-separated integers representing an interval.

## Output Format
- Return a single integer representing the number of removed intervals.

## Sample Input
```
4
1 2
2 3
3 4
1 3
```

## Sample Output
```
1
```

## Edge Cases
- All intervals are mutually exclusive (remove 0).
- All intervals heavily overlap each other.

## Approach 1
Brute Force
**Explanation:** Find all possible combinations of non-overlapping intervals (powerset).
**Time Complexity:** $O(2^N)$
**Space Complexity:** $O(N)$

## Approach 2
Optimal Approach (Greedy Scheduling)
**Explanation:** 
This problem is mathematically identical to the classic **Activity Selection Problem**.
To remove the minimum number of intervals, we need to *keep* the maximum number of non-overlapping intervals.
To fit as many intervals as possible, we should always pick the interval that **ends the earliest**.
1. Sort the intervals based on their **END TIMES** (not start times).
2. Initialize `count = 0` (for removed intervals) and `last_end = INT_MIN`.
3. Iterate through the sorted intervals.
4. If `interval[0] >= last_end`, it means it does NOT overlap with the previously selected interval. We select it by updating `last_end = interval[1]`.
5. If it does overlap (`interval[0] < last_end`), we must remove it to avoid conflict. Increment `count++`.

**Dry Run:**
`[[1,2], [2,3], [3,4], [1,3]]`
- Sorted by end times: `[[1,2], [1,3], [2,3], [3,4]]`
- `last_end = -inf`, `count = 0`
- `[1,2]`: `1 >= -inf`. Select it. `last_end = 2`.
- `[1,3]`: `1 < 2` (Overlap). Remove it. `count = 1`.
- `[2,3]`: `2 >= 2`. Select it. `last_end = 3`.
- `[3,4]`: `3 >= 3`. Select it. `last_end = 4`.
Return `count = 1`.

**Time Complexity:** $O(N \log N)$ due to sorting.
**Space Complexity:** $O(1)$ if sorting is done in-place, or $O(\log N)$ auxiliary space for sort.

## Java Solution
```java
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        // Sort by end time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        
        int count = 0;
        int lastEnd = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < lastEnd) {
                count++; // Overlaps, we must remove it
            } else {
                lastEnd = intervals[i][1]; // No overlap, update end
            }
        }
        
        return count;
    }
}
```

## Python Solution
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                count += 1
            else:
                last_end = intervals[i][1]
                
        return count
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    static bool comp(const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1]; // Sort by end time
    }
    
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        sort(intervals.begin(), intervals.end(), comp);
        
        int count = 0;
        int lastEnd = intervals[0][1];
        
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < lastEnd) {
                count++;
            } else {
                lastEnd = intervals[i][1];
            }
        }
        
        return count;
    }
};
```

## Common Mistakes
- **Sorting by Start Time:** If you sort by start time, an interval that starts early but lasts extremely long (e.g., `[1, 100]`) will block everything else that comes after it (`[2, 3], [4, 5]`). Sorting by end time guarantees that the interval finishes as quickly as possible, leaving room for the maximum number of future intervals.

## Similar Questions
- Merge Intervals
- Meeting Rooms II
