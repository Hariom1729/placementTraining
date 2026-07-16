# Group Anagrams

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, Facebook, Google

## Topic
Strings / Hash Table

## Pattern
Sorting & Hashing

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Input
- `strs` vector of strings.

## Output
- Return a vector of vector of strings.

## Sample Test Cases

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

## Edge Cases
- All words are anagrams of each other.
- No words are anagrams of each other.
- Array contains empty strings (valid, they should be grouped together).

## Intuition
The core property of anagrams is that **when sorted, all anagrams of a word become identical**.
For example, `"eat"`, `"tea"`, and `"ate"` all become `"aet"` when sorted alphabetically.
This gives us a perfect **key** to use in a Hash Map!
We can map each sorted string to a list of its original strings: `unordered_map<string, vector<string>>`.
Iterate through the array. For each word, sort a copy of it, and use the sorted version as the key to push the original word into the map.
At the end, simply extract all the values from the map into a 2D vector.

*Optimization:* Sorting each string takes $O(K \log K)$ where $K$ is the length of the string. Since $K \le 100$, this is extremely fast. However, if $K$ was huge, we could create a frequency array `[0,0,1,0...]` and convert it to a string `"0#0#1..."` to use as the key, achieving $O(K)$ per word instead of $O(K \log K)$. For typical interviews, the sorting method is fully expected and accepted.

## Brute Force Approach
**Explanation:** For every string, compare it against every other string using a `isValidAnagram()` function. Group them and mark them as visited.
**Time Complexity:** $O(N^2 \times K)$ where $N$ is number of strings, $K$ is string length.
**Space Complexity:** $O(N)$ for visited array.

## Optimal Approach (Sorting & Hashing)
**Detailed explanation:**
1. Create an `unordered_map<string, vector<string>> mp`.
2. Iterate through each string `s` in `strs`:
   - Create a copy `string key = s`.
   - `sort(key.begin(), key.end())`.
   - Push the original string into the map: `mp[key].push_back(s)`.
3. Create a result `vector<vector<string>> ans`.
4. Iterate through the map `for (auto it : mp)` and push `it.second` into `ans`.
5. Return `ans`.

**Time Complexity:** $O(N \times K \log K)$ where $N$ is the number of strings and $K$ is the maximum length of a string.
**Space Complexity:** $O(N \times K)$ to store the grouped strings in the map.

## C++ Solution

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        // Group strings by their sorted version
        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            mp[key].push_back(s);
        }
        
        // Extract the grouped anagrams
        vector<vector<string>> ans;
        for (auto it : mp) {
            ans.push_back(it.second);
        }
        
        return ans;
    }
};
```

## Optimal Approach 2 (Frequency Hashing - $O(N \times K)$)
*(Use this only if the interviewer asks to optimize the $K \log K$ sorting step).*
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for (string s : strs) {
            string key = "";
            vector<int> count(26, 0);
            
            // Count frequencies
            for (char c : s) {
                count[c - 'a']++;
            }
            
            // Build key like "1#0#2#..."
            for (int i = 0; i < 26; i++) {
                key += to_string(count[i]) + "#";
            }
            
            mp[key].push_back(s);
        }
        
        vector<vector<string>> ans;
        for (auto it : mp) {
            ans.push_back(it.second);
        }
        return ans;
    }
};
```

## Dry Run
`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- `s = "eat"`: key = `"aet"`. `mp["aet"] = ["eat"]`
- `s = "tea"`: key = `"aet"`. `mp["aet"] = ["eat", "tea"]`
- `s = "tan"`: key = `"ant"`. `mp["ant"] = ["tan"]`
- `s = "ate"`: key = `"aet"`. `mp["aet"] = ["eat", "tea", "ate"]`
- `s = "nat"`: key = `"ant"`. `mp["ant"] = ["tan", "nat"]`
- `s = "bat"`: key = `"abt"`. `mp["abt"] = ["bat"]`

Iterate over map and build `ans`:
`[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## Common Mistakes
- **Passing the string by reference in the loop:** If you use `for(string& s : strs)` and then `sort(s.begin(), s.end())`, you actually mutate the original array! You want to return the original words, not the sorted ones. Always sort a **copy** of the word.
- **Worrying about return order:** The problem states "You can return the answer in any order." This means the unpredictable iteration order of `unordered_map` is completely fine. Don't waste time sorting the final result.

## Similar Problems
- Valid Anagram
- Find All Anagrams in a String
