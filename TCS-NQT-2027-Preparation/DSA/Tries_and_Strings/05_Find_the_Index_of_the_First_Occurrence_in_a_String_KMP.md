# Problem 5: Find the Index of the First Occurrence in a String (KMP Algorithm)

## Problem Statement
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Constraints
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

---

## Approach: KMP (Knuth-Morris-Pratt) Algorithm

The naive string matching algorithm takes `O(N * M)` time. KMP optimizes this to `O(N + M)` by precomputing an LPS (Longest Prefix Suffix) array for the `needle`.
The LPS array tells us how many characters we can skip matching if a mismatch occurs, preventing us from backtracking the `haystack` pointer.

### Steps:
1. **Compute LPS Array:** `lps[i]` stores the length of the longest proper prefix of `needle[0...i]` which is also a suffix of `needle[0...i]`.
2. **String Matching:**
   - Use pointer `i` for `haystack` and `j` for `needle`.
   - If characters match (`haystack[i] == needle[j]`), increment both.
   - If `j == needle.length()`, we found a match at `i - j`. Return it.
   - If characters mismatch:
     - If `j > 0`, don't backtrack `i`. Instead, update `j = lps[j-1]`. (We know the prefix `needle[0...j-1]` matched, so we look up its longest prefix-suffix to skip redundant checks).
     - If `j == 0`, simply increment `i`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
private:
    void computeLPSArray(string pat, int M, vector<int>& lps) {
        int len = 0; // length of the previous longest prefix suffix
        lps[0] = 0; // lps[0] is always 0
        int i = 1;
        
        // Calculate lps[i] for i = 1 to M-1
        while (i < M) {
            if (pat[i] == pat[len]) {
                len++;
                lps[i] = len;
                i++;
            } else { // pat[i] != pat[len]
                if (len != 0) {
                    len = lps[len - 1];
                } else { // if len == 0
                    lps[i] = 0;
                    i++;
                }
            }
        }
    }

public:
    int strStr(string haystack, string needle) {
        int N = haystack.length();
        int M = needle.length();
        
        if (M == 0) return 0;
        
        vector<int> lps(M);
        computeLPSArray(needle, M, lps);
        
        int i = 0; // index for haystack
        int j = 0; // index for needle
        
        while (i < N) {
            if (needle[j] == haystack[i]) {
                j++;
                i++;
            }
            
            if (j == M) {
                return i - j; // Match found
            } else if (i < N && needle[j] != haystack[i]) {
                // Mismatch after j matches
                if (j != 0) {
                    j = lps[j - 1]; // Use LPS array to avoid backtracking i
                } else {
                    i = i + 1;
                }
            }
        }
        
        return -1; // No match found
    }
};

int main() {
    Solution sol;
    string haystack = "sadbutsad";
    string needle = "sad";
    
    cout << "Index: " << sol.strStr(haystack, needle) << endl; 
    // Expected: 0
    
    string haystack2 = "leetcode";
    string needle2 = "leeto";
    cout << "Index: " << sol.strStr(haystack2, needle2) << endl; 
    // Expected: -1

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N + M)` where `N` is the length of `haystack` and `M` is the length of `needle`.
- **Space Complexity:** `O(M)` for the LPS array.
