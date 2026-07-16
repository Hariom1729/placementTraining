# Largest Number

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Sorting / Strings / Greedy

## Pattern
Custom String Comparator

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
Explanation: "210" > "102".
```

**Example 2:**
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## Edge Cases
- All numbers are `0` (`[0, 0]`). The output should be `"0"`, not `"00"`.
- Single digit vs double digit ties (e.g. `3` vs `30` -> `"330"` > `"303"`, so `3` should come first).

## Intuition
We want to arrange the numbers to maximize the final concatenated value.
At first glance, you might think we should just sort the numbers in descending order: `9, 5, 34, 30, 3`. But what about `3` and `30`? Alphabetically, `"30"` comes before `"3"`. If we sort alphabetically descending, we get `"30"`, then `"3"`, which yields `"303"`. But `"330"` is larger!

To solve this, we need a **Custom Comparator**!
Instead of comparing string `a` and string `b` directly, we compare their **concatenated combinations**:
Does `a + b` form a larger number than `b + a`?
If `a + b > b + a`, then `a` MUST come before `b` in our sorted array!
Example: `a = "3"`, `b = "30"`.
`a + b = "330"`. `b + a = "303"`.
Since `"330" > "303"`, `"3"` should be placed before `"30"`!

Because we are dealing with massive numbers that overflow 64-bit integers, we MUST perform this concatenation and comparison using **Strings**.

## Brute Force Approach
**Explanation:** Generate all permutations of the array and find the maximum string.
**Time Complexity:** $O(N!)$
**Space Complexity:** $O(N)$

## Optimal Approach (Custom String Comparator)
**Detailed explanation:**
1. Convert all integers in `nums` into strings and store them in a `vector<string> strNums`.
2. Sort `strNums` using a custom lambda function:
   - `[](const string& a, const string& b) { return a + b > b + a; }`
3. **Edge Case Handling:** If the highest priority string (at index 0) is `"0"`, it means ALL numbers were 0s. Return `"0"`.
4. Concatenate all strings in the sorted `strNums` into a `result` string.
5. Return `result`.

**Time Complexity:** $O(N \log N \times M)$ where $N$ is the number of integers and $M$ is the average length of the strings (which is at most 10 digits). Effectively $O(N \log N)$.
**Space Complexity:** $O(N \times M)$ to store the array of strings.

## C++ Solution

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strNums;
        
        // Convert all integers to strings
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }
        
        // Custom sort: compare a+b vs b+a
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Edge case: if the largest number after sorting is "0", the whole array is 0s
        if (strNums[0] == "0") {
            return "0";
        }
        
        // Concatenate the sorted strings
        string result = "";
        for (string s : strNums) {
            result += s;
        }
        
        return result;
    }
};
```

## Dry Run
`nums = [3, 30, 34, 5, 9]`
- `strNums = ["3", "30", "34", "5", "9"]`.
- Compare `"3"` and `"30"`: `"330" > "303"` -> `"3"` > `"30"`.
- Compare `"3"` and `"34"`: `"334" < "343"` -> `"34"` > `"3"`.
- Compare `"5"` and `"9"`: `"59" < "95"` -> `"9"` > `"5"`.
- Sorted `strNums`: `["9", "5", "34", "3", "30"]`.
- `result = "9" + "5" + "34" + "3" + "30" = "9534330"`.

## Common Mistakes
- **Failing the `[0, 0]` test case:** If the input is `[0, 0]`, the code without the edge case check will return `"00"`. A number cannot have leading zeros, so it must return `"0"`. Since we sorted in descending order, if the very first string is `"0"`, the rest MUST also be `"0"`.
- **Comparing strings alphabetically:** `a > b` fails for `"3"` and `"30"`. You must compare the concatenations: `a + b > b + a`.

## Similar Problems
- Sort Array By Parity
- Reorder Data in Log Files
