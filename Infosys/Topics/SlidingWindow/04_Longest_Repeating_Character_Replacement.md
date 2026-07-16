# Longest Repeating Character Replacement

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Uber

## Topic
Sliding Window / Hash Table / Strings

## Pattern
Variable Size Window with Max Frequency Tracking

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Input
- `s` string.
- `k` integer.

## Output
- Return an integer.

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
```

## Edge Cases
- `k == 0` (Find the longest substring of identical characters).
- `k >= s.length()` (Return the entire string length, since we can replace everything).

## Intuition
We want to find a substring where we can make all characters identical by replacing at most `k` characters.
In any given window `[left, right]`, which characters should we replace?
Obviously, we should pick the character that appears the **MOST** in the current window, and replace all the *other* characters to match it!

The number of replacements we need to make is exactly:
`Replacements Needed = (Length of Window) - (Frequency of the most common character in the window)`.

If `Replacements Needed <= k`, our window is valid! We can expand `right`.
If `Replacements Needed > k`, our window is invalid! We must shrink `left` until it becomes valid again.

To implement this efficiently, we use a **frequency array** of size 26 to keep track of character counts inside the window, and a variable `maxFreq` to track the frequency of the most common character in the window.

## Optimal Approach (Sliding Window)
**Detailed explanation:**
1. Initialize `left = 0`, `maxLength = 0`, `maxFreq = 0`.
2. Create an array `count` of size 26 initialized to 0.
3. Loop `right` from `0` to `s.length() - 1`:
   - Increment the frequency of `s[right]`: `count[s[right] - 'A']++`.
   - Update `maxFreq = max(maxFreq, count[s[right] - 'A'])`. (Note: `maxFreq` might not perfectly update when we shrink the window, but mathematically it doesn't matter! We only care about finding a *larger* window, which would require a *larger* `maxFreq` anyway!).
   - Calculate replacements needed: `(right - left + 1) - maxFreq`.
   - While `(right - left + 1) - maxFreq > k`:
     - Our window is invalid.
     - Decrement the frequency of `s[left]`: `count[s[left] - 'A']--`.
     - `left++`.
   - Update `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ constant space (array of size 26).

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
            // Add the new character to the window
            count[s[right] - 'A']++;
            
            // Keep track of the maximum frequency of ANY character in the window
            maxFreq = max(maxFreq, count[s[right] - 'A']);
            
            // The number of characters we need to replace is:
            // Total characters in window - count of the most frequent character
            int replacementsNeeded = (right - left + 1) - maxFreq;
            
            // If we need to replace more characters than we are allowed (k)
            // Then the window is invalid, shrink it from the left
            if (replacementsNeeded > k) {
                count[s[left] - 'A']--;
                left++;
            }
            
            // Update the maximum length (Note: if the window was invalid, 
            // left and right moved by the same amount, so length didn't increase)
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

## Dry Run
`s = "AABABBA", k = 1`
- `right = 0` ('A'). `count['A'] = 1`. `maxFreq = 1`. `Replacements = 1 - 1 = 0 <= 1`. `maxLen = 1`.
- `right = 1` ('A'). `count['A'] = 2`. `maxFreq = 2`. `Replacements = 2 - 2 = 0 <= 1`. `maxLen = 2`.
- `right = 2` ('B'). `count['B'] = 1`. `maxFreq = 2`. `Replacements = 3 - 2 = 1 <= 1`. `maxLen = 3`.
- `right = 3` ('A'). `count['A'] = 3`. `maxFreq = 3`. `Replacements = 4 - 3 = 1 <= 1`. `maxLen = 4`.
- `right = 4` ('B'). `count['B'] = 2`. `maxFreq = 3`. `Replacements = 5 - 3 = 2 > 1`. Invalid!
  - `count['A']-- -> 2`. `left++ -> 1`.
- `right = 5` ('B'). `count['B'] = 3`. `maxFreq = max(3, 3) = 3`. `Replacements = 5 - 3 = 2 > 1`. Invalid!
  - `count['A']-- -> 1`. `left++ -> 2`.
- `right = 6` ('A'). `count['A'] = 2`. `maxFreq = 3`. `Replacements = 5 - 3 = 2 > 1`. Invalid!
  - `count['B']-- -> 2`. `left++ -> 3`.
- Return `4`.

## Common Mistakes
- **Recalculating `maxFreq` when shrinking:** You might think that when we `left++`, if we removed the most frequent character, we need to loop through the 26 array to find the new `maxFreq`. Interestingly, you **DON'T**! We are trying to maximize the overall window length. We can only achieve a larger window length if we find a `maxFreq` that is *even larger* than our historical best. Therefore, holding onto a falsely high `maxFreq` just keeps the window size constant while it slides, until it hits a substring that actually drives `maxFreq` higher! This is a massive optimization.

## Similar Problems
- Max Consecutive Ones III
- Longest Substring Without Repeating Characters
