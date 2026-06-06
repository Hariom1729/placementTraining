# Problem 8: Longest Consecutive Sequence (Hashing Re-visited)

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(N)` time.

*(Note: This problem was also covered in Arrays, but its optimal O(N) solution heavily relies on Hashing via `unordered_set`, making it a core Hashing problem as well).*

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the length of the sequence.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach: Unordered Set

To achieve `O(N)` time, we cannot sort the array (`O(N log N)`). Instead, we throw everything into a hash set.

1. Insert all elements into an `unordered_set<int> set`. This provides `O(1)` lookups.
2. Iterate through the array (or set). For each number `num`, check if it's the *start* of a sequence.
3. A number is the start of a sequence only if `num - 1` does NOT exist in the set.
4. If it is a starting point, continuously check if `num + 1`, `num + 2`, etc., exist in the set and keep a running count of the length.
5. Update `longestStreak` with the maximum length found.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        unordered_set<int> hashSet(nums.begin(), nums.end());
        int longestStreak = 0;

        for (int num : hashSet) { 
            // Check if it's the start of a sequence
            if (!hashSet.count(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                // Count the length of the sequence going forward
                while (hashSet.count(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = max(longestStreak, currentStreak);
            }
        }
        
        return longestStreak;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {100, 4, 200, 1, 3, 2};
    cout << "Longest Consecutive Sequence: " << sol.longestConsecutive(nums) << endl; // Expected: 4
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. It looks like there's a nested loop, but the inner `while` loop only runs when a starting element is found. Therefore, each element is visited at most twice.
- **Space Complexity:** `O(N)` to store elements in the unordered set.
