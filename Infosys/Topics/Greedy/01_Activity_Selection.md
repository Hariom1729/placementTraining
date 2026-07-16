# Activity Selection / N Meetings in One Room

## Difficulty
Medium

## Asked In
Infosys DSE
Infosys SP
Frequency: High

---

## Problem Statement
There is one meeting room. You are given `N` meetings with their start times and end times. Find the maximum number of meetings that can be accommodated in the room if only one meeting can be held at a time.

---

## Optimal Approach (Greedy)
**Detailed explanation:**
Sort the meetings according to their finishing time.
Always select the first meeting (since it finishes the earliest, leaving maximum time for remaining meetings).
For subsequent meetings, if the start time is strictly greater than the end time of the previously selected meeting, select it.

**Complexity:**
- **Time Complexity:** $O(N \log N)$ for sorting.
- **Space Complexity:** $O(N)$ to store pairs.

---

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

struct Meeting {
    int start;
    int end;
};

// Custom comparator to sort based on end time
bool compare(Meeting a, Meeting b) {
    return a.end < b.end;
}

int maxMeetings(int start[], int end[], int n) {
    vector<Meeting> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i].start = start[i];
        arr[i].end = end[i];
    }
    
    sort(arr.begin(), arr.end(), compare);
    
    int count = 1; // Always pick the first meeting
    int free_time = arr[0].end;
    
    for (int i = 1; i < n; i++) {
        if (arr[i].start > free_time) {
            count++;
            free_time = arr[i].end; // Update free time
        }
    }
    
    return count;
}
```
