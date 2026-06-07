# Problem 4: Remove Duplicates from a Sorted Array

## Problem Statement
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

## Input Format
- A sorted vector of integers `nums`.

## Output Format
- An integer representing the number of unique elements.
- The array `nums` must be modified in-place so that the first `k` elements contain the unique elements.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

---

## Approach

Because the array is already sorted, all duplicate elements will be adjacent to each other. We use the **Two Pointers** pattern.
1. Use pointer `i` to keep track of the index of the last unique element found.
2. Use pointer `j` to iterate through the array starting from index 1.
3. Compare `nums[j]` with `nums[i]`. 
4. If they are different, we have found a new unique element. We increment `i` and set `nums[i] = nums[j]`.
5. If they are the same, we simply continue iterating with `j` to skip the duplicate.
6. The total number of unique elements will be `i + 1`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int i = 0; // Pointer for unique elements
        
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        
        return i + 1; // Return the new length
    }
};

int main() {
    Solution sol;
    vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int k = sol.removeDuplicates(nums);
    
    cout << "Number of unique elements: " << k << endl; // Expected: 5
    cout << "Array after removal: ";
    for (int i = 0; i < k; i++) {
        cout << nums[i] << " "; // Expected: 0 1 2 3 4
    }
    cout << endl;
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. The pointer `j` iterates exactly `N-1` times.
- **Space Complexity:** `O(1)`. The operations are performed directly in the input array.
