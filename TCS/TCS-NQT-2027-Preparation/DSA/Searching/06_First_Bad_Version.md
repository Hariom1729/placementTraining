# Problem 6: First Bad Version

## Problem Statement
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Input Format
- An integer `n`.

## Output Format
- An integer representing the first bad version.

## Constraints
- `1 <= bad <= n <= 2^31 - 1`

---

## Approach

This is a classic "Binary Search on Answer" problem where the array of versions isn't explicitly given as a data structure, but we search through the range of integers `[1, n]`.
The versions look like this: `Good, Good, Good, Bad, Bad, Bad`. We need to find the first `Bad`.

1. Initialize `low = 1` and `high = n`.
2. While `low <= high`:
   - Calculate `mid = low + (high - low) / 2`.
   - If `isBadVersion(mid)` is true, `mid` could be the first bad version, but there might be an earlier bad version on the left. So we record `ans = mid` and move `high = mid - 1`.
   - If `isBadVersion(mid)` is false, it means the first bad version must be strictly on the right. So we move `low = mid + 1`.

---

## C++ Solution

```cpp
#include <iostream>
using namespace std;

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1;
        int high = n;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (isBadVersion(mid)) {
                ans = mid; // Potential answer
                high = mid - 1; // Look for an earlier bad version
            } else {
                low = mid + 1; // First bad version is on the right
            }
        }
        
        return ans;
    }
};

// Mock API for local testing
int firstBad = 4;
bool isBadVersion(int version) {
    return version >= firstBad;
}

int main() {
    Solution sol;
    cout << "First bad version: " << sol.firstBadVersion(5) << endl; // Expected: 4
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)` where `N` is the total number of versions.
- **Space Complexity:** `O(1)`.
