# Problem 14: Longest Common Prefix

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Input Format
- An array of strings `strs`.

## Output Format
- A single string representing the longest common prefix.

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

---

## Approach

This problem can be solved in a few ways. The most elegant and common interview approach is **Horizontal Scanning**.
1. Assume the first string `strs[0]` is the longest common prefix.
2. Iterate through the rest of the strings from index 1 to `N-1`.
3. For each string `strs[i]`, continuously check if the current prefix is at the *beginning* of `strs[i]`. In C++, we can check if `strs[i].find(prefix) == 0`.
4. If it doesn't return `0`, shorten the prefix by removing the last character (`prefix = prefix.substr(0, prefix.length() - 1)`).
5. If the prefix becomes empty, return `""` immediately.
6. Return the prefix after checking all strings.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }
        
        // Assume the first string is the common prefix
        string prefix = strs[0];
        
        for (int i = 1; i < strs.size(); i++) {
            // While the current string does not start with the prefix
            while (strs[i].find(prefix) != 0) {
                // Shorten the prefix by one character from the end
                prefix = prefix.substr(0, prefix.length() - 1);
                
                // If prefix becomes empty, there is no common prefix
                if (prefix.empty()) {
                    return "";
                }
            }
        }
        
        return prefix;
    }
};

int main() {
    Solution sol;
    vector<string> strs1 = {"flower", "flow", "flight"};
    cout << sol.longestCommonPrefix(strs1) << endl; // Expected: "fl"
    
    vector<string> strs2 = {"dog", "racecar", "car"};
    cout << sol.longestCommonPrefix(strs2) << endl; // Expected: ""
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(S)` where `S` is the sum of all characters in all strings. In the worst case, all strings are identical.
- **Space Complexity:** `O(1)`. We only use constant extra space to store the prefix string.
