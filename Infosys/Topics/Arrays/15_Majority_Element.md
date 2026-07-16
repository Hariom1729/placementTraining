# Majority Element

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, TCS

## Topic
Arrays

## Pattern
Moore's Voting Algorithm

## Problem Statement
Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Constraints
- $n == nums.length$
- $1 \le n \le 5 \times 10^4$
- $-10^9 \le nums[i] \le 10^9$

## Input Format
- First line: `N` (size of array).
- Second line: `N` space-separated integers.

## Output Format
- Return a single integer representing the majority element.

## Sample Input
```
7
2 2 1 1 1 2 2
```

## Sample Output
```
2
```

## Edge Cases
- Array of size 1 (the single element is the majority).
- All elements are the same.

## Approach 1
Brute Force
**Explanation:** For every element, count its occurrences in the array using a nested loop. If the count exceeds `n/2`, return it.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Hash Map)
**Explanation:** Iterate through the array and store the frequency of each element in a Hash Map. Then iterate through the Hash Map and return the key whose value is $> n/2$.
**Complexity:** $O(N)$ time, $O(N)$ space.

## Approach 3
Optimal Approach (Boyer-Moore Voting Algorithm)
**Explanation:** 
Since the majority element appears *more* than `n/2` times, its count will always outweigh the combined count of all other elements.
1. Initialize `candidate = -1` and `count = 0`.
2. Iterate through the array.
3. If `count == 0`, pick the current element as the new `candidate` and set `count = 1`.
4. If the current element matches the `candidate`, increment `count`.
5. If it doesn't match, decrement `count`.
6. The `candidate` remaining at the end is guaranteed to be the majority element.

**Dry Run:**
`nums = [2, 2, 1, 1, 1, 2, 2]`
- `i=0` (2): `count=0` -> `candidate=2`, `count=1`
- `i=1` (2): `num == candidate` -> `count=2`
- `i=2` (1): `num != candidate` -> `count=1`
- `i=3` (1): `num != candidate` -> `count=0`
- `i=4` (1): `count=0` -> `candidate=1`, `count=1`
- `i=5` (2): `num != candidate` -> `count=0`
- `i=6` (2): `count=0` -> `candidate=2`, `count=1`
Return 2.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }
        
        return candidate;
    }
}
```

## Python Solution
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            
            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }
        
        return candidate;
    }
};
```

## Common Mistakes
- **Forgetting to verify:** The algorithm guarantees the correct answer *only if a majority element is known to exist*. If the problem states a majority element *might not* exist, you MUST do a second pass to count the final `candidate` and verify it actually appears $> n/2$ times. In this specific problem, it's guaranteed.

## Interview Tips
- Mention the Hash Map approach first. The interviewer will ask for $O(1)$ space. That is your cue to bring out Boyer-Moore Voting.
- Also mention that sorting the array and returning `nums[n/2]` works in $O(N \log N)$ time, as the majority element will always cross the middle of the sorted array.

## Similar Questions
- Majority Element II (Elements appearing $> n/3$ times).
- Check If a Number Is Majority Element in a Sorted Array

## Variations Asked in Infosys
- Return all elements that appear more than `N/3` times (Requires two candidates and two counts).
