# Problem 10: Task Scheduler

## Problem Statement
You are given an array of CPU `tasks`, each represented by letters A to Z, and a cooling time `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: **identical** tasks must be separated by at least `n` intervals due to cooling time.
Return the minimum number of intervals required to complete all tasks.

## Input Format
- An array of characters `tasks`.
- An integer `n`.

## Output Format
- An integer representing the minimum number of intervals.

## Constraints
- `1 <= task.length <= 10^4`
- `tasks[i]` is upper-case English letter.
- `0 <= n <= 100`

---

## Approach: Math / Frequency Counting

This problem can be simulated using a Priority Queue and a regular Queue, but the mathematical frequency counting approach is much faster and simpler `O(N)`.

1. Count the frequency of each task.
2. Find the maximum frequency, let's call it `max_freq`.
3. The most frequent task creates "chunks" or "blocks" of empty slots that must be filled.
   - For example, if task 'A' appears 3 times and `n = 2`: `A _ _ A _ _ A`.
   - The number of gaps is `max_freq - 1` (which is 2 gaps).
   - The length of each gap is `n`.
   - Total empty slots = `(max_freq - 1) * n`.
4. However, other tasks might also have the same `max_freq`. These tasks will sit at the end of the blocks. We count how many tasks have the same `max_freq` (let's call it `max_count`).
5. The formula for the required length is:
   `length = (max_freq - 1) * (n + 1) + max_count`.
6. What if `n` is very small or zero, and the calculated `length` is actually *less* than the total number of tasks? In that case, we don't need any idle time, so the answer is just the total number of tasks.
   `Answer = max((int)tasks.size(), length)`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);
        int max_freq = 0;
        
        // 1. Calculate frequencies and find the max frequency
        for (char task : tasks) {
            freq[task - 'A']++;
            max_freq = max(max_freq, freq[task - 'A']);
        }
        
        // 2. Count how many tasks have that max frequency
        int max_count = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == max_freq) {
                max_count++;
            }
        }
        
        // 3. Apply formula
        int required_intervals = (max_freq - 1) * (n + 1) + max_count;
        
        // 4. Return the maximum of required intervals and total tasks
        return max((int)tasks.size(), required_intervals);
    }
};

int main() {
    Solution sol;
    vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 2;
    
    cout << "Minimum Intervals: " << sol.leastInterval(tasks, n) << endl; 
    // Expected: 8 (A -> B -> idle -> A -> B -> idle -> A -> B)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of tasks. We iterate through the tasks array once.
- **Space Complexity:** `O(1)` as the frequency array is always size 26.
