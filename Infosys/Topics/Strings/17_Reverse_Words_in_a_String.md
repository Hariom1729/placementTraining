# Reverse Words in a String

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Strings / Two Pointers

## Pattern
String Parsing / In-place Reversal

## Problem Statement
Given an input string `s`, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Input
- `s` string.

## Output
- Return the reversed string.

## Sample Test Cases

**Example 1:**
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

## Edge Cases
- String with only one word, surrounded by massive amounts of whitespace.
- String with spaces at the beginning and end.

## Intuition
The easiest way in Python or Java is to split the string by spaces, reverse the array of words, and join them back.
In C++, we can simulate this efficiently using `stringstream`, which automatically tokenizes strings by whitespace and skips multiple spaces seamlessly!
We just read words from the stringstream, push them to a list, reverse the list, and build our final string.
*Follow-up:* Can you do it in $O(1)$ extra space? (In-place).
To do it in-place in C++, we have to manually shift characters to remove extra spaces, reverse the ENTIRE string, and then reverse EACH individual word back to its correct spelling!

## Optimal Approach 1 (StringStream - Recommended for standard interviews)
**Detailed explanation:**
1. Create a `stringstream ss(s)`.
2. Create a `vector<string> words`.
3. Create a temporary `string word`.
4. While `ss >> word`, push `word` into `words`. (This perfectly extracts all words and ignores all extra spaces).
5. Iterate through the `words` vector in reverse order `for (int i = words.size() - 1; i >= 0; i--)`.
6. Append the word to our result string. Append a space if it's not the last word.
7. Return the result string.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ to store the tokens.

## Optimal Approach 2 (In-Place Reversal - $O(1)$ Space)
**Detailed explanation:**
1. **Reverse the entire string:** `reverse(s.begin(), s.end())`. (e.g., `"  hello world "` becomes `" dlrow olleh  "`).
2. **Reverse individual words:** Iterate through `s`. When you find a word, reverse just that segment. (Becomes `" world hello  "`).
3. **Clean up spaces:** Use a slow pointer and a fast pointer to compact the string, removing leading, trailing, and multiple spaces. Finally, `s.resize(slow)`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## C++ Solution (StringStream)

```cpp
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        string result = "";
        vector<string> words;
        
        // Extract all words, ignoring extra spaces
        while (ss >> word) {
            words.push_back(word);
        }
        
        // Build the result in reverse order
        for (int i = words.size() - 1; i >= 0; i--) {
            result += words[i];
            // Add a space after every word EXCEPT the last one
            if (i > 0) {
                result += " ";
            }
        }
        
        return result;
    }
};
```

## C++ Solution (In-Place $O(1)$ Space)
```cpp
class Solution {
public:
    string reverseWords(string s) {
        // 1. Reverse the entire string
        reverse(s.begin(), s.end());
        
        int n = s.length();
        int left = 0, right = 0, i = 0;
        
        while (i < n) {
            // Skip leading spaces for the current word
            while (i < n && s[i] == ' ') i++;
            
            if (i == n) break; // Reached the end
            
            // If it's not the first word, add a single space separator
            if (right != 0) s[right++] = ' ';
            
            left = right; // Mark the start of the current word
            
            // Copy the word characters
            while (i < n && s[i] != ' ') {
                s[right++] = s[i++];
            }
            
            // Reverse the current word to fix its spelling
            reverse(s.begin() + left, s.begin() + right);
        }
        
        // Resize the string to cut off trailing garbage characters
        s.resize(right);
        
        return s;
    }
};
```

## Dry Run (StringStream)
`s = "a good   example"`
- `ss >> word` loop:
  - Extracts `"a"`. `words = ["a"]`.
  - Extracts `"good"`. `words = ["a", "good"]`.
  - Extracts `"example"`. `words = ["a", "good", "example"]`.
- Reverse loop:
  - `i = 2`: `result += "example "`.
  - `i = 1`: `result += "good "`.
  - `i = 0`: `result += "a"`.
- Returns `"example good a"`.

## Common Mistakes
- **Manually parsing spaces poorly:** If you try to manually split the string by looking for `' '` instead of using `stringstream`, you will likely mess up multiple consecutive spaces `s[i] == ' ' && s[i+1] == ' '`. `stringstream` natively ignores continuous delimiters.
- **Adding a trailing space to the final string:** Be sure your loop condition prevents appending `" "` after the very last word, otherwise you fail the test cases.

## Similar Problems
- Reverse String
- Reverse Words in a String III
