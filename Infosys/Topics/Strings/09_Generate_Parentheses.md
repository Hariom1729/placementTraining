# Generate Parentheses

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, Facebook, Google

## Topic
Strings / Backtracking

## Pattern
Backtracking (Permutations/Combinations)

## Problem Statement
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Constraints
- `1 <= n <= 8`

## Input
- `n` integer.

## Output
- Return a vector of strings.

## Sample Test Cases

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

## Edge Cases
- `n = 1` yields exactly one combination `"()"`.
- Constraints are tiny (`n <= 8`) which is a huge hint that an exponential backtracking solution $O(2^{2N})$ is perfectly acceptable.

## Intuition
We are trying to build a string of length `2n`. At each step, we can either place a `(` or a `)`.
This is a classic Backtracking problem where we build the string step by step.
However, we can't just place any bracket. We have two rules for a *well-formed* combination:
1. **Rule 1 (Open brackets):** We can place an open bracket `(` as long as we haven't used up all `n` of them. (`openCount < n`).
2. **Rule 2 (Close brackets):** We can ONLY place a close bracket `)` if it has a matching open bracket to pair with! This means the number of close brackets placed so far MUST be strictly less than the number of open brackets placed so far. (`closeCount < openCount`).

When our string reaches length `2n`, we have successfully built a valid combination, so we add it to our answer list!

## Brute Force Approach
**Explanation:** Generate all possible strings of length `2n` consisting of `(` and `)` ($2^{2N}$ possibilities). Then run an $O(N)$ valid parenthesis check on every single one.
**Time Complexity:** $O(2^{2N} \times N)$
**Space Complexity:** $O(2^{2N})$

## Optimal Approach (Backtracking with Pruning)
**Detailed explanation:**
1. Create a `vector<string> ans`.
2. Create a helper function `backtrack(string current, int open, int close, int n, vector<string>& ans)`.
3. **Base Case:** If `current.length() == 2 * n`, we've finished! Add `current` to `ans` and return.
4. **Try Open:** If `open < n`, we are allowed to place an open bracket. 
   - Recurse: `backtrack(current + "(", open + 1, close, n, ans)`.
5. **Try Close:** If `close < open`, we are allowed to place a close bracket (to close an existing open one).
   - Recurse: `backtrack(current + ")", open, close + 1, n, ans)`.

**Time Complexity:** $O(\frac{4^N}{\sqrt{N}})$ (The $n$-th Catalan number). Every string generated is guaranteed to be valid, avoiding the massive overhead of checking invalid strings.
**Space Complexity:** $O(N)$ for the recursion stack (depth is $2N$).

## C++ Solution

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        backtrack("", 0, 0, n, ans);
        return ans;
    }
    
private:
    void backtrack(string current, int openCount, int closeCount, int n, vector<string>& ans) {
        // Base case: if the string length is 2*n, a valid combination is formed
        if (current.length() == 2 * n) {
            ans.push_back(current);
            return;
        }
        
        // We can add an open parenthesis if we haven't used all 'n' open parentheses
        if (openCount < n) {
            backtrack(current + "(", openCount + 1, closeCount, n, ans);
        }
        
        // We can add a close parenthesis if we have more open than close parentheses
        if (closeCount < openCount) {
            backtrack(current + ")", openCount, closeCount + 1, n, ans);
        }
    }
};
```

## Dry Run
`n = 2`
- `backtrack("", 0, 0)`
  - `open < 2`. Calls `backtrack("(", 1, 0)`.
    - `open < 2`. Calls `backtrack("((", 2, 0)`.
      - `close < open (0 < 2)`. Calls `backtrack("(()", 2, 1)`.
        - `close < open (1 < 2)`. Calls `backtrack("(())", 2, 2)`.
          - Base case met (len 4). `ans.push_back("(())")`.
    - `close < open (0 < 1)`. Calls `backtrack("()", 1, 1)`.
      - `open < 2`. Calls `backtrack("()(", 2, 1)`.
        - `close < open (1 < 2)`. Calls `backtrack("()()", 2, 2)`.
          - Base case met (len 4). `ans.push_back("()()")`.

Result: `["(())", "()()"]`.

## Common Mistakes
- **Checking `closeCount < n` instead of `closeCount < openCount`:** If you just check if you haven't used all `n` closing brackets, the algorithm might place a closing bracket FIRST (e.g., `")("`), which is permanently invalid. A close bracket can ONLY follow an unmatched open bracket!
- **Using string push_back and pop_back improperly:** Passing `current + "("` by value automatically handles the backtracking (creating a new string copy for the next frame). If you pass `current` by reference to save memory, you MUST `current.pop_back()` after the recursive call returns!

## Similar Problems
- Valid Parentheses
- Letter Combinations of a Phone Number
