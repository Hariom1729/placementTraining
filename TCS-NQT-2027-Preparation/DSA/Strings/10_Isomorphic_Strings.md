# Problem 10: Isomorphic Strings

## Problem Statement
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Input Format
- Two strings `s` and `t`.

## Output Format
- Boolean `true` or `false`.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

---

## Approach

This problem requires a 1-to-1 mapping. Since the constraints say "any valid ascii character", an array of size 256 is perfect.
1. We need to ensure that every character in `s` maps uniquely to a character in `t`, AND every character in `t` maps uniquely to `s`.
2. To avoid using two separate `unordered_map`s, we can use two integer arrays `map1` and `map2` of size 256, initialized to 0.
3. We iterate through the strings. For character at index `i`:
   - If we have seen `s[i]` before, its recorded last seen position in `map1` should match the recorded last seen position of `t[i]` in `map2`.
   - Update `map1[s[i]]` and `map2[t[i]]` to the current index + 1.
4. If at any point the recorded indices don't match, return false.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;
        
        // Arrays to store the last seen positions of characters
        vector<int> map1(256, 0);
        vector<int> map2(256, 0);
        
        for (int i = 0; i < s.length(); i++) {
            char charS = s[i];
            char charT = t[i];
            
            // If the last seen positions don't match, it's not a valid 1-to-1 mapping
            if (map1[charS] != map2[charT]) {
                return false;
            }
            
            // Update the last seen positions
            // We use i + 1 because the default array value is 0
            map1[charS] = i + 1;
            map2[charT] = i + 1;
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    cout << (sol.isIsomorphic("egg", "add") ? "true" : "false") << endl;     // Expected: true
    cout << (sol.isIsomorphic("foo", "bar") ? "true" : "false") << endl;     // Expected: false
    cout << (sol.isIsomorphic("paper", "title") ? "true" : "false") << endl; // Expected: true
    cout << (sol.isIsomorphic("badc", "baba") ? "true" : "false") << endl;   // Expected: false
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the strings.
- **Space Complexity:** `O(1)`. The arrays are of a fixed size `256`, which represents the ASCII character set.
