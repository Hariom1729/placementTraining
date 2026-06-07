# Problem 1: Assign Cookies

## Problem Statement
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content.
Your goal is to maximize the number of your content children and output the maximum number.

## Constraints
- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

---

## Approach: Greedy + Sorting

To maximize the number of content children, we should always try to satisfy the least greedy children first, and we should use the smallest cookie that satisfies them. This leaves the larger cookies for the more greedy children.

1. Sort the greed array `g` in ascending order.
2. Sort the cookie size array `s` in ascending order.
3. Use two pointers: `i` for children (`g`) and `j` for cookies (`s`).
4. While `i < g.length` and `j < s.length`:
   - If `s[j] >= g[i]`: The cookie satisfies the child. Move both pointers (`i++`, `j++`).
   - If `s[j] < g[i]`: The cookie is too small. Move to the next larger cookie (`j++`).
5. Return `i` (which represents the number of satisfied children).

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int i = 0; // Pointer for children
        int j = 0; // Pointer for cookies
        
        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) {
                // Cookie satisfies child
                i++;
                j++;
            } else {
                // Cookie is too small, try next cookie
                j++;
            }
        }
        
        return i; // Number of satisfied children
    }
};

int main() {
    Solution sol;
    vector<int> g = {1, 2, 3}; // Greed factors
    vector<int> s = {1, 1};    // Cookie sizes
    
    cout << "Satisfied Children: " << sol.findContentChildren(g, s) << endl; 
    // Expected: 1 (Only the child with greed 1 gets the cookie of size 1)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \log N + M \log M)` where `N` is the length of `g` and `M` is the length of `s`, due to sorting.
- **Space Complexity:** `O(1)` (or `O(\log N)` depending on the sorting algorithm implementation).
