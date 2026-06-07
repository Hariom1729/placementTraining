# Problem 2: Find Highest and Lowest Frequency Elements

## Problem Statement
Given an array `arr` of size `N`, find the elements that have the highest and lowest frequencies. 
If there are multiple elements with the same frequency, return the element with the smaller value.

## Input Format
- An array of integers `arr`.

## Output Format
- A pair of integers: `[highest_frequency_element, lowest_frequency_element]`.

## Constraints
- `1 <= N <= 10^5`
- `1 <= arr[i] <= 10^9`

---

## Approach

1. **Count Frequencies:** Use an `unordered_map<int, int>` to count the occurrences of each element, just like the previous problem.
2. **Find Min/Max:** Iterate through the map.
   - Keep track of `maxFreq`, `minFreq`, `maxEle`, and `minEle`.
   - Initialize `maxFreq = 0` and `minFreq = INT_MAX`.
   - For each `(element, count)` pair in the map:
     - If `count > maxFreq`, update `maxFreq` and `maxEle`. If `count == maxFreq`, update `maxEle` to be the smaller of the two elements.
     - If `count < minFreq`, update `minFreq` and `minEle`. If `count == minFreq`, update `minEle` to be the smaller of the two elements.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>
#include <algorithm>
using namespace std;

class Solution {
public:
    pair<int, int> highestAndLowestFrequency(vector<int>& arr) {
        unordered_map<int, int> freqMap;
        for (int x : arr) {
            freqMap[x]++;
        }
        
        int maxFreq = 0, minFreq = INT_MAX;
        int maxEle = -1, minEle = -1;
        
        for (auto it : freqMap) {
            int element = it.first;
            int count = it.second;
            
            // Handle Highest Frequency
            if (count > maxFreq) {
                maxFreq = count;
                maxEle = element;
            } else if (count == maxFreq) {
                maxEle = min(maxEle, element); // Tie-breaker
            }
            
            // Handle Lowest Frequency
            if (count < minFreq) {
                minFreq = count;
                minEle = element;
            } else if (count == minFreq) {
                minEle = min(minEle, element); // Tie-breaker
            }
        }
        
        return {maxEle, minEle};
    }
};

int main() {
    Solution sol;
    vector<int> arr = {10, 5, 10, 15, 10, 5};
    pair<int, int> res = sol.highestAndLowestFrequency(arr);
    
    cout << "Highest Freq Element: " << res.first << endl; // Expected: 10
    cout << "Lowest Freq Element: " << res.second << endl; // Expected: 15
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the array once to build the map, and then iterate through the map (which has at most `N` elements) once.
- **Space Complexity:** `O(N)` to store the frequencies in the hash map.
