# Problem 13: Largest Odd Number in String

## Problem Statement
You are given a string `num`, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string `""` if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

## Input Format
- A string `num` consisting of digits.

## Output Format
- A string representing the largest odd substring.

## Constraints
- `1 <= num.length <= 10^5`
- `num` only consists of digits and does not contain any leading zeros.

---

## Approach

This is a clever logic-based question frequently asked in TCS Ninja.
1. Any number is odd if and only if its last digit is odd.
2. We want the *largest-valued* odd integer. Since `num` itself is the largest possible substring starting at index `0`, any substring starting at index `0` and ending at the last odd digit will be the largest possible odd integer.
3. So, we simply traverse the string from right to left (end to beginning).
4. The moment we find a digit that is odd (i.e., `(char - '0') % 2 != 0`), the substring from the beginning of `num` up to this digit inclusive is our answer.
5. If we traverse the whole string and find no odd digit, return `""`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string largestOddNumber(string num) {
        // Start from the end of the string
        for (int i = num.length() - 1; i >= 0; i--) {
            // Check if the current digit is odd
            if ((num[i] - '0') % 2 != 0) {
                // Return the substring from the start to the odd digit
                return num.substr(0, i + 1);
            }
        }
        
        // No odd digit found
        return "";
    }
};

int main() {
    Solution sol;
    cout << sol.largestOddNumber("52") << endl;    // Expected: "5"
    cout << sol.largestOddNumber("4206") << endl;  // Expected: ""
    cout << sol.largestOddNumber("35427") << endl; // Expected: "35427"
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the string. In the worst case, we traverse the entire string from right to left exactly once. The `substr` operation takes `O(N)` as well.
- **Space Complexity:** `O(1)` auxiliary space. We only return a new string.
