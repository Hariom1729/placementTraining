# Problem 8: Candy

## Problem Statement
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.
You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

## Constraints
- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

---

## Approach: Greedy (Two Passes)

This problem can be elegantly solved using a greedy approach with two passes: Left-to-Right and Right-to-Left.

1. Initialize a `candies` array of size `n` with `1`s (every child gets at least one candy).
2. **Left-to-Right Pass:** Iterate from `1` to `n-1`.
   - If `ratings[i] > ratings[i-1]`, then `candies[i] = candies[i-1] + 1`. This satisfies the left neighbor condition.
3. **Right-to-Left Pass:** Iterate from `n-2` down to `0`.
   - If `ratings[i] > ratings[i+1]`, then the `i`th child must have more candies than the `(i+1)`th child.
   - However, they might already have more candies due to the first pass. Thus, update `candies[i] = max(candies[i], candies[i+1] + 1)`.
4. Sum all the elements in the `candies` array.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1);
        
        // Left to Right Pass
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        // Right to Left Pass
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = max(candies[i], candies[i + 1] + 1);
            }
        }
        
        // Sum all candies
        return accumulate(candies.begin(), candies.end(), 0);
    }
};

int main() {
    Solution sol;
    vector<int> ratings1 = {1, 0, 2};
    cout << "Minimum Candies: " << sol.candy(ratings1) << endl; 
    // Expected: 5 (Candies given: 2, 1, 2)
    
    vector<int> ratings2 = {1, 2, 2};
    cout << "Minimum Candies: " << sol.candy(ratings2) << endl; 
    // Expected: 4 (Candies given: 1, 2, 1)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We do two passes over the array.
- **Space Complexity:** `O(N)` for the `candies` array.
