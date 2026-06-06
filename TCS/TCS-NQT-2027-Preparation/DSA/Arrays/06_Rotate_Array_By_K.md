# Problem 6: Rotate an Array by K Places

## Problem Statement
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- The array `nums` modified in-place.

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Approach

The most optimal way to solve this in `O(N)` time and `O(1)` space is using the **Reversal Algorithm**.

When we rotate an array of size `N` to the right by `k` steps, the last `k` elements come to the front, and the first `N-k` elements shift to the back.
*(Note: If `k > N`, rotating `k` times is the same as rotating `k % N` times)*.

**Algorithm:**
1. Reverse the entire array `nums`.
2. Reverse the first `k` elements.
3. Reverse the remaining `N - k` elements.

*(Alternatively for left rotation: reverse first `k`, reverse remaining `N-k`, reverse all)*.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void rotateRight(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; // Handle cases where k > n
        
        // Reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // Reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // Reverse the rest of the array
        reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    sol.rotateRight(nums, 3);
    
    cout << "Rotated Array: ";
    for (int x : nums) {
        cout << x << " "; // Expected: 5 6 7 1 2 3 4
    }
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Reversing an array of size `N` takes `O(N)` time. We perform three reversals which sum up to `O(2N) = O(N)`.
- **Space Complexity:** `O(1)`. All reversals are done in-place using `std::reverse`.
