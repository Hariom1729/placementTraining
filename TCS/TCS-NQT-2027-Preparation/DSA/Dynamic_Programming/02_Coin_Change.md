# Problem 2: Coin Change

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
You may assume that you have an infinite number of each kind of coin.

## Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

---

## Approach: 1D DP (Unbounded Knapsack)

This is a classic DP problem. We want to find the minimum coins for every amount from `1` to `amount`.
Let `dp[i]` be the minimum number of coins needed to make amount `i`.
Initialize `dp` array with `amount + 1` (which acts as infinity). `dp[0] = 0`.

For each amount `i` from `1` to `amount`:
- For each `coin` in `coins`:
  - If `i - coin >= 0`:
    - `dp[i] = min(dp[i], dp[i - coin] + 1)`

After filling the array, if `dp[amount]` is still `amount + 1`, it means we couldn't make the amount. Return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Initialize DP array with a value strictly greater than the maximum possible coins (amount)
        int MAX = amount + 1;
        vector<int> dp(amount + 1, MAX);
        
        dp[0] = 0; // 0 coins needed to make amount 0
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] == MAX ? -1 : dp[amount];
    }
};

int main() {
    Solution sol;
    vector<int> coins = {1, 2, 5};
    int amount = 11;
    
    cout << "Minimum coins: " << sol.coinChange(coins, amount) << endl; 
    // Expected: 3 (5 + 5 + 1)
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(amount * N)` where `N` is the number of coins. We iterate through `amount` and for each, we iterate through `coins`.
- **Space Complexity:** `O(amount)` for the DP array.
