# Isomorphic Strings

## Difficulty
Easy

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: LinkedIn, Amazon, Google

## Topic
Hashing / Strings

## Pattern
Bi-directional Mapping

## Problem Statement
Given two strings `s` and `t`, determine if they are isomorphic.
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order of characters. **No two characters may map to the same character**, but a character may map to itself.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

## Input
- `s` string.
- `t` string.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
Explanation: 'e' maps to 'a', 'g' maps to 'd'. It perfectly transforms "egg" to "add".
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
Explanation: 'f' maps to 'b', 'o' maps to 'a'. But then the second 'o' must ALSO map to 'a', yielding "baa". It doesn't match "bar".
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
```

**Example 4:**
```
Input: s = "badc", t = "baba"
Output: false
Explanation: 'b' maps to 'b'. 'a' maps to 'a'. 'd' maps to 'b'. BUT 'b' is already mapped TO! (No two characters may map to the same character).
```

## Edge Cases
- Invalid strings lengths (not possible given constraints `s.length == t.length`).
- Characters mapped to themselves.

## Intuition
We need to create a dictionary/map connecting characters from `s` to characters from `t`.
Every time we read a character `s[i]`, we check:
1. Have we seen `s[i]` before? If yes, it MUST be mapped to the exact same character `t[i]` that it was mapped to previously! If it's mapped to something else, return `false`!
2. If we haven't seen `s[i]` before, we create a new mapping `mapS[s[i]] = t[i]`.

BUT WAIT! There's a catch (Example 4). "No two characters may map to the same character".
If we map `'d'` to `'b'`, we must ensure that NO OTHER character has already claimed `'b'` as its target!
This means we need a **Bi-directional mapping**. We need to ensure `s[i]` strictly points to `t[i]`, AND `t[i]` strictly points to `s[i]`.
We can use two `vector<int>` of size 256 (to handle all ASCII characters).
`mapS` tracks what `s[i]` points to.
`mapT` tracks what `t[i]` points to.

## Brute Force Approach
N/A - Parsing algorithm required.

## Optimal Approach (Two ASCII Hash Maps)
**Detailed explanation:**
1. Create two integer arrays `mapS` and `mapT` of size 256, initialized to `-1` (or `0` if using a 1-based index trick).
2. Loop `i` from `0` to `s.length() - 1`:
   - `char c1 = s[i]`, `char c2 = t[i]`.
   - If `mapS[c1] != -1` AND `mapS[c1] != c2`: return `false`. (c1 already mapped to something else).
   - If `mapT[c2] != -1` AND `mapT[c2] != c1`: return `false`. (c2 already mapped FROM something else).
   - Establish the mapping: `mapS[c1] = c2` and `mapT[c2] = c1`.
3. Return `true`.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;
        
        // 256 covers all ASCII characters. Initialize with -1.
        vector<int> mapS(256, -1);
        vector<int> mapT(256, -1);
        
        for (int i = 0; i < s.length(); i++) {
            char c1 = s[i];
            char c2 = t[i];
            
            // Check if c1 has been mapped to a different character
            if (mapS[c1] != -1 && mapS[c1] != c2) {
                return false;
            }
            
            // Check if c2 has been claimed by a different character
            if (mapT[c2] != -1 && mapT[c2] != c1) {
                return false;
            }
            
            // Create the bi-directional mapping
            mapS[c1] = c2;
            mapT[c2] = c1;
        }
        
        return true;
    }
};
```

## Dry Run
`s = "foo", t = "bar"`
- `i=0`: `s='f'`, `t='b'`. MapS['f']=-1, MapT['b']=-1. Set `MapS['f']='b'`, `MapT['b']='f'`.
- `i=1`: `s='o'`, `t='a'`. MapS['o']=-1, MapT['a']=-1. Set `MapS['o']='a'`, `MapT['a']='o'`.
- `i=2`: `s='o'`, `t='r'`. MapS['o'] is `'a'`. But `t` is `'r'`. `'a' != 'r'`.
  - Collision! Return `false`.

`s = "badc", t = "baba"`
- `i=0`: `s='b'`, `t='b'`. MapS['b']='b', MapT['b']='b'.
- `i=1`: `s='a'`, `t='a'`. MapS['a']='a', MapT['a']='a'.
- `i=2`: `s='d'`, `t='b'`. MapS['d']=-1. MapT['b'] is `'b'`. But `c1` is `'d'`. `'b' != 'd'`.
  - Collision! Return `false`.

## Common Mistakes
- **Using only ONE map:** If you only track `mapS[s[i]] = t[i]`, you will fail Example 4 where multiple characters map to the same target character. You MUST ensure 1-to-1 mapping via bi-directional checks.

## Similar Problems
- Word Pattern
- Valid Anagram
