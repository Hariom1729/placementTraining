# Top K Frequent Elements

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Facebook, Google

## Topic
Sorting / Hashing / Heap

## Pattern
Bucket Sort / Min-Heap

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

**Follow up:** Your algorithm's time complexity must be better than $O(n \log n)$, where $n$ is the array's size.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is unique.

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return a vector of integers.

## Sample Test Cases

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time. The top 2 most frequent are 1 and 2.
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Edge Cases
- `k` equals the number of unique elements (return all unique elements).
- Multiple elements have the same frequency.

## Intuition
First, we must count the frequencies of all numbers. We can do this in $O(N)$ time using an `unordered_map<int, int> count`.

Now we have pairs of `(number, frequency)`. How do we find the top `k` frequencies in better than $O(N \log N)$ time?
**Approach 1: Min-Heap.**
Just like "Kth Largest Element", we can maintain a Min-Heap of size `k`. But this time, we sort the heap based on the *frequency*, not the number itself.
This gives $O(N \log K)$ time, which strictly beats $O(N \log N)$ since $K \le N$.

**Approach 2: Bucket Sort ($O(N)$).**
This is the true $O(N)$ masterclass.
What is the MAXIMUM frequency any number can have? It's `N` (if the array is all identical elements).
We can create an array of "buckets": `vector<vector<int>> buckets(N + 1)`.
The index of the bucket represents the **frequency**. The contents of the bucket are the **numbers** that have that frequency!
Once we populate the buckets, we simply scan the bucket array *backwards* (from frequency `N` down to `1`) and collect `k` elements!

Let's implement **Bucket Sort** for guaranteed $O(N)$ performance.

## Optimal Approach (Bucket Sort)
**Detailed explanation:**
1. Create `unordered_map<int, int> countMap` and count frequencies of `nums`.
2. Create `vector<vector<int>> buckets(nums.size() + 1)`.
3. Iterate through `countMap`:
   - Push the `number` into the bucket at index `frequency`: `buckets[freq].push_back(num)`.
4. Create `vector<int> result`.
5. Iterate `i` from `nums.size()` down to `1`:
   - Iterate through the numbers in `buckets[i]`:
     - If `result.size() < k`, push the number to `result`.
     - If `result.size() == k`, return `result`.

**Time Complexity:** $O(N)$ to count, $O(N)$ to group into buckets, $O(N)$ to scan buckets. Overall $O(N)$!
**Space Complexity:** $O(N)$ for the hash map and the bucket array.

## C++ Solution (Bucket Sort - O(N))

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count frequencies
        unordered_map<int, int> countMap;
        for (int num : nums) {
            countMap[num]++;
        }
        
        // Step 2: Create buckets where index = frequency
        // Size is nums.size() + 1 because max frequency is nums.size()
        vector<vector<int>> buckets(nums.size() + 1);
        
        for (auto it : countMap) {
            int num = it.first;
            int freq = it.second;
            buckets[freq].push_back(num);
        }
        
        // Step 3: Scan buckets backwards to get highest frequencies first
        vector<int> result;
        for (int i = buckets.size() - 1; i > 0; i--) {
            // A bucket might have multiple numbers with the same frequency
            for (int num : buckets[i]) {
                result.push_back(num);
                // Once we have k elements, we are done
                if (result.size() == k) {
                    return result;
                }
            }
        }
        
        return result;
    }
};
```

## Dry Run
`nums = [1, 1, 1, 2, 2, 3], k = 2`
- `countMap = {1:3, 2:2, 3:1}`.
- `buckets` array of size 7:
  - `buckets[1] = [3]`
  - `buckets[2] = [2]`
  - `buckets[3] = [1]`
  - `buckets[4,5,6] = []`
- Loop `i` from 6 down to 1:
  - `i=6..4`: Empty.
  - `i=3`: Found `1`. `result = [1]`. Size is 1.
  - `i=2`: Found `2`. `result = [1, 2]`. Size is 2. `result.size() == k` -> return `[1, 2]`.

## Common Mistakes
- **Sorting the Hash Map:** You cannot sort an `unordered_map` in C++. You would have to copy it to a `vector<pair<int, int>>` and use `std::sort`. This takes $O(N \log N)$ and fails the follow-up constraint. Use Bucket Sort or a Priority Queue instead!

## Similar Problems
- Sort Characters By Frequency
- Kth Largest Element in an Array
