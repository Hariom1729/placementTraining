# Problem 18: Rearrange Array Elements by Sign

## Problem Statement
You are given a **0-indexed** integer array `nums` of **even** length consisting of an **equal** number of positive and negative integers.

You should rearrange the elements of `nums` such that the modified array follows the given conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in `nums` is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

## Input Format
- An array of integers `nums`.

## Output Format
- A new array with elements rearranged.

## Constraints
- `2 <= nums.length <= 2 * 10^5`
- `nums.length` is even
- `1 <= |nums[i]| <= 10^5`
- `nums` consists of equal number of positive and negative integers.

---

## Approach

Since we must preserve the relative order of elements, doing this perfectly in-place is highly complex `O(N^2)`. Given the constraints, we can use an extra array of size `N`.
1. Create a `vector<int> ans` of the same size as `nums`, initialized to 0.
2. We know positive numbers must go to even indices (`0, 2, 4...`) and negative numbers to odd indices (`1, 3, 5...`).
3. Initialize two pointers: `posIndex = 0` and `negIndex = 1`.
4. Iterate through `nums`:
   - If `nums[i] > 0`, place it at `ans[posIndex]` and increment `posIndex` by 2.
   - If `nums[i] < 0`, place it at `ans[negIndex]` and increment `negIndex` by 2.
5. Return the `ans` array.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 0); // Result array
        
        int posIndex = 0; // Starts at even index
        int negIndex = 1; // Starts at odd index
        
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                ans[posIndex] = nums[i];
                posIndex += 2;
            } else {
                ans[negIndex] = nums[i];
                negIndex += 2;
            }
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {3, 1, -2, -5, 2, -4};
    vector<int> res = sol.rearrangeArray(nums);
    
    cout << "Rearranged Array: ";
    for (int x : res) {
        cout << x << " "; // Expected: 3 -2 1 -5 2 -4
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We iterate through the array once.
- **Space Complexity:** `O(N)` for creating the output array.
