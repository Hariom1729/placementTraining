# Problem 3: Next Greater Element I

## Problem Statement
The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given an array `nums`. For each element `nums[i]`, find the next greater element to its right. If there is no greater element, the answer should be `-1`.

## Input Format
- An array of integers `nums`.

## Output Format
- An array of integers representing the next greater element for each index.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## Approach: Monotonic Decreasing Stack

A naive `O(N^2)` approach involves two nested loops. We can solve this in `O(N)` using a stack that stores elements in decreasing order.

We traverse the array from **right to left** (from `N-1` down to `0`).
1. We maintain a stack that stores the potential "next greater" candidates.
2. For the current element `nums[i]`:
   - While the stack is not empty and the top of the stack is **less than or equal to** `nums[i]`, we `pop` it. (Because smaller elements cannot be the "next greater" element for `nums[i]` or any element to its left).
   - If the stack becomes empty, there is no greater element to the right. Answer for `i` is `-1`.
   - If the stack is not empty, the top element is strictly greater. Answer for `i` is `st.top()`.
3. Push `nums[i]` onto the stack so it can be a candidate for elements to its left.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> st;
        
        // Traverse from right to left
        for (int i = n - 1; i >= 0; i--) {
            // Remove elements smaller than current, as they are useless
            while (!st.empty() && st.top() <= nums[i]) {
                st.pop();
            }
            
            // If stack is not empty, top is the next greater element
            if (!st.empty()) {
                result[i] = st.top();
            }
            
            // Push current element for future numbers to its left
            st.push(nums[i]);
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6};
    
    vector<int> result = sol.nextGreaterElement(nums);
    
    cout << "Input:  ";
    for(int x : nums) cout << x << " ";
    cout << "\nResult: ";
    for(int x : result) cout << x << " ";
    cout << "\n";
    // For 4 -> 12. For 12 -> -1. For 5 -> 6. etc.
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each element is pushed and popped at most once. So the `while` loop runs at most `N` times across all iterations.
- **Space Complexity:** `O(N)` for the stack and the result array.
