# Find Minimum in Rotated Sorted Array

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Microsoft, Amazon, Goldman Sachs

## Topic
Arrays (Binary Search)

## Pattern
Binary Search on Rotated Array

## Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.
You must write an algorithm that runs in $O(\log n)$ time.

## Constraints
- $n == nums.length$
- $1 \le n \le 5000$
- $-5000 \le nums[i] \le 5000$
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a single integer representing the minimum element.

## Sample Input
```
5
3 4 5 1 2
```

## Sample Output
```
1
```

## Edge Cases
- Array is not rotated (the minimum element is at `nums[0]`).
- Array size is 1 or 2.

## Approach 1
Brute Force
**Explanation:** Iterate through the array to find the minimum element.
**Time Complexity:** $O(N)$ (Fails the $O(\log N)$ requirement).
**Space Complexity:** $O(1)$

## Approach 2
Optimal Approach (Binary Search)
**Explanation:** 
Like "Search in Rotated Sorted Array", we can use Binary Search.
1. We initialize `low = 0` and `high = n - 1`.
2. We initialize `ans = INT_MAX`.
3. In each step, we calculate `mid = (low + high) / 2`.
4. We check which half of the array is perfectly sorted.
5. If the left half is sorted (`nums[low] <= nums[mid]`):
   - The minimum element in this perfectly sorted left half is strictly `nums[low]`.
   - Update `ans = min(ans, nums[low])`.
   - We no longer care about the left half, so we discard it by setting `low = mid + 1`.
6. Else, the right half is sorted (`nums[mid] <= nums[high]`):
   - The minimum element in this perfectly sorted right half is strictly `nums[mid]`.
   - Update `ans = min(ans, nums[mid])`.
   - Discard the right half by setting `high = mid - 1`.

**Optimization:** If the entire search space `[low...high]` is sorted (i.e., `nums[low] <= nums[high]`), then the minimum is simply `nums[low]`, and we can just update `ans` and `break` early.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        int ans = Integer.MAX_VALUE;
        
        while (low <= high) {
            // Optimization: If the current search space is already sorted
            if (nums[low] <= nums[high]) {
                ans = Math.min(ans, nums[low]);
                break;
            }
            
            int mid = low + (high - low) / 2;
            
            // If left half is sorted
            if (nums[low] <= nums[mid]) {
                ans = Math.min(ans, nums[low]);
                low = mid + 1;
            } 
            // If right half is sorted
            else {
                ans = Math.min(ans, nums[mid]);
                high = mid - 1;
            }
        }
        
        return ans;
    }
}
```

## Python Solution
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = float('inf')
        
        while low <= high:
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break
                
            mid = low + (high - low) // 2
            
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
                
        return ans
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        int ans = INT_MAX;
        
        while (low <= high) {
            if (nums[low] <= nums[high]) {
                ans = min(ans, nums[low]);
                break;
            }
            
            int mid = low + (high - low) / 2;
            
            if (nums[low] <= nums[mid]) {
                ans = min(ans, nums[low]);
                low = mid + 1;
            } else {
                ans = min(ans, nums[mid]);
                high = mid - 1;
            }
        }
        
        return ans;
    }
};
```

## Common Mistakes
- **Assuming `mid` is the minimum:** The value at `mid` is not necessarily the minimum, it merely tells us which half is sorted. Always compare `ans` with the `low` (or `mid`) boundary of the sorted half.

## Similar Questions
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array II (contains duplicates)
