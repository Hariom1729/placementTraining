# Problem 7: Job Sequencing Problem

## Problem Statement
Given a set of `N` jobs where each job `i` has a deadline and profit associated with it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the number of jobs done and the maximum profit.

## Constraints
- `1 <= N <= 10^5`
- `1 <= Deadline <= 100`
- `1 <= Profit <= 500`

---

## Approach: Greedy (Sort by Profit)

To maximize profit, we should prioritize jobs with the highest profit.
However, to ensure we can accommodate as many jobs as possible, we should perform a high-profit job **as late as possible** (i.e., on its deadline day), leaving earlier time slots empty for other jobs that might have earlier deadlines.

1. Sort the jobs in descending order of their profit.
2. Find the maximum deadline among all jobs to determine the size of our schedule array. Let's call it `maxDeadline`.
3. Create a `schedule` array of size `maxDeadline + 1` initialized to `-1` (indicating empty slots).
4. Iterate through the sorted jobs:
   - For a job with deadline `d`, check the `schedule` array starting from index `d` down to `1`.
   - If an empty slot is found (`schedule[slot] == -1`), assign the job to this slot, add its profit to the total profit, increment job count, and break.
5. Return the total count and total profit.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Job {
    int id;       // Job Id
    int dead;     // Deadline of job
    int profit;   // Profit if job is over before or on deadline
};

class Solution {
private:
    static bool comp(Job a, Job b) {
        return a.profit > b.profit; // Sort descending by profit
    }

public:
    // Function to find the maximum profit and the number of jobs done.
    vector<int> JobScheduling(Job arr[], int n) {
        sort(arr, arr + n, comp);
        
        int maxDeadline = 0;
        for (int i = 0; i < n; i++) {
            maxDeadline = max(maxDeadline, arr[i].dead);
        }
        
        // Array to keep track of free time slots
        vector<int> schedule(maxDeadline + 1, -1);
        
        int countJobs = 0;
        int jobProfit = 0;
        
        for (int i = 0; i < n; i++) {
            // Find a free slot for this job (starting from its deadline down to 1)
            for (int j = arr[i].dead; j > 0; j--) {
                if (schedule[j] == -1) {
                    schedule[j] = arr[i].id; // Assign job to this slot
                    countJobs++;
                    jobProfit += arr[i].profit;
                    break;
                }
            }
        }
        
        return {countJobs, jobProfit};
    }
};

int main() {
    Solution sol;
    Job arr[] = {{1, 4, 20}, {2, 1, 10}, {3, 1, 40}, {4, 1, 30}};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    vector<int> res = sol.JobScheduling(arr, n);
    cout << "Jobs Done: " << res[0] << ", Total Profit: " << res[1] << endl; 
    // Expected: Jobs Done: 2, Total Profit: 60 (Job 3 on day 1, Job 1 on day 4)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N + N \times M)` where `N` is the number of jobs and `M` is the maximum deadline. In the worst case, searching for a slot takes `O(M)`. Since `M` is usually small, it's efficient. (Can be optimized to `O(N \log N)` using Disjoint Set Union).
- **Space Complexity:** `O(M)` for the schedule array.
