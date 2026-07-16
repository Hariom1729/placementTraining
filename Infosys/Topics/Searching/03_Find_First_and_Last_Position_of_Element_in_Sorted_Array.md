# Find First and Last Position of Element in Sorted Array

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Facebook, Amazon, Google

## Topic
Searching / Arrays

## Pattern
Binary Search (Lower Bound & Upper Bound)

## Problem Statement
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Input
- `nums` vector of integers.
- `target` integer.

## Output
- Return a vector of two integers `[first_position, last_position]`.

## Sample Test Cases

**Example 1:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:**
```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Edge Cases
- Target appears exactly once (first and last positions are the same).
- Target occupies the entire array.
- Empty array.

## Intuition
Normally, binary search stops the *exact moment* it finds the target.
But if the array is `[8, 8, 8, 8, 8]` and we hit the middle `8`, we don't know if the first `8` is to our left, or if the last `8` is to our right!

If we just use binary search to find ONE target, and then use a linear scan (a `while` loop going left and right) to find the bounds, the worst-case time complexity becomes $O(N)$! The problem strictly demands $O(\log N)$.

To achieve $O(\log N)$, we must run **Binary Search TWICE**!
1. **First Binary Search (Find Left Bound):**
   When we find the target (`nums[mid] == target`), we DO NOT STOP! We record the index as a potential answer, and then we force the search to continue on the **LEFT** half (`right = mid - 1`) to see if there is an even earlier occurrence!
2. **Second Binary Search (Find Right Bound):**
   When we find the target (`nums[mid] == target`), we record the index as a potential answer, and then force the search to continue on the **RIGHT** half (`left = mid + 1`) to see if there is an even later occurrence!

## Optimal Approach (Double Binary Search)
**Detailed explanation:**
1. Create a helper function `findBound(nums, target, isFirst)` that returns an integer.
2. Initialize `left = 0`, `right = nums.size() - 1`, `result = -1`.
3. Loop `while (left <= right)`:
   - `mid = left + (right - left) / 2`.
   - If `nums[mid] == target`:
     - `result = mid`. (Record this as our best answer so far).
     - If `isFirst == true`, we want to look for earlier ones, so `right = mid - 1`.
     - Else, we want to look for later ones, so `left = mid + 1`.
   - Else if `nums[mid] < target`:
     - `left = mid + 1`.
   - Else:
     - `right = mid - 1`.
4. Return `result`.
5. In the main function, call `first = findBound(nums, target, true)` and `last = findBound(nums, target, false)`. Return `[first, last]`.

**Time Complexity:** $O(\log N)$ (Two separate $O(\log N)$ passes).
**Space Complexity:** $O(1)$ constant space.

## C++ Solution

```cpp
#include <vector>
using namespace std;

class Solution {
private:
    int findBound(vector<int>& nums, int target, bool isFirst) {
        int left = 0;
        int right = nums.size() - 1;
        int result = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                result = mid; // Record the potential answer
                
                // Force the binary search to keep going
                if (isFirst) {
                    right = mid - 1; // Look left for earlier occurrences
                } else {
                    left = mid + 1;  // Look right for later occurrences
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = findBound(nums, target, true);
        
        // Minor optimization: If first is -1, the target doesn't exist, so don't run the second search
        if (first == -1) {
            return {-1, -1};
        }
        
        int last = findBound(nums, target, false);
        
        return {first, last};
    }
};

/*
// Alternative solution using C++ STL
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto it1 = lower_bound(nums.begin(), nums.end(), target);
        auto it2 = upper_bound(nums.begin(), nums.end(), target);
        
        if (it1 == nums.end() || *it1 != target) {
            return {-1, -1};
        }
        
        return {(int)(it1 - nums.begin()), (int)(it2 - nums.begin() - 1)};
    }
};
*/
```

## Dry Run
`nums = [5, 7, 7, 8, 8, 10], target = 8`
- `findBound(isFirst = true)`:
  - `left=0`, `right=5`, `mid=2` (`7`). `7 < 8` -> `left=3`.
  - `left=3`, `right=5`, `mid=4` (`8`). `8 == 8`. `result=4`. Look left: `right=3`.
  - `left=3`, `right=3`, `mid=3` (`8`). `8 == 8`. `result=3`. Look left: `right=2`.
  - `left=3`, `right=2`. Loop breaks. Return `3`.
- `findBound(isFirst = false)`:
  - `left=0`, `right=5`, `mid=2` (`7`). `7 < 8` -> `left=3`.
  - `left=3`, `right=5`, `mid=4` (`8`). `8 == 8`. `result=4`. Look right: `left=5`.
  - `left=5`, `right=5`, `mid=5` (`10`). `10 > 8`. Look left: `right=4`.
  - `left=5`, `right=4`. Loop breaks. Return `4`.
- Output: `[3, 4]`.

## Common Mistakes
- **Linear Scan Fallback:** A very common mistake is finding the element via standard Binary Search, and then writing a `while(nums[left] == target) left--;` loop to find the bounds. If the array is `[8, 8, 8... 8]` and `target = 8`, this takes $O(N)$ time, failing the hard constraints.

## Similar Problems
- Search Insert Position
- Find Minimum in Rotated Sorted Array
