# Problem 1: Reverse a String

## Problem Statement
Write a function that reverses a string. The input string is given as an array of characters `s` (or a `std::vector<char>` in C++).
You must do this by modifying the input array in-place with `O(1)` extra memory.

## Input Format
- A vector of characters `s`.

## Output Format
- The same vector `s` modified in-place to be reversed.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ascii character.

---

## Approach

This is a classic problem that utilizes the **Two Pointers** pattern.
1. We place one pointer, `left`, at the beginning of the vector (index `0`).
2. We place another pointer, `right`, at the end of the vector (index `n - 1`).
3. We swap the characters at the `left` and `right` pointers using `std::swap`.
4. Move `left` forward (`left++`) and `right` backward (`right--`).
5. Continue this process until the `left` pointer crosses or meets the `right` pointer (`left >= right`).

This ensures that we swap the outer elements, then the inner elements, completely reversing the sequence in-place.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;
        
        while (left < right) {
            // Swap the characters using built-in std::swap
            swap(s[left], s[right]);
            
            // Move pointers towards the center
            left++;
            right--;
        }
    }
};

int main() {
    Solution sol;
    vector<char> s1 = {'h', 'e', 'l', 'l', 'o'};
    sol.reverseString(s1);
    for(char c : s1) cout << c; // Expected Output: olleh
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of characters. We iterate exactly half of the array `(N/2)` times.
- **Space Complexity:** `O(1)` since we are modifying the input array in-place and only using a few primitive variables.

---

## Interview Notes
- **C++ Advantage:** In C++, `std::string` is also mutable. If the input was `std::string s`, you could use the exact same logic: `swap(s[left], s[right])`. Alternatively, you can just use `std::reverse(s.begin(), s.end())`. However, the interviewer will want to see the two-pointer manual implementation.
