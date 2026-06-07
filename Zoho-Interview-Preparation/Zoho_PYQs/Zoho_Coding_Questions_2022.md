# Zoho Coding Questions - 2022

## Round 2: Basic Programming

### 1. Alternate Sorting in O(N) Time
**Problem:** Given an unsorted array, sort it such that the first element is the largest, second is smallest, third is second largest, etc.
**Input:** `[1, 7, 3, 4, 9, 2]`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> arr = {1, 7, 3, 4, 9, 2};
    sort(arr.begin(), arr.end()); // Zoho expects custom merge sort usually
    
    int left = 0, right = arr.size() - 1;
    bool maxFlag = true;
    while(left <= right) {
        if(maxFlag) cout << arr[right--] << " ";
        else cout << arr[left++] << " ";
        maxFlag = !maxFlag;
    }
    return 0;
}
```

### 2. Print Pattern (X Shape)
**Problem:** Print a string of odd length in an 'X' format.
**Input:** `12345`
**Output:**
```text
1   5
 2 4
  3
 2 4
1   5
```
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    string s = "12345";
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j || i + j == n - 1) cout << s[j];
            else cout << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

## Round 3: Advanced Logic

### 3. Grandchildren Count
**Problem:** Given a 2D array of `[child, father]`, and a name, find the number of grandchildren that person has.
**Input:** `[["luke", "shaw"], ["wayne", "rooney"], ["rooney", "ronaldo"], ["shaw", "rooney"]]`, Target: `"rooney"`
**Output:** 2 (luke and shaw's children, wait: rooney's children are wayne and shaw. Shaw's child is luke. Wayne has no children. Total grandchildren = 1 (luke)).
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    vector<pair<string, string>> relations = {
        {"luke", "shaw"}, {"wayne", "rooney"}, 
        {"rooney", "ronaldo"}, {"shaw", "rooney"}
    };
    string target = "rooney";
    
    unordered_map<string, vector<string>> childrenMap;
    for(auto& p : relations) {
        childrenMap[p.second].push_back(p.first); // father -> children
    }
    
    int grandChildrenCount = 0;
    if(childrenMap.find(target) != childrenMap.end()) {
        for(string child : childrenMap[target]) {
            if(childrenMap.find(child) != childrenMap.end()) {
                grandChildrenCount += childrenMap[child].size();
            }
        }
    }
    
    cout << "Grandchildren of " << target << ": " << grandChildrenCount << "\n";
    return 0;
}
```

## Technical Interview Questions
1. How does a HashMap resolve collisions internally?
2. What happens if you don't define a virtual destructor in a base class?
3. How is encapsulation different from abstraction? Give a real-world example.
