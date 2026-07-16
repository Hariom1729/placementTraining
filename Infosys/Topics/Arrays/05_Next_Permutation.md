# Next Permutation

## Difficulty
Medium-Hard

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, Adobe

## Topic
Arrays

## Pattern
Math / Array Traversal

## Problem Statement
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
Given an array of integers `nums`, find the next permutation of `nums`.
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

You must rearrange the numbers in-place with $O(1)$ extra memory.

## Constraints
- $1 \le nums.length \le 100$
- $0 \le nums[i] \le 100$

## Input Format
- First line contains `N`, the number of elements.
- Second line contains `N` space-separated integers.

## Output Format
- Return the modified array in-place.

## Sample Input
```
3
1 2 3
```

## Sample Output
```
1 3 2
```

## Edge Cases
- Array is already sorted in descending order (e.g., `3 2 1`). The next permutation should be the sorted array in ascending order `1 2 3`.
- Array with duplicates (e.g., `1 1 5`).

## Approach 1
Brute Force
**Explanation:** Generate all possible permutations in lexicographical order. Store them, search for the current permutation, and return the next one.
**Time Complexity:** $O(N!)$
**Space Complexity:** $O(N!)$ to store all permutations.

## Approach 2
There is no intermediate better approach. We jump directly to the mathematical pattern approach.

## Approach 3
Optimal Approach (Linear Traversal)
**Explanation:** 
1. Traverse the array from right to left to find the first element that is smaller than the element immediately after it. Let's call its index `i`. (This is the breaking point of the decreasing sequence from the right).
2. If no such element is found, the array is in descending order. We just reverse the entire array to get the lowest possible order.
3. If `i` is found, traverse the array again from right to left to find the first element that is strictly greater than `nums[i]`. Let's call its index `j`.
4. Swap `nums[i]` and `nums[j]`.
5. Reverse the sub-array starting from `i+1` to the end.

**Dry Run:**
`nums = [1, 3, 5, 4, 2]`
- Step 1: Find `i`. Right to left. `4 > 2` (No). `5 > 4` (No). `3 < 5` (Yes!). So `i = 1` (`nums[i] = 3`).
- Step 3: Find `j`. Right to left greater than 3. `2 > 3` (No). `4 > 3` (Yes!). So `j = 3` (`nums[j] = 4`).
- Step 4: Swap `nums[i]` and `nums[j]`. `nums` is now `[1, 4, 5, 3, 2]`.
- Step 5: Reverse from `i+1` (index 2) to end. Reverse `[5, 3, 2]` to `[2, 3, 5]`.
- Result: `[1, 4, 2, 3, 5]`.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Python Solution
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        # Reverse the suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```

## Common Mistakes
- **Finding j:** Make sure `j` scans from the very end of the array to the left, NOT from `i+1` to the right. We want the smallest number that is larger than `nums[i]`, and since the suffix is in descending order, scanning right-to-left guarantees finding it first.

## Interview Tips
- Mention that C++ STL has a built-in `std::next_permutation()` function, but immediately state that you understand they want the manual algorithm implementation. This shows language mastery and algorithmic thinking simultaneously.

## Similar Questions
- Permutations
- Permutations II
- Permutation Sequence

## Variations Asked in Infosys
- Find the previous permutation.
