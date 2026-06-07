# Problem 13: Minimum Days to Make M Bouquets

## Problem Statement
You are given an integer array `bloomDay`, an integer `m` and an integer `k`.
You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent** flowers from the garden.
The garden consists of `n` flowers, the `i`-th flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make `m` bouquets. If it is impossible, return `-1`.

## Input Format
- An integer array `bloomDay`.
- An integer `m`.
- An integer `k`.

## Output Format
- An integer representing minimum days.

## Constraints
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`

---

## Approach

**Binary Search on Answer:**
1. If `m * k > n`, return `-1`.
2. **Search Space:** `low = min(bloomDay)`, `high = max(bloomDay)`.
3. **Helper Function `possible(day)`:** Check if we can make `m` bouquets by checking adjacent bloomed flowers (`bloomDay[i] <= day`).
4. **Binary Search:**
   - If `possible(mid)` is true, try an earlier day (`high = mid - 1`).
   - Else, wait longer (`low = mid + 1`).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    bool possible(vector<int>& bloomDay, int m, int k, int day) {
        int count = 0;
        int bouquetsMade = 0;
        
        for (int i = 0; i < bloomDay.size(); i++) {
            if (bloomDay[i] <= day) {
                count++;
                if (count == k) {
                    bouquetsMade++;
                    count = 0; 
                }
            } else {
                count = 0; 
            }
        }
        return bouquetsMade >= m;
    }

public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        long long val = 1LL * m * 1LL * k;
        if (val > bloomDay.size()) return -1;
        
        int low = *min_element(bloomDay.begin(), bloomDay.end());
        int high = *max_element(bloomDay.begin(), bloomDay.end());
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (possible(bloomDay, m, k, mid)) {
                ans = mid;
                high = mid - 1; 
            } else {
                low = mid + 1; 
            }
        }
        return ans;
    }
};
```
