# Word Pattern

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Hashing / Strings

## Pattern
Bi-directional Mapping (Char to Word)

## Problem Statement
Given a `pattern` and a string `s`, find if `s` follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

## Constraints
- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

## Input
- `pattern` string.
- `s` string (sentence).

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation: 'a' maps to "dog", 'b' maps to "cat". Everything aligns.
```

**Example 2:**
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Explanation: The second 'a' should map to "dog", but it sees "fish".
```

**Example 3:**
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Explanation: 'a' maps to "dog". But then it sees "cat".
```

**Example 4:**
```
Input: pattern = "abba", s = "dog dog dog dog"
Output: false
Explanation: 'a' maps to "dog". Then 'b' maps to "dog". INVALID! Bi-jection means 'b' cannot map to "dog" because 'a' already claimed it!
```

## Edge Cases
- `pattern.length` does not match the number of words in `s`. (Immediately return `false`).

## Intuition
This problem is exactly the same as **Isomorphic Strings**, except instead of mapping `Char -> Char`, we are mapping `Char -> Word`!
Because we need Bi-directional mapping (bijection), we must ensure:
1. `pattern[i]` maps to a specific `word`.
2. That specific `word` maps back strictly to `pattern[i]`.

First, we use a `stringstream` to easily extract all words from `s` into a `vector<string> words`.
If the length of `pattern` does not match the size of `words`, they obviously don't match, return `false`.
Next, we maintain two Hash Maps:
- `unordered_map<char, string> charToWord`
- `unordered_map<string, char> wordToChar`

We loop through `pattern` and `words` simultaneously and apply the exact same collision checks we used in Isomorphic Strings!

## Brute Force Approach
N/A - Parsing algorithm required.

## Optimal Approach (Two Hash Maps + Stringstream)
**Detailed explanation:**
1. Extract words from `s` using `stringstream ss(s)`. Push to a `vector<string> words`.
2. If `pattern.length() != words.size()`, return `false`.
3. Create `unordered_map<char, string> c2w` and `unordered_map<string, char> w2c`.
4. Loop `i` from `0` to `pattern.length() - 1`:
   - `char c = pattern[i]`, `string w = words[i]`.
   - If `c2w.count(c)` and `c2w[c] != w`: return `false`.
   - If `w2c.count(w)` and `w2c[w] != c`: return `false`.
   - `c2w[c] = w` and `w2c[w] = c`.
5. Return `true`.

**Time Complexity:** $O(N + M)$ where $N$ is length of pattern and $M$ is length of $s$ (for stringstream parsing). Hashing string lookups take proportional time to string lengths.
**Space Complexity:** $O(M)$ to store the array of words and hash maps.

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        stringstream ss(s);
        string word;
        
        // Extract all words from the sentence
        while (ss >> word) {
            words.push_back(word);
        }
        
        // If the number of characters doesn't match the number of words
        if (pattern.length() != words.size()) {
            return false;
        }
        
        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;
        
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern[i];
            string w = words[i];
            
            // If character is already mapped to a different word
            if (charToWord.count(c) && charToWord[c] != w) {
                return false;
            }
            
            // If word is already claimed by a different character
            if (wordToChar.count(w) && wordToChar[w] != c) {
                return false;
            }
            
            // Establish the bijection mapping
            charToWord[c] = w;
            wordToChar[w] = c;
        }
        
        return true;
    }
};
```

## Dry Run
`pattern = "abba", s = "dog dog dog dog"`
- `words = ["dog", "dog", "dog", "dog"]`. Lengths match (4).
- `i=0`: `c='a'`, `w="dog"`. Map empty. `c2w['a']="dog"`, `w2c["dog"]='a'`.
- `i=1`: `c='b'`, `w="dog"`. `c2w['b']` empty. `w2c["dog"]` exists! It is `'a'`. 
  - `'a' != 'b'`. Collision! Return `false`.

## Common Mistakes
- **Forgetting to check the sizes:** If you don't check `pattern.length() == words.size()`, your loop will likely cause an index-out-of-bounds exception when accessing `words[i]`.
- **Manually parsing spaces:** Similar to `Reverse Words in a String`, attempting to manually loop and slice substrings looking for `' '` is incredibly error-prone compared to the 3 lines of code using `stringstream`.

## Similar Problems
- Isomorphic Strings
- Group Anagrams
