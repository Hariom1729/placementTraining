# Merge Intervals

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2021, 2023
Frequency: High

---

## Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## Input Format
- The first line contains an integer `N`, the number of intervals.
- The next `N` lines each contain two space-separated integers, representing the start and end of an interval.

---

## Output Format
- Return a list of merged intervals.

---

## Constraints
- $1 \le intervals.length \le 10^4$
- $intervals[i].length == 2$
- $0 \le start_i \le end_i \le 10^4$

---

## Examples

### Example 1
**Input:** 
```
4
1 3
2 6
8 10
15 18
```
**Output:** 
```
[[1, 6], [8, 10], [15, 18]]
```
**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

### Example 2
**Input:** 
```
2
1 4
4 5
```
**Output:** 
```
[[1, 5]]
```
**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.

---

## Brute Force Approach
1. Sort the intervals based on their start times.
2. Iterate through each interval. For each interval, check if it overlaps with any other interval that has not been merged yet. If it does, update the start and end bounds to encompass both.
3. This requires keeping track of merged intervals and constantly rescanning the list.

**Time Complexity:** $O(N^2)$ due to nested scanning.
**Space Complexity:** $O(N)$ for storing merged intervals.

---

## Better Approach
We can optimize by sorting and using a more structured loop, checking the current interval against all subsequent overlapping ones in a single inner loop.

**Complexity:** 
- **Time Complexity:** $O(N \log N)$ for sorting + $O(N)$ for merging.
- **Space Complexity:** $O(N)$ to store the answer.

---

## Optimal Approach
**Detailed explanation:**
1. Sort the intervals based on the starting value.
2. Create an empty result list `merged`.
3. Push the first interval into `merged`.
4. Iterate through the remaining intervals. 
   - If the current interval overlaps with the last interval in `merged` (i.e., `current[start] <= merged.back()[end]`), merge them by updating the end of the last interval to `max(merged.back()[end], current[end])`.
   - If it does not overlap, simply push the current interval to `merged`.

**Dry Run:**
`intervals = [[1,3], [2,6], [8,10], [15,18]]`
- Sorted: (Already sorted).
- `merged` = `[[1,3]]`
- Next `[2,6]`: $2 \le 3$. Overlaps. Update end to $\max(3, 6) = 6$. `merged = [[1,6]]`.
- Next `[8,10]`: $8 > 6$. No overlap. Push. `merged = [[1,6], [8,10]]`.
- Next `[15,18]`: $15 > 10$. No overlap. Push. `merged = [[1,6], [8,10], [15,18]]`.

**Complexity:**
- **Time Complexity:** $O(N \log N)$ due to sorting. The linear scan takes $O(N)$. Overall $O(N \log N)$.
- **Space Complexity:** $O(N)$ for the returned list, $O(1)$ auxiliary space.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) return {};
    
    // 1. Sort based on starting times
    sort(intervals.begin(), intervals.end());
    
    vector<vector<int>> merged;
    merged.push_back(intervals[0]);
    
    // 2. Iterate and merge
    for (int i = 1; i < intervals.size(); i++) {
        // If overlap, update the end of the last interval in merged
        if (intervals[i][0] <= merged.back()[1]) {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        } 
        // If no overlap, add the current interval
        else {
            merged.push_back(intervals[i]);
        }
    }
    
    return merged;
}

int main() {
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> res = mergeIntervals(intervals);
    
    for (auto interval : res) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }
    // Output: [1, 6] [8, 10] [15, 18]
    return 0;
}
```

---

## Common Mistakes
- **Not Sorting First:** The logic absolutely requires the intervals to be sorted by their start times first. Without sorting, `[15,18]` could appear before `[1,3]`.
- **Sorting by End Time:** Sorting by end time works for *Greedy Activity Selection*, but not for standard interval merging.

---

## Similar Questions
- Insert Interval
- Non-overlapping Intervals
- Meeting Rooms I & II

---

## Interview Tips
- Point out that C++ `sort` automatically sorts a `vector<vector<int>>` based on the first element of each inner vector, which is exactly what we need.

---

## Variations Asked
- Find the total length of covered segments.
- Find if all intervals can be attended by a single person (Meeting Rooms).

---

## Pattern Recognition
**Identify this when:** The problem involves line segments, time intervals, meetings, or ranges. Sorting by start time and maintaining a running "current interval" is the core pattern for all interval problems.
