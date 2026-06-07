# Problem 3: Valid Anagram

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Approach: Frequency Array (Hash Map)

Since the strings only contain lowercase English letters, we can use an integer array of size 26 to count the frequency of each character.

1. If the lengths of `s` and `t` are different, they cannot be anagrams. Return `false`.
2. Create an array `count` of size 26, initialized to 0.
3. Iterate through both strings simultaneously:
   - Increment the count for the character in `s` (`count[s[i] - 'a']++`).
   - Decrement the count for the character in `t` (`count[t[i] - 'a']--`).
4. After the loop, iterate through the `count` array. If any value is not 0, it means the frequencies didn't match. Return `false`.
5. If all values are 0, return `true`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        vector<int> count(26, 0);
        
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    string s = "anagram", t = "nagaram";
    cout << "Is Anagram? " << (sol.isAnagram(s, t) ? "Yes" : "No") << endl; 
    // Expected: Yes
    
    string s2 = "rat", t2 = "car";
    cout << "Is Anagram? " << (sol.isAnagram(s2, t2) ? "Yes" : "No") << endl; 
    // Expected: No

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the strings.
- **Space Complexity:** `O(1)` because the size of the array is fixed at 26, regardless of the input size.
