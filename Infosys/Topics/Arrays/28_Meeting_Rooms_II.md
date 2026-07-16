# Meeting Rooms II

## Difficulty
Medium-Hard

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Facebook, Google, Uber

## Topic
Arrays

## Pattern
Intervals / Chronological Ordering / Sweep Line

## Problem Statement
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

## Constraints
- $1 \le intervals.length \le 10^4$
- $0 \le start_i < end_i \le 10^6$

## Input Format
- First line: `N`
- Next `N` lines: Two space-separated integers representing start and end times.

## Output Format
- Return a single integer representing the minimum number of rooms.

## Sample Input
```
3
0 30
5 10
15 20
```

## Sample Output
```
2
```

## Edge Cases
- Meetings that end exactly when another begins (e.g., `[1,2]` and `[2,3]`). These do not overlap and can use the same room.
- Single meeting.

## Approach 1
Brute Force
**Explanation:** For every minute of the day, count how many meetings are active. The maximum count across all minutes is the answer.
**Time Complexity:** $O(N \times \text{Max\_Time})$ (Will TLE if times are large).
**Space Complexity:** $O(\text{Max\_Time})$

## Approach 2
Optimal Approach (Chronological Ordering / Sweep Line)
**Explanation:** 
Separate the start times and end times into two independent arrays, and sort both of them.
The core logic is: whenever a meeting starts, we need a room. Whenever a meeting ends, a room becomes free.
1. Use two pointers, one for `start_times` and one for `end_times`.
2. Compare the current start time with the current end time.
3. If `start_times[s] < end_times[e]`, a meeting is starting before the earliest meeting ends. We must allocate a new room (`rooms++`). Move the `s` pointer forward.
4. If `start_times[s] >= end_times[e]`, a meeting has ended. A room is freed (`rooms--`). Move the `e` pointer forward. (Also note the `>=`, this perfectly handles meetings starting exactly as another ends).
5. Track the maximum number of simultaneous rooms needed at any point.

**Dry Run:**
Intervals: `[[0, 30], [5, 10], [15, 20]]`
- Starts: `[0, 5, 15]`
- Ends: `[10, 20, 30]`
- Pointers: `s=0, e=0`, `rooms=0`, `maxRooms=0`
- `Starts[0] < Ends[0]` (`0 < 10`): Room needed. `rooms=1, max=1`, `s=1`.
- `Starts[1] < Ends[0]` (`5 < 10`): Room needed. `rooms=2, max=2`, `s=2`.
- `Starts[2] >= Ends[0]` (`15 >= 10`): Room freed. `rooms=1`, `e=1`.
- `Starts[2] < Ends[1]` (`15 < 20`): Room needed. `rooms=2, max=2`, `s=3`.
- `s` reaches end. Max rooms needed is 2.

**Time Complexity:** $O(N \log N)$ for sorting the arrays.
**Space Complexity:** $O(N)$ for the independent start and end arrays.

## Java Solution
```java
import java.util.Arrays;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        
        int n = intervals.length;
        int[] starts = new int[n];
        int[] ends = new int[n];
        
        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        
        Arrays.sort(starts);
        Arrays.sort(ends);
        
        int rooms = 0;
        int maxRooms = 0;
        int s = 0, e = 0;
        
        while (s < n) {
            if (starts[s] < ends[e]) {
                rooms++;
                maxRooms = Math.max(maxRooms, rooms);
                s++;
            } else {
                rooms--;
                e++;
            }
        }
        
        return maxRooms;
    }
}
```

## Python Solution
```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        s, e = 0, 0
        rooms = 0
        max_rooms = 0
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1
                
        return max_rooms
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        int n = intervals.size();
        vector<int> starts(n);
        vector<int> ends(n);
        
        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        
        int s = 0, e = 0;
        int rooms = 0;
        int maxRooms = 0;
        
        while (s < n) {
            if (starts[s] < ends[e]) {
                rooms++;
                maxRooms = max(maxRooms, rooms);
                s++;
            } else {
                rooms--;
                e++;
            }
        }
        
        return maxRooms;
    }
};
```

## Common Mistakes
- **Sorting by both start and end together:** Many candidates try to sort the `intervals` array as a whole and then use a Priority Queue (Min-Heap). While a Priority Queue is perfectly valid (storing the end times of active meetings), the chronological sweep-line approach is faster in practice and easier to write without relying on complex heap structures.
- **Off-by-one errors:** Not handling the equality correctly `starts[s] < ends[e]`. If a meeting starts at 10 and another ends at 10, the room is freed simultaneously, so it should hit the `else` block (decreasing the room count before allocating it again).

## Similar Questions
- Merge Intervals
- Meeting Rooms
- Minimum Number of Arrows to Burst Balloons
