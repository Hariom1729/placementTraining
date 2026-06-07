# Problem 8: Dota2 Senate

## Problem Statement
In the world of Dota2, there are two parties: the Radiant and the Dire.
The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
1. **Ban one senator's right:** A senator can make another senator lose all his rights in this and all the following rounds.
2. **Announce the victory:** If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change.

Given a string `senate` representing each senator's party belonging (R for Radiant, D for Dire), determine which party will announce the victory. The output should be `"Radiant"` or `"Dire"`.

## Input Format
- A string `senate`.

## Output Format
- A string representing the winning party.

## Constraints
- `n == senate.length`
- `1 <= n <= 10^4`
- `senate[i]` is either `'R'` or `'D'`.

---

## Approach: Two Queues

A senator should optimally ban the *next available* senator of the opposing party to prevent them from voting.
1. Use two queues: `rad` for Radiant senators' indices and `dir` for Dire senators' indices.
2. Populate the queues with the initial indices of the senators.
3. While both queues are not empty:
   - Compare the front indices: `r_idx = rad.front()` and `d_idx = dir.front()`.
   - The senator with the smaller index gets to vote first. They will ban the other senator.
   - The winning senator gets to vote again in the *next round*. So we push `winner_idx + n` to the back of their respective queue.
   - Pop both elements from the front.
4. The game ends when one of the queues is empty. The non-empty queue indicates the winning party.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.length();
        queue<int> rad, dir;
        
        // Add indices to the respective queues
        for (int i = 0; i < n; i++) {
            if (senate[i] == 'R') {
                rad.push(i);
            } else {
                dir.push(i);
            }
        }
        
        // Simulate rounds
        while (!rad.empty() && !dir.empty()) {
            int r_idx = rad.front();
            int d_idx = dir.front();
            
            rad.pop();
            dir.pop();
            
            // The one who appears earlier gets to ban the other
            // and moves to the next round (+n to index)
            if (r_idx < d_idx) {
                rad.push(r_idx + n);
            } else {
                dir.push(d_idx + n);
            }
        }
        
        return rad.empty() ? "Dire" : "Radiant";
    }
};

int main() {
    Solution sol;
    cout << "Winner: " << sol.predictPartyVictory("RD") << endl; // Expected: Radiant (R bans D)
    cout << "Winner: " << sol.predictPartyVictory("RDD") << endl; // Expected: Dire (R bans D1, D2 bans R, D2 wins)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each senator is processed at most a few times before being eliminated.
- **Space Complexity:** `O(N)` for the two queues storing the indices.
