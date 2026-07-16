# Reverse Words in a String

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2021, 2023
Frequency: High

---

## Problem Statement
Given an input string `s`, reverse the order of the words.

A **word** is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
**Note:** `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

---

## Input Format
- A single string `s` enclosed in quotes.

---

## Output Format
- Return a single string representing the reversed words.

---

## Constraints
- $1 \le s.length \le 10^4$
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

---

## Examples

### Example 1
**Input:** 
```
"the sky is blue"
```
**Output:** 
```
"blue is sky the"
```

### Example 2
**Input:** 
```
"  hello world  "
```
**Output:** 
```
"world hello"
```
**Explanation:** Your reversed string should not contain leading or trailing spaces.

### Example 3
**Input:** 
```
"a good   example"
```
**Output:** 
```
"example good a"
```
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

---

## Brute Force Approach
Create a temporary string or list to hold the words. Iterate through the string character by character, building words. Push each word into an array or stack. Finally, pop them out or iterate backwards and append them with a single space.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

---

## Better Approach (Using stringstream)
In C++, `std::stringstream` naturally ignores all whitespace (including multiple spaces). We can extract word by word and prepend it to the result string.

**Complexity:** 
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for string building.

---

## Optimal Approach (In-place Reversal)
**Detailed explanation:**
If we want to avoid $O(N)$ extra space (excluding the output string space), we can do it in two steps:
1. Reverse the entire string.
2. Iterate through the string, find each word boundaries, reverse each individual word, and shift it to the correct position (removing extra spaces).

However, `stringstream` is the standard and widely accepted $O(N)$ space optimal method in interviews due to its clean logic and safety against edge cases. We will provide the `stringstream` solution as it is most preferred.

**Dry Run (Stringstream):**
`s = "  hello world  "`
- Stream extracts: `hello`
- `result = "hello"`
- Stream extracts: `world`
- `result = "world" + " " + "hello" = "world hello"`
- Trailing space removed safely by structure.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string reverseWords(string s) {
    stringstream ss(s);
    string word;
    string result = "";
    
    // Extract words separated by spaces
    while (ss >> word) {
        if (result.empty()) {
            result = word;
        } else {
            result = word + " " + result;
        }
    }
    
    return result;
}

int main() {
    string s = "  a good   example  ";
    cout << "\"" << reverseWords(s) << "\"" << endl; // Output: "example good a"
    return 0;
}
```

---

## Common Mistakes
- **Handling multiple spaces manually:** Doing `s[i] == ' '` logic without a state machine often leads to missing multiple spaces and having them end up in the output string.
- **Leading/Trailing spaces:** Forgetting to strip these out if parsing manually.

---

## Similar Questions
- Reverse String II
- Rotate String

---

## Interview Tips
- Mention the manual reversal technique (reverse whole string -> reverse individual words -> shift to remove spaces) to show you understand in-place operations, but implement the `stringstream` approach unless the interviewer explicitly demands $O(1)$ space.

---

## Variations Asked
- Preserve the multiple spaces (only reverse the letters of the words).

---

## Pattern Recognition
**Identify this when:** A string needs parsing by delimiters (like spaces). **Stringstream** in C++ or `.split()` in other languages is the fastest way to extract tokens.
