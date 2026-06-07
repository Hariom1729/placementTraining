# Problem 4: Next Greater Element II (Circular Array)

## Problem Statement
Given a **circular integer array** `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the next greater number for every element in `nums`.

The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

## Input Format
- An array of integers `nums`.

## Output Format
- An array of integers representing the next greater element for each index.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach: Monotonic Stack + Imaginary Doubled Array

Because the array is circular, the next greater element for the last element might be at the beginning of the array.
The standard trick for circular arrays is to pretend the array is **doubled in length**.
For an array `[1, 2, 1]`, we pretend it is `[1, 2, 1, 1, 2, 1]`.

1. The length of the array is `n`. The imaginary array length is `2 * n`.
2. We loop `i` from `2 * n - 1` down to `0`.
3. To access elements without actually doubling the array in memory, we use the modulo operator: `index = i % n`.
4. Apply the same monotonic stack logic:
   - While stack is not empty and `stack.top() <= nums[index]`, `stack.pop()`.
   - If `i < n` (meaning we are calculating the answer for the actual elements, not the imaginary ones), store `st.top()` in `result[index]`.
   - Push `nums[index]` to the stack.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> st;
        
        // Loop 2n times, simulating a doubled array
        for (int i = 2 * n - 1; i >= 0; i--) {
            int index = i % n;
            
            // Pop smaller elements
            while (!st.empty() && st.top() <= nums[index]) {
                st.pop();
            }
            
            // Only update result for the original n elements
            if (i < n) {
                if (!st.empty()) {
                    result[index] = st.top();
                }
            }
            
            // Push current element
            st.push(nums[index]);
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 1};
    vector<int> result = sol.nextGreaterElements(nums);
    
    cout << "Input:  ";
    for(int x : nums) cout << x << " ";
    cout << "\nResult: ";
    for(int x : result) cout << x << " ";
    cout << "\n";
    // Expected: 2 -1 2
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate `2N` times. Each element is pushed and popped at most once.
- **Space Complexity:** `O(N)` for the stack.
