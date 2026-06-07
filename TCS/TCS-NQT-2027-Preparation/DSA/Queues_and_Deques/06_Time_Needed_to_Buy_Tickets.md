# Problem 6: Time Needed to Buy Tickets

## Problem Statement
There are `n` people in a line queuing to buy tickets, where the `0`th person is at the front of the line and the `(n - 1)`th person is at the back of the line.
You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the `i`th person would like to buy is `tickets[i]`.
Each person takes exactly `1` second to buy a ticket. A person can only buy `1` ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position `k` (0-indexed) to finish buying tickets.

## Input Format
- An array of integers `tickets`.
- An integer `k`.

## Output Format
- An integer representing the total time taken.

## Constraints
- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`

---

## Approach: One Pass (Without actual Queue Simulation)

While we *could* simulate the queue, it's unnecessary and slow. We can calculate exactly how many tickets each person buys before person `k` finishes.
1. Person `k` needs to buy `tickets[k]` tickets. So they will go to the front of the line `tickets[k]` times.
2. For any person `i` **in front** of `k` (where `i <= k`):
   - They will have the opportunity to buy tickets up to `tickets[k]` times (since they are ahead of `k`, they buy their ticket *before* `k` finishes their round).
   - The actual number of tickets they buy is `min(tickets[i], tickets[k])`.
3. For any person `i` **behind** `k` (where `i > k`):
   - By the time `k` finishes their `tickets[k]`-th ticket, the people behind `k` haven't had their turn for that final round yet.
   - So, they get to buy at most `tickets[k] - 1` tickets.
   - The actual number of tickets they buy is `min(tickets[i], tickets[k] - 1)`.
4. Sum all these tickets up.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int time = 0;
        
        for (int i = 0; i < tickets.size(); i++) {
            // If the person is at or in front of k
            if (i <= k) {
                time += min(tickets[i], tickets[k]);
            } 
            // If the person is behind k
            else {
                time += min(tickets[i], tickets[k] - 1);
            }
        }
        
        return time;
    }
};

int main() {
    Solution sol;
    vector<int> tickets = {2, 3, 2};
    int k = 2;
    
    cout << "Time required: " << sol.timeRequiredToBuy(tickets, k) << endl; 
    // Expected: 6 (1st pass: 1,2,1 -> 2nd pass: 0,1,0 -> done)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of people. We iterate through the array once.
- **Space Complexity:** `O(1)` as we only use a few integer variables.
