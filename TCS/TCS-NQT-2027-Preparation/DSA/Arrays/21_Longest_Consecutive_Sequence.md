# Problem 21: Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(N)` time.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the length of the longest consecutive sequence.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

Since the requirement is `O(N)` time, sorting the array (`O(N log N)`) is not optimal. We must use Hashing.
1. Insert all elements of the array into an `unordered_set`. This allows `O(1)` lookups and automatically handles duplicates.
2. Iterate through the array (or the set).
3. For each number `num`, check if it's the *start* of a sequence. It is the start if `num - 1` is NOT present in the set.
4. If it is the start of a sequence, keep checking if `num + 1`, `num + 2`, etc., exist in the set, and count the length of the sequence.
5. Keep track of the `longestStreak` found across all starting numbers.

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

        for (int num : hashSet) { // Iterating over the set avoids checking duplicates
            // Check if it's the start of a sequence
            if (!hashSet.count(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                // Count the length of the sequence
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
    cout << "Longest Consecutive Sequence: " << sol.longestConsecutive(nums) << endl; // Expected: 4 (from 1, 2, 3, 4)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. Inserting elements into the set takes `O(N)`. Finding the start of a sequence and counting takes `O(N)` overall, because the inner `while` loop only runs for elements that are part of a sequence, meaning each element is visited at most twice.
- **Space Complexity:** `O(N)`. The `unordered_set` takes space proportional to the number of unique elements.
