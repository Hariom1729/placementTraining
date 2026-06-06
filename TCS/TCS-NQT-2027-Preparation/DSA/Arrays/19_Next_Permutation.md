# Problem 19: Next Permutation

## Problem Statement
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

You must modify the array in-place.

## Input Format
- An array of integers `nums`.

## Output Format
- The array `nums` modified in-place.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## Approach

This is a frequently asked tricky algorithm.
1. **Find the break point:** Traverse the array from right to left to find the first element that is smaller than the element immediately after it. Let's call its index `ind1`. (`nums[i] < nums[i+1]`).
2. **If no break point exists:** This means the array is sorted in descending order (it's the very last permutation). Just reverse the entire array and return.
3. **Find the next greater element:** If `ind1` exists, traverse from the right end again to find the first element that is strictly greater than `nums[ind1]`. Let its index be `ind2`.
4. **Swap:** Swap `nums[ind1]` and `nums[ind2]`.
5. **Reverse the right half:** The elements from `ind1 + 1` to the end of the array will be in descending order. Reverse them to make them ascending, ensuring the *smallest* possible lexicographical increase.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int ind1 = -1;
        int ind2 = -1;
        
        // Step 1: Find the break point
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                ind1 = i;
                break;
            }
        }
        
        // Step 2: If no break point, reverse the whole array
        if (ind1 == -1) {
            reverse(nums.begin(), nums.end());
        } else {
            // Step 3: Find the next greater element
            for (int i = n - 1; i >= 0; i--) {
                if (nums[i] > nums[ind1]) {
                    ind2 = i;
                    break;
                }
            }
            // Step 4: Swap
            swap(nums[ind1], nums[ind2]);
            
            // Step 5: Reverse the right half
            reverse(nums.begin() + ind1 + 1, nums.end());
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3};
    sol.nextPermutation(nums);
    
    cout << "Next Permutation: ";
    for (int x : nums) {
        cout << x << " "; // Expected: 1 3 2
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements. In the worst case, we do 3 passes (find break point, find next greater, reverse).
- **Space Complexity:** `O(1)`. All operations are performed in-place.
