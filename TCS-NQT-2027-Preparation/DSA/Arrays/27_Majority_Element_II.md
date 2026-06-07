# Problem 27: Majority Element II

## Problem Statement
Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

## Input Format
- An array of integers `nums`.

## Output Format
- An array of integers containing all the majority elements.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

Since we are looking for elements appearing more than `N/3` times, there can be at most **two** such elements.
We use the **Extended Moore's Voting Algorithm**.
1. We need two counters (`count1`, `count2`) and two candidates (`num1`, `num2`).
2. Iterate through the array.
   - If `nums[i] == num1`, increment `count1`.
   - Else if `nums[i] == num2`, increment `count2`.
   - Else if `count1 == 0`, set `num1 = nums[i]`, `count1 = 1`.
   - Else if `count2 == 0`, set `num2 = nums[i]`, `count2 = 1`.
   - Else, decrement both `count1` and `count2`.
3. The candidates `num1` and `num2` are *potential* answers. Since the problem doesn't guarantee they exist, we must do a **second pass** to count their actual frequencies and verify if they are strictly greater than `N/3`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int num1 = -1, num2 = -1;
        int count1 = 0, count2 = 0;
        int len = nums.size();
        
        // Pass 1: Find potential candidates
        for (int i = 0; i < len; i++) {
            if (nums[i] == num1) {
                count1++;
            } else if (nums[i] == num2) {
                count2++;
            } else if (count1 == 0) {
                num1 = nums[i];
                count1 = 1;
            } else if (count2 == 0) {
                num2 = nums[i];
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }
        
        // Pass 2: Verify candidates
        vector<int> ans;
        count1 = 0; 
        count2 = 0;
        
        for (int i = 0; i < len; i++) {
            if (nums[i] == num1) count1++;
            else if (nums[i] == num2) count2++;
        }
        
        if (count1 > len / 3) ans.push_back(num1);
        if (count2 > len / 3) ans.push_back(num2);
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {3, 2, 3};
    vector<int> res = sol.majorityElement(nums);
    
    cout << "Majority Elements: ";
    for (int x : res) cout << x << " "; // Expected: 3
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements. We do two passes over the array.
- **Space Complexity:** `O(1)`. Only 4 integer variables are used.
