# Problem 2: Fractional Knapsack

## Problem Statement
Given weights and values of `N` items, we need to put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.
Unlike 0/1 knapsack, you are allowed to break the item in fractional parts.

## Constraints
- `1 <= N <= 10^5`
- `1 <= W <= 10^5`
- `1 <= value_i, weight_i <= 10^4`

---

## Approach: Greedy Choice based on Value/Weight Ratio

To maximize the total value, we should always greedily pick items that give the maximum value for the minimum weight. This means we want the items with the highest `Value / Weight` ratio.

1. Calculate the ratio `(Value / Weight)` for each item.
2. Sort the items in descending order of this ratio.
3. Iterate through the sorted items:
   - If the current item's weight is less than or equal to the remaining knapsack capacity, take the whole item. Add its full value to total value, and subtract its weight from the capacity.
   - If the current item's weight is greater than the remaining capacity, take a fraction of the item that exactly fills the remaining capacity. Add the fractional value to the total value, and break the loop (capacity is 0).
4. Return the total value.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int value;
    int weight;
};

class Solution {
private:
    // Custom comparator to sort items in descending order of value/weight ratio
    static bool comp(Item a, Item b) {
        double r1 = (double)a.value / (double)a.weight;
        double r2 = (double)b.value / (double)b.weight;
        return r1 > r2;
    }

public:
    double fractionalKnapsack(int W, Item arr[], int n) {
        sort(arr, arr + n, comp);
        
        int currentWeight = 0;
        double finalValue = 0.0;
        
        for (int i = 0; i < n; i++) {
            if (currentWeight + arr[i].weight <= W) {
                // If the item can fit completely
                currentWeight += arr[i].weight;
                finalValue += arr[i].value;
            } else {
                // If it can't fit completely, take a fraction
                int remain = W - currentWeight;
                finalValue += (arr[i].value / (double)arr[i].weight) * (double)remain;
                break; // Knapsack is full
            }
        }
        
        return finalValue;
    }
};

int main() {
    Solution sol;
    int W = 50;
    Item arr[] = {{60, 10}, {100, 20}, {120, 30}};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Maximum Value: " << sol.fractionalKnapsack(W, arr, n) << endl; 
    // Expected: 240.0 (Take item 1 (wt 10, val 60), item 2 (wt 20, val 100). Remaining wt = 20. 
    // Take fraction of item 3: (120/30) * 20 = 80. Total = 60 + 100 + 80 = 240).

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N)` due to sorting the items.
- **Space Complexity:** `O(1)` as we are sorting in-place.
