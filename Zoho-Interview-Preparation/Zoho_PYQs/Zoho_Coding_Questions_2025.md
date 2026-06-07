# Zoho Coding Questions - 2025

## Round 2: Basic Programming

### 1. Merge Intervals
**Problem:** Given an array of intervals, merge all overlapping intervals.
**Input:** `[[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}};
    if(intervals.empty()) return 0;
    
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged;
    merged.push_back(intervals[0]);
    
    for(int i = 1; i < intervals.size(); i++) {
        if(merged.back()[1] >= intervals[i][0]) {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        } else {
            merged.push_back(intervals[i]);
        }
    }
    
    for(auto& v : merged) cout << "[" << v[0] << "," << v[1] << "] ";
    return 0;
}
```

### 2. Search in a 2D Matrix
**Problem:** Write an efficient algorithm that searches for a value in an m x n matrix where integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.
**Input:** `Matrix, Target = 3`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> matrix = {
        {1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}
    };
    int target = 3;
    int m = matrix.size(), n = matrix[0].size();
    int left = 0, right = m * n - 1;
    
    bool found = false;
    while(left <= right) {
        int mid = left + (right - left) / 2;
        int midVal = matrix[mid / n][mid % n];
        if(midVal == target) {
            found = true; break;
        }
        else if(midVal < target) left = mid + 1;
        else right = mid - 1;
    }
    cout << (found ? "Found" : "Not Found") << "\n";
    return 0;
}
```

## Round 3: Advanced Logic

### 3. Nearest Smaller Element
**Problem:** Find the nearest smaller number on the left of every element.
**Input:** `[1, 6, 4, 10, 2, 5]`
**Output:** `[-1, 1, 1, 4, 1, 2]`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    vector<int> arr = {1, 6, 4, 10, 2, 5};
    stack<int> s;
    
    for(int i=0; i<arr.size(); i++) {
        while(!s.empty() && s.top() >= arr[i]) s.pop();
        if(s.empty()) cout << "-1 ";
        else cout << s.top() << " ";
        s.push(arr[i]);
    }
    return 0;
}
```

## Technical Interview Questions
1. How does a B-Tree differ from a B+ Tree? Why are B+ Trees preferred in DBMS?
2. Explain the difference between Process and Thread.
3. What is TCP 3-way handshake?
