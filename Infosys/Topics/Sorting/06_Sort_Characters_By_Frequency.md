# Sort Characters By Frequency

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Bloomberg

## Topic
Sorting / Hashing / Strings

## Pattern
Bucket Sort / Max-Heap

## Problem Statement
Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.

## Input
- `s` string.

## Output
- Return a string.

## Sample Test Cases

**Example 1:**
```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**
```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**
```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

## Edge Cases
- All characters have the same frequency (return original string).
- String is very large (requires $O(N)$ time).

## Intuition
This problem is almost identical to **Top K Frequent Elements**.
We need to:
1. Count the frequencies of all characters in the string.
2. Sort the characters based on their frequency in descending order.
3. Build the final string by appending the character $F$ times (where $F$ is its frequency).

Because `s` can be up to $5 \times 10^5$ characters long, counting frequencies takes $O(N)$.
We *could* sort the map elements using a custom comparator, which takes $O(U \log U)$ where $U$ is the number of unique characters. Since $U \le 62$ (26 lower + 26 upper + 10 digits), sorting $U$ elements takes essentially $O(1)$ time! So simple sorting is $O(N + U \log U) = O(N)$.

Alternatively, we can use **Bucket Sort**. We create an array of "buckets" where the index is the frequency. Since the maximum possible frequency is $N$, we can have an array of size $N+1$. We dump the characters into their respective frequency buckets, scan backwards, and append!

## Optimal Approach (Bucket Sort)
**Detailed explanation:**
1. Create `unordered_map<char, int> countMap` and count frequencies of `s`.
2. Create `vector<vector<char>> buckets(s.length() + 1)`.
3. Iterate through `countMap`:
   - Push the `char` into the bucket at index `frequency`: `buckets[freq].push_back(c)`.
4. Create `string result = ""`.
5. Iterate `i` from `s.length()` down to `1`:
   - For every character in `buckets[i]`:
     - We append that character to `result` exactly `i` times! (Since `i` is the frequency).
6. Return `result`.

**Time Complexity:** $O(N)$ to count, $O(N)$ to bucket, $O(N)$ to build result. Overall $O(N)$.
**Space Complexity:** $O(N)$ for buckets and the resulting string.

## C++ Solution (Bucket Sort - O(N))

```cpp
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count frequencies
        unordered_map<char, int> countMap;
        for (char c : s) {
            countMap[c]++;
        }
        
        // Step 2: Bucket Sort. Index = Frequency
        vector<vector<char>> buckets(s.length() + 1);
        for (auto it : countMap) {
            char c = it.first;
            int freq = it.second;
            buckets[freq].push_back(c);
        }
        
        // Step 3: Build the string backwards (Highest freq first)
        string result = "";
        for (int freq = buckets.size() - 1; freq > 0; freq--) {
            for (char c : buckets[freq]) {
                // Append the character 'freq' times
                result.append(freq, c);
            }
        }
        
        return result;
    }
};
```

## Dry Run
`s = "tree"`
- `countMap = {'t':1, 'r':1, 'e':2}`.
- `buckets` array of size 5:
  - `buckets[1] = ['t', 'r']`
  - `buckets[2] = ['e']`
- Scan backwards:
  - `freq=4..3`: empty.
  - `freq=2`: found `'e'`. Append `'e'` 2 times. `result = "ee"`.
  - `freq=1`: found `'t', 'r'`. 
    - Append `'t'` 1 time. `result = "eet"`.
    - Append `'r'` 1 time. `result = "eetr"`.
- Return `"eetr"`.

## Common Mistakes
- **Sorting the string natively:** `sort(s.begin(), s.end())` sorts by alphabetical order, not by frequency. You MUST use an intermediate data structure to capture frequencies.

## Similar Problems
- Top K Frequent Elements
- Custom Sort String
