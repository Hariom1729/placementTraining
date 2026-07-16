# Next Greater Element III

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, ByteDance

## Topic
Arrays / Math

## Pattern
Next Permutation

## Problem Statement
Given a positive integer `n`, find the smallest integer which has exactly the same digits existing in the integer `n` and is greater in value than `n`. If no such positive integer exists, return `-1`.
Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return `-1`.

## Constraints
- $1 \le n \le 2^{31} - 1$

## Input Format
- A single integer `N`.

## Output Format
- Return a single integer representing the next greater element, or `-1`.

## Sample Input
```
12
```

## Sample Output
```
21
```

## Sample Input 2
```
21
```

## Sample Output 2
```
-1
```

## Edge Cases
- Number is already the maximum possible permutation (e.g., `4321` -> return `-1`).
- Number has duplicate digits (e.g., `230241`).
- The resulting next greater element overflows the 32-bit signed integer limit.

## Approach 1
Brute Force
**Explanation:** Generate all permutations of the digits of `n`, sort them, and find the one that comes immediately after `n`.
**Time Complexity:** $O(D! \log(D!))$ where $D$ is the number of digits (max 10).
**Space Complexity:** $O(D!)$

## Approach 2
Optimal Approach (Next Permutation Logic)
**Explanation:** 
This problem is mathematically identical to finding the "Next Permutation" of an array. We just treat the digits of the number as an array.
1. Convert the integer `n` into a character array (or array of digits).
2. Traverse from right to left to find the first digit that is smaller than the digit immediately after it. Let this be index `i`.
3. If no such digit is found, the digits are sorted in descending order, meaning this is the largest possible permutation. Return `-1`.
4. If found, traverse again from right to left to find the first digit that is strictly greater than the digit at index `i`. Let this be index `j`.
5. Swap the digits at index `i` and `j`.
6. Reverse all the digits from index `i + 1` to the end of the array.
7. Convert the character array back to an integer. If it exceeds `INT_MAX`, return `-1`.

**Dry Run:**
`n = 230241` -> Array: `['2', '3', '0', '2', '4', '1']`
- Step 2: Find `i`. Right to left. `4 > 1` (No). `2 < 4` (Yes!). So `i = 3` (`nums[i] = '2'`).
- Step 4: Find `j`. Right to left greater than '2'. `1 > 2` (No). `4 > 2` (Yes!). So `j = 4` (`nums[j] = '4'`).
- Step 5: Swap `nums[3]` and `nums[4]`. Array is now `['2', '3', '0', '4', '2', '1']`.
- Step 6: Reverse from `i+1` (index 4) to end. Reverse `['2', '1']` to `['1', '2']`.
- Array becomes `['2', '3', '0', '4', '1', '2']`.
- Result: 230412.

**Time Complexity:** $O(D)$, where $D$ is the number of digits (max 10). This is effectively $O(1)$.
**Space Complexity:** $O(D)$ to store the digits as a string/array. Effectively $O(1)$.

## Java Solution
```java
class Solution {
    public int nextGreaterElement(int n) {
        char[] digits = String.valueOf(n).toCharArray();
        
        int i = digits.length - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) {
            i--;
        }
        
        if (i < 0) return -1;
        
        int j = digits.length - 1;
        while (j >= 0 && digits[j] <= digits[i]) {
            j--;
        }
        
        swap(digits, i, j);
        reverse(digits, i + 1);
        
        try {
            return Integer.parseInt(new String(digits));
        } catch (NumberFormatException e) {
            return -1; // 32-bit integer overflow
        }
    }
    
    private void swap(char[] digits, int i, int j) {
        char temp = digits[i];
        digits[i] = digits[j];
        digits[j] = temp;
    }
    
    private void reverse(char[] digits, int start) {
        int i = start, j = digits.length - 1;
        while (i < j) {
            swap(digits, i, j);
            i++;
            j--;
        }
    }
}
```

## Python Solution
```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        if i < 0:
            return -1
            
        j = len(digits) - 1
        while j >= 0 and digits[j] <= digits[i]:
            j -= 1
            
        digits[i], digits[j] = digits[j], digits[i]
        
        # Reverse suffix
        left, right = i + 1, len(digits) - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
            
        ans = int("".join(digits))
        return ans if ans <= 2**31 - 1 else -1
```

## C++ Solution
```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        int i = s.length() - 2;
        
        while (i >= 0 && s[i] >= s[i + 1]) {
            i--;
        }
        
        if (i < 0) return -1;
        
        int j = s.length() - 1;
        while (j >= 0 && s[j] <= s[i]) {
            j--;
        }
        
        swap(s[i], s[j]);
        reverse(s.begin() + i + 1, s.end());
        
        long long res = stoll(s);
        if (res > INT_MAX) return -1;
        
        return res;
    }
};
```

## Common Mistakes
- **Missing Overflow Check:** The prompt explicitly states the answer must fit in a 32-bit signed integer. For example, `n = 1999999999` has a next greater element of `9199999999`, which overflows `INT_MAX`. Failing to handle this will result in compilation/runtime errors or wrong answers on test cases.

## Interview Tips
- When asked this, immediately recognize that it's just "Next Permutation" applied to digits. This shows strong pattern recognition.

## Similar Questions
- Next Permutation
- Next Greater Element I
- Next Greater Element II
