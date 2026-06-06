# Problem 12: Find the Number that Appears Once

## Problem Statement
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the single number.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

---

## Approach

While we could use a Hash Map to count frequencies, it would take `O(N)` space. The optimal approach uses **Bit Manipulation**.

**Approach: XOR Operation**
- The XOR operator `^` has the following properties:
  1. `X ^ X = 0` (XORing a number with itself results in 0).
  2. `X ^ 0 = X` (XORing a number with 0 results in the number itself).
  3. XOR is associative and commutative.
- If we XOR all numbers in the array together, all numbers that appear twice will cancel each other out (become 0). The only remaining number will be the one that appears once.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xor_val = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            xor_val ^= nums[i]; // XOR operation
        }
        
        return xor_val;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << "Single Number: " << sol.singleNumber(nums) << endl; // Expected: 4
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the array. We iterate through the array once.
- **Space Complexity:** `O(1)`. Only one variable is used.
