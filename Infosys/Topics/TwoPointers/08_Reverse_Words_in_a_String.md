# Reverse Words in a String

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Two Pointers / Strings

## Pattern
Reverse Operations

## Problem Statement
Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Input
- `s` string.

## Output
- Return a string.

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
- String consists of only spaces and one word.
- Multiple contiguous spaces between every word.

## Intuition
The naive approach is to split the string by spaces into an array of words, reverse the array, and join it back together with a single space.
While this is very easy in languages like Python (`" ".join(s.split()[::-1])`), C++ does not have built-in `split` or `join` functions, making it slightly more tedious.

Instead, we can do this highly optimally **in-place** (or building a new string linearly) using Two Pointers!
Because we want the words in reverse order, let's start scanning the string from the **end** (right-to-left).
When we find a letter, we've found the end of a word.
We keep moving our pointer left to find the start of the word.
Once we find the start, we extract that word and append it to our result string, followed by a space.

## Optimal Approach (Two Pointers Right-to-Left)
**Detailed explanation:**
1. Initialize an empty string `result = ""`.
2. Set a pointer `i = s.length() - 1`.
3. Loop while `i >= 0`:
   - Skip any trailing spaces: `while (i >= 0 && s[i] == ' ') i--;`
   - If `i < 0` break. (We finished the string).
   - This `i` is the end index of the current word. Store it: `int end = i`.
   - Find the start of the word by continuing to move left: `while (i >= 0 && s[i] != ' ') i--;`
   - We just passed the start of the word (so it starts at `i + 1`). Extract the substring: `word = s.substr(i + 1, end - i)`.
   - If `result` is empty, just assign `result = word`. If it's not empty, append `" " + word`. (This perfectly handles the single space separation).
4. Return `result`.

**Time Complexity:** $O(N)$ since every character is visited at most twice.
**Space Complexity:** $O(N)$ to build the final string. (Note: True $O(1)$ in-place reversal is possible by reversing the entire string, then reversing each individual word, and finally shifting characters to remove extra spaces. But $O(N)$ space is completely acceptable and preferred for C++ strings which are mutable but resizing is slow).

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        int n = s.length();
        int i = n - 1;
        
        while (i >= 0) {
            // 1. Skip spaces to find the end of a word
            while (i >= 0 && s[i] == ' ') {
                i--;
            }
            
            if (i < 0) break; // Finished scanning
            
            // i is now pointing to the last character of a word
            int end = i;
            
            // 2. Find the start of the word
            while (i >= 0 && s[i] != ' ') {
                i--;
            }
            
            // The word starts at i + 1 and goes up to 'end'
            // Length of the word is (end - i)
            string word = s.substr(i + 1, end - i);
            
            // 3. Append to result with a single space if it's not the first word
            if (result.empty()) {
                result = word;
            } else {
                result += " " + word;
            }
        }
        
        return result;
    }
};
```

## Dry Run
`s = "  hello world  "`
- `i = 14`.
- Skip spaces: `i` moves from 14 down to 12 ('d').
- `end = 12`.
- Find start: `i` moves from 12 down to 7 (space before 'w').
- Word = `substr(8, 12 - 7 = 5)`. Word = `"world"`.
- `result` is empty, so `result = "world"`.
- Loop continues. `i = 7`.
- Skip spaces: `i` moves down to 6 ('o').
- `end = 6`.
- Find start: `i` moves from 6 down to 1 (space before 'h').
- Word = `substr(2, 6 - 1 = 5)`. Word = `"hello"`.
- `result` is not empty, so `result += " hello"`. `result = "world hello"`.
- Loop continues. `i = 1`.
- Skip spaces: `i` moves down to `-1`.
- `i < 0`. Break!
- Return `"world hello"`.

## Common Mistakes
- **Handling extra spaces:** A brute force approach using `stringstream` is very common in C++, but sometimes interviewers ban `stringstream`. Learning the manual two-pointer parse is vastly superior to demonstrate control over indices.

## Similar Problems
- Reverse String
- Reverse Words in a String III
