# Longest Common Prefix

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Apple, Microsoft

## Topic
Strings

## Pattern
Vertical Scanning / Sorting

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## Input
- `strs` vector of strings.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Edge Cases
- Array contains only 1 string. Return the string.
- Any string is empty. Return `""`.
- The common prefix is the entirety of one of the strings (e.g., `["ab", "abc"]` returns `"ab"`).

## Intuition
**Approach 1: Horizontal Scanning.** 
Take the first string as the initial "prefix". Compare this prefix with the second string and shorten the prefix until it matches. Then compare with the third, and so on. If the prefix ever becomes `""`, stop and return.

**Approach 2: Sorting (The Easiest).**
If we sort the array of strings alphabetically, the strings that are most DIFFERENT from each other will be at the absolute start (`strs[0]`) and the absolute end (`strs[n-1]`) of the array!
Therefore, the common prefix of the *entire* array is simply the common prefix between the **first string** and the **last string** in the sorted array!

## Brute Force Approach
**Explanation:** Vertical scanning character by character for all strings.
**Time Complexity:** $O(S)$ where $S$ is the sum of all characters in all strings.
**Space Complexity:** $O(1)$

## Optimal Approach (Sorting)
**Detailed explanation:**
1. Sort the vector of strings lexicographically: `sort(strs.begin(), strs.end());`.
2. Take the first string: `string first = strs[0];`
3. Take the last string: `string last = strs.back();`
4. Initialize an index `i = 0`.
5. While `i < first.length() && i < last.length()` AND `first[i] == last[i]`:
   - Increment `i++`.
6. Return `first.substr(0, i)`.

**Time Complexity:** $O(N \log N \times M)$ where $N$ is the number of strings and $M$ is the max length of a string (due to string comparison during sort).
**Space Complexity:** $O(1)$

*Note: The sorting approach is extremely clean to write, but slightly slower theoretically than Horizontal Scanning $O(N \times M)$. In interviews, both are highly respected. Let's provide the Sorting one as it's less prone to indexing bugs.*

## C++ Solution (Sorting)

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        
        // Sort strings lexicographically
        sort(strs.begin(), strs.end());
        
        string first = strs[0];
        string last = strs[strs.size() - 1];
        
        int i = 0;
        // Compare the first and last strings
        while (i < first.length() && i < last.length() && first[i] == last[i]) {
            i++;
        }
        
        // The common prefix of the most different strings is the common prefix of all
        return first.substr(0, i);
    }
};
```

## Optimal Approach 2 (Horizontal Scanning - Technically Faster)
```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        
        string prefix = strs[0];
        
        for (int i = 1; i < strs.size(); i++) {
            // While the current string does NOT start with the prefix
            while (strs[i].find(prefix) != 0) {
                // Shorten the prefix by 1 character from the end
                prefix = prefix.substr(0, prefix.length() - 1);
                
                // If prefix becomes empty, there's no common prefix at all
                if (prefix.empty()) return "";
            }
        }
        
        return prefix;
    }
};
```

## Dry Run (Sorting Approach)
`strs = ["flower", "flow", "flight"]`
- `sort(strs)` -> `["flight", "flow", "flower"]`
- `first = "flight"`, `last = "flower"`
- `i = 0`: `first[0]` ('f') == `last[0]` ('f'). `i = 1`.
- `i = 1`: `first[1]` ('l') == `last[1]` ('l'). `i = 2`.
- `i = 2`: `first[2]` ('i') != `last[2]` ('o'). Loop breaks.
- Return `first.substr(0, 2)` -> `"fl"`.

## Common Mistakes
- **Going out of bounds:** In manual character-by-character scanning, you must ensure you don't exceed the length of the shortest string. The condition `i < first.length() && i < last.length()` handles this perfectly.
- **Using `==` on `find()` without checking `0`:** In the horizontal approach, `strs[i].find(prefix) == 0` is required. If it returns something like `2`, it means the prefix is inside the string, but NOT at the beginning! We only want prefixes.

## Similar Problems
- Implement strStr()
- Longest Palindromic Substring
