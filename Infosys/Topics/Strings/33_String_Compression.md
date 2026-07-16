# String Compression

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Google, Bloomberg

## Topic
Strings / Two Pointers

## Pattern
In-Place Array Modification

## Problem Statement
Given an array of characters `chars`, compress it using the following algorithm:
Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
- If the group's length is 1, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.
After you are done **modifying the input array**, return the new length of the array.
You must write an algorithm that uses only constant extra space.

## Constraints
- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.

## Input
- `chars` vector of characters.

## Output
- Return an integer (new length). (The array must be modified in place).

## Sample Test Cases

**Example 1:**
```
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

**Example 2:**
```
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
```

**Example 3:**
```
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

## Edge Cases
- Array length 1.
- Counts > 9 (need to split into `"1"`, `"2"`).

## Intuition
Since we must modify the array **in-place** with $O(1)$ space, we can use a standard read/write pointer approach.
- `read` pointer: Iterates through the array to find groups of repeating characters.
- `write` pointer: Keeps track of where we should write the next compressed output in the array.

Because compression ALWAYS makes the array smaller or keeps it the same size, the `write` pointer will never overtake the `read` pointer. This guarantees we won't accidentally overwrite data we haven't read yet!
When we find a group of identical characters, we count them. We write the character itself using `write++`. If the count is $>1$, we convert the count to a string, and write each digit of the string using `write++`.

## Brute Force Approach
N/A - This is an implementation problem.

## Optimal Approach (Two Pointers Read/Write)
**Detailed explanation:**
1. Initialize `read = 0` and `write = 0`.
2. Loop while `read < chars.length()`:
   - Mark the start of the current group: `int start = read`.
   - Iterate `read` forward as long as `chars[read] == chars[start]`.
   - The count of characters is `read - start`.
   - Write the character to the array: `chars[write++] = chars[start]`.
   - If `count > 1`:
     - Convert count to a string: `string s = to_string(count)`.
     - Iterate through the characters in the string and write them:
       `for (char c : s) { chars[write++] = c; }`
3. Return `write` (which is exactly the new length of the valid array).

**Time Complexity:** $O(N)$ because the `read` pointer traverses the array exactly once, and inner loops just move `read` forward.
**Space Complexity:** $O(1)$ constant extra space.

## C++ Solution

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int read = 0;
        int write = 0;
        int n = chars.size();
        
        while (read < n) {
            int start = read;
            
            // Advance read pointer to find the end of the current group
            while (read < n && chars[read] == chars[start]) {
                read++;
            }
            
            int count = read - start;
            
            // Write the character
            chars[write] = chars[start];
            write++;
            
            // If count > 1, write the count as characters
            if (count > 1) {
                string countStr = to_string(count);
                for (char c : countStr) {
                    chars[write] = c;
                    write++;
                }
            }
        }
        
        return write;
    }
};
```

## Dry Run
`chars = ["a","a","b","b","c","c","c"]`
- `read = 0, write = 0`.
- Loop 1: `start=0 ('a')`. `read` moves to 2. `count = 2`.
  - Write `'a'` at index 0. `write = 1`.
  - Count > 1. Write `'2'` at index 1. `write = 2`.
  - Array state: `["a", "2", "b", "b", "c", "c", "c"]`
- Loop 2: `start=2 ('b')`. `read` moves to 4. `count = 2`.
  - Write `'b'` at index 2. `write = 3`.
  - Write `'2'` at index 3. `write = 4`.
  - Array state: `["a", "2", "b", "2", "c", "c", "c"]`
- Loop 3: `start=4 ('c')`. `read` moves to 7 (end). `count = 3`.
  - Write `'c'` at index 4. `write = 5`.
  - Write `'3'` at index 5. `write = 6`.
- Return `write = 6`.

## Common Mistakes
- **Creating a new array:** Returning `result.size()` after pushing to a new `vector<char> result` violates the $O(1)$ space requirement. You must overwrite `chars`.
- **Handling counts >= 10 poorly:** Writing `chars[write++] = count + '0'` works for numbers 2-9, but turns 12 into an invalid ASCII symbol. Using `to_string(count)` safely breaks numbers into multiple single-digit characters.

## Similar Problems
- Count and Say
- Encode and Decode Strings
