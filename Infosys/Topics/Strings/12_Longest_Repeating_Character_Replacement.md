# Longest Repeating Character Replacement

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Microsoft

## Topic
Strings / Hash Table

## Pattern
Sliding Window

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Input
- `s` string.
- `k` integer (number of replacements allowed).

## Output
- Return an integer representing the maximum length.

## Sample Test Cases

**Example 1:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

## Edge Cases
- `k >= s.length()`. We can replace everything! Return `s.length()`.
- String contains all identical characters natively.
- `k = 0`. Problem reduces to finding the longest consecutive sequence of identical characters.

## Intuition
This is a standard **Sliding Window** problem with a clever math condition.
For any window `[left, right]`, the length of the window is `window_size = right - left + 1`.
Inside this window, there is some character that appears the MOST times. Let's call its frequency `maxFreq`.
To make the entire window identical, we should pick the character with `maxFreq` to be the target, and replace ALL the OTHER characters in the window!
The number of other characters we need to replace is exactly:
**`characters_to_replace = window_size - maxFreq`**

If `characters_to_replace <= k`, this window is VALID! We can afford to replace the non-matching characters.
If `characters_to_replace > k`, this window is INVALID! We cannot afford to replace them, so we must SHRINK the window by moving `left` forward.

## Brute Force Approach
**Explanation:** Check all possible substrings $O(N^2)$. Count character frequencies for each, find the max frequency, and check if `length - maxFreq <= k`.
**Time Complexity:** $O(N^3)$ or $O(N^2)$ optimized.
**Space Complexity:** $O(1)$ (frequency array of size 26).

## Optimal Approach (Sliding Window)
**Detailed explanation:**
1. Create a frequency array `vector<int> count(26, 0)`.
2. Initialize `left = 0`, `maxLength = 0`, `maxFreq = 0`.
3. Loop `right` from 0 to `s.length() - 1`:
   - Increment the count of the incoming character: `count[s[right] - 'A']++`.
   - Update `maxFreq` = `max(maxFreq, count[s[right] - 'A'])`. (Note: `maxFreq` represents the historical maximum frequency seen in any window so far. We actually don't need to decrement it when `left` moves. Why? Because the `maxLength` window can only GROW if we find a NEW `maxFreq` that is LARGER than our historical max! Decrementing it requires a full $O(26)$ scan and gains us no mathematical advantage for finding the *maximum* length).
   - Check if window is invalid: `while ((right - left + 1) - maxFreq > k)`:
     - Decrement the count of the outgoing character: `count[s[left] - 'A']--`.
     - Move `left++`.
   - Update `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

**Time Complexity:** $O(N)$ since both `left` and `right` pointers traverse the string at most once. No inner loops over the 26 characters.
**Space Complexity:** $O(1)$ constant space for the 26-element array.

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int left = 0;
        int maxFreq = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // Add the current character to our window's count
            count[s[right] - 'A']++;
            
            // Keep track of the highest frequency of any single character in the window
            maxFreq = max(maxFreq, count[s[right] - 'A']);
            
            // If the number of characters we need to replace exceeds 'k', the window is invalid
            // Formula: WindowLength - MostFrequentCharacterCount > k
            while ((right - left + 1) - maxFreq > k) {
                // Shrink the window from the left
                count[s[left] - 'A']--;
                left++;
                
                // Note: We don't strictly need to update maxFreq here! 
                // We only care about finding a strictly LARGER valid window.
                // A larger window is mathematically impossible to achieve unless maxFreq goes UP anyway.
            }
            
            // The window is now valid. Record its length.
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

## Dry Run
`s = "AABABBA", k = 1`
- `R=0 ('A')`: `count['A']=1`. `maxFreq=1`. Window="A" (len=1). `1-1 <= 1`. `maxLen=1`.
- `R=1 ('A')`: `count['A']=2`. `maxFreq=2`. Window="AA" (len=2). `2-2 <= 1`. `maxLen=2`.
- `R=2 ('B')`: `count['B']=1`. `maxFreq=2`. Window="AAB" (len=3). `3-2 <= 1`. `maxLen=3`.
- `R=3 ('A')`: `count['A']=3`. `maxFreq=3`. Window="AABA" (len=4). `4-3 <= 1`. `maxLen=4`.
- `R=4 ('B')`: `count['B']=2`. `maxFreq=3`. Window="AABAB" (len=5). `5-3 > 1` (Invalid!).
  - Shrink: `count['A']--`. `L=1`. Window="ABAB".
- `R=5 ('B')`: `count['B']=3`. `maxFreq=3`. Window="ABABB" (len=5). `5-3 > 1` (Invalid!).
  - Shrink: `count['A']--`. `L=2`. Window="BABB".
- `R=6 ('A')`: `count['A']=2`. `maxFreq=3`. Window="BABBA" (len=5). `5-3 > 1` (Invalid!).
  - Shrink: `count['B']--`. `L=3`. Window="ABBA".
Result: `4`.

## Common Mistakes
- **Trying to update `maxFreq` inside the while loop:** If you scan the 26-array to find the new `maxFreq` when shrinking the window, it runs in $O(26 \times N)$, which is theoretically $O(N)$ but completely unnecessary! The math proves that to find a *longer* substring than our current `maxLength`, we MUST encounter a completely new `maxFreq` that is greater than our historical one! Therefore, leaving `maxFreq` artificially high doesn't break the algorithm, it just prevents the window from expanding until a true larger frequency is found.

## Similar Problems
- Longest Substring Without Repeating Characters
- Max Consecutive Ones III
