# Problem 2: Longest Common Prefix

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

---

## Approach 1: Horizontal Scanning / Sorting

A very clever and optimal approach involves sorting the array of strings lexicographically.
Once the array is sorted, the strings that are most different from each other will be at the beginning and the end of the array.
Therefore, the longest common prefix of the *entire* array is simply the common prefix between the **first string** and the **last string** in the sorted array.

## Approach 2: Using a Trie

We can insert all strings into a Trie. Then, we walk down the Trie starting from the root. As long as a node has exactly **one child** and is **not an end of a word**, we add that character to our prefix and continue.

*We will implement Approach 1 as it is much simpler and faster in practice (`O(N \log N * M)`).*

---

## C++ Solution (Sorting)

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        
        // Sort the array of strings
        sort(strs.begin(), strs.end());
        
        // After sorting, the most different strings are the first and the last ones.
        // We only need to find the common prefix between the first and last string.
        string first = strs[0];
        string last = strs[strs.size() - 1];
        
        string prefix = "";
        
        for (int i = 0; i < min(first.length(), last.length()); i++) {
            if (first[i] == last[i]) {
                prefix += first[i];
            } else {
                break;
            }
        }
        
        return prefix;
    }
};

int main() {
    Solution sol;
    vector<string> strs = {"flower", "flow", "flight"};
    cout << "Longest Common Prefix: " << sol.longestCommonPrefix(strs) << endl; 
    // Expected: "fl"
    
    vector<string> strs2 = {"dog", "racecar", "car"};
    cout << "Longest Common Prefix: " << sol.longestCommonPrefix(strs2) << endl; 
    // Expected: ""

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N * M)` where `N` is the number of strings and `M` is the maximum length of a string. Sorting strings takes time proportional to their lengths.
- **Space Complexity:** `O(1)` (excluding the space required to return the result string).
