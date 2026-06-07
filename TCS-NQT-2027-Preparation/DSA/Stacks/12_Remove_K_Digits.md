# Problem 12: Remove K Digits

## Problem Statement
Given string `num` representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

## Input Format
- A string `num`.
- An integer `k`.

## Output Format
- A string representing the smallest possible integer.

## Constraints
- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

---

## Approach: Monotonic Stack

To make the number as small as possible, we should prioritize removing larger digits from the most significant positions (the left side). For example, in "1432219", removing '4' gives "132219" which is smaller than removing '9' ("143221").

1. We use a stack to build the final number.
2. Iterate through each digit `d` in `num`.
3. While `k > 0`, the stack is not empty, and the top of the stack is **greater than** `d`, pop the stack and decrement `k`. (We found a smaller digit that can take a more significant position).
4. Push `d` to the stack.
5. If `k > 0` after the loop (e.g., the number was already sorted like "1234"), pop from the back of the stack `k` times.
6. Construct the string from the stack.
7. Remove leading zeros. If the string is empty, return "0".

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        string res = ""; // Using string as a stack
        
        for (char c : num) {
            while (res.length() > 0 && k > 0 && res.back() > c) {
                res.pop_back();
                k--;
            }
            // Prevent leading zeros
            if (res.length() > 0 || c != '0') {
                res.push_back(c);
            }
        }
        
        // If k > 0, remove from the end
        while (res.length() > 0 && k > 0) {
            res.pop_back();
            k--;
        }
        
        return res.empty() ? "0" : res;
    }
};

int main() {
    Solution sol;
    cout << sol.removeKdigits("1432219", 3) << endl; // Expected: "1219"
    cout << sol.removeKdigits("10200", 1) << endl;   // Expected: "200"
    cout << sol.removeKdigits("10", 2) << endl;      // Expected: "0"
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each digit is pushed and popped at most once.
- **Space Complexity:** `O(N)` to store the result string/stack.
