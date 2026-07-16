# Two Sum

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
Hash Map

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have **exactly one solution**, and you may not use the same element twice.
You can return the answer in any order.

## Constraints
- $2 \le nums.length \le 10^4$
- $-10^9 \le nums[i] \le 10^9$
- $-10^9 \le target \le 10^9$
- Only one valid answer exists.

## Input Format
- First line: `N` (size of array).
- Second line: `N` space-separated integers.
- Third line: `target` integer.

## Output Format
- Return two integers representing the indices of the two numbers.

## Sample Input
```
4
2 7 11 15
9
```

## Sample Output
```
0 1
```

## Edge Cases
- The array can contain negative numbers and zeroes.
- The two numbers that add up to target can be the same value but at different indices (e.g., `nums = [3, 3], target = 6`).

## Approach 1
Brute Force
**Explanation:** Use two nested loops. The outer loop iterates through the array from `i = 0` to `n-1`. The inner loop iterates from `j = i+1` to `n-1`. For each pair, check if `nums[i] + nums[j] == target`.
**Time Complexity:** $O(N^2)$
**Space Complexity:** $O(1)$

## Approach 2
Two Pointers (If Array is Sorted)
**Explanation:** If we are allowed to modify the array, we can store the values alongside their original indices as pairs, sort the array based on values, and then use two pointers (left at 0, right at n-1) to find the sum. However, this takes $O(N \log N)$ time and $O(N)$ space for the pairs. We can do better.
**Complexity:** $O(N \log N)$ time, $O(N)$ space.

## Approach 3
Optimal Approach (Hash Map)
**Explanation:** Iterate through the array once. For every element `nums[i]`, calculate its `complement = target - nums[i]`. Check if this complement already exists in the Hash Map.
- If it does, we have found our two numbers! Return the current index `i` and the index stored in the Hash Map for the complement.
- If it doesn't, insert the current element `nums[i]` and its index `i` into the Hash Map.

**Dry Run:**
`nums = [2, 7, 11, 15]`, `target = 9`
- `i = 0`, `num = 2`: complement = 7. Map is empty. Insert `(2, 0)`.
- `i = 1`, `num = 7`: complement = 2. 2 exists in map at index 0. Return `[0, 1]`.

**Time Complexity:** $O(N)$ because inserting and looking up in a Hash Map takes $O(1)$ on average.
**Space Complexity:** $O(N)$ to store elements in the Hash Map.

## Java Solution
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[] {}; // Should not reach here based on constraints
    }
}
```

## Python Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
```

## C++ Solution
```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }
};
```

## Common Mistakes
- **Checking the map after full insertion:** If you insert all elements into the map *before* checking for complements, you run the risk of using the same element twice (e.g., if target is 6 and the array has a single 3, `6-3=3` will find the same 3). The one-pass algorithm inherently prevents this.

## Interview Tips
- This is often a warm-up question. Implement the Hash Map approach flawlessly and quickly to set a good tone. If asked for an $O(1)$ space solution (ignoring the requirement to return indices), mention the Two Pointers approach on a sorted array.

## Similar Questions
- 3Sum
- 4Sum
- Two Sum II - Input Array Is Sorted
- Subarray Sum Equals K

## Variations Asked in Infosys
- Return the actual numbers instead of the indices. (In this case, Two Pointers + Sorting is $O(1)$ space and highly preferred).
