# Problem 7: Reverse Words in a String

## Problem Statement
Given an input string `s`, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

---

## Approach: String Stream / Two Pointers

**Approach 1: Built-in split / stringstream (Easier in interviews)**
We can use a `stringstream` to automatically extract words separated by spaces. We store the words in an array/vector, and then build the result string by iterating through the vector in reverse.

**Approach 2: In-place Two Pointers (O(1) Space - Tricky)**
1. Reverse the entire string.
2. Iterate through the string, find each word, and reverse the word individually.
3. Clean up extra spaces (leading, trailing, and multiple spaces between words) by shifting characters to the left.

*Below is the Stringstream approach which is highly readable and less prone to off-by-one errors during interviews.*

---

## C++ Solution (Stringstream)

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        
        // Extract words (ignores multiple spaces automatically)
        while (ss >> word) {
            words.push_back(word);
        }
        
        string result = "";
        
        // Build the result string in reverse order
        for (int i = words.size() - 1; i >= 0; i--) {
            result += words[i];
            if (i > 0) {
                result += " "; // Add space between words, but not at the end
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    string s = "  hello world  ";
    
    cout << "Reversed Words: '" << sol.reverseWords(s) << "'" << endl; 
    // Expected: 'world hello'
    
    string s2 = "a good   example";
    cout << "Reversed Words: '" << sol.reverseWords(s2) << "'" << endl; 
    // Expected: 'example good a'

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. `stringstream` parses the string in linear time.
- **Space Complexity:** `O(N)` to store the vector of words and the result string.
