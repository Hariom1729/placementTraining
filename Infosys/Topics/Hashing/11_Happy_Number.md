# Happy Number

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google

## Topic
Hashing / Math / Two Pointers

## Pattern
Cycle Detection / Hash Set

## Problem Statement
Write an algorithm to determine if a number `n` is happy.
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
3. Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

## Constraints
- `1 <= n <= 2^31 - 1`

## Input
- `n` integer.

## Output
- Return a boolean value.

## Sample Test Cases

**Example 1:**
```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Example 2:**
```
Input: n = 2
Output: false
Explanation: The sequence will eventually loop back to 4, generating an endless cycle that never hits 1.
```

## Edge Cases
- `n = 1` (immediately true).
- Maximum integer value (sum of squares of digits shrinks the number massively, so it never overflows).

## Intuition
The problem literally tells us exactly what will happen:
- Either it reaches `1`.
- Or it enters an **endless cycle**.

How do we detect an endless cycle?
1. We can use a **Hash Set**. Every time we compute a new sum, we add it to our Hash Set. If we ever compute a sum that is *already* in our Hash Set, we have entered a cycle! Return `false`. If we hit `1`, return `true`.
2. We can use **Floyd's Cycle-Finding Algorithm** (Tortoise and Hare)! This is exactly like detecting a cycle in a Linked List. We have a slow pointer that computes the next sum once, and a fast pointer that computes the next sum twice. If they ever meet, there is a cycle. If either hits `1`, it's a happy number. This uses $O(1)$ space!

## Optimal Approach 1 (Hash Set)
**Detailed explanation:**
1. Create a helper function `getNext(int n)`:
   - Extract digits using `n % 10`, square them, add to sum, and `n /= 10`. Return sum.
2. Create an `unordered_set<int> seen`.
3. Loop while `n != 1` AND `!seen.count(n)`:
   - `seen.insert(n)`.
   - `n = getNext(n)`.
4. Return `n == 1`.

**Time Complexity:** $O(\log n)$ to extract digits. The sequence length is proven to be small (max sum of squares for any 32-bit int is $9^2 \times 10 = 810$).
**Space Complexity:** $O(\log n)$ for the hash set.

## Optimal Approach 2 (Floyd's Cycle Finding - O(1) Space)
**Detailed explanation:**
1. Create helper `getNext(int n)`.
2. Initialize `slow = n`, `fast = getNext(n)`.
3. Loop while `fast != 1` AND `slow != fast`:
   - `slow = getNext(slow)`.
   - `fast = getNext(getNext(fast))`.
4. Return `fast == 1`.

**Time Complexity:** $O(\log n)$
**Space Complexity:** $O(1)$

## C++ Solution (Floyd's Cycle Finding)

```cpp
#include <unordered_set>
using namespace std;

class Solution {
private:
    int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int digit = n % 10;
            totalSum += digit * digit;
            n /= 10;
        }
        return totalSum;
    }

public:
    bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);
        
        // Loop until fast hits 1 (Happy!) or fast catches up to slow (Cycle!)
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        
        return fast == 1;
    }
};
```

## Dry Run
`n = 19`
- `slow = 19`. `fast = getNext(19) = 82`.
- Loop 1: `fast != 1` and `19 != 82`.
  - `slow = getNext(19) = 82`.
  - `fast = getNext(getNext(82)) = getNext(68) = 100`.
- Loop 2: `fast != 1` and `82 != 100`.
  - `slow = getNext(82) = 68`.
  - `fast = getNext(getNext(100)) = getNext(1) = 1`.
- Loop terminates because `fast == 1`.
- Return `true`.

## Common Mistakes
- **Worrying about Integer Overflow:** The max 32-bit integer is `2,147,483,647` (10 digits). If we pretend it was `9,999,999,999`, the sum of squares is $10 \times 81 = 810$. So the number shrinks massively on the very first step. It can never overflow.

## Similar Problems
- Linked List Cycle
- Add Digits
