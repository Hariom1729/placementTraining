# Problem 12: Reverse Words in a String

## Problem Statement
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Input Format
- A single string `s`.

## Output Format
- A string representing the words in reverse order.

## Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

---

## Approach

**Approach (Two Pointers - Interview Preferred):**
1. Traverse the string backwards from `n-1` to `0`.
2. When a non-space character is found, mark it as the end of a word.
3. Keep moving backwards until a space is found. The characters from this space to the end mark form a word.
4. Append this word to the `result` string.
5. Repeat.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        int i = s.length() - 1;
        
        while (i >= 0) {
            // Skip trailing spaces
            while (i >= 0 && s[i] == ' ') {
                i--;
            }
            if (i < 0) break;
            
            // i is now at the last character of a word
            int j = i;
            
            // Find the start of the word
            while (i >= 0 && s[i] != ' ') {
                i--;
            }
            
            // Append the word to result (and a space if it's not the first word appended)
            if (result.empty()) {
                result += s.substr(i + 1, j - i);
            } else {
                result += " " + s.substr(i + 1, j - i);
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.reverseWords("the sky is blue") << endl;  // Expected: "blue is sky the"
    cout << sol.reverseWords("  hello world  ") << endl;  // Expected: "world hello"
    cout << sol.reverseWords("a good   example") << endl; // Expected: "example good a"
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. We traverse the string once backwards. String extraction `substr` takes linear time but across the entire process, it sums up to `O(N)`.
- **Space Complexity:** `O(N)` for the output string. If the question asked to modify the string in-place, we could do it in `O(1)` space by reversing the entire string in C++, then reversing each individual word, and finally erasing extra spaces.
