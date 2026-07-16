# Subarray Sum Equals K

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Meta, Google

## Topic
Arrays

## Pattern
Prefix Sum / Hash Map

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

## Constraints
- $1 \le nums.length \le 2 \times 10^4$
- $-1000 \le nums[i] \le 1000$
- $-10^7 \le k \le 10^7$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.
- Third line: `K`

## Output Format
- Return a single integer representing the count of subarrays.

## Sample Input
```
3
1 2 3
3
```

## Sample Output
```
2
```

## Edge Cases
- Subarray might contain negative numbers, meaning a sum could decrease and then increase back to `k`. (Sliding window will fail here).
- `nums[i]` could be exactly `k`.
- Multiple overlapping subarrays can sum to `k`.

## Approach 1
Brute Force
**Explanation:** Iterate through all possible starting and ending points, sum the elements, and check if it equals `k`.
**Time Complexity:** $O(N^2)$ (Will TLE).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Prefix Sum + Hash Map)
**Explanation:** 
Sliding window does NOT work here because the array can contain negative numbers. Instead, we use Prefix Sum.
If the cumulative sum up to index `i` is `prefix_sum`, and there exists some previous index `j` where the cumulative sum was `prefix_sum - k`, it means the subarray from `j+1` to `i` has a sum exactly equal to `k`.

1. Initialize a Hash Map to store `(prefix_sum, frequency)`.
2. Crucial Step: Add `(0, 1)` to the map. This handles the case where the prefix sum exactly equals `k` right from the 0th index.
3. Iterate through `nums`, maintaining a running `prefix_sum`.
4. If `(prefix_sum - k)` exists in the map, add its frequency to `count`.
5. Add the current `prefix_sum` to the map (or increment its frequency).

**Dry Run:**
`nums = [1, 2, 3]`, `k = 3`
- init: map = `{0: 1}`, `sum = 0`, `count = 0`
- `i=0` (1): `sum = 1`. `sum - k = 1 - 3 = -2`. Not in map. Map becomes `{0: 1, 1: 1}`.
- `i=1` (2): `sum = 3`. `sum - k = 3 - 3 = 0`. In map! `count += map[0]` -> `count = 1`. Map becomes `{0: 1, 1: 1, 3: 1}`.
- `i=2` (3): `sum = 6`. `sum - k = 6 - 3 = 3`. In map! `count += map[3]` -> `count = 2`. Map becomes `{0: 1, 1: 1, 3: 1, 6: 1}`.
Return 2.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Java Solution
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        
        int count = 0;
        int prefixSum = 0;
        
        for (int num : nums) {
            prefixSum += num;
            
            if (map.containsKey(prefixSum - k)) {
                count += map.get(prefixSum - k);
            }
            
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }
        
        return count;
    }
}
```

## Python Solution
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        count = 0
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
                
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
            
        return count
```

## C++ Solution
```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixMap;
        prefixMap[0] = 1;
        
        int count = 0;
        int prefixSum = 0;
        
        for (int num : nums) {
            prefixSum += num;
            
            if (prefixMap.find(prefixSum - k) != prefixMap.end()) {
                count += prefixMap[prefixSum - k];
            }
            
            prefixMap[prefixSum]++;
        }
        
        return count;
    }
};
```

## Common Mistakes
- **Using Sliding Window:** Because the array contains negative constraints, `sum` can go up and down. A sliding window depends on the `sum` strictly increasing so we know when to confidently shrink `left`.
- **Forgetting `map[0] = 1`:** If `nums = [3]` and `k = 3`, `prefix_sum - k` is `0`. If `0` isn't in the map, it will incorrectly return 0.

## Interview Tips
- Emphasize *why* sliding window fails. Interviewers love this question specifically to catch candidates who blindly apply sliding window to subarray sum problems without checking constraints for negative numbers.

## Similar Questions
- Subarray Sums Divisible by K
- Path Sum III
- Continuous Subarray Sum
