# Problem 7: Group Anagrams

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Input Format
- An array of strings `strs`.

## Output Format
- A 2D array (vector of vector of strings) containing the grouped anagrams.

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Approach: Sorting String as Key

We need a way to identify if two strings are anagrams of each other. The easiest way is to realize that if you sort two anagram strings, they become exactly identical. For example, "eat", "tea", and "ate" all become "aet" after sorting.

1. Create an `unordered_map<string, vector<string>> map`. The key will be the sorted version of the string, and the value will be a list of all original strings that map to that sorted version.
2. Iterate through each string `s` in `strs`.
3. Create a copy of `s` and sort it. Let's call it `sorted_s`.
4. Add the original string `s` to the list mapped by `sorted_s`: `map[sorted_s].push_back(s)`.
5. After the loop, extract all the lists from the map and return them as a 2D array.

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
        
        for (const string& s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            map[sorted_s].push_back(s);
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
    
    for (auto& group : res) {
        cout << "[ ";
        for (string s : group) {
            cout << s << " ";
        }
        cout << "]\n";
    }
    // Expected output groups: ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * K log K)` where `N` is the number of strings and `K` is the maximum length of a string. For each of the `N` strings, we sort it which takes `O(K log K)`.
- **Space Complexity:** `O(N * K)`. We store all strings inside the unordered_map.
