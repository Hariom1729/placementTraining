# Problem 10: Lemonade Change

## Problem Statement
At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.
Note that you don't have any change in hand at first.
Given an integer array `bills` where `bills[i]` is the bill the `i`th customer pays, return `true` if you can provide every customer with correct change, or `false` otherwise.

## Constraints
- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

---

## Approach: Greedy Simulation

We keep track of the number of `$5` and `$10` bills we have. We don't need to track `$20` bills because they can never be used as change (all items cost `$5`, so the max change needed is `$15`).

For each customer paying with a bill:
- **If `$5`:** We just accept it and increase our `$5` count.
- **If `$10`:** We must give a `$5` back. If we don't have a `$5`, return `false`. Otherwise, decrement `$5` count and increment `$10` count.
- **If `$20`:** We need to give `$15` back.
  - *Greedy Choice:* We should always prefer giving one `$10` and one `$5` instead of three `$5`s. This is because `$5` bills are more versatile (they can make change for both `$10` and `$20`, whereas `$10` bills can only make change for `$20`).
  - If we have at least one `$10` and one `$5`, we use them.
  - Otherwise, if we have at least three `$5`s, we use them.
  - If neither, we can't make change, so return `false`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int ten = 0;
        
        for (int bill : bills) {
            if (bill == 5) {
                five++;
            } else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else { // bill == 20
                // Greedily prefer giving one 10 and one 5
                if (ten > 0 && five > 0) {
                    ten--;
                    five--;
                } 
                // Fallback to three 5s
                else if (five >= 3) {
                    five -= 3;
                } 
                // Cannot make change
                else {
                    return false;
                }
            }
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    vector<int> bills = {5, 5, 5, 10, 20};
    cout << "Can provide change? " << (sol.lemonadeChange(bills) ? "Yes" : "No") << endl; 
    // Expected: Yes
    
    vector<int> bills2 = {5, 5, 10, 10, 20};
    cout << "Can provide change? " << (sol.lemonadeChange(bills2) ? "Yes" : "No") << endl; 
    // Expected: No (For the 20, we don't have a 5 left)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` since we iterate through the bills exactly once.
- **Space Complexity:** `O(1)` as we only use two integer variables.
