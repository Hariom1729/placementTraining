# Problem 15: Majority Element

## Problem Statement
Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the majority element.

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

The most optimal way to find the majority element in `O(1)` space is using **Moore's Voting Algorithm**.
1. We maintain a `count` variable and an `element` variable.
2. Iterate through the array.
3. If `count == 0`, we assume the current `nums[i]` is the majority element and set `count = 1`.
4. If `nums[i]` is equal to our assumed `element`, we increment `count`.
5. If `nums[i]` is different from our assumed `element`, we decrement `count`.
6. Because the majority element appears more than `N/2` times, its count will mathematically never hit 0 at the end of the traversal.

*(Note: Since the problem guarantees the majority element exists, we don't need a second pass to verify it.)*

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int element = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                element = nums[i];
                count = 1;
            } else if (nums[i] == element) {
                count++;
            } else {
                count--;
            }
        }
        
        return element;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    cout << "Majority Element: " << sol.majorityElement(nums) << endl; // Expected: 2
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements in the array. We iterate through the array once.
- **Space Complexity:** `O(1)` as only two variables are used.
