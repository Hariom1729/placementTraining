# Problem 14: Sort an Array of 0s, 1s, and 2s (Sort Colors)

## Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

## Input Format
- An array of integers `nums` where `nums[i]` is either `0`, `1`, or `2`.

## Output Format
- The array `nums` modified in-place.

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

---

## Approach

This problem is a variation of the **Dutch National Flag Algorithm** proposed by Edsger Dijkstra.
1. Use three pointers: `low = 0`, `mid = 0`, `high = n - 1`.
2. The logic is to maintain three regions:
   - Elements from `0` to `low-1` are `0`s.
   - Elements from `high+1` to `n-1` are `2`s.
   - Elements between `low` and `mid-1` are `1`s.
3. Iterate while `mid <= high`:
   - If `nums[mid] == 0`: Swap `nums[low]` and `nums[mid]`, then increment both `low` and `mid`.
   - If `nums[mid] == 1`: Just increment `mid`.
   - If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`, then decrement `high`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sol.sortColors(nums);
    
    for (int x : nums) {
        cout << x << " "; // Expected: 0 0 1 1 2 2
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We process each element at most once.
- **Space Complexity:** `O(1)` as we do the sorting in-place.
