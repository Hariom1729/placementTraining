# Problem 3: Valid Anagram

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input Format
- Two strings, `s` and `t`.

## Output Format
- Boolean `true` or `false`.

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Approach

### Approach 1: Sorting (Sub-optimal Time)
If you sort both strings, they should become exactly the same string.
- Sort both `s` and `t` using `std::sort`.
- Compare them: `return s == t;`.
- **Time Complexity:** `O(N log N)`.

### Approach 2: Frequency Array / Hashing (Optimal)
Since the problem states that the strings consist of *lowercase English letters*, we only have 26 possible characters. We can use an integer vector `vector<int>(26, 0)`.
1. Check if lengths are equal. If not, return false immediately.
2. Initialize `vector<int> count(26, 0)`.
3. Iterate through the strings. For every character in `s`, increment `count[s[i] - 'a']`. For `t`, decrement `count[t[i] - 'a']`.
4. Loop through the `count` array. If any value is non-zero, it means `t` had extra or missing characters. Return false.
5. If all values are zero, return true.

---

## C++ Solution (Optimal)

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If lengths don't match, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Frequency array for 26 lowercase English letters
        vector<int> count(26, 0);
        
        // Traverse and update counts
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        // Check if any frequency is non-zero
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    cout << (sol.isAnagram("anagram", "nagaram") ? "true" : "false") << endl; // Expected: true
    cout << (sol.isAnagram("rat", "car") ? "true" : "false") << endl; // Expected: false
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We iterate through the string once, and then through the array of length 26.
- **Space Complexity:** `O(1)`. The `count` vector takes exactly 26 integer spaces regardless of input size $N$.

---

## Interview Notes
- **Follow-up:** What if the inputs contain Unicode characters? 
  - *Answer:* Use an `std::unordered_map<char, int>` to keep track of character counts instead of a fixed size `vector`.
