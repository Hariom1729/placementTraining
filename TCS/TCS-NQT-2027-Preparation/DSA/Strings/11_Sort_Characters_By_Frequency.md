# Problem 11: Sort Characters By Frequency

## Problem Statement
Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

## Input Format
- A single string `s`.

## Output Format
- A string representing the sorted order.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.

---

## Approach

This problem can be solved effectively using a **Priority Queue (Max-Heap)** or **Bucket Sort**. Let's use Bucket Sort for better average performance.
1. Use an `unordered_map` to count the frequency of each character.
2. Create a vector of strings (buckets). The index of the vector will represent the frequency. Since the maximum frequency is the length of the string, the array size will be `s.length() + 1`.
3. Iterate through the map and append `char_count` copies of the character to the string in the corresponding bucket.
4. Iterate through the buckets array from the end (highest frequency) to the beginning.
5. For each bucket, append its string to the final result string.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count character frequencies
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Step 2: Create buckets based on frequency
        // buckets[i] will store a string of characters that appear exactly i times
        vector<string> buckets(s.length() + 1, "");
        for (auto& pair : freq) {
            char c = pair.first;
            int count = pair.second;
            buckets[count].append(count, c);
        }
        
        // Step 3: Build the result string from highest frequency to lowest
        string result = "";
        for (int i = s.length(); i > 0; i--) {
            if (!buckets[i].empty()) {
                result += buckets[i];
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.frequencySort("tree") << endl;   // Expected: "eert" or "eetr"
    cout << sol.frequencySort("cccaaa") << endl; // Expected: "cccaaa" or "aaaccc"
    cout << sol.frequencySort("Aabb") << endl;   // Expected: "bbAa" or "bbaA"
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. Counting takes `O(N)`. Populating buckets takes `O(U)` where `U` is unique characters. Building the string takes `O(N)`.
- **Space Complexity:** `O(N)`. The map stores unique characters `O(U)`, the buckets vector is size `O(N)`, and the result string takes `O(N)` space.
