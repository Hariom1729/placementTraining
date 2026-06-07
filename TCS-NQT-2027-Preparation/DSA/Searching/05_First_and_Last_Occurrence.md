# Problem 5: Find First and Last Position of Element in Sorted Array

## Problem Statement
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Input Format
- A sorted array of integers `nums`.
- An integer `target`.

## Output Format
- A vector of two integers `[first_occurrence, last_occurrence]`.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

---

## Approach

We can solve this problem elegantly by combining our knowledge of **Lower Bound** and **Upper Bound**.
1. **First Occurrence:** This is simply the Lower Bound of `target`. The lower bound gives the index of the first element `>= target`. We just need to verify if the element at that index is actually equal to `target`.
2. **Last Occurrence:** The Upper Bound of `target` gives the first index where the element is strictly `> target`. Therefore, the last occurrence of `target` will be exactly one index before the upper bound (i.e., `upper_bound - 1`).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int getFirstOccurrence(const vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        int first = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                first = mid;
                high = mid - 1; // Look on the left for earlier occurrence
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return first;
    }
    
    int getLastOccurrence(const vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        int last = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                last = mid;
                low = mid + 1; // Look on the right for later occurrence
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return last;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = getFirstOccurrence(nums, target);
        
        // If first occurrence is not found, last occurrence won't exist either
        if (first == -1) return {-1, -1};
        
        int last = getLastOccurrence(nums, target);
        
        return {first, last};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;
    
    vector<int> res = sol.searchRange(nums, target);
    cout << "Range: [" << res[0] << ", " << res[1] << "]" << endl; // Expected: [3, 4]
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(log N)` since we are performing two independent Binary Searches. `O(log N) + O(log N) = O(log N)`.
- **Space Complexity:** `O(1)`.
