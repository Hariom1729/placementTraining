# Koko Eating Bananas

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Google, Amazon, Facebook, Airbnb

## Topic
Searching / Arrays

## Pattern
Binary Search on Answer Range

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Input
- `piles` vector of integers.
- `h` integer (hours).

## Output
- Return an integer `k` (the minimum eating speed).

## Sample Test Cases

**Example 1:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation:
At speed 4:
Pile 3 takes 1 hour.
Pile 6 takes 2 hours.
Pile 7 takes 2 hours.
Pile 11 takes 3 hours.
Total = 1 + 2 + 2 + 3 = 8 hours. Perfect!
```

**Example 2:**
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: She only has 5 hours for 5 piles, so she must eat a whole pile every hour. The max pile is 30, so speed must be 30.
```

**Example 3:**
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Edge Cases
- Massive arrays and massive `h` values requiring `long long` for hours tracking to prevent overflow.
- `h == piles.length` (speed must exactly equal the maximum element in `piles`).

## Intuition
This is a classic **Binary Search on the Answer** problem!
The array `piles` is NOT sorted. But the **range of possible eating speeds** IS sorted!
What is the minimum possible eating speed? `1` banana per hour.
What is the maximum possible eating speed? `max(piles)` (eating more than the largest pile doesn't help because she stops after finishing a pile anyway).

Because the speeds `[1, 2, 3, ..., MAX_PILE]` form a perfectly sorted array, and the function "hours needed to eat all bananas at speed k" is **monotonically decreasing** (faster speed = less hours), we can use Binary Search!

1. We set `left = 1` and `right = max(piles)`.
2. We pick a mid speed: `k = left + (right - left) / 2`.
3. We calculate how many hours it takes to eat all bananas at speed `k`.
   - For a pile of size `P`, hours needed = `ceil(P / k)`. (Integer math: `(P + k - 1) / k`).
4. If total hours `<= h`: The speed is valid! But we want the *minimum* speed, so let's try an even slower speed: `right = k`.
5. If total hours `> h`: The speed is too slow! We must eat faster: `left = k + 1`.

## Brute Force Approach
**Explanation:** Test every speed starting from `k = 1` upwards until you find a speed that finishes in `<= h` hours.
**Time Complexity:** $O(\max(P) \times N)$. Will Time Limit Exceed.
**Space Complexity:** $O(1)$

## Optimal Approach (Binary Search on Answer)
**Detailed explanation:**
1. Helper function `getHours(piles, k)`:
   - Loop through `p` in `piles`.
   - `totalHours += (p + k - 1) / k` (which is integer ceiling division).
   - Return `totalHours`. (Use `long long` to prevent overflow).
2. Find the max element in `piles` to set `right`.
3. `left = 1`, `right = max(piles)`.
4. Loop while `left < right`:
   - `mid = left + (right - left) / 2`.
   - If `getHours(piles, mid) <= h`:
     - This speed is valid, but can we go slower? `right = mid`.
   - Else:
     - This speed is too slow. We must go faster. `left = mid + 1`.
5. Return `left`.

**Time Complexity:** $O(N \log(\max(P)))$ where $N$ is number of piles and $\max(P)$ is the largest pile.
**Space Complexity:** $O(1)$

## C++ Solution

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    long long getHours(const vector<int>& piles, int speed) {
        long long hours = 0;
        for (int p : piles) {
            // Integer ceiling division: ceil(p / speed)
            hours += (p + speed - 1) / speed;
        }
        return hours;
    }

public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        // The maximum possible speed we would ever need is the size of the largest pile
        int right = *max_element(piles.begin(), piles.end());
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            long long hoursNeeded = getHours(piles, mid);
            
            if (hoursNeeded <= h) {
                // Speed is valid, try to find a slower (smaller) speed
                right = mid;
            } else {
                // Speed is too slow, we must increase it
                left = mid + 1;
            }
        }
        
        return left;
    }
};
```

## Dry Run
`piles = [3, 6, 7, 11], h = 8`
- `left = 1`, `right = 11`.
- `mid = 6`.
  - `getHours(6)`: `ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)` = `1 + 1 + 2 + 2 = 6` hours.
  - `6 <= 8`. Valid! But can we go slower? `right = 6`.
- `left = 1`, `right = 6`.
- `mid = 3`.
  - `getHours(3)`: `1 + 2 + 3 + 4 = 10` hours.
  - `10 > 8`. Too slow! Must go faster. `left = 4`.
- `left = 4`, `right = 6`.
- `mid = 5`.
  - `getHours(5)`: `1 + 2 + 2 + 3 = 8` hours.
  - `8 <= 8`. Valid! `right = 5`.
- `left = 4`, `right = 5`.
- `mid = 4`.
  - `getHours(4)`: `1 + 2 + 2 + 3 = 8` hours.
  - `8 <= 8`. Valid! `right = 4`.
- Loop breaks `left == right (4)`. Return 4.

## Common Mistakes
- **Using `double` and `ceil()`:** Floating point math in C++ is notoriously slow and susceptible to precision errors. The integer math formula `(a + b - 1) / b` computes `ceil(a/b)` instantly and safely.
- **Integer overflow for `totalHours`:** If $h$ is $10^9$ and the piles are very large, adding up the hours will easily overflow a 32-bit `int`. The `getHours` function MUST return a `long long`.

## Similar Problems
- Capacity To Ship Packages Within D Days
- Minimum Number of Days to Make m Bouquets
- Split Array Largest Sum
