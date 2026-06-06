# Problem 17: Best Time to Buy and Sell Stock

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Input Format
- An array of integers `prices`.

## Output Format
- An integer representing the maximum profit.

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Approach

We need to buy at the lowest price and sell at the highest price *after* the buying day.
1. Initialize `minPrice` to a very large value (`INT_MAX`) and `maxProfit` to `0`.
2. Iterate through the `prices` array.
3. For each price, check if it's lower than the current `minPrice`. If it is, update `minPrice`.
4. If it's not the minimum, calculate the potential profit if we sold today: `prices[i] - minPrice`.
5. If this potential profit is greater than our current `maxProfit`, update `maxProfit`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;
        
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minPrice) {
                // Update minimum price encountered so far
                minPrice = prices[i];
            } else if (prices[i] - minPrice > maxProfit) {
                // Update maximum profit
                maxProfit = prices[i] - minPrice;
            }
        }
        
        return maxProfit;
    }
};

int main() {
    Solution sol;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << "Max Profit: " << sol.maxProfit(prices) << endl; // Expected: 5 (Buy at 1, Sell at 6)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements in the `prices` array. Single pass through the array.
- **Space Complexity:** `O(1)`. Only constant extra space is required.
