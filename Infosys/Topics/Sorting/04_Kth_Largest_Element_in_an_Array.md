# Kth Largest Element in an Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Amazon, Google

## Topic
Sorting / Divide and Conquer / Heap

## Pattern
Quickselect / Min-Heap

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Can you solve it without sorting?

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Input
- `nums` vector of integers.
- `k` integer.

## Output
- Return an integer.

## Sample Test Cases

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Edge Cases
- `k = 1` (Max element).
- `k = nums.length` (Min element).

## Intuition
**Approach 1: Sorting.** Sort the array in descending order and return `nums[k-1]`. Takes $O(N \log N)$. Easy, but fails the interview follow-up.
**Approach 2: Min-Heap (Priority Queue).** We can maintain a Min-Heap of size `k`. As we iterate through the array, we push elements into the heap. If the heap size exceeds `k`, we pop the top (which is the smallest element). At the end, the heap contains the `k` largest elements, and the top of the Min-Heap is exactly the `k`th largest! Takes $O(N \log K)$.
**Approach 3: Quickselect.** This is a massive brain-flex in an interview. We use the exact partition logic from Quick Sort!
In Quick Sort, after partitioning, the pivot is placed in its **exact, final sorted position**.
If we want the $K$th largest element, that is index `nums.size() - k` in a sorted array!
So we partition the array. If the pivot lands perfectly at index `nums.size() - k`, we are done! We found it in $O(N)$ time without sorting the rest of the array!
If the pivot lands at an index smaller than our target, we only recurse on the right side. If it's larger, we only recurse on the left side!

*Let's provide both Min-Heap (most common) and Quickselect (most optimal).*

## Optimal Approach 1 (Min-Heap)
**Detailed explanation:**
1. Create a `priority_queue<int, vector<int>, greater<int>> minHeap`.
2. Loop `num` in `nums`:
   - Push `num` into `minHeap`.
   - If `minHeap.size() > k`, `minHeap.pop()`.
3. Return `minHeap.top()`.

**Time Complexity:** $O(N \log K)$
**Space Complexity:** $O(K)$

## Optimal Approach 2 (Quickselect)
**Detailed explanation:**
1. Target index is `target = nums.size() - k`.
2. Create `quickSelect(nums, low, high, target)`:
   - Use the exact same Lomuto partition logic from Quick Sort (with random pivot).
   - Get the pivot index `pi = partition(...)`.
   - If `pi == target`, return `nums[pi]`.
   - If `pi < target`, return `quickSelect(nums, pi + 1, high, target)`.
   - If `pi > target`, return `quickSelect(nums, low, pi - 1, target)`.
3. Call `quickSelect(nums, 0, nums.size() - 1, target)`.

**Time Complexity:** Average $O(N)$. We discard half the array every iteration, so $N + N/2 + N/4... = 2N = O(N)$. Worst case $O(N^2)$.
**Space Complexity:** Average $O(\log N)$ for recursion stack.

## C++ Solution (Quickselect - O(N))

```cpp
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

class Solution {
private:
    int partition(vector<int>& nums, int low, int high) {
        int randomIndex = low + rand() % (high - low + 1);
        swap(nums[randomIndex], nums[high]);
        
        int pivot = nums[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (nums[j] < pivot) {
                i++;
                swap(nums[i], nums[j]);
            }
        }
        
        swap(nums[i + 1], nums[high]);
        return i + 1;
    }
    
    int quickSelect(vector<int>& nums, int low, int high, int target) {
        if (low == high) return nums[low];
        
        int pi = partition(nums, low, high);
        
        if (pi == target) {
            return nums[pi];
        } else if (pi < target) {
            return quickSelect(nums, pi + 1, high, target);
        } else {
            return quickSelect(nums, low, pi - 1, target);
        }
    }

public:
    int findKthLargest(vector<int>& nums, int k) {
        // The kth largest element is at index (N - k) in a sorted array
        int targetIndex = nums.size() - k;
        return quickSelect(nums, 0, nums.size() - 1, targetIndex);
    }
};
```

## C++ Solution (Min-Heap - O(N log K))

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Min-Heap
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop(); // Remove the smallest element
            }
        }
        
        // The top of the heap is the kth largest
        return minHeap.top(); 
    }
};
```

## Common Mistakes
- **Max-Heap instead of Min-Heap:** Many people intuitively think "Kth Largest? I need a Max-Heap!". No! If you use a Max-Heap, you have to push ALL $N$ elements into it, taking $O(N \log N)$ time, and then pop $K$ times. A Min-Heap allows you to constrain the size to exactly $K$, dropping the time to $O(N \log K)$.

## Similar Problems
- Top K Frequent Elements
- K Closest Points to Origin
