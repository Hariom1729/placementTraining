# Multiply Strings

## Difficulty
Medium

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Facebook, Amazon, Google

## Topic
Strings / Math

## Pattern
Simulation (Primary School Multiplication)

## Problem Statement
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Constraints
- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number "0" itself.

## Input
- `num1` string.
- `num2` string.

## Output
- Return the product as a string.

## Sample Test Cases

**Example 1:**
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Edge Cases
- Multiplying by `"0"`. (Must return exactly `"0"`).
- Large numbers that completely exceed `unsigned long long` limits.

## Intuition
Since we can't use `int` or `long long` due to overflow (numbers can be 200 digits long!), we must simulate standard primary school multiplication!
When we multiply a number of length $N$ by a number of length $M$, the maximum possible length of the product is exactly $N + M$.
For example, `99 * 99 = 9801` (length 2 + length 2 = max length 4).

If we create an array `result` of size $N + M$ initialized to 0, we can multiply every digit in `num1` by every digit in `num2` and add the products into the correct positions in the `result` array!
If `num1[i]` and `num2[j]` are multiplied, their product goes into two positions in the `result` array: `i + j` and `i + j + 1`.
Specifically:
- `product = (num1[i] - '0') * (num2[j] - '0')`
- `sum = product + result[i + j + 1]` (add the existing value at the lower position)
- `result[i + j + 1] = sum % 10` (the digit itself)
- `result[i + j] += sum / 10` (the carry over to the next higher position)

After populating the array, we just convert it to a string, ignoring any leading zeros.

## Brute Force Approach
N/A - Direct conversion fails due to constraints. Simulating string addition in a loop is $O(N \times M)$ anyway, but highly complex to write. Array math is cleaner.

## Optimal Approach (Array Multiplication)
**Detailed explanation:**
1. If `num1 == "0"` or `num2 == "0"`, return `"0"`.
2. Let $N = num1.length(), M = num2.length()$.
3. Create `vector<int> result(N + M, 0)`.
4. Iterate `i` backwards from $N-1$ down to 0:
   - Iterate `j` backwards from $M-1$ down to 0:
     - `int mul = (num1[i] - '0') * (num2[j] - '0')`
     - `int p1 = i + j`, `p2 = i + j + 1`
     - `int sum = mul + result[p2]`
     - `result[p2] = sum % 10`
     - `result[p1] += sum / 10`
5. Convert `result` array to string. Skip any leading zeros.
6. Return string.

**Time Complexity:** $O(N \times M)$ because we have nested loops over the two strings.
**Space Complexity:** $O(N + M)$ for the result array.

## C++ Solution

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";
        
        int n = num1.length();
        int m = num2.length();
        vector<int> result(n + m, 0);
        
        // Multiply each digit starting from the end
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                
                // p1 is the tens place (carry), p2 is the ones place for this iteration
                int p1 = i + j;
                int p2 = i + j + 1;
                
                int sum = mul + result[p2];
                
                result[p2] = sum % 10;
                result[p1] += sum / 10;
            }
        }
        
        // Convert the result array back to a string, skipping leading zeros
        string finalString = "";
        bool leadingZero = true;
        
        for (int digit : result) {
            if (digit != 0) {
                leadingZero = false;
            }
            if (!leadingZero) {
                finalString += to_string(digit);
            }
        }
        
        return finalString;
    }
};
```

## Dry Run
`num1 = "12", num2 = "34"` (Lengths: 2, 2. Array size 4).
- `i=1 ('2')`, `j=1 ('4')`: `mul = 8`. `p1=2, p2=3`. `sum = 8`. `res[3]=8`, `res[2]=0`. Array: `[0,0,0,8]`
- `i=1 ('2')`, `j=0 ('3')`: `mul = 6`. `p1=1, p2=2`. `sum = 6`. `res[2]=6`, `res[1]=0`. Array: `[0,0,6,8]`
- `i=0 ('1')`, `j=1 ('4')`: `mul = 4`. `p1=1, p2=2`. `sum = 4 + res[2] = 4 + 6 = 10`. `res[2]=0`, `res[1]=1`. Array: `[0,1,0,8]`
- `i=0 ('1')`, `j=0 ('3')`: `mul = 3`. `p1=0, p2=1`. `sum = 3 + res[1] = 3 + 1 = 4`. `res[1]=4`, `res[0]=0`. Array: `[0,4,0,8]`
- Final array: `[0, 4, 0, 8]`. Skip leading zero `0`.
- Final string: `"408"`.

## Common Mistakes
- **Converting to numbers:** If you try `stoll(num1) * stoll(num2)`, it WILL fail the hidden test cases where lengths are 200 digits long, triggering Integer Overflow exceptions.
- **Forgetting `+ result[p2]`:** When you multiply the next set of digits, you MUST add whatever value is ALREADY sitting at `result[p2]` from previous carries, otherwise you overwrite valid math.

## Similar Problems
- Add Strings
- Add Two Numbers
