# Subarray Sums Divisible by K

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE

## Topic
Arrays

## Pattern
Prefix Sum / Modulo Arithmetic

## Problem Statement
Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.
A subarray is a contiguous part of an array.

## Constraints
- $1 \le nums.length \le 3 \times 10^4$
- $-10^4 \le nums[i] \le 10^4$
- $2 \le k \le 10^4$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.
- Third line: `K`

## Output Format
- Return a single integer representing the count of subarrays.

## Sample Input
```
6
4 5 0 -2 -3 1
5
```

## Sample Output
```
7
```

## Edge Cases
- Arrays with all negative numbers.
- `nums[i]` exactly a multiple of `K`.

## Approach 1
Brute Force
**Explanation:** Check the sum of every possible subarray.
**Time Complexity:** $O(N^2)$ (TLE).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Prefix Sum Modulo)
**Explanation:** 
If the cumulative sum up to index `i` modulo `K` is equal to the cumulative sum up to index `j` modulo `K`, it mathematically implies that the sum of the elements between `i` and `j` is perfectly divisible by `K`.
Why? Let $S_i \% K = R$ and $S_j \% K = R$.
Then $(S_j - S_i) \% K = (R - R) \% K = 0$.

1. We use a Hash Map (or frequency array) to store the frequencies of the remainders.
2. Initialize `map[0] = 1` because a remainder of 0 natively means the subarray from index 0 is divisible by `K`.
3. Keep a running `prefixSum`. Find the `remainder = prefixSum % K`.
4. If `remainder` is negative (due to negative numbers in C++/Java), normalize it by adding `K`: `remainder = (remainder + K) % K`.
5. Add `map[remainder]` to our total count, because we can form a valid subarray with every previous occurrence of this remainder.
6. Increment `map[remainder]`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(K)$ for the remainder frequencies.

## Java Solution
```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] remainderFreq = new int[k];
        remainderFreq[0] = 1; // Base case
        
        int prefixSum = 0;
        int count = 0;
        
        for (int num : nums) {
            prefixSum += num;
            
            int remainder = prefixSum % k;
            if (remainder < 0) {
                remainder += k; // Normalize negative remainders
            }
            
            count += remainderFreq[remainder];
            remainderFreq[remainder]++;
        }
        
        return count;
    }
}
```

## Python Solution
```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_freq = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            
            remainder = prefix_sum % k
            # Python modulo inherently handles negative numbers correctly, 
            # so no manual adjustment is needed for standard Python % operator.
            
            count += remainder_freq.get(remainder, 0)
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
            
        return count
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> remainderFreq(k, 0);
        remainderFreq[0] = 1;
        
        int prefixSum = 0;
        int count = 0;
        
        for (int num : nums) {
            prefixSum += num;
            
            int remainder = prefixSum % k;
            if (remainder < 0) {
                remainder += k;
            }
            
            count += remainderFreq[remainder];
            remainderFreq[remainder]++;
        }
        
        return count;
    }
};
```

## Common Mistakes
- **Negative Remainders in C++/Java:** In C++ and Java, `-2 % 5` is `-2`. But mathematically for modular arithmetic, the remainder should be `3`. You MUST normalize negative remainders by doing `(rem + k) % k` or checking `if (rem < 0) rem += k;`.
- **Forgetting `map[0] = 1`:** If the prefix sum itself is exactly divisible by `K` right off the bat, you need this base case to count it.

## Similar Questions
- Subarray Sum Equals K
- Continuous Subarray Sum
- Make Sum Divisible by P
