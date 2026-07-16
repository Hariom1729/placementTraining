# Longest Palindrome

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google

## Topic
Strings / Hash Table / Greedy

## Pattern
Frequency Counting

## Problem Statement
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, `"Aa"` is not considered a palindrome here.

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of lowercase and/or uppercase English letters only.

## Input
- `s` string.

## Output
- Return an integer length.

## Sample Test Cases

**Example 1:**
```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

**Example 2:**
```
Input: s = "a"
Output: 1
Explanation: The longest palindrome is "a", whose length is 1.
```

## Edge Cases
- All characters have even frequencies. (Length is `s.length()`).
- All characters have odd frequencies (e.g., `"abc"`). Length is 1.

## Intuition
To build a palindrome, we need symmetry. For every character on the left side of the palindrome, we need an identical character on the right side.
This means we can use pairs of identical characters! If we have 4 `'c'`s, we can put two on the left and two on the right.
So, any character that appears an **even** number of times can be fully used in our palindrome.
What if a character appears an **odd** number of times? (e.g., 5 `'a'`s).
We can still use 4 of them in pairs! The remaining 1 `'a'` is leftover.
Generally, we can use `count / 2 * 2` of ANY character.

Finally, a palindrome can have exactly ONE character sitting perfectly in the middle (e.g., the `'a'` in `"dccaccd"`).
So, if we have ANY leftovers (any character with an odd frequency), we can place exactly ONE of those leftovers in the dead center of the palindrome to increase its length by 1.

## Brute Force Approach
N/A - This is a purely mathematical/greedy problem based on counting.

## Optimal Approach (Greedy Frequency Array)
**Detailed explanation:**
1. Create a frequency array `vector<int> count(128, 0)` (128 handles both uppercase and lowercase ASCII).
2. Count the frequencies of all characters in `s`.
3. Initialize `length = 0` and a boolean flag `hasOdd = false`.
4. Iterate through the frequency array:
   - If `count[i]` is even, we can use all of them: `length += count[i]`.
   - If `count[i]` is odd, we can use the even part of it: `length += count[i] - 1`. We also set `hasOdd = true` because we have a leftover character!
5. If `hasOdd` is true, we can place exactly one leftover character in the center, so we return `length + 1`.
6. Else, return `length`.

**Time Complexity:** $O(N)$ where $N$ is the length of the string to build the frequency map. The iteration over the 128-size array takes $O(1)$. Total $O(N)$.
**Space Complexity:** $O(1)$ constant extra space for the frequency array.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        vector<int> count(128, 0);
        
        // Count frequencies of all characters
        for (char c : s) {
            count[c]++;
        }
        
        int length = 0;
        bool hasOdd = false;
        
        for (int i = 0; i < 128; i++) {
            if (count[i] % 2 == 0) {
                // If even, we can use all of them symmetrically
                length += count[i];
            } else {
                // If odd, we can use all but one (making it even) symmetrically
                length += count[i] - 1;
                // Mark that we have at least one odd leftover
                hasOdd = true;
            }
        }
        
        // If we had any odd leftovers, we can place exactly ONE in the center
        if (hasOdd) {
            length++;
        }
        
        return length;
    }
};
```

## Dry Run
`s = "abccccdd"`
Counts: `'a': 1`, `'b': 1`, `'c': 4`, `'d': 2`
- `i = 'a'`: count is 1 (odd). `length += 0`. `hasOdd = true`.
- `i = 'b'`: count is 1 (odd). `length += 0`. `hasOdd = true`.
- `i = 'c'`: count is 4 (even). `length += 4`.
- `i = 'd'`: count is 2 (even). `length += 2`.
Loop ends. `length = 6`.
`hasOdd` is true, so `length++` -> 7.
Returns `7`.

## Common Mistakes
- **Using an array of size 26:** The problem states the string can contain BOTH lowercase and uppercase letters. `'A'` and `'a'` are distinct. Using a 26-size array and `c - 'a'` will cause out-of-bounds errors for uppercase letters. Use size 128 and just index it with `count[c]`.
- **Adding multiple odd characters to the center:** You can only put ONE character in the exact center of a palindrome. If you have 3 different odd-count characters, you can only use ONE of them for the center. The other 2 are completely wasted. The boolean flag correctly ensures we only add `+1` once.

## Similar Problems
- Palindrome Permutation
- Longest Palindromic Substring
