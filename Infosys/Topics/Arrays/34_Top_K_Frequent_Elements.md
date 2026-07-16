# Top K Frequent Elements

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Meta, Google

## Topic
Arrays / Hash Map / Heap

## Pattern
Bucket Sort / Priority Queue

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.
Your algorithm's time complexity must be better than $O(n \log n)$, where $n$ is the array's size.

## Constraints
- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.
- Third line: `K`

## Output Format
- Return a 1D array of size `K`.

## Sample Input
```
6
1 1 1 2 2 3
2
```

## Sample Output
```
1 2
```

## Edge Cases
- All elements have the exact same frequency.
- `K` equals the total number of unique elements.

## Approach 1
Min-Heap
**Explanation:** 
1. Use a Hash Map to count the frequency of each element.
2. Use a Min-Heap of size `k` to keep track of the top `k` frequent elements. The heap stores pairs `(frequency, number)`.
3. Iterate through the map. Push each entry to the heap. If the heap size exceeds `k`, pop the top (which removes the element with the lowest frequency).
**Time Complexity:** $O(N \log K)$
**Space Complexity:** $O(N)$ for map and heap.

## Approach 2
Optimal Approach (Bucket Sort)
**Explanation:** 
1. Use a Hash Map to count the frequency of each element.
2. Create an array of lists `buckets` of size `N + 1`. The index of the array represents the *frequency*.
3. Iterate over the map, and place each number into the bucket corresponding to its frequency (`buckets[freq].add(num)`).
4. Iterate over the `buckets` array from right to left (from highest frequency `N` down to `1`). Collect the numbers into the result array until we have `k` elements.

**Dry Run:**
`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
- Map: `{1: 3, 2: 2, 3: 1}`
- Buckets (size 7): 
  - `idx 0`: []
  - `idx 1`: [3]  *(3 appeared 1 time)*
  - `idx 2`: [2]  *(2 appeared 2 times)*
  - `idx 3`: [1]  *(1 appeared 3 times)*
- Traverse backwards from idx 6.
- Idx 3 has `[1]`. Add to result. `res = [1]`. Need 1 more.
- Idx 2 has `[2]`. Add to result. `res = [1, 2]`. Have `k` elements. Stop.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

## Java Solution (Bucket Sort)
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int key : map.keySet()) {
            int freq = map.get(key);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(key);
        }
        
        int[] res = new int[k];
        int idx = 0;
        
        for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    res[idx++] = num;
                    if (idx == k) return res;
                }
            }
        }
        
        return res;
    }
}
```

## Python Solution (Bucket Sort)
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
```

## C++ Solution (Min-Heap)
*(C++ doesn't natively support arrays of vectors as cleanly as Java/Python, so Min-Heap is much more common and completely acceptable for the $O(N \log K)$ limit).*
```cpp
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        for (int num : nums) {
            countMap[num]++;
        }
        
        // Min heap storing pair<frequency, number>
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        
        for (auto& entry : countMap) {
            minHeap.push({entry.second, entry.first});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        vector<int> res;
        while (!minHeap.empty()) {
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        
        return res;
    }
};
```

## Common Mistakes
- **Confusing Kth Largest with Top K Frequent:** Kth Largest cares about the *value* of the number. Top K Frequent cares about the *frequency count* from the Hash Map.

## Similar Questions
- Kth Largest Element in an Array
- Sort Characters By Frequency
