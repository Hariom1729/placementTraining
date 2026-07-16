# Largest Number

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Strings / Sorting

## Pattern
Custom Comparator

## Problem Statement
Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`

## Input
- `nums` vector of integers.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: nums = [10,2]
Output: "210"
Explanation: 2 combined with 10 is 210. 10 combined with 2 is 102. 210 > 102.
```

**Example 2:**
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## Edge Cases
- All zeros: `[0, 0]`. Should return `"0"`, NOT `"00"`.
- Single element array. Returns that element as string.

## Intuition
We want to sort the array, but standard numerical sorting or alphabetical sorting fails.
Example: `[3, 30]`. Alphabetical sort puts `"30"` before `"3"`. So the result would be `"303"`.
But mathematically, `"3" + "30" = "330"`, which is LARGER than `"303"`.
Therefore, `"3"` must come *before* `"30"`.

To solve this, we define a **Custom Sorting Rule**:
For any two strings `a` and `b`, we simply compare the concatenated results!
- If `a + b > b + a`, then `a` must come FIRST.
- If `b + a > a + b`, then `b` must come FIRST.

By applying this single rule to a standard sorting algorithm, the entire array effortlessly perfectly arranges itself to form the largest possible mathematical number.

## Brute Force Approach
**Explanation:** Generate all permutations of the array, concatenate each, and find the max string.
**Time Complexity:** $O(N!)$
**Space Complexity:** $O(N)$

## Optimal Approach (Custom Sort)
**Detailed explanation:**
1. Convert all integers in `nums` to a `vector<string> strs`.
2. Sort the `strs` array using a custom lambda comparator function:
   `[](const string& a, const string& b) { return a + b > b + a; }`
3. If the largest string (now at index 0) is `"0"`, it means all numbers were zeros. Return `"0"`. (This handles the `[0, 0]` edge case).
4. Iterate through `strs` and concatenate all strings into a single result string.
5. Return the result.

**Time Complexity:** $O(N \log N \times K)$ where $N$ is the number of integers and $K$ is the max length of the string representation (up to 10 for $10^9$).
**Space Complexity:** $O(N \times K)$ for the string array.

## C++ Solution

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strs;
        for (int num : nums) {
            strs.push_back(to_string(num));
        }
        
        // Custom comparator: compare a+b vs b+a
        sort(strs.begin(), strs.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Handle edge case where all numbers are 0
        if (strs[0] == "0") {
            return "0";
        }
        
        // Concatenate sorted strings
        string result = "";
        for (const string& s : strs) {
            result += s;
        }
        
        return result;
    }
};
```

## Dry Run
`nums = [3, 30, 34, 5, 9]`
- Convert to strings: `["3", "30", "34", "5", "9"]`.
- Sorting comparisons:
  - `"3" + "30"` (`"330"`) vs `"30" + "3"` (`"303"`). `"330" > "303"`. So `"3"` comes before `"30"`.
  - `"34" + "3"` (`"343"`) vs `"3" + "34"` (`"334"`). `"343" > "334"`. So `"34"` comes before `"3"`.
  - `"9" + "5"` (`"95"`) vs `"5" + "9"` (`"59"`). `"9"` comes before `"5"`.
- After fully sorting: `["9", "5", "34", "3", "30"]`.
- Result: `"9534330"`.

## Common Mistakes
- **Writing a complex character-by-character comparison function:** Trying to manually compare characters and handle length differences is a nightmare and prone to dozens of edge cases. `a + b > b + a` is a bulletproof mathematical shortcut.
- **Forgetting the leading zeros edge case:** If `nums = [0, 0]`, the sorted array is `["0", "0"]`. Concatenation yields `"00"`, which is mathematically incorrect for a number representation. Returning `"0"` if the first string is `"0"` perfectly fixes this.

## Similar Problems
- Sort Array By Parity
- Kth Largest Element in an Array
