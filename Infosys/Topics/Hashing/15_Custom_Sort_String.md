# Custom Sort String

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Amazon, Apple

## Topic
Hashing / Strings / Sorting

## Pattern
Custom Comparator / Frequency Map

## Problem Statement
You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.
Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return any permutation of `s` that satisfies this property.

## Constraints
- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All the characters of `order` are **unique**.

## Input
- `order` string.
- `s` string.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

**Example 2:**
```
Input: order = "cbafg", s = "abcd"
Output: "cbad"
```

## Edge Cases
- `s` contains characters that are not in `order`. (Just append them to the end).
- `s` is empty (Not possible per constraints).

## Intuition
There are two beautiful ways to solve this.
**Approach 1: Frequency Map.**
Count the frequency of all characters in `s` using an array `count[26]`.
Then, iterate through `order`. For each character, check its frequency in `s`, and append it to our result string that many times! After doing this, we have exhausted all characters from `s` that were in `order`.
Finally, iterate through the `count` array and append whatever is left (characters in `s` but not in `order`). This is wildly fast $O(N)$.

**Approach 2: Custom Sorting.**
Use `std::sort` with a custom lambda! 
We assign a "weight" or "priority" to each character based on its index in `order`. If a character isn't in `order`, its priority is 27.
Then, `sort` just compares the priorities of characters!

Let's write the **Frequency Map** solution, as it is $O(N)$ instead of $O(N \log N)$ and truly demonstrates Hashing.

## Brute Force Approach
N/A - Standard sorting without weights doesn't work.

## Optimal Approach (Frequency Map)
**Detailed explanation:**
1. Create `vector<int> count(26, 0)`.
2. Iterate through `s` and populate frequencies: `count[c - 'a']++`.
3. Create `string result = ""`.
4. Iterate through `char c` in `order`:
   - If `count[c - 'a'] > 0`:
     - Append `c` to `result` exactly `count[c - 'a']` times.
     - Reset `count[c - 'a'] = 0`.
5. Iterate through `char c` from `'a'` to `'z'`:
   - If `count[c - 'a'] > 0`:
     - Append `c` to `result` exactly `count[c - 'a']` times.
6. Return `result`.

**Time Complexity:** $O(N)$ where $N$ is the length of `s`. We scan `s`, then scan `order` (up to 26), then scan the alphabet (26). Extremely fast.
**Space Complexity:** $O(1)$ constant space (26-element array).

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> count(26, 0);
        
        // Count frequencies of characters in s
        for (char c : s) {
            count[c - 'a']++;
        }
        
        string result = "";
        
        // 1. Append characters that exist in 'order' following the custom order
        for (char c : order) {
            while (count[c - 'a'] > 0) {
                result += c;
                count[c - 'a']--;
            }
        }
        
        // 2. Append the remaining characters that were NOT in 'order'
        for (int i = 0; i < 26; i++) {
            while (count[i] > 0) {
                result += (char)(i + 'a');
                count[i]--;
            }
        }
        
        return result;
    }
};
```

## Dry Run
`order = "cba", s = "abcd"`
- `count` map: `'a':1, 'b':1, 'c':1, 'd':1`.
- Iterate `order`:
  - `c='c'`: count is 1. `result = "c"`. count is 0.
  - `c='b'`: count is 1. `result = "cb"`. count is 0.
  - `c='a'`: count is 1. `result = "cba"`. count is 0.
- Iterate alphabet:
  - `i=0` to `2`: counts are 0.
  - `i=3 ('d')`: count is 1. `result = "cbad"`. count is 0.
- Return `"cbad"`.

## Common Mistakes
- **Trying to physically swap elements in `s`:** Trying to write your own bubbling logic to reorder characters based on `order.find(c)` will quickly result in spaghetti code and infinite loops. Rebuilding the string from scratch using a frequency map is vastly cleaner.

## Similar Problems
- Sort Characters By Frequency
- Top K Frequent Elements
