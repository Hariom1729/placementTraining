# Problem 7: Check if Strings are Rotations of Each Other

## Problem Statement
Given two strings `s1` and `s2`, write code to check if `s2` is a rotation of `s1`. 
For example, "waterbottle" is a rotation of "erbottlewat".

## Input Format
- Two strings, `s1` and `s2`.

## Output Format
- Boolean `true` or `false`.

## Constraints
- `1 <= s1.length, s2.length <= 10^5`

---

## Approach

There is a very elegant 1-line logical trick to solve this problem, which is highly favored in TCS Digital.
1. First, check if `s1` and `s2` are of the same length. If not, they cannot be rotations.
2. Concatenate `s1` with itself: `string temp = s1 + s1;`.
3. If `s2` is indeed a rotation of `s1`, it MUST be a substring of `temp`. 
   - Example: `s1` = "waterbottle", `s2` = "erbottlewat".
   - `temp` = "waterbottlewaterbottle"
   - You can clearly see "erbottlewat" inside "wat**erbottlewat**erbottle".
4. Use the built-in substring search `temp.find(s2) != string::npos` to check if `s2` is present in `temp`.

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool areRotations(string s1, string s2) {
        // If lengths are different, they cannot be rotations
        if (s1.length() != s2.length()) {
            return false;
        }
        
        // Concatenate s1 with itself
        string temp = s1 + s1;
        
        // Check if s2 is a substring of temp
        return temp.find(s2) != string::npos;
    }
};

int main() {
    Solution sol;
    cout << (sol.areRotations("waterbottle", "erbottlewat") ? "true" : "false") << endl; // Expected: true
    cout << (sol.areRotations("hello", "llohe") ? "true" : "false") << endl;             // Expected: true
    cout << (sol.areRotations("hello", "loleh") ? "true" : "false") << endl;             // Expected: false
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of `s1`. The `std::string::find` method in C++ operates generally in `O(N)` average time.
- **Space Complexity:** `O(N)` because we create a new string `temp` which is twice the length of `s1`.

---

## Interview Notes
- If the interviewer asks you to solve it in `O(1)` space without creating the concatenated string, you can simulate the concatenation using modulo arithmetic. Iterate through `s1` as the starting point, and for each character, compare `s2[j]` with `s1[(i + j) % N]`. If a full match is found, return `true`. This approach takes `O(N^2)` time but `O(1)` space.
