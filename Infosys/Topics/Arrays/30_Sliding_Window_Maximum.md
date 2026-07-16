# Sliding Window Maximum

## Difficulty
Hard

## Probability
★★★★★

## Asked In
Infosys SP
Related Companies: Amazon, Google, Microsoft

## Topic
Arrays / Deque

## Pattern
Sliding Window / Monotonic Queue

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

## Constraints
- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$
- $1 \le k \le nums.length$

## Input Format
- First line: `N K`
- Second line: `N` space-separated integers.

## Output Format
- Return an array containing the maximum of each window.

## Sample Input
```
8 3
1 3 -1 -3 5 3 6 7
```

## Sample Output
```
3 3 5 5 6 7
```

## Edge Cases
- $K = 1$ (just return the original array).
- Window size $K$ equals the array size (return a single element).

## Approach 1
Brute Force
**Explanation:** For every window from `i = 0` to `n - k`, loop through the `k` elements to find the max.
**Time Complexity:** $O((N - K) \times K)$ (Will TLE).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Monotonic Deque)
**Explanation:** 
We can use a Deque (Double Ended Queue) to store the indices of the elements. The deque will maintain a monotonically decreasing order of values.
Why? Because if a new element is larger than the previous elements in the window, those previous smaller elements will NEVER be the maximum for any future window. We can safely pop them from the back of the deque.
1. Iterate through the array.
2. **Remove Out of Bounds:** If the index at the front of the deque is $\le i - k$, it is out of the current sliding window. Pop it from the front.
3. **Maintain Monotonicity:** While the deque is not empty and the current element `nums[i]` is strictly greater than the element at the index stored at the back of the deque, pop from the back.
4. Add the current index `i` to the back of the deque.
5. If we have processed at least `k` elements (`i >= k - 1`), the maximum for this window is at the front of the deque (`nums[deque.front()]`). Add it to the result.

**Time Complexity:** $O(N)$ (Each element is pushed and popped at most once).
**Space Complexity:** $O(K)$ for the deque.

## Java Solution
```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        
        int n = nums.length;
        int[] result = new int[n - k + 1];
        int ri = 0;
        
        Deque<Integer> q = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            // Remove numbers out of range k
            while (!q.isEmpty() && q.peek() < i - k + 1) {
                q.poll();
            }
            
            // Remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && nums[q.peekLast()] < nums[i]) {
                q.pollLast();
            }
            
            q.offer(i);
            
            if (i >= k - 1) {
                result[ri++] = nums[q.peek()];
            }
        }
        
        return result;
    }
}
```

## Python Solution
```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Stores indices
        res = []
        
        for i in range(len(nums)):
            # Remove indices that are out of bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # Maintain decreasing order
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            q.append(i)
            
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
```

## C++ Solution
```cpp
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        
        for (int i = 0; i < nums.size(); i++) {
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }
            
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
            
            if (i >= k - 1) {
                ans.push_back(nums[dq.front()]);
            }
        }
        
        return ans;
    }
};
```

## Common Mistakes
- **Storing values instead of indices:** The deque MUST store the indices of the array, not the raw integer values. If you store values, you have no way of knowing if the value at the front of the deque has slid out of the `k` bounds.

## Interview Tips
- This problem is the ultimate test for understanding monotonic queues. If you can explain clearly why "smaller elements before a larger element become useless", you will ace this interview.

## Similar Questions
- Minimum Window Substring
- Longest Substring Without Repeating Characters
