# Length of Last Word

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE

## Topic
Strings

## Pattern
Reverse Traversal

## Problem Statement
Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.
A word is a maximal substring consisting of non-space characters only.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Input
- `s` string.

## Output
- Return an integer length.

## Sample Test Cases

**Example 1:**
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

## Edge Cases
- String with trailing spaces (must ignore them to find the actual last word).
- String with only one word, surrounded by spaces.

## Intuition
We just want the LAST word. So why start reading the string from the beginning? Let's read it from the **END** (right to left)!
Because there might be trailing spaces at the very end of the string, our first job is to skip them.
Once we hit a letter, we start counting!
We keep counting and moving left until we hit a space (or reach the beginning of the string).
That count is our answer.

## Optimal Approach (Reverse Traversal)
**Detailed explanation:**
1. Initialize `length = 0`.
2. Start iterating `i` from `s.length() - 1` down to 0.
3. If `s[i] == ' '`:
   - If `length > 0`, it means we have finished reading the last word! `return length`.
   - If `length == 0`, it means we are just skipping trailing spaces. Continue loop.
4. If `s[i] != ' '`:
   - `length++`.
5. After the loop, return `length` (in case the entire string was just one word with no leading spaces).

**Time Complexity:** $O(N)$ worst case (entire string is one word). Best case $O(L)$ where $L$ is trailing spaces + last word.
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        
        // Traverse from right to left
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                // If we've already started counting a word, 
                // this space means the word has ended.
                if (length > 0) {
                    return length;
                }
                // Otherwise, it's just a trailing space. Skip it.
            } else {
                // It's a character, increment length
                length++;
            }
        }
        
        return length;
    }
};
```

## Dry Run
`s = "   fly me   to   the moon  "`
- `i = 26 (' ')`: `length = 0`. Skip.
- `i = 25 (' ')`: `length = 0`. Skip.
- `i = 24 ('n')`: `length = 1`.
- `i = 23 ('o')`: `length = 2`.
- `i = 22 ('o')`: `length = 3`.
- `i = 21 ('m')`: `length = 4`.
- `i = 20 (' ')`: `length = 4`. Since `length > 0`, return `4`.

## Common Mistakes
- **Using `stringstream`:** While `stringstream ss(s)` and extracting words works perfectly, it runs in full $O(N)$ time and $O(N)$ space because it tokenizes the ENTIRE string into memory before giving you the last one. The reverse loop is $O(1)$ space and often finishes in a fraction of $O(N)$ time.

## Similar Problems
- Reverse Words in a String
