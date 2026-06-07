# Problem 9: Gas Station

## Problem Statement
There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is `gas[i]`.
You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station to its next `(i + 1)`th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

## Constraints
- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

---

## Approach: Greedy

This problem relies on two key mathematical observations:
1. **Total Gas vs Total Cost:** If the sum of all `gas` is less than the sum of all `cost`, it's impossible to complete the circle, no matter where we start. So we can return `-1` in this case. If the total gas is `>=` total cost, a solution is guaranteed to exist.
2. **Greedy Start Selection:** If we start at station `A` and run out of gas before reaching station `B` (i.e., at station `B-1`), it means we cannot reach `B` from ANY station between `A` and `B-1`. Why? Because arriving at any intermediate station from `A` means we enter it with `>= 0` gas. If starting fresh from an intermediate station was better, we wouldn't have run out of gas.
Therefore, if we fail to reach `B` from `A`, the next possible starting point is `B`.

1. Keep track of `total_surplus` (sum of `gas[i] - cost[i]`).
2. Keep track of `current_surplus`.
3. Set `start_index = 0`.
4. Iterate through the arrays:
   - Add `gas[i] - cost[i]` to both `total_surplus` and `current_surplus`.
   - If `current_surplus < 0`: This means we can't reach the next station from our current `start_index`. So, we update `start_index = i + 1` and reset `current_surplus = 0`.
5. After the loop, if `total_surplus < 0`, return `-1`. Otherwise, return `start_index`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_surplus = 0;
        int current_surplus = 0;
        int start_index = 0;
        
        for (int i = 0; i < gas.size(); i++) {
            total_surplus += gas[i] - cost[i];
            current_surplus += gas[i] - cost[i];
            
            // If we run out of gas, the stations before cannot be the starting point
            if (current_surplus < 0) {
                start_index = i + 1; // Try the next station
                current_surplus = 0; // Reset current surplus
            }
        }
        
        // If total gas >= total cost, a solution exists
        return (total_surplus >= 0) ? start_index : -1;
    }
};

int main() {
    Solution sol;
    vector<int> gas = {1, 2, 3, 4, 5};
    vector<int> cost = {3, 4, 5, 1, 2};
    
    cout << "Starting Index: " << sol.canCompleteCircuit(gas, cost) << endl; 
    // Expected: 3

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the arrays once.
- **Space Complexity:** `O(1)`. Only constant extra space is used.
