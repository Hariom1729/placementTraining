# Problem 11: Allocate Minimum Number of Pages (Book Allocation)

## Problem Statement
Given an array `arr` of integer numbers, where `arr[i]` represents the number of pages in the `i`-th book. There are `m` number of students, and the task is to allocate all the books to their students. Allocate books in such a way that:
1. Each student gets at least one book.
2. Each book should be allocated to a student.
3. Book allocation should be in a **contiguous** manner.

You have to allocate the books so that the **maximum number of pages assigned to a student is minimized**. If it's not possible to allocate the books, return `-1`.

## Input Format
- An array of integers `arr`.
- An integer `m` (number of students).

## Output Format
- An integer representing the minimized maximum number of pages.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^9`
- `1 <= m <= 10^5`

---

## Approach: Binary Search on Answer

This is a classic "minimize the maximum" problem, which screams Binary Search on Answer.

1. **Edge Case:** If `m > arr.size()`, allocation is impossible. Return `-1`.
2. **Search Space:**
   - Minimum possible answer `low = max(arr)`.
   - Maximum possible answer `high = sum(arr)`.
3. **Helper Function `isValid(maxPages)`:** Can we allocate books such that no student gets more than `maxPages`?
   - Iterate through books, keeping a running sum for the current student.
   - If adding a book exceeds `maxPages`, allocate to the next student.
4. **Binary Search:**
   - If `isValid(mid)` is true, try to find a *smaller* maximum limit (`high = mid - 1`).
   - If false, the limit is too strict (`low = mid + 1`).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
private:
    bool isValid(vector<int>& arr, int m, int maxPages) {
        int studentsRequired = 1;
        long long currentPages = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            if (currentPages + arr[i] <= maxPages) {
                currentPages += arr[i];
            } else {
                studentsRequired++;
                currentPages = arr[i];
            }
        }
        return studentsRequired <= m;
    }

public:
    int allocateBooks(vector<int>& arr, int m) {
        if (m > arr.size()) return -1;
        
        int low = *max_element(arr.begin(), arr.end());
        int high = accumulate(arr.begin(), arr.end(), 0);
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (isValid(arr, m, mid)) {
                ans = mid;
                high = mid - 1; 
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};
```
