# Kth Largest Element in an Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Related Companies: Facebook, Amazon, LinkedIn

## Topic
Arrays / Heap

## Pattern
Priority Queue / Quickselect

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.
Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.
You must solve it in $O(n)$ time complexity.

## Constraints
- $1 \le k \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.
- Third line: `K`

## Output Format
- Return a single integer representing the kth largest element.

## Sample Input
```
6
3 2 1 5 6 4
2
```

## Sample Output
```
5
```

## Edge Cases
- `k == 1` (Find the absolute maximum).
- `k == n` (Find the absolute minimum).
- Array with all identical elements.

## Approach 1
Brute Force (Sorting)
**Explanation:** Sort the array in descending order and return `nums[k-1]`. Or sort ascending and return `nums[n-k]`.
**Time Complexity:** $O(N \log N)$ (Technically fails strict $O(N)$ requirement, but often accepted).
**Space Complexity:** $O(1)$

## Approach 2
Better Approach (Min-Heap)
**Explanation:** Use a Min-Heap of size `k`. Iterate through the array. If the heap size is $< k$, push the element. If the heap is full and the current element is greater than the top of the heap, pop the top and push the current element. At the end, the top of the heap is the $k$th largest element.
**Time Complexity:** $O(N \log K)$
**Space Complexity:** $O(K)$

## Approach 3
Optimal Approach (Quickselect)
**Explanation:** 
Quickselect is similar to Quicksort, but instead of recursing into both sides of the pivot, we only recurse into the side that contains the $k$th largest element.
1. Choose a random pivot.
2. Partition the array so all elements greater than the pivot are to the left, and elements smaller are to the right.
3. Let `p` be the index of the pivot after partitioning.
4. If `p == k - 1`, we found our element!
5. If `p > k - 1`, the $k$th largest element is in the left half. Recurse left.
6. If `p < k - 1`, the $k$th largest element is in the right half. Recurse right.

**Time Complexity:** Average $O(N)$, Worst case $O(N^2)$ (rare with randomized pivot).
**Space Complexity:** $O(1)$ (or $O(\log N)$ recursion stack).

## Java Solution (Min-Heap)
*(Note: Min-Heap is the standard accepted solution in most interviews due to stability vs Quickselect worst-case)*
```java
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        return minHeap.peek();
    }
}
```

## Python Solution (Min-Heap)
```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return min_heap[0]
```

## C++ Solution (Min-Heap)
```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        return minHeap.top();
    }
};
```

## Common Mistakes
- **Using a Max-Heap instead of a Min-Heap:** If you use a Max-Heap, you have to put ALL $N$ elements into the heap (costing $O(N \log N)$ space/time) and then pop $k$ times. A Min-Heap restricts the size to $K$, drastically saving space and bounding the time to $O(N \log K)$.

## Similar Questions
- Top K Frequent Elements
- Kth Smallest Element in a Sorted Matrix
