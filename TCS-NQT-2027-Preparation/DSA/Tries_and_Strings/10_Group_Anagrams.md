# Problem 10: Group Anagrams

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Approach: Hash Map with Sorted String as Key

Two strings are anagrams if and only if their sorted strings are exactly the same.
For example, sorting "eat", "tea", and "ate" all result in "aet".

1. Create a hash map where the key is a string and the value is a vector of strings (`unordered_map<string, vector<string>>`).
2. Iterate through each string in `strs`.
3. Make a copy of the current string and sort it.
4. Use the sorted string as the key in the hash map, and push the original string into the vector associated with that key.
5. After iterating through all strings, extract all the vectors from the hash map values and return them as a 2D array.

*(Optimization: Instead of sorting `O(K \log K)`, you can count the character frequencies and use a string representation of the frequency array as the key, e.g., "1#0#0...#1", taking `O(K)` time).*

---

## C++ Solution (Sorted Key)

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
            sort(key.begin(), key.end()); // Sort the string to form the key
            
            map[key].push_back(s); // Group the original string
        }
        
        vector<vector<string>> result;
        for (auto it = map.begin(); it != map.end(); it++) {
            result.push_back(it->second);
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    
    vector<vector<string>> grouped = sol.groupAnagrams(strs);
    
    cout << "Grouped Anagrams: " << endl;
    for (int i = 0; i < grouped.size(); i++) {
        cout << "[ ";
        for (int j = 0; j < grouped[i].size(); j++) {
            cout << grouped[i][j] << " ";
        }
        cout << "]" << endl;
    }
    // Expected output structure (order may vary):
    // [ bat ]
    // [ tan nat ]
    // [ eat tea ate ]

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * K \log K)` where `N` is the number of strings and `K` is the maximum length of a string in `strs` (due to sorting).
- **Space Complexity:** `O(N * K)` to store the hash map and the resulting grouped array.
