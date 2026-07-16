# Search in Rotated Sorted Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, LinkedIn

## Topic
Arrays (Binary Search)

## Pattern
Binary Search on Rotated Array

## Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Constraints
- $1 \le nums.length \le 5000$
- $-10^4 \le nums[i] \le 10^4$
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- $-10^4 \le target \le 10^4$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.
- Third line: `target`

## Output Format
- Return the 0-based index of the target, or `-1`.

## Sample Input
```
7
4 5 6 7 0 1 2
0
```

## Sample Output
```
4
```

## Edge Cases
- Array is not rotated at all (pivot is 0).
- Array size is 1 or 2.
- Target is not present.

## Approach 1
Brute Force
**Explanation:** Iterate through the array and check each element.
**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$
*Note: Fails the $O(\log N)$ requirement.*

## Approach 2
Optimal Approach (Binary Search)
**Explanation:** 
Even though the array is rotated, if we split it in half at `mid`, *at least one half of the array will always be strictly sorted*.
1. Set `low = 0`, `high = n - 1`.
2. Find `mid = (low + high) / 2`.
3. If `nums[mid] == target`, return `mid`.
4. Check which half is sorted:
   - **Left half is sorted (`nums[low] <= nums[mid]`):**
     - Check if the target lies within the sorted left half: `nums[low] <= target < nums[mid]`.
     - If yes, target is in left half -> `high = mid - 1`.
     - Else, target is in right half -> `low = mid + 1`.
   - **Right half is sorted (`nums[mid] <= nums[high]`):**
     - Check if target lies within the sorted right half: `nums[mid] < target <= nums[high]`.
     - If yes, target is in right half -> `low = mid + 1`.
     - Else, target is in left half -> `high = mid - 1`.

**Time Complexity:** $O(\log N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // Check if left half is sorted
            if (nums[low] <= nums[mid]) {
                if (target >= nums[low] && target < nums[mid]) {
                    high = mid - 1; // Target is in left half
                } else {
                    low = mid + 1;  // Target is in right half
                }
            } 
            // Else right half is sorted
            else {
                if (target > nums[mid] && target <= nums[high]) {
                    low = mid + 1;  // Target is in right half
                } else {
                    high = mid - 1; // Target is in left half
                }
            }
        }
        
        return -1;
    }
}
```

## Python Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
                
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) return mid;
            
            if (nums[low] <= nums[mid]) {
                if (target >= nums[low] && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        
        return -1;
    }
};
```

## Common Mistakes
- **`<` vs `<=`:** Missing the equals sign on `nums[low] <= nums[mid]` will cause failure on arrays of size 2.

## Similar Questions
- Search in Rotated Sorted Array II (contains duplicates)
- Find Minimum in Rotated Sorted Array
