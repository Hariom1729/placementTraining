# Problem 12: Koko Eating Bananas

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Input Format
- An array of integers `piles`.
- An integer `h`.

## Output Format
- An integer representing the minimum eating speed `k`.

## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## Approach

**Binary Search on Answer**
1. **Search Space:** Minimum speed `k = 1`. Maximum speed `k = max(piles)`.
2. **Helper Function `calculateHours(speed)`:** Calculates total hours to eat all bananas at a given `speed`. For a pile of size `p`, hours needed is `ceil((double)p / speed)`.
3. **Binary Search:**
   - If `hours <= h`, she finishes in time. Try a slower speed (`high = mid - 1`).
   - If `hours > h`, she is too slow. Increase speed (`low = mid + 1`).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
private:
    long long calculateHours(vector<int>& piles, int speed) {
        long long totalHours = 0;
        for (int pile : piles) {
            totalHours += ceil((double)pile / speed);
        }
        return totalHours;
    }

public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (calculateHours(piles, mid) <= h) {
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
