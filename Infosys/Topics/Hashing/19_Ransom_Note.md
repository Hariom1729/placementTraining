# Ransom Note

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Apple

## Topic
Hashing / Strings

## Pattern
Frequency Array Subtraction

## Problem Statement
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

## Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Input
- `ransomNote` string.
- `magazine` string.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

**Example 2:**
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
Explanation: We need two 'a's, but the magazine only has one.
```

**Example 3:**
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Edge Cases
- `ransomNote` is longer than `magazine`. (Immediately return `false` because we obviously don't have enough letters).

## Intuition
This is a resource allocation problem. We have a set of resources (`magazine`), and we have a demand (`ransomNote`).
To solve this, we:
1. Catalog all our resources. We scan `magazine` and count exactly how many of each letter we have using a frequency map / array.
2. We attempt to fulfill the demand. We scan `ransomNote` and for each letter, we deduct it from our resource pool.
3. If our resource pool ever drops below `0` for any letter, it means we don't have enough! Return `false`.
4. If we successfully build the whole note, return `true`.

Since it's only lowercase English letters, a 26-element array `int count[26]` is the best Hash Map representation.

## Brute Force Approach
**Explanation:** For every character in `ransomNote`, scan `magazine` to find it, delete it from `magazine`, and continue.
**Time Complexity:** $O(R \times M)$
**Space Complexity:** $O(M)$ (if creating a copy of the string to delete chars).

## Optimal Approach (Frequency Array)
**Detailed explanation:**
1. If `ransomNote.length() > magazine.length()`, return `false`.
2. Initialize `vector<int> count(26, 0)`.
3. Iterate `c` through `magazine`:
   - `count[c - 'a']++`.
4. Iterate `c` through `ransomNote`:
   - `count[c - 'a']--`.
   - If `count[c - 'a'] < 0`: return `false`.
5. Return `true`.

**Time Complexity:** $O(R + M)$ where $R$ is length of ransom note and $M$ is length of magazine. We scan each string exactly once.
**Space Complexity:** $O(1)$ constant space for the size-26 array.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // Optimization: If the note is longer than the magazine, it's impossible
        if (ransomNote.length() > magazine.length()) {
            return false;
        }
        
        vector<int> letterCounts(26, 0);
        
        // Catalog available resources from the magazine
        for (char c : magazine) {
            letterCounts[c - 'a']++;
        }
        
        // Deduct resources to build the ransom note
        for (char c : ransomNote) {
            letterCounts[c - 'a']--;
            
            // If we ran out of a required letter
            if (letterCounts[c - 'a'] < 0) {
                return false;
            }
        }
        
        return true;
    }
};
```

## Dry Run
`ransomNote = "aa", magazine = "aab"`
- Lengths check: `2 > 3` is false.
- Catalog `magazine`: `letterCounts['a'] = 2`, `letterCounts['b'] = 1`.
- Fulfill `ransomNote`:
  - `c='a'`: `letterCounts['a']--` -> `1`. Not `< 0`.
  - `c='a'`: `letterCounts['a']--` -> `0`. Not `< 0`.
- Loop finishes. Return `true`.

## Common Mistakes
- **Iterating the map at the end:** Some candidates count characters for both strings into two separate maps `mapR` and `mapM`, and then loop `for (int i=0; i<26; i++) { if (mapR[i] > mapM[i]) return false; }`. This works but requires 3 passes. Fulfilling the demand on the fly by decrementing one map is much cleaner and fails faster (short-circuit evaluation).

## Similar Problems
- Valid Anagram
- Find the Difference
