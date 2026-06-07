# Problem 5: N Meetings in One Room

## Problem Statement
There is one meeting room in a firm. There are `N` meetings in the form of `(start[i], end[i])` where `start[i]` is start time of meeting `i` and `end[i]` is finish time of meeting `i`.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?
Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

## Constraints
- `1 <= N <= 10^5`
- `0 <= start[i] < end[i] <= 10^5`

---

## Approach: Greedy (Sort by End Time)

To maximize the number of meetings, we should always pick the meeting that finishes earliest, leaving as much time as possible for subsequent meetings.

1. Create a custom `struct` to hold `start`, `end`, and `pos` (meeting ID) for each meeting.
2. Store all meetings in a vector.
3. Sort the vector based on the **end time** in ascending order. (If end times are equal, you can optionally sort by position, but just sorting by end time is sufficient to maximize count).
4. Maintain a `limit` variable to track the end time of the last selected meeting. Initially, `limit = -1`.
5. Iterate through the sorted meetings:
   - If the `start` time of the current meeting is strictly greater than `limit`, we can select this meeting.
   - Increment `count` and update `limit` to the `end` time of this current meeting.
6. Return `count`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Meeting {
    int start;
    int end;
    int pos;
};

class Solution {
private:
    static bool comp(Meeting m1, Meeting m2) {
        if (m1.end < m2.end) return true;
        else if (m1.end > m2.end) return false;
        else if (m1.pos < m2.pos) return true;
        return false;
    }

public:
    int maxMeetings(int start[], int end[], int n) {
        vector<Meeting> meet(n);
        for (int i = 0; i < n; i++) {
            meet[i].start = start[i];
            meet[i].end = end[i];
            meet[i].pos = i + 1;
        }
        
        // Sort by end time
        sort(meet.begin(), meet.end(), comp);
        
        int count = 1;
        int limit = meet[0].end;
        
        for (int i = 1; i < n; i++) {
            if (meet[i].start > limit) {
                count++;
                limit = meet[i].end;
            }
        }
        
        return count;
    }
};

int main() {
    Solution sol;
    int start[] = {1, 3, 0, 5, 8, 5};
    int end[] =  {2, 4, 6, 7, 9, 9};
    int n = sizeof(start) / sizeof(start[0]);
    
    cout << "Maximum Meetings: " << sol.maxMeetings(start, end, n) << endl; 
    // Expected: 4 (Meetings: (1,2), (3,4), (5,7), (8,9))

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N)` due to the sorting step.
- **Space Complexity:** `O(N)` to store the array of structs.
