# Find the Duplicate Number

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Microsoft, Amazon, Google

## Topic
Arrays

## Pattern
Cycle Sort / Floyd's Tortoise and Hare

## Problem Statement
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
There is only **one repeated number** in `nums`, return this repeated number.
You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

## Constraints
- $1 \le n \le 10^5$
- $nums.length == n + 1$
- $1 \le nums[i] \le n$
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

## Input Format
- First line contains `N`, the size of the array.
- Second line contains `N` space-separated integers.

## Output Format
- Return a single integer representing the duplicate number.

## Sample Input
```
5
1 3 4 2 2
```

## Sample Output
```
2
```

## Edge Cases
- The duplicate number can appear more than twice (e.g., `[2, 2, 2, 2]`).

## Approach 1
Brute Force
**Explanation:** Sort the array and iterate through it to find adjacent elements that are equal.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$ or $O(N)$ depending on sorting algorithm. 
*Note: This violates the "without modifying the array" constraint.*

## Approach 2
Better Approach (Hash Set)
**Explanation:** Iterate through the array and insert each element into a Hash Set. If an element already exists in the set, return it.
**Complexity:** $O(N)$ time, $O(N)$ space.
*Note: This violates the "constant extra space" constraint.*

## Approach 3
Optimal Approach (Floyd's Tortoise and Hare)
**Explanation:** 
Since the numbers are strictly in the range `[1, n]` and there are `n+1` numbers, we can treat the array values as pointers to indices (i.e., `index -> nums[index]`). Because there is a duplicate number, multiple indices will point to the same target index, creating a cycle.
We use Floyd's Cycle Detection algorithm:
1. Initialize a `slow` pointer and a `fast` pointer to the first element (`nums[0]`).
2. Move `slow` by one step (`nums[slow]`) and `fast` by two steps (`nums[nums[fast]]`) until they meet inside the cycle.
3. Once they meet, reset the `slow` pointer back to `nums[0]`. Keep `fast` where it is.
4. Move both pointers by one step at a time. The point where they meet again is the entrance to the cycle, which is the duplicate number.

**Dry Run:**
`nums = [1, 3, 4, 2, 2]`
- Pointers init: `slow = nums[0] = 1`, `fast = nums[0] = 1`
- Phase 1 (Find intersection):
  - Step 1: `slow = nums[1] = 3`, `fast = nums[nums[1]] = nums[3] = 2`
  - Step 2: `slow = nums[3] = 2`, `fast = nums[nums[2]] = nums[4] = 2`
  - `slow == fast` (Intersection at 2)
- Phase 2 (Find entrance):
  - Reset `slow = nums[0] = 1`.
  - Step 1: `slow = nums[1] = 3`, `fast = nums[2] = 4`
  - Step 2: `slow = nums[3] = 2`, `fast = nums[4] = 2`
  - `slow == fast` at 2. Return 2.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];
        
        // Phase 1: Find intersection
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        // Phase 2: Find cycle entrance
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
}
```

## Python Solution
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];
        
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
};
```

## Common Mistakes
- **Using XOR or Math Sum:** You cannot use the standard missing/duplicate Math or XOR trick because the duplicate number might appear *more than twice* (e.g., `[2, 2, 2]`), which completely throws off the arithmetic.

## Interview Tips
- This problem is the ultimate test of understanding array values as pointers. When you see constraints like "numbers in range [1, N]" and "no modification allowed", Floyd's Cycle Detection is the gold standard.

## Similar Questions
- Linked List Cycle II
- Missing Number
- Set Mismatch

## Variations Asked in Infosys
- What if the array is read-only but you can use $O(N)$ space? (Use Hash Set).
