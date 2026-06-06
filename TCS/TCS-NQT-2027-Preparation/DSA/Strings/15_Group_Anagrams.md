# Problem 15: Group Anagrams

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input Format
- An array of strings `strs`.

## Output Format
- A list of lists of strings, where each sub-list contains words that are anagrams of each other.

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Approach

To group anagrams, we need a unique "key" that is identical for all strings that are anagrams of each other.

**Approach: Sorting String**
1. For every string, sort it.
2. The sorted string is the key. Example: "eat", "tea", and "ate" all sort to "aet".
3. Use an `unordered_map<string, vector<string>>` where the key is the sorted string ("aet") and the value is a vector of the original strings.
4. Iterate through the map and push the vectors into the result.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        
        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            map[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : map) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> res = sol.groupAnagrams(strs);
    
    for (const auto& group : res) {
        cout << "[ ";
        for (const string& word : group) {
            cout << word << " ";
        }
        cout << "]\n";
    }
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * K log K)` where `N` is the number of strings and `K` is the maximum length of a string in `strs`. Sorting each string takes `O(K log K)`.
- **Space Complexity:** `O(N * K)`. The unordered_map stores all strings, taking `O(N * K)` space.
