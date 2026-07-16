# Jewels and Stones

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Adobe

## Topic
Hashing / Strings

## Pattern
Hash Set Lookups

## Problem Statement
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

## Constraints
- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters.
- All the characters of `jewels` are **unique**.

## Input
- `jewels` string.
- `stones` string.

## Output
- Return an integer (the count of jewels in your possession).

## Sample Test Cases

**Example 1:**
```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Explanation: We have 1 'a' and 2 'A's. Total = 3.
```

**Example 2:**
```
Input: jewels = "z", stones = "ZZ"
Output: 0
Explanation: 'z' and 'Z' are different.
```

## Edge Cases
- No stones are jewels.
- All stones are jewels.

## Intuition
This is the textbook example of why Hash Sets are useful.
We have a collection of "valid" items (`jewels`). We need to scan our inventory (`stones`) and quickly determine if each item is valid.
If we use a Hash Set, we can check if a stone is a jewel in exactly $O(1)$ time!

Since the strings only contain English letters, an array of size `128` (ASCII table size) acts as an ultra-fast, zero-overhead Hash Set.

## Brute Force Approach
**Explanation:** For each stone in `stones`, loop through `jewels` to see if it matches.
**Time Complexity:** $O(J \times S)$
**Space Complexity:** $O(1)$

## Optimal Approach (Boolean Array as Hash Set)
**Detailed explanation:**
1. Create a boolean array `bool isJewel[128] = {false}`.
2. Iterate through `jewels`:
   - `isJewel[c] = true`.
3. Initialize `count = 0`.
4. Iterate through `stones`:
   - If `isJewel[c]` is true:
     - `count++`.
5. Return `count`.

**Time Complexity:** $O(J + S)$ where $J$ is length of jewels and $S$ is length of stones.
**Space Complexity:** $O(1)$ constant space (array of size 128).

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        // ASCII array acts as an O(1) hash set
        bool isJewel[128] = {false};
        
        // Mark all jewels in our set
        for (char j : jewels) {
            isJewel[j] = true;
        }
        
        int count = 0;
        
        // Count how many of our stones exist in the jewel set
        for (char s : stones) {
            if (isJewel[s]) {
                count++;
            }
        }
        
        return count;
    }
};
```

## Dry Run
`jewels = "aA", stones = "aAAbbbb"`
- `isJewel['a'] = true`, `isJewel['A'] = true`.
- Scan stones:
  - `s = 'a'`: `isJewel['a']` is true. `count=1`.
  - `s = 'A'`: `isJewel['A']` is true. `count=2`.
  - `s = 'A'`: `isJewel['A']` is true. `count=3`.
  - `s = 'b'`: `isJewel['b']` is false.
  - ...
- Return `3`.

## Common Mistakes
- **Using an `unordered_set<char>`:** While mathematically correct and $O(1)$, an `unordered_set` has dynamic memory allocation overhead. A flat `bool` array is infinitely faster and takes 128 bytes, which is less memory than the `unordered_set` overhead!

## Similar Problems
- Find the Difference
- Ransom Note
