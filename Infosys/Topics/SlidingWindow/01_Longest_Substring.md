# Longest Substring Without Repeating Characters

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2021, 2022, 2023
Frequency: Very High

---

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

---

## Input Format
- A single string `s`.

---

## Output Format
- An integer representing the length of the longest substring.

---

## Constraints
- $0 \le s.length \le 5 \times 10^4$
- `s` consists of English letters, digits, symbols and spaces.

---

## Examples

### Example 1
**Input:** 
```
"abcabcbb"
```
**Output:** 
```
3
```
**Explanation:** The answer is "abc", with the length of 3.

### Example 2
**Input:** 
```
"pwwkew"
```
**Output:** 
```
3
```
**Explanation:** The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

## Brute Force Approach
Generate all possible substrings, check if they contain unique characters using a Hash Set, and keep track of the maximum length.

**Time Complexity:** $O(N^3)$
**Space Complexity:** $O(N)$ for checking uniqueness.

---

## Optimal Approach (Sliding Window / Two Pointers)
**Detailed explanation:**
Use a Sliding Window defined by two pointers, `left` and `right`. As `right` iterates through the string:
- If `s[right]` is not in our set (or map), we add it, calculate the window size `right - left + 1`, and update the maximum length.
- If `s[right]` IS in the set, it means we have a duplicate. We must shrink the window from the `left` until the duplicate is removed from the window.

*Optimization with Map:* Instead of shrinking by 1 step at a time, store the index of characters in a Map. If a duplicate is found, jump `left` directly to `map[s[right]] + 1`.

**Dry Run:**
`s = "abcabcbb"`
- `i = 0` ('a'): map = {a:0}, max = 1
- `i = 1` ('b'): map = {a:0, b:1}, max = 2
- `i = 2` ('c'): map = {a:0, b:1, c:2}, max = 3
- `i = 3` ('a'): 'a' is in map! `left` jumps to `max(left, map['a'] + 1) = max(0, 0+1) = 1`. Update map['a'] = 3. max = 3.
- ...

**Complexity:**
- **Time Complexity:** $O(N)$ since `left` and `right` only traverse forward.
- **Space Complexity:** $O(\min(N, M))$ where $M$ is the character set size (e.g., 256 for ASCII).

---

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int lengthOfLongestSubstring(string s) {
    vector<int> dict(256, -1); // To store the last seen index of each character
    int maxLen = 0, left = 0;
    
    for (int right = 0; right < s.length(); right++) {
        // If character was seen and its index is within current window
        if (dict[s[right]] >= left) {
            left = dict[s[right]] + 1; // Jump left pointer
        }
        
        dict[s[right]] = right; // Update last seen index
        maxLen = max(maxLen, right - left + 1); // Update max length
    }
    
    return maxLen;
}

int main() {
    cout << "Max Length: " << lengthOfLongestSubstring("abcabcbb") << endl; // 3
    return 0;
}
```

---

## Common Mistakes
- **Jumping Left Pointer Backwards:** When updating the `left` pointer using the map, you MUST do `left = max(left, dict[s[right]] + 1)`. If you just do `left = dict[s[right]] + 1`, the `left` pointer might jump backwards if it encounters an old duplicate that is outside the current window.

---

## Similar Questions
- Longest Substring with At Most K Distinct Characters
- Subarrays with K Different Integers

---

## Pattern Recognition
**Identify this when:** Finding the longest/shortest contiguous sequence (substring/subarray) satisfying a condition (like uniqueness). This is the hallmark of the **Dynamic Sliding Window** pattern.
