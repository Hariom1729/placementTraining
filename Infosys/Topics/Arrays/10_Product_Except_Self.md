# Product of Array Except Self

## Difficulty
Medium

## Asked In
Infosys SP
Infosys DSE
Year: 2022
Frequency: Medium

---

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
**You must write an algorithm that runs in $O(N)$ time and without using the division operation.**

---

## Input Format
- The first line contains an integer `N`.
- The second line contains `N` space-separated integers.

---

## Output Format
- Return an array of size `N` containing the products.

---

## Constraints
- $2 \le nums.length \le 10^5$
- $-30 \le nums[i] \le 30$

---

## Examples

### Example 1
**Input:** 
```
4
1 2 3 4
```
**Output:** 
```
24 12 8 6
```

### Example 2
**Input:** 
```
5
-1 1 0 -3 3
```
**Output:** 
```
0 0 9 0 0
```

---

## Brute Force Approach
For every index `i`, loop through the entire array and multiply all elements where `j != i`.

**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$ auxiliary.

---

## Better Approach (Using Division)
Calculate the total product of the entire array. Then, for each element, the answer is `total_product / nums[i]`.
However, this fails if there are zeros in the array. 
- If one zero: All answers are 0, except for the index with the zero.
- If multiple zeros: All answers are 0.
Additionally, the problem specifically forbids the division operator.

**Complexity:** 
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

## Optimal Approach (Prefix and Suffix Products)
**Detailed explanation:**
Instead of dividing, we can use the property:
`answer[i] = (product of all elements to the left) * (product of all elements to the right)`

1. Create a `prefix` array where `prefix[i]` holds the product of all elements to the left of `i`.
2. Create a `suffix` array where `suffix[i]` holds the product of all elements to the right of `i`.
3. `answer[i] = prefix[i] * suffix[i]`.

**Space Optimization:**
Instead of using two extra arrays, we can construct the `answer` array to hold the prefix products first. Then, we iterate backwards, keeping a running track of the suffix product and multiplying it directly into the `answer` array.

**Dry Run:**
`nums = [1, 2, 3, 4]`
- Forward pass (build prefix in answer):
  - `ans[0] = 1` (default)
  - `ans[1] = ans[0]*nums[0] = 1`
  - `ans[2] = ans[1]*nums[1] = 2`
  - `ans[3] = ans[2]*nums[2] = 6`
  - `ans` is now `[1, 1, 2, 6]`
- Backward pass (using running `right` multiplier):
  - `right = 1`
  - `i = 3`: `ans[3] = ans[3]*right = 6*1 = 6`. `right = right*nums[3] = 4`.
  - `i = 2`: `ans[2] = ans[2]*right = 2*4 = 8`. `right = right*nums[2] = 12`.
  - `i = 1`: `ans[1] = ans[1]*right = 1*12 = 12`. `right = right*nums[1] = 24`.
  - `i = 0`: `ans[0] = ans[0]*right = 1*24 = 24`. 
- Final `ans = [24, 12, 8, 6]`.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$ auxiliary (the output array doesn't count towards space complexity).

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    
    // Left pass: store prefix products in ans
    int left_prod = 1;
    for (int i = 0; i < n; i++) {
        ans[i] = left_prod;
        left_prod *= nums[i];
    }
    
    // Right pass: multiply with suffix products
    int right_prod = 1;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] *= right_prod;
        right_prod *= nums[i];
    }
    
    return ans;
}

int main() {
    vector<int> nums = {1, 2, 3, 4};
    vector<int> res = productExceptSelf(nums);
    
    for (int num : res) {
        cout << num << " ";
    }
    // Output: 24 12 8 6
    return 0;
}
```

---

## Common Mistakes
- **Using Division:** The prompt explicitly says not to use division. Using it fails the OA hidden constraints intentionally looking for the division operator.
- **Handling Zeros Incorrectly:** If you manually try to handle zeros in a single pass without prefix arrays, the edge cases get messy. The prefix/suffix approach naturally handles any number of zeros flawlessly.

---

## Similar Questions
- Trapping Rain Water (Uses identical left/right prefix logic)
- Candy

---

## Interview Tips
- Mention the $O(N)$ space Prefix/Suffix array approach first. When asked to optimize space, explain how the output array can double as the prefix array, and a scalar variable can act as the suffix array.

---

## Pattern Recognition
**Identify this when:** A problem requires aggregated calculations from both sides of an element (left side and right side). This is the hallmark of the **Prefix & Suffix Array** pattern.
