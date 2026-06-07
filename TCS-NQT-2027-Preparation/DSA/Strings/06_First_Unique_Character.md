# Problem 6: First Unique Character in a String

## Problem Statement
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Input Format
- A single string `s` containing lowercase English letters.

## Output Format
- An integer representing the 0-based index of the first unique character. Return `-1` if all characters repeat.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

---

## Approach

This problem is highly frequent in TCS Ninja. We use the **Hashing / Frequency Array** pattern.
1. We know the string only contains lowercase English letters, so we can use an integer array `vector<int>(26, 0)` to store the frequency of each character.
2. **First Pass:** Iterate through the string `s` and populate the frequency array: `count[s[i] - 'a']++`.
3. **Second Pass:** Iterate through the string `s` again. For each character, check its frequency in the `count` array.
4. The first character we encounter with a frequency of exactly `1` is our answer. Return its index.
5. If the loop completes without returning, return `-1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        // Frequency array for 26 lowercase English letters
        vector<int> count(26, 0);
        
        // Pass 1: Count occurrences of each character
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
        }
        
        // Pass 2: Find the first character with a count of 1
        for (int i = 0; i < s.length(); i++) {
            if (count[s[i] - 'a'] == 1) {
                return i;
            }
        }
        
        // If no unique character exists
        return -1;
    }
};

int main() {
    Solution sol;
    cout << sol.firstUniqChar("leetcode") << endl;     // Expected: 0 ('l')
    cout << sol.firstUniqChar("loveleetcode") << endl; // Expected: 2 ('v')
    cout << sol.firstUniqChar("aabb") << endl;         // Expected: -1
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of characters in the string. We iterate over the string exactly twice.
- **Space Complexity:** `O(1)`. The integer vector size is fixed at 26, which uses constant memory.

---

## Interview Notes
- In C++, if the constraints mention "Unicode characters" instead of lowercase English letters, you MUST switch your `vector<int>` array to an `std::unordered_map<char, int>`.
