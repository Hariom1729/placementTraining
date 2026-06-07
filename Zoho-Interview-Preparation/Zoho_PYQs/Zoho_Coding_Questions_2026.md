# Zoho Coding Questions - 2026 (Recent Patterns)

## Round 2: Basic Programming

### 1. Count Subarrays with Sum K
**Problem:** Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
**Input:** `[1, 1, 1]`, `k = 2`
**Output:** `2`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    vector<int> nums = {1, 1, 1};
    int k = 2;
    unordered_map<int, int> prefixSum;
    prefixSum[0] = 1;
    int sum = 0, count = 0;
    
    for(int num : nums) {
        sum += num;
        if(prefixSum.find(sum - k) != prefixSum.end()) {
            count += prefixSum[sum - k];
        }
        prefixSum[sum]++;
    }
    cout << count << "\n";
    return 0;
}
```

### 2. First Unique Character in a String
**Problem:** Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.
**Input:** `s = "zohocorporation"`
**Output:** `z` (index 0)
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string s = "zohocorporation";
    vector<int> freq(256, 0);
    
    for(char c : s) freq[c]++;
    
    int index = -1;
    for(int i = 0; i < s.length(); i++) {
        if(freq[s[i]] == 1) {
            index = i;
            break;
        }
    }
    cout << "Index: " << index << "\n";
    return 0;
}
```

## Round 3: Advanced Logic

### 3. Word Break Problem
**Problem:** Given a string `s` and a dictionary of strings `wordDict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.
**Input:** `s = "zohocorp", wordDict = ["zoho", "corp"]`
**Output:** `true`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    string s = "zohocorp";
    unordered_set<string> dict = {"zoho", "corp"};
    vector<bool> dp(s.length() + 1, false);
    dp[0] = true;
    
    for(int i = 1; i <= s.length(); i++) {
        for(int j = 0; j < i; j++) {
            if(dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                dp[i] = true;
                break;
            }
        }
    }
    
    cout << (dp[s.length()] ? "True" : "False") << "\n";
    return 0;
}
```

## Technical Interview Questions
1. Difference between `std::vector` and `std::list`? When to use which?
2. What is virtual memory? Explain paging.
3. What is dependency injection?
