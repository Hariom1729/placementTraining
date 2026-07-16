# Insert Interval

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Google, Amazon, Microsoft

## Topic
Arrays

## Pattern
Intervals

## Problem Statement
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

## Constraints
- $0 \le intervals.length \le 10^4$
- $intervals[i].length == 2$
- $0 \le start_i \le end_i \le 10^5$
- `intervals` is sorted by `start_i` in ascending order.
- $newInterval.length == 2$
- $0 \le start \le end \le 10^5$

## Input Format
- First line: `N`
- Next `N` lines: Two integers representing `start_i` and `end_i`.
- Last line: Two integers representing `newInterval`.

## Output Format
- Return a 2D array of the merged intervals.

## Sample Input
```
2
1 3
6 9
2 5
```

## Sample Output
```
[[1,5], [6,9]]
```

## Edge Cases
- `intervals` is empty. Just return `[newInterval]`.
- `newInterval` comes before all other intervals.
- `newInterval` comes after all other intervals.
- `newInterval` engulfs all other intervals entirely.

## Approach 1
Brute Force
**Explanation:** Append `newInterval` to the end of `intervals`. Then sort the entire array based on start times, and apply the standard Merge Intervals algorithm.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(N)$ for sorting/output.

## Approach 2
Optimal Approach (Linear Scan)
**Explanation:** 
Since the array is already sorted, we can avoid the $O(N \log N)$ sort and do it in one pass $O(N)$.
We can break the problem into three phases:
1. **Left non-overlapping:** Add all intervals that end *before* `newInterval` starts (`interval[1] < newInterval[0]`).
2. **Merging overlapping:** While intervals overlap with `newInterval` (`interval[0] <= newInterval[1]`), merge them by updating `newInterval[0] = min(start, interval[0])` and `newInterval[1] = max(end, interval[1])`. Then add this merged `newInterval`.
3. **Right non-overlapping:** Add the rest of the intervals.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the result array.

## Java Solution
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int n = intervals.length;
        
        // 1. Add all intervals before newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i]);
            i++;
        }
        
        // 2. Merge overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);
        
        // 3. Add remaining intervals
        while (i < n) {
            result.add(intervals[i]);
            i++;
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
```

## Python Solution
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0;
        int n = intervals.size();
        
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);
        
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }
        
        return result;
    }
};
```

## Common Mistakes
- **Trying to modify the array in-place:** Since arrays/vectors require shifting elements when you merge/delete intervals, doing it in-place usually degrades to $O(N^2)$ due to array shifting overhead. It's standard and expected to return a new `result` array.

## Similar Questions
- Merge Intervals
- Non-overlapping Intervals
