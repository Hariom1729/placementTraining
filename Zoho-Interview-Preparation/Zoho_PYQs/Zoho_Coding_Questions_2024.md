# Zoho Coding Questions - 2024

## Round 2: Basic Programming

### 1. Sliding Window Maximum
**Problem:** Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.
**Input:** `arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], K = 3`
**Output:** `3 3 4 5 5 5 6`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    vector<int> arr = {1, 2, 3, 1, 4, 5, 2, 3, 6};
    int k = 3;
    deque<int> dq;
    
    for(int i = 0; i < arr.size(); i++) {
        if(!dq.empty() && dq.front() == i - k) dq.pop_front();
        while(!dq.empty() && arr[dq.back()] <= arr[i]) dq.pop_back();
        dq.push_back(i);
        if(i >= k - 1) cout << arr[dq.front()] << " ";
    }
    return 0;
}
```

### 2. Add Two Numbers represented as Arrays
**Problem:** Two arrays represent two large numbers. Add them and return the sum as an array.
**Input:** `a = [9, 2, 8, 1, 3, 5], b = [9, 1, 4]`
**Output:** `[9, 2, 9, 0, 4, 9]`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> a = {9, 2, 8, 1, 3, 5};
    vector<int> b = {9, 1, 4};
    vector<int> res;
    
    int i = a.size() - 1, j = b.size() - 1;
    int carry = 0;
    
    while(i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if(i >= 0) sum += a[i--];
        if(j >= 0) sum += b[j--];
        res.push_back(sum % 10);
        carry = sum / 10;
    }
    
    reverse(res.begin(), res.end());
    for(int val : res) cout << val << " ";
    return 0;
}
```

## Round 3: Advanced Logic

### 3. Distinct Substrings with Constraints
**Problem:** Find the longest substring with at most K distinct characters.
**Input:** `s = "eceba", k = 2`
**Output:** `3` ("ece")
**C++ Solution:**
```cpp
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string s = "eceba";
    int k = 2;
    unordered_map<char, int> map;
    int maxLen = 0, left = 0;
    
    for(int right = 0; right < s.length(); right++) {
        map[s[right]]++;
        while(map.size() > k) {
            map[s[left]]--;
            if(map[s[left]] == 0) map.erase(s[left]);
            left++;
        }
        maxLen = max(maxLen, right - left + 1);
    }
    cout << maxLen << "\n";
    return 0;
}
```

## Technical Interview Questions
1. Explain the difference between primary key, foreign key, and unique key.
2. What are ACID properties? Explain isolation levels.
3. Write a SQL query to find the employee with the second highest salary.
