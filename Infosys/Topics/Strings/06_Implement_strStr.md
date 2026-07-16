# Find the Index of the First Occurrence in a String

## Difficulty
Easy / Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook

## Topic
Strings / String Matching

## Pattern
Two Pointers / KMP Algorithm

## Problem Statement
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Constraints
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Input
- `haystack` string.
- `needle` string.

## Output
- Return an integer index.

## Sample Test Cases

**Example 1:**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

**Example 2:**
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Edge Cases
- `needle.length() > haystack.length()`: return `-1` instantly.
- `needle` equals `haystack`: return `0`.

## Intuition
This is the classic substring matching problem (historically implemented as `strStr()` in C).
There are two main approaches for interviews:
1. **The Brute Force Sliding Window:** We slide a window of size `needle.length()` across `haystack` and compare the characters. This works perfectly fine in C++ because `haystack.substr()` or internal loops are heavily optimized.
2. **KMP (Knuth-Morris-Pratt) Algorithm:** A linear time $O(N+M)$ algorithm. It precomputes a "Longest Prefix Suffix" (LPS) array for the `needle`. When a mismatch occurs during matching, it uses the LPS array to skip redundant comparisons instead of starting over from scratch. *Note: KMP is rarely demanded in a 45-minute interview, but the Brute Force is extremely common.*

## Brute Force Approach (Sliding Window / Substring)
**Detailed explanation:**
Iterate through the `haystack` from index `0` up to `haystack.length() - needle.length()`.
At each index `i`, extract a substring of the same length as the needle. If it matches, return `i`.
Alternatively, do it without `.substr()` by using an inner loop to avoid memory allocations.

**Time Complexity:** $O(N \times M)$ where $N$ is haystack length and $M$ is needle length.
**Space Complexity:** $O(1)$ constant space.

## Optimal Approach (Brute Force without substr allocations)
**Detailed explanation:**
1. Check if needle is larger than haystack. If so, return `-1`.
2. Iterate `i` from `0` to `haystack.length() - needle.length()`.
3. For each `i`, use a pointer `j` to iterate over `needle`.
4. While `j < needle.length()` and `haystack[i + j] == needle[j]`, increment `j`.
5. If `j == needle.length()`, we successfully matched the whole needle! Return `i`.
6. Otherwise, outer loop continues to `i + 1`.

**Time Complexity:** $O(N \times M)$ worst case, but practically $O(N)$ for most natural text strings since mismatches occur early.
**Space Complexity:** $O(1)$.

## C++ Solution (Optimal for Interviews)

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length();
        int n = needle.length();
        
        if (n == 0) return 0;
        if (n > m) return -1;
        
        for (int i = 0; i <= m - n; i++) {
            int j = 0;
            // Try to match needle starting at haystack[i]
            while (j < n && haystack[i + j] == needle[j]) {
                j++;
            }
            
            // If we successfully matched the entire needle
            if (j == n) {
                return i;
            }
        }
        
        return -1;
    }
};
```

*(For those interested in KMP, building the LPS array takes $O(M)$ time, and the matching traversal takes $O(N)$ time. Since constraints here are $10^4$, KMP runs in ~20,000 operations, while brute force runs in worst case ~100,000,000 operations. Both comfortably pass within the 1-second C++ limit).*

## Dry Run
`haystack = "sadbutsad", needle = "sad"`
- `m = 9, n = 3`. Loop `i` from `0` to `6`.
- `i = 0`: 
  - `j = 0`: `h[0]=='s'`, `n[0]=='s'`. match.
  - `j = 1`: `h[1]=='a'`, `n[1]=='a'`. match.
  - `j = 2`: `h[2]=='d'`, `n[2]=='d'`. match.
  - `j = 3`. `j == n` (3==3). Returns `0`.

`haystack = "leetcode", needle = "leeto"`
- `i = 0`: matches "leet", but `h[4]=='c' != n[4]=='o'`. Mismatch.
- `i = 1`: `h[1]=='e' != n[0]=='l'`. Mismatch.
... continues returning -1.

## Common Mistakes
- **Looping `i` all the way to `haystack.length() - 1`:** If `haystack` is length 5 and `needle` is length 3, starting a search at index 4 is mathematically impossible and will cause an Out-Of-Bounds exception when checking `haystack[i+j]`. You MUST stop at `haystack.length() - needle.length()`.
- **Using `string::find`:** Using `return haystack.find(needle);` will solve the problem in 1 line, but interviewers will immediately reject it because the purpose of the problem is to implement string matching logic from scratch.

## Similar Problems
- Shortest Palindrome
- Repeated Substring Pattern
