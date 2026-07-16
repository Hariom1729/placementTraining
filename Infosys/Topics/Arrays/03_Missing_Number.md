# Missing Number

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Year: 2020, 2022
Frequency: High

---

## Problem Statement
Given an array `nums` containing `N` distinct numbers in the range `[0, N]`, return the only number in the range that is missing from the array.

---

## Input Format
- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers in the range `[0, N]`.

---

## Output Format
- Return a single integer representing the missing number.

---

## Constraints
- $N == nums.length$
- $1 \le N \le 10^4$
- $0 \le nums[i] \le N$
- All the numbers of `nums` are unique.

---

## Examples

### Example 1
**Input:** 
```
3
3 0 1
```
**Output:** 
```
2
```
**Explanation:** N = 3, so the range is [0,3]. 2 is the missing number.

### Example 2
**Input:** 
```
2
0 1
```
**Output:** 
```
2
```

---

## Brute Force Approach
Iterate from `0` to `N` and for each number, run a linear search over the array to check if it exists. If it doesn't, return it.

**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

---

## Better Approach
Use a Hash Set. Insert all array elements into the Hash Set. Then loop from `0` to `N` and check if each number exists in the set.

**Complexity:** 
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ for the Hash Set.

---

## Optimal Approach (Math or Bit Manipulation)
**Detailed explanation (Math):**
The sum of the first `N` natural numbers is given by the formula $S = \frac{N \times (N + 1)}{2}$. We can calculate this expected sum, then subtract all the elements currently in the array. The remaining value is the missing number.

**Detailed explanation (XOR):**
XOR has a property where $A \oplus A = 0$. If we XOR all numbers in the range `[0, N]` and also XOR all elements in the array, every number present in the array will cancel out with its counterpart in the range. The only number left will be the missing one.

**Dry Run (Math):**
`nums = [3, 0, 1]`, `N = 3`
- Expected Sum: $3 \times (3 + 1) / 2 = 6$.
- Actual Sum: $3 + 0 + 1 = 4$.
- Missing: $6 - 4 = 2$.

**Complexity:**
- **Time Complexity:** $O(N)$ for a single pass.
- **Space Complexity:** $O(1)$.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Approach 1: Math
int missingNumberMath(vector<int>& nums) {
    int n = nums.size();
    long long expectedSum = (long long)n * (n + 1) / 2;
    long long actualSum = 0;
    
    for (int num : nums) {
        actualSum += num;
    }
    
    return expectedSum - actualSum;
}

// Approach 2: XOR (Bit Manipulation)
int missingNumberXOR(vector<int>& nums) {
    int missing = nums.size();
    for (int i = 0; i < nums.size(); i++) {
        missing ^= i ^ nums[i];
    }
    return missing;
}

int main() {
    vector<int> nums = {3, 0, 1};
    cout << "Missing (Math): " << missingNumberMath(nums) << endl; // Output: 2
    cout << "Missing (XOR): " << missingNumberXOR(nums) << endl; // Output: 2
    return 0;
}
```

---

## Common Mistakes
- **Integer Overflow:** If `N` is very large (e.g., $10^5$), $N \times (N+1)$ can overflow a 32-bit integer. Always use `long long` for sum calculations to be safe, or use the XOR approach which mathematically cannot overflow.

---

## Similar Questions
- Find the Duplicate Number
- Missing and Repeating Number

---

## Interview Tips
- The interviewer will almost always ask for the XOR approach after you explain the Math approach to test your knowledge of Bit Manipulation. Know both.

---

## Variations Asked
- Array starts from 1 instead of 0.
- Array contains negative numbers.

---

## Pattern Recognition
**Identify this when:** A problem deals with numbers in a continuous range `[0, N]` or `[1, N]`, and one or more numbers are missing/duplicated. **Cyclic Sort**, **Math Formulas**, and **XOR** are the ultimate tri-factor for these problems.
